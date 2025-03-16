from pydantic import BaseModel
from app.domain.value_objects.message_value import MessageValue

class HelloEntity(BaseModel):
    message: MessageValue

    def update_message(self, new_message: str):
        self.message = MessageValue(value=new_message)