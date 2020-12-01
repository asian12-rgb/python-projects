# this is practice programme knows as translator in this you can set a scr. language and a dest. language to translator you want
from googletrans import Translator

while True:

    sentence=str(input("say what do you want to Translate"))

    translator=Translator()

    translated_sentence=translator.translate(sentence,src='en',dest='hi')

    print(translated_sentence.text)
