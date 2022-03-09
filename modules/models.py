#python
from typing import Optional
from uuid import uuid4 as uuid
from datetime import date, datetime
#pydantic
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    user_id : Optional[str]
    email : EmailStr = Field(...)
    
    class config:
        eschema_extra = {
            "example":{
                "email" : "luis@example.com"
            }
        }

class UserLogin(UserBase):
    password: str = Field(...,
                          min_length=8,
                          max_length=64)
    class config:
        eschema_extra = {
            "example":{
                "password" : "thismybadpassword"
            }
        }

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
    class config:
        eschema_extra = {
            "example":{
                "first_name" : "Luis",
                "last_name" : "zavala",
                "birth_date" :"1985-08-05",
            }
        } 
        
class UserRegister(UserLogin, User):
    class config:
        eschema_extra = {
            "example":{
                "email" : "example@gmail.com",           
                "password" : "thismybadpassword",
                "first_name" : "Luis",
                "last_name" : "zavala",
                "birth_date" :"1985-08-05",
            }
        }
 
class UserUpdate(BaseModel):
    
        first_name : str = Field(
                             min_length=1,
                             max_length=50,
                             title="username",
                             description="The username"
                             )
        last_name: str = Field(
                            min_length=1,
                            max_length=50,
                            title="Lastname",
                            description="The Lastname username"
                            )
        birth_date : Optional[date] =Field(default=None,
                                       title="birthdate",
                                       description="User´s birthdate ")
        class config:        
                eschema_extra = {
                    "example":{
                        "first_name" : "Luis",
                        "last_name" : "zavala",
                        "birth_date" :"1985-08-05",
                    }
                } 
 
class Tweet(BaseModel):
    tweet_id : Optional[str]
    content: str = Field(...,
                         min_length=1,
                         max_length=256)
    created_at: datetime  = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
    
    class config:
        eschema_extra = {
            "example":{
                    "tweet_id" : str(uuid),
                    "content": "Esto es un twwet",
                    
            }
        }
            
class TweetUpdate(BaseModel):
    tweet_id : Optional[str]
    content: str = Field(...,
                         min_length=1,
                         max_length=256)
    updated_at: Optional[datetime] = Field(default=datetime.now())
    
            
            

    
    