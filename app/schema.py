from pydantic import BaseModel


class BookRead(BaseModel):
    title: str
    author: str
    content: str


