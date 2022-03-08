import json
from fastapi import Body, FastAPI
from fastapi import status, HTTPException
from typing import List, Dict
from starlette.responses import RedirectResponse
from uuid import uuid4 as uuid
#modules
from modules.models import UserBase, UserLogin, User, Tweet, UserRegister
app = FastAPI()


#path operations
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Redirect to Docs",
    tags=["Index"],
)
def index():
    return RedirectResponse(url="/docs/")
## users
### Register a user
@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"],
)
def singup(user: UserRegister = Body(...
                                     )):
    """**_summary_**</br>
    This function, Create at User new.</br>
    
    **Parameters:** </br>
    user : UserRegister = Body with :</br>
    - user_id</br>
    - email</br>
    - password</br>
    - first_name</br>
    - last_name</br>
    - birth_date </br>
      
    **Return:**</br>
    response with user body: user and verification 201 created a user into json dict
    - user_id</br>
    - email</br>
    - first_name</br>
    - last_name</br>
    - birth_date </br>
    """
    with open("json/users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        #created uuid for new user
        user.user_id = str(uuid()) 
        # transform model that json for work in this
        user_dict = user.dict()
        # castings vars, for havent future problems
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user
 

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"],
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="show all Users",
    tags=["Users"],
)
def show_all_users():
    """**_summary_**</br>
    This path operation show all users in the app</br>
    
    **returns:**</br>
    return a json list witch all users in the app, with the followings keys
    - user_id</br>
    - email</br>
    - first_name</br>
    - last_name</br>
    - birth_date </br>
    """
    with open("json/users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results


### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"],
)
def show_a_user(user_id : str ):
    with open("json/users.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
        for user in users:
            if user["user_id"] == user_id:
                return user
            else:
                raise HTTPException(status_code=404, detail="Item not found") 


### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"],
)
def delete_a_user(user_id : str):
    with open("json/users.json", "r+", encoding="utf-8") as f:
        users = json.loads(f.read())
        for index, user in enumerate(users):
            if user["user_id"] == user_id:
                users.pop(index)
                f.write(json.dumps(users))
                return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")

### Update a user
@app.put(
    path="/users/{user.id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"],
)
def update_a_user():
    pass


##tweets
### Show all tweets
@app.get(
        path="/tweets",
        response_model=List[Tweet],
        status_code= status.HTTP_200_OK,
        summary="show all tweets",
        tags=["Tweets"],         
         )
def show_all_tweets():
    """_summary_: </br>
    This path operation, shows all tweets

    Returns:</br>
        Returns: return a json list with all tweets in the profile
    """
    with open("json/tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

### Created at tweet
@app.post(
    path="/post",
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary="Created at tweet",
    tags=["Tweets"],
)
def post(tweet : Tweet = Body (...,
    )):
    """ **_summary_**</br>
    This path operation post a tweet in the app
        
    **Parameters:** </br>
    tweet: Tweet = request body 

          
    **Return:**</br>
    Response a json with the basic Tweet information:
    - tweet_id : UUID 
    - content: str 
    - created_at: datetime  
    - updated_at: Optional[datetime] 
    - by: User 
    """
    with open("json/tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        # transform model that json for work in this
        tweet_dict = tweet.dict()
        # castings vars, for havent future problems
        tweet_dict["tweet_id"] = str(uuid()) 
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        # if exists, cast
        tweet_dict["updated_at"] =str(tweet_dict["updated_at"])
        ## casting keys with uuid and date format
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary="show a tweet",
    tags=["Tweets"],
)
def show_a_tweet(tweet_id : str ):
    with open("json/tweets.json", "r", encoding="utf-8") as f:
        tweets = json.loads(f.read())
    
    for user in tweets:
        if user["tweet_id"] == tweet_id:
            return user
        else:
            return {"Error404" : "Notfound"} 

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"],
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary="update a tweet",
    tags=["Tweets"],
)
def update_a_tweet():
    pass