# Deps
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

# Routes
from src.routes.get import get_router
from src.routes.post import post_router
from src.routes.delete import delete_router
from src.routes.welcome import get_welcome
from src.routes.put import put_router

# Connectors
from src.lifespan import lifespan

# CONFIGS
config = dotenv_values(".env")
app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ROUTES
app.include_router(get_router)
app.include_router(post_router)
app.include_router(delete_router)
app.include_router(get_welcome)
app.include_router(put_router)
