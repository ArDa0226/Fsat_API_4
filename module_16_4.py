from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int
@app.get('/user')
async def get_all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found.')
    return edit_user

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        del_user = users.pop(user_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
    return del_user



