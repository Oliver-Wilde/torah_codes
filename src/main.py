from els_search import find_els, extract_context, break_into_segments
from visualize import visualize_search_results
from statistics import calculate_significance
from translate import translate_batch

def main():
    print("Welcome to the Torah Code Program")
    with open("../data/cleaned_torah.txt", "r", encoding="utf-8") as file:
        torah_text = file.read()
    
    while True:
        name = input("Enter the Hebrew name (or 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        
        positions = find_els(name, torah_text, num_workers=8)  # Increase number of workers for faster search
        results = []
        for pos, skip in positions:
            context = extract_context(torah_text, pos, skip, name)
            segments = break_into_segments(context)
            translated_context = ' '.join(translate_batch(segments))  # Batch translation
            results.append((pos, skip, context, translated_context))
        
        if results:
            print(f"Found '{name}' in {len(results)} positions. Displaying results:")
            visualize_search_results(name, results)
            significance = calculate_significance(name, torah_text, positions)
            print(f"Statistical significance of finding '{name}': {significance}")
        else:
            print(f"'{name}' not found in the text with the given parameters")
    
    print("Thank you for using the Torah Code Program")

if __name__ == "__main__":
    main()
