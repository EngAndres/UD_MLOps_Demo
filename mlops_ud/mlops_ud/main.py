"""
This file contains some web services.
"""

from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def read_root():
    """This service is just a healthcheck endpoint."""
    return {"Hello": "World"}


@api.post("/predict")
def predict():
    """This service returns a prediction value."""
    return {"prediction": "1.0"}
