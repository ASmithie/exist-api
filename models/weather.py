from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temp: float
    condition: str