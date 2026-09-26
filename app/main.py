from . import models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# Apply schema changes with `alembic upgrade head` before starting the app.

app = FastAPI()

# public api
origins=["*"]

# private api 
# origins=["https://solutionstudio.bd/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for post and user endpoints
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}



