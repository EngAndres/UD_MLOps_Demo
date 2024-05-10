"""
This file has a ML model to predict if some will survive to the titanic disaster.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import xgboost as xgb


class MLModel:
    """Class with a simple xgboost model"""

    def __init__(self):
        self.data = self.preprocessing_data()
        x_train, x_test, y_train, y_test = self.generate_datasets(self.data)
        self.model = self.train_model(x_train, y_train)
        self.evaluate_model(x_test, y_test)

    def preprocessing_data(self):
        """This method makes a simple pre-processing"""
        current_dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(current_dir, "train.csv")
        data = pd.read_csv(data_file_path)

        # Preprocess the data
        data = data.fillna(0)
        data["Sex"] = LabelEncoder().fit_transform(data["Sex"])
        data["Embarked"] = LabelEncoder().fit_transform(data["Embarked"].astype(str))
        return data

    def generate_datasets(self, data: pd.DataFrame) -> tuple:
        """
        This method splits the datasets.

        Args:
            data (pd.DataFrame): The data to be splitted.

        Returns:
            A tuple with the splitted datasets.
        """
        # Split the data into features and target
        x = data.drop(["Survived", "Name", "Ticket", "Cabin", "PassengerId"], axis=1)
        y = data["Survived"]

        # Split the data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=42
        )
        return x_train, x_test, y_train, y_test

    def train_model(self, x_train: pd.DataFrame, y_train: pd.DataFrame) -> object:
        """
        This method trains the model.

        Args:
            x_train (pd.DataFrame): The features of the training dataset.
            y_train (pd.Series): The target of the training dataset.

        Returns:
            An object with the trained model.
        """
        model = xgb.XGBClassifier(use_label_encoder=False)
        model.fit(x_train, y_train)
        return model

    def evaluate_model(self, x_test: pd.DataFrame, y_test: pd.DataFrame):
        """
        This method prints the metrics.

        Args:
            x_test (pd.DataFrame): The features of the test dataset.
            y_test (pd.Series): The target of the test dataset.
        """
        # Predict the test data
        y_pred = self.model.predict(x_test)

        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        print(
            f"Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\nF1: {f1}"
        )

    def prediction(self, input_df: pd.DataFrame) -> int:
        """
        This method makes a prediction.

        Args:
            input_values (list): The values to be predicted.

        Returns:
            An integer with the prediction.
        """
        # Make prediction
        prediction = self.model.predict(input_df)
        return prediction
