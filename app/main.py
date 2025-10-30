from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.Models.Login import *
from app.config import *
from app.routes import chat, graph

app = FastAPI()
# app.include_router(users.router)
app.include_router(chat.router)
app.include_router(graph.router)


@app.get("/health")
async def health():
    return {"Hello!": "Это чат с AI моделью. Авторизуйся и общайся с AI через /chat"}


@app.post("/token", response_model=LoginResponseModel,
          tags=["Login",],
          summary="Login and get token",)
async def token(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Enter USERNAME and PASSWORD for get AUTH token"""
    if data.username.lower() == USERNAME and data.password == PASSWORD:
        token = f"{USERNAME}{PASSWORD}"
        return LoginResponseModel(access_token=token)
    else:
        raise HTTPException(status_code=404, detail="Credentials not found")


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response
