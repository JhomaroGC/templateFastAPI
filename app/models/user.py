from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    email: str = Field(..., example="user@example.com")
    password: str = Field(
        ...,
        max_length=72,
        min_length=8,
        # pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$",
    )


class UserLogin(BaseModel):
    email: str = Field(..., example="user@example.com")
    password: str = Field(
        ...,
        max_length=72,
        min_length=8,
        # pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$",
    )
