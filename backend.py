from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Store users in memory (temporary database)
users = []

# Define User model
class User(BaseModel):
    name: str
    age: int

# API to add a user
@app.post("/add_user/")
async def add_user(user: User):
    users.append(user)
    return {"message": "User added successfully"}

# API to get all users
@app.get("/get_users/", response_model=List[User])
async def get_users():
    return users
