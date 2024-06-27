from multiprocessing import Pool

def find_els_worker(args):
    name, text, max_skip, start, end = args
    positions = []
    name_len = len(name)
    
    for skip in range(1, max_skip + 1):
        for pos in range(start, end):
            match = True
            for i in range(name_len):
                if pos + i * skip >= len(text) or text[pos + i * skip] != name[i]:
                    match = False
                    break
            if match:
                positions.append((pos, skip))
    return positions

def find_els(name, text, max_skip=100, num_workers=4):
    chunk_size = len(text) // num_workers
    args = [(name, text, max_skip, i * chunk_size, (i + 1) * chunk_size) for i in range(num_workers)]
    
    with Pool(num_workers) as pool:
        results = pool.map(find_els_worker, args)
    
    # Flatten the list of results
    positions = [pos for sublist in results for pos in sublist]
    return positions

def extract_context(text, position, skip, name, length=50):
    start, end = position, position + skip * (len(name) - 1)
    context_start = max(0, start - length)
    context_end = min(len(text), end + length)
    context = text[context_start:context_end]
    
    highlighted = list(context)
    for i in range(len(name)):
        highlighted[(start - context_start) + i * skip] = f"[{highlighted[(start - context_start) + i * skip]}]"
    
    return ''.join(highlighted)

def break_into_segments(context, segment_length=100):
    return [context[i:i + segment_length] for i in range(0, len(context), segment_length)]

if __name__ == "__main__":
    with open("../data/cleaned_torah.txt", "r", encoding="utf-8") as file:
        torah_text = file.read()
    
    name = input("Enter the Hebrew name: ")
    positions = find_els(name, torah_text)
    
    for pos, skip in positions:
        context = extract_context(torah_text, pos, skip, name)
        segments = break_into_segments(context)
        for segment in segments:
            print(segment)
