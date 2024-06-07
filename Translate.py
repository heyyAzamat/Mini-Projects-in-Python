from mtranslate import translate

def translate_text(text, target_language="en"):
    translated_text = translate(text, target_language)
    return translated_text

text = input("Введите текст для перевода: ")
target_language = input("Введите язык перевода (например, 'en' для английского): ")
translated_text = translate_text(text, target_language)
print("Переведенный текст:", translated_text)