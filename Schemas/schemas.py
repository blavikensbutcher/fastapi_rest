from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    avatar: str
    password: str


class UserSchemaResponse(UserSchema):
    id: int

    class Config:
        from_attributes: True

