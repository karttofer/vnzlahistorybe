# Deps
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from pymongo import MongoClient
from contextlib import asynccontextmanager

# Routes
from src.routes.get import get_router
from src.routes.post import post_router
from src.routes.delete import delete_router

# CONFGIS
config = dotenv_values(".env")
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

    print("Connected to the MongoDB database!")

    yield

    app.mongodb_client.close()
    print("Closed the MongoDB database connection!")


# ROUTES
app.include_router(get_router)
app.include_router(post_router)
app.include_router(delete_router)
