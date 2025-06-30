from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

default_users = []

the_app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class Authentication:
    @staticmethod
    def validateCredentials(username: str, password: str) -> bool:
        return any(user.username == username and user.password == password for user in default_users)

    @staticmethod
    def generateToken(username: str) -> str:
        return f'token-{username}'  # Simple token generation for the sake of this example

@the_app.post('/api/users/register')
def register(user: User):
    if any(existing_user.username == user.username for existing_user in default_users):
        raise HTTPException(status_code=400, detail='Username already exists')
    default_users.append(user)
    return {'msg': 'User registered successfully'}

@the_app.post('/api/users/login')
def login(user: User):
    if Authentication.validateCredentials(user.username, user.password):
        token = Authentication.generateToken(user.username)
        return {'token': token}
    raise HTTPException(status_code=401, detail='Invalid credentials')

@the_app.put('/api/users/profile')
def update_profile(user: User):
    for existing_user in default_users:
        if existing_user.username == user.username:
            existing_user.email = user.email
            return {'msg': 'Profile updated successfully'}
    raise HTTPException(status_code=404, detail='User not found')

@the_app.delete('/api/users')
def delete_account(user: User):
    global default_users
    default_users = [existing_user for existing_user in default_users if existing_user.username != user.username]
    return {'msg': 'Account deleted successfully'}
