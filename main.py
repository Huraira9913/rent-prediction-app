from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib

# ------------------ APP ------------------
app = FastAPI(title="Rent Prediction API")

# ------------------ CORS ------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ LOAD MODEL ------------------
model = joblib.load("rent_model.pkl")

# ------------------ LOAD FRONTEND ------------------
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# ------------------ INPUT SCHEMA ------------------
class HouseInput(BaseModel):
    city_center_distance_km: float
    furnished: int
    house_size_sqft: float
    num_balconies: int

# ------------------ ROUTES ------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return html_content

@app.post("/predict")
def predict_rent(data: HouseInput):
    X = [[
        data.city_center_distance_km,
        data.furnished,
        data.house_size_sqft,
        data.num_balconies
    ]]
    prediction = model.predict(X)[0]
    return {"predicted_rent": int(prediction)}
