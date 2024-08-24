import joblib
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.environ.get("MODEL_PATH", "./server/assets/model.h5")

class ChurnModel:
    
    def __init__(self) -> None:
        print(MODEL_PATH)
        self.model = self.__load_model_from_path(MODEL_PATH)
        
    @staticmethod
    def __load_model_from_path(path):
        model = joblib.load(path)
        return model

    def predict(
        self, 
        data,
        #return_option = "prob",
    ):
        df = pd.DataFrame(data)
        prediction = self.model.predict(df)
        return prediction