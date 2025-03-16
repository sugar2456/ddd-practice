from app.domain.repositoryies_interface.hello_repository import HelloRepository
from app.domain.entities.hello_entity import HelloEntity
from app.domain.value_objects.message_value import MessageValue

class GetHelloMessageUseCase:
    def __init__(self, repository: HelloRepository):
        self.repository = repository

    def execute(self) -> HelloEntity:
        message = self.repository.get_hello_message()
        return HelloEntity(message=MessageValue(value=message))