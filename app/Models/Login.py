from pydantic import BaseModel, Field


class LoginModel(BaseModel):
    username: str
    password: str


class LoginResponseModel(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")