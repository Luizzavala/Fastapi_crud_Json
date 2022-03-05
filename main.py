from fastapi import FastAPI, status
from typing import List, Dict
#modules
from modules.models import UserBase, UserLogin, User, tweet
app = FastAPI()


#path operations
@app.get(path="/")
def home():
    return {"API": "Working!"}

## users
@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_OK,
    summary="Register a User",
    tags=["users"],
)
def singup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["users"],
)
def login():
    pass

@app.get(
    path="/users",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="show all Users",
    tags=["users"],
)
def show_all_users():
    pass

@app.get(
    path="/users/{user.id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["users"],
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user.id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["users"],
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user.id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["users"],
)
def update_a_user():
    pass


##tweets

