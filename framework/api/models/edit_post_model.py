from pydantic import BaseModel


class Edit(BaseModel):
    userId: int
    id: int
    title: str
    body: str
