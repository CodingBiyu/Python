from googletrans import Translator, LANGUAGES
from googletrans.models import Translated

lang = list(LANGUAGES.values())
print("Welcome !!")
print(lang)
input_text = input("Please Enter Your Text in english:\n")

out_lang = input("Please enter output language name (ex.urdu,arabic) :\n ").lower()

if out_lang not in lang:
    print("Sorry This Language is not available to translate")
else:
    translator = Translator()   #translator object

    translated = translator.translate(text = input_text, src="english",dest = out_lang)
    translated = str(translated).split(", ")
    converted = translated[2]
    pro = translated[3]
    print(converted)
    print(pro)

    # Translated(src=en, dest=ur, text=میرانام, pronunciation = None, extra_data = "{'confiden...")