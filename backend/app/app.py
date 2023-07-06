import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import users
from pymongo import MongoClient

app = FastAPI()

app.include_router(users.router)


@app.on_event("startup")
def startup_db_client():
    mongo_uri = f"mongodb://{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}"
    app.mongodb_client = MongoClient(os.getenv("MONGO_HOST"))
    app.database = app.mongodb_client[os.getenv("DB_NAME")]
    print("Connected to the MongoDB database!")


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/health-check")
async def root():
    return {"message": "ToDoList is up!"}

