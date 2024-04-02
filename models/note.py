from pydantic import BaseModel

class Note(BaseModel):
    title: str
    description: str
    important : bool = None  # type: ignore