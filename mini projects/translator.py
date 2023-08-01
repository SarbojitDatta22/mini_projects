from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

def main():
    print("Welcome to the Language Translator!")
    input_text = input("Enter the text you want to translate: ")
    source_language = input("Enter the source language (e.g., en, es, fr, ja): ")
    target_language = input("Enter the target language (e.g., en, es, fr, ja): ")

    try:
        translated_text = translate_text(input_text, source_language, target_language)
        print("Translation:")
        print(translated_text)
    except Exception as e:
        print("An error occurred during translation:")
        print(e)

if __name__ == "__main__":
    main()
