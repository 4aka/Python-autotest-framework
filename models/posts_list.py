import pydantic
from pydantic import BaseModel
from models.post_response import Post


class UserList(BaseModel):
    pydantic.RootModel: list[Post]

