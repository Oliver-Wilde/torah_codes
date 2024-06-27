import re

def preprocess_torah():
    with open("../data/torah.txt", "r", encoding="utf-8") as file:
        torah_text = file.read()
    
    # Remove spaces and punctuation, only keep Hebrew letters
    cleaned_text = re.sub(r'[^א-ת]', '', torah_text)
    
    with open("../data/cleaned_torah.txt", "w", encoding="utf-8") as file:
        file.write(cleaned_text)

if __name__ == "__main__":
    preprocess_torah()
