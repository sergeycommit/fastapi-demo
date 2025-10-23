from sqlmodel import Field, SQLModel



class UserBase(SQLModel):
    name: str = Field(index=True)
    count: int | None = Field(default=0, index=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str