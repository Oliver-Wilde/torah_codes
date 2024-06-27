from googletrans import Translator
import time

def translate_text(text, src='he', dest='en'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

def translate_batch(texts, src='he', dest='en'):
    translator = Translator()
    translations = []
    for text in texts:
        try:
            translations.append(translator.translate(text, src=src, dest=dest).text)
        except Exception as e:
            translations.append("Translation Error")
            time.sleep(1)  # To handle rate limiting
    return translations

if __name__ == "__main__":
    sample_text = "שלום עולם"
    translated = translate_text(sample_text)
    print(f"Translated text: {translated}")
