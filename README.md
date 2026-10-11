# Rent Prediction App

Machine Learning based web application that predicts house rent using a trained model served via FastAPI.

## Features

- FastAPI backend exposing a `/predict` endpoint
- Simple HTML frontend for user input
- Model loaded with joblib
- Accepts features: distance from city center, furnished status, house size, number of balconies

## Tech Stack

- Python
- FastAPI
- scikit-learn / joblib
- HTML / CSS

## Project Structure

```
rent-prediction-app/
├── main.py          # FastAPI application
├── index.html       # Frontend interface
├── rent_model.pkl   # Trained model (required)
└── README.md
```

## Setup & Run

```bash
# Install dependencies
pip install fastapi uvicorn joblib scikit-learn pydantic

# Make sure rent_model.pkl is present in the project root

# Run the API
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## API

**POST /predict**

```json
{
  "city_center_distance_km": 5.2,
  "furnished": 1,
  "house_size_sqft": 1200,
  "num_balconies": 2
}
```

Response:
```json
{
  "predicted_rent": 45000
}
```

## Author

Muhammad Abu Huraira  
https://github.com/Huraira9913
