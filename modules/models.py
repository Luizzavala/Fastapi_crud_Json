#python
from typing import Optional
from uuid import UUID
from datetime import date, datetime

#pydantic
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    user_id : UUID = Field(...)
    email : EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(...,
                          min_length=8,
                          max_length=64)

class User(UserBase):
    
    first_name : str = Field(...,
                             min_length=1,
                             max_length=50,
                             title="username",
                             description="The username"
                             )
    last_name: str = Field(...,
                            min_length=1,
                            max_length=50,
                            title="Lastname",
                            description="The Lastname username"
                            )
    birth_date : Optional[date] =Field(default=None,
                                       title="birthdate",
                                       description="User´s birthdate ")

class UserRegister(User, UserLogin):
    pass    
    
class Tweet(BaseModel):
    tweet_id : UUID = Field(...)
    content: str = Field(...,
                         min_length=1,
                         max_length=256)
    created_at: datetime  = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
    