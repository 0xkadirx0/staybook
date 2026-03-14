from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms = [
    {"id": 1, "name": "Standard Room", "price": 100},
    {"id": 2, "name": "Deluxe Room", "price": 150},
    {"id": 3, "name": "Suite", "price": 250},
]

@app.get("/")
def read_root():
    return {"message": "StayBook API running"}

@app.get("/rooms")
def get_rooms():
    return rooms

@app.get("/recommend")
def recommend_room(budget: int):
    
    if budget < 120:
        return {"recommended": "Standard Room"}

    elif budget < 200:
        return {"recommended": "Deluxe Room"}

    else:
        return {"recommended": "Suite"}
