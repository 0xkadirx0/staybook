from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import services

app = FastAPI(
    title="StayBook API",
    description="Hotel Room Recommendation System",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "StayBook API running"}

@app.get("/rooms", tags=["Rooms"])
def get_rooms():
    return services.get_rooms()

@app.get("/recommend", tags=["Recommendation"])
def recommend_room(budget: int):
    return services.recommend_room(budget)
