from service import listagem_service_categories
from .router import router
from fastapi import status


# Listagem de Categorias
@router.get('/categorias', status_code=status.HTTP_200_OK)
def listagem_controller_categories():
    return listagem_service_categories()
