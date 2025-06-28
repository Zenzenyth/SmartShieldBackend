import uvicorn
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from weathertools import *

OPENWEATHER_APIKEY = "dae844ddfd6f64e5675dff334e04e621" #REMOVE BEFORE PUSHING
MAPBOX_APIKEY = ""

class Location(BaseModel):
    latitude: float
    longitude: float

class Response(BaseModel):
    Heat_index: float
    Humidity: int


#TODO add proper response model

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/process_lat_lon", response_model= Response)
def processlatlon(location: Location):
    latitude = location.latitude
    longitude = location.longitude
    weatherAPI(latitude, longitude, OPENWEATHER_APIKEY) #TODO: Proper response model

@app.get("/testget/{testres}/")
def testrun(testres: str = Path(..., description = "Testrun of get function")):
    return testres