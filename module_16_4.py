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
async def create_user(user: User) -> str:
    user.id = len(users)
    users.append(user)
    return 'User created!'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, user_name: str = Body(), user_age: int = Body()) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = user_name
        edit_user.age = user_age

    except IndexError:
        raise HTTPException(status_code=404, detail='User not found.')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
    except IndexError:
        raise HTTPException(status_code=404, detail='Message not found')
