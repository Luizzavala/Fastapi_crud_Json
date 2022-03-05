from fastapi import FastAPI
#modules
from modules.models import UserBase, UserLogin, User, tweet
app = FastAPI()

@app.get(path="/")
def home():
    return {"API": "Working!"}