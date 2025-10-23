from pydantic import BaseModel


class SystemPromptModel(BaseModel):
    role: str = "system"
    content: str | None


class UserMessageModel(BaseModel):
    role: str = "user"
    content: str

class ResponseMessageModel(BaseModel):
    system_prompt: str | None
    user_request: str
    message: str