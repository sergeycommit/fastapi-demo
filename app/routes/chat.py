from fastapi import APIRouter, Depends, Query
from openai import AsyncOpenAI

from app.Models.Message import *
from ..dependencies import oauth2_scheme
from app.config import *

router = APIRouter(
            tags=["Chat"],
            responses={404: {"description": "Not found"}},
)

openai_client = AsyncOpenAI(
    api_key=OR_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


@router.get("/chat", response_model=ResponseMessageModel,
         tags=["Chat",],
         summary="Chatting with AI",
         dependencies=[Depends(oauth2_scheme)])
async def chat(
        message: str = Query(title="User message", max_length=1500),
        system_prompt: str = Query(default=None, max_length=1500),
               ):
    """For chatting enter AUTH token from /token/ and message"""
    response = await openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            SystemPromptModel(content=system_prompt),
            UserMessageModel(content=message),
        ],
    )
    return ResponseMessageModel(
        system_prompt=system_prompt,
        user_request=message,
        message=response.choices[0].message.content,
    )