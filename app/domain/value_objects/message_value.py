from pydantic import BaseModel

class MessageValue(BaseModel):
    value: str

    def __eq__(self, other):
        if isinstance(other, MessageValue):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)