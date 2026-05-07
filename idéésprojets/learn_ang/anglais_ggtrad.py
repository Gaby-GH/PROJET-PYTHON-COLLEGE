from googletrans import Translator

text1 = "holla"


print("traduis en fr : ", Translator.translate(text1, src="es", dest="fr"))
