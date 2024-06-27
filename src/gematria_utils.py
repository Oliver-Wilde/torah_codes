hebrew_gematria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7,
    'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40,
    'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100,
    'ר': 200, 'ש': 300, 'ת': 400
}

def gematria_value(word):
    return sum(hebrew_gematria.get(letter, 0) for letter in word)

if __name__ == "__main__":
    word = input("Enter a Hebrew word: ")
    value = gematria_value(word)
    print(f"The Gematria value of '{word}' is {value}")
