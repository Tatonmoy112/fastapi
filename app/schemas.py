from pydantic import BaseModel, EmailStr, ConfigDict, conint
from datetime import datetime
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: "UserOut"

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: Post
    Votes: int 


class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema for representing a user in the response
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
# login schema for user authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: int  | None = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
    # when dont need negative number use below
    # dir: conint(ge=0, le=1)