rooms = [
    {"id": 1, "name": "Standard Room", "price": 100},
    {"id": 2, "name": "Deluxe Room", "price": 150},
    {"id": 3, "name": "Suite", "price": 250}
]


def get_rooms():
    return rooms


def recommend_room(budget):
    for room in rooms:
        if room["price"] <= budget:
            return room

    return {"message": "No rooms available"}
