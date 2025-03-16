from app.domain.repositoryies_interface.hello_repository import HelloRepository

class InMemoryHelloRepository(HelloRepository):

    def get_hello_message(self) -> str:
        return "Hello World"