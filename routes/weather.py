from fastapi import APIRouter
from models.weather import WeatherResponse

router = APIRouter()

@router.get("/", response_model=WeatherResponse)
def get_weather():
    return WeatherResponse(city="Bolton", temp=21, condition="cloudy")

@router.get("/{city}")
def get_weather_by_city(city: str):
    return WeatherResponse(city=city, temp=21, condition="cloudy")