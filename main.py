from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import services

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "StayBook API running"}


@app.get("/rooms")
def get_rooms():
    return services.get_rooms()


@app.get("/recommend")
def recommend_room(budget: int):
    return services.recommend_room(budget)
