from service import listagem_service_jokes
from .router import router
from fastapi import status


#Rota
@router.get('', status_code=status.HTTP_200_OK)
def listagem_controller_jokes():
    return listagem_service_jokes()