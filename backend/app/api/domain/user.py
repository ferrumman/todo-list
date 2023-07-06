from pydantic import BaseModel

class User(BaseModel):
    user_id: str = None
    username: str
    password: str
