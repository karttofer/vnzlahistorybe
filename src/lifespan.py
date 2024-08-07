from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from dotenv import dotenv_values

config = dotenv_values(".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(config["ATLAS_URL"])
    app.database = app.mongodb_client["sample_mflix"]

    yield
