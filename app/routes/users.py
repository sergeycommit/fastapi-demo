from fastapi import APIRouter

from app.DB.Tables.User import User
from app.DB.db import SessionDep


router = APIRouter(
            tags=["Users"],
            responses={404: {"description": "Not found"}},
)


@router.post("/users/")
def create_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user