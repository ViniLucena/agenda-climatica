from fastapi import FastAPI, HTTPException
from backend.weather import get_weather

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/weather")
def weather(city: str):
    return get_weather(city)
    