from requests import request
from decouple import config


# GET na API Chuck Norris
def listagem_repository_jokes():
    listagem = request(
        'GET',
        '%s/' % (
            config('URL')
        ),
        headers={
            'Content-Type': 'application/json'
        }
    )

    response = listagem.json()
    return response
