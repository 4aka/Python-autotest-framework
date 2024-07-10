from pydantic import BaseModel


class Document(BaseModel):
    DocumentNumber: int
    Phone: str


class MethodProperties(BaseModel):
    Documents: list[Document]


class Tracking(BaseModel):
    apiKey: str
    modelName: str
    calledMethod: str
    methodProperties: MethodProperties
    system: str
