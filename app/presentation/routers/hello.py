from fastapi import APIRouter, Depends
from app.presentation.models.hello_model import HelloResponse
from app.presentation.dependencies.message_dependencies import get_hello_message_usecase
from app.application.usecase.get_hello_message_usecase import GetHelloMessageUseCase
from app.domain.entities.hello_entity import HelloEntity

router = APIRouter()

@router.get("/hello", response_model=HelloResponse)
def hello(usecase: GetHelloMessageUseCase = Depends(get_hello_message_usecase)):
    entity: HelloEntity = usecase.execute()
    return HelloResponse(message=entity.message.value)