from pydantic import BaseModel

class Name(BaseModel):
    id: int = None
    name: str
    item: str