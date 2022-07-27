from googletrans import Translator

def tradutor(texto, lingua):
    if lingua == 'Espanhol':
        lingua = 'es'
    if lingua == 'Italiano':
        lingua = 'it'
    if lingua == 'Frances':
        lingua = 'fr'
    if lingua == 'Ingles':
        lingua = 'en'
    if lingua == 'Portugues':
        lingua = 'pt'
    translator = Translator()
    translation = translator.translate(texto, dest=lingua)
    return translation.text