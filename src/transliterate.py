# Basic transliteration mapping (not comprehensive)
transliteration_dict = {
    'a': 'א', 'b': 'ב', 'g': 'ג', 'd': 'ד', 'h': 'ה', 'v': 'ו',
    'z': 'ז', 'ch': 'ח', 't': 'ט', 'y': 'י', 'k': 'כ', 'l': 'ל',
    'm': 'מ', 'n': 'נ', 's': 'ס', 'e': 'ע', 'p': 'פ', 'tz': 'צ',
    'q': 'ק', 'r': 'ר', 'sh': 'ש', 'th': 'ת'
}

def transliterate(name):
    hebrew_name = ""
    i = 0
    while i < len(name):
        # Check for two-letter combinations first
        if i+1 < len(name) and name[i:i+2] in transliteration_dict:
            hebrew_name += transliteration_dict[name[i:i+2]]
            i += 2
        elif name[i] in transliteration_dict:
            hebrew_name += transliteration_dict[name[i]]
            i += 1
        else:
            i += 1
    return hebrew_name

if __name__ == "__main__":
    name = input("Enter an English name: ")
    hebrew_name = transliterate(name.lower())
    print(f"The Hebrew transliteration of '{name}' is '{hebrew_name}'")
