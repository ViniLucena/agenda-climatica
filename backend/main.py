from fastapi import FastAPI, HTTPException, Query
from backend.weather import get_weather

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/weather")
def weather(city: str = Query(..., min_length= 1, description="Nome da cidade para buscar o clima")):
    weather_data = get_weather(city)
    if "error" in weather_data:
        raise HTTPException(status_code=404, detail=weather_data["error"])
    return weather_data
    