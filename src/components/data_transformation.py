## to do feature negineeriing nd cleaning of data
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
import sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import oneHotEncoder , StandardScaler

from src.excpetion import CustomException
from src.logger import logging
import os

class DataTransformationConfig:
    preprocessor_object_file_path = os.path.join('artifacts' , "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score" , "reading_score"]
            categorical_columns = [
                "gender",
                "race/ethinicity",
                "parental level of education"
                "lunch"
                "test preparation course"

            ]
            ##create a pipeline for handling missing values
            num_pipeline = Pipeline(
                steps = [
                    ("imputer" , SimpleImputer(Strategy = "median")##handling missing values
                     ("scaler" , StandardScaler()))
                ]
            )

            cat_pipeline = Pipeline(
                    steps=[
                        ("imputer" , SimpleImputer(strategy = "most_frequent")),
                        ("one_hot_encoder" , OneHotEncoder()),
                        ("scaler" , StandardScaler())
                    ]
            )
            logging.info(f"Categorical columns : {categorical_columns}")
            logging.info(f"Numerical columns : {numerical_columns}")

            

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline" , num_pipeline , numerical_columns)
                    ("cat_pipeline" , cat_pipeline , categorical_columns)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e , sys)
    def initiate_data_transformation(self  , train_path , test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read  train and test data completed")
            logging.info("Obtaining preprocessing objecct")

            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math_score"