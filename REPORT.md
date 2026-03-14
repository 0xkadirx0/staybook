# StayBook - Hotel Room Recommendation System

## Project Description

StayBook is a simple hotel room reservation and recommendation web application.  
The goal of this project is to demonstrate how modern web technologies can be used together to build a small full-stack system.

The system allows users to view available hotel rooms and receive recommendations based on their budget.

This project was developed as part of the **SWE314 Web Programming course**.

---

## Business Problem

Hotels need a simple system that allows customers to:

- View available rooms
- Compare prices
- Receive room recommendations based on their budget

This system provides a lightweight solution that demonstrates how such functionality can be implemented using modern web technologies.

---

# Technologies Used

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- FastAPI

## Other Concepts Applied
- REST API
- Fetch API
- Client–Server Architecture
- JSON data exchange
- AI-based recommendation logic (simple rule-based system)

---

# System Architecture

The system consists of two main parts.

## 1. Frontend

The frontend is built using **HTML, CSS, and JavaScript**.

Pages included:

- `index.html` – Main homepage
- `rooms.html` – Displays available rooms

JavaScript uses the **Fetch API** to retrieve room data dynamically from the backend API.

---

## 2. Backend

The backend is built using **Python FastAPI**.

It exposes REST API endpoints that allow the frontend to retrieve room information and receive recommendations.

---

## Available API Endpoints

### GET `/rooms`

Returns a list of available rooms and their prices.

Example response:

```json
[
  { "id": 1, "name": "Standard Room", "price": 100 },
  { "id": 2, "name": "Deluxe Room", "price": 150 },
  { "id": 3, "name": "Suite", "price": 250 }
]
```

---

### GET `/recommend?budget=VALUE`

Returns a recommended room based on the user's budget.

Example request:

```
/recommend?budget=150
```

Example response:

```json
{
  "name": "Deluxe Room",
  "price": 150
}
```

---

# AI Recommendation Logic

A simple rule-based recommendation system was implemented.

Rules used:

- Budget < 120 → Standard Room
- Budget < 200 → Deluxe Room
- Budget ≥ 200 → Suite

This demonstrates a simple AI-style decision system integrated into the web application.

---

# Project Repository Structure

```
staybook
│
├ index.html
├ rooms.html
├ style.css
│
├ main.py
├ database.py
├ models.py
├ schemas.py
├ services.py
│
├ README.md
├ REPORT.md
├ requirements.txt
│
└ responsibilities/
```

---

# Conclusion

This project demonstrates how multiple web technologies can be combined to build a small full-stack system.

The system integrates **frontend development, backend API development, and a simple AI recommendation logic**.

It demonstrates the practical application of concepts learned in the **SWE314 Web Programming course**.
