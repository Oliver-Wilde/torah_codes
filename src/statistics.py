import random
from els_search import find_els

def randomize_text(text):
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

def calculate_significance(name, text, positions):
    random_hits = []
    for _ in range(1000):  # Number of randomizations
        random_text = randomize_text(text)
        random_positions = find_els(name, random_text)
        random_hits.append(len(random_positions))
    
    actual_hits = len(positions)
    average_random_hits = sum(random_hits) / len(random_hits)
    
    significance = (actual_hits - average_random_hits) / max(1, average_random_hits)
    return significance

if __name__ == "__main__":
    with open("../data/cleaned_torah.txt", "r", encoding="utf-8") as file:
        torah_text = file.read()
    
    name = input("Enter the Hebrew name: ")
    positions = find_els(name, torah_text)
    significance = calculate_significance(name, torah_text, positions)
    
    print(f"Statistical significance of finding '{name}': {significance}")
