from app.infrastructure.memory.get_hello_message import InMemoryHelloRepository
from app.application.usecase.get_hello_message_usecase import GetHelloMessageUseCase

def get_hello_message_usecase() -> GetHelloMessageUseCase:
    repository = InMemoryHelloRepository()
    return GetHelloMessageUseCase(repository)