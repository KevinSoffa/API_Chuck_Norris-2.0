from repository import listagem_repository_jokes
from googletrans import Translator
from fastapi import HTTPException

def translate_to_portuguese(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='pt').text
    return translated_text

def listagem_service_jokes():
    response = listagem_repository_jokes()

    if response:
        # Traduzindo a piada para o português
        piada_traduzida = translate_to_portuguese(response['value'])
        
        return {
            "api": "Chuck Norris",
            "joke": piada_traduzida,
        }
    
    raise HTTPException(status_code=404)

