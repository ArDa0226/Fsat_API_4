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

@app.post('/user/')
async def create_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user

@app.put('/user/')
async def update_user(user: User) -> User:
    try:
        edit_user = users[user.id - 1]
        edit_user.username = user.username
        edit_user.age = user.age
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found.')
    return edit_user

@app.delete('/user/')
async def delete_user(user: User) -> User:
    try:
        del_user = users.pop(user.id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found.')
    return del_user


print(users)