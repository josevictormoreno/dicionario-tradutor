from googletrans import Translator
from lingua_selecionada import lingua_selecionada
def tradutor(texto, lingua):
    translator = Translator()
    translation = translator.translate(texto, dest=lingua_selecionada(lingua))
    return translation.text