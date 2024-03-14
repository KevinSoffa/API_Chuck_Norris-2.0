from requests import request
from decouple import config


# Listagem de Categorias
def listagem_repository_categories():
    #requisição na API
    cat = request(
        'GET',
        '%s/' % (
            config('URL_CATEGORIA')
        ),
        headers={
            'Content-Type': 'application/json'
        }
    )
    

    response = cat.json()
    return response