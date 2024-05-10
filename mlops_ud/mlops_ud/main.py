"""
This file contains some web services.
"""

# pylint: disable=import-error
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from sklearn.preprocessing import LabelEncoder

from model_ml import MLModel

# pylint: disable=too-few-public-methods
class Passenger(BaseModel):
    """Data Structure for the ML model."""

    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str


api = FastAPI()
model = MLModel()


@api.get("/")
def read_root():
    """This service is just a healthcheck endpoint."""
    return {"Hello": "World"}


@api.post("/predict")
def predict_passenger_survival(passenger: Passenger) -> dict:
    """
    This service returns a prediction value.

    Args:
        passenger (Passenger): The passenger data.

    Returns:
        A dictionaty with the predicted value.
    """
    # Convert input to DataFrame
    input_df = pd.DataFrame([dict(passenger)])

    # Preprocess the data
    input_df["Sex"] = LabelEncoder().fit_transform(input_df["Sex"])
    input_df["Embarked"] = LabelEncoder().fit_transform(
        input_df["Embarked"].astype(str)
    )

    # Make prediction
    prediction = model.prediction(input_df)

    return {"prediction": int(prediction[0])}
