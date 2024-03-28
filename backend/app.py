from pydantic import BaseModel
import pymongo
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["prity"]  # database name here
collection = db["users"]


class User(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str


def save_user_to_database(user: User):
    collection.insert_one(user.dict())


def is_username_unique_in_database(username: str):
    user = collection.find_one({"username": username})
    return user is None


def is_email_unique_in_database(email: str):
    user = collection.find_one({"email": email})
    return user is None


def is_phone_unique_in_database(phone_number: str):
    user = collection.find_one({"phone_number": phone_number})
    return user is None


def is_valid_username_length(username: str):
    return len(username) > 5


def is_valid_password_length(password: str, confirm_password: str):
    return len(password) > 6 and password == confirm_password


def is_valid_phone_number_length(phone_number: str):
    return len(phone_number) == 11


@app.get("/")
async def read_root():
    return {"message": "Hello, It's my App!"}


@app.post("/register/")
async def register_user(user: User):
    if not is_valid_username_length(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username should have more than 5 characters.")

    if not is_email_unique_in_database(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists.")

    if not is_phone_unique_in_database(user.phone_number):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone number already exists.")

    if not is_valid_phone_number_length(user.phone_number):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone number should have exactly 11 digits.")

    if not is_username_unique_in_database(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists.")

    save_user_to_database(user)
    return {"message": "User registered successfully"}
