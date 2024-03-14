from repository import listagem_repository_categories
from fastapi import HTTPException
from google_trans_new import google_translator

def translate_to_english(text):
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt='en')
    return translated_text

def listagem_service_categories():
    # Obtendo a lista de categorias do repositório
    response = listagem_repository_categories()

    if response:
        # Traduzindo a lista de categorias para o inglês
        traducao = [translate_to_english(category) for category in response]
        return traducao

    raise HTTPException(status_code=404, detail="Falha ao obter categorias do repositório")







'''from repository import listagem_repository_categories
from fastapi import HTTPException


def listagem_service_categories():

    response = listagem_repository_categories()

    if response:
        return response

    raise HTTPException(
        status_code=404
    )'''