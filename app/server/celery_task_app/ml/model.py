from tensorflow.keras.models import load_model
from fastapi import File, UploadFile
import pandas as pd
import numpy as np
from io import StringIO
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.environ.get("MODEL_PATH", "./assets/haarcb.keras")

class ChurnModel:
    N_FEATURES = 3
    TIME_PERIOD = 50
    STEP_DISTANCE = 40
    dropped_cols = ["time", "seconds_elapsed"]
    
    def __init__(self) -> None:
        self.model = self.__load_model_from_path(MODEL_PATH)
        
    @staticmethod
    def __load_model_from_path(path):
        model = load_model(MODEL_PATH)
        return model
    
    @classmethod
    async def __segmentize(cls, df:pd.DataFrame):
        time_steps = cls.TIME_PERIOD
        step = cls.STEP_DISTANCE
        segments = []
        for i in range(0, len(df) - time_steps, step):
            xs = df['x'].values[i:i+time_steps]
            ys = df['y'].values[i:i+time_steps]
            zs = df['z'].values[i:i+time_steps]

            segments.append([xs, ys, zs])

        reshaped_segments = np.asarray(segments, dtype=np.float32).reshape(-1, time_steps, cls.N_FEATURES)

        return reshaped_segments
    
    async def read_file(self, file):
        return await file.read()
        
    @classmethod
    async def _format_data(cls, data) -> pd.DataFrame:
        data_str = data.decode("utf-8")
        data_io = StringIO(data_str)
        df = pd.read_csv(data_io)
        df.drop(columns=cls.dropped_cols, inplace=True, axis = 1)
        return df
    
    def _predict(
        self, 
        data
    ):
        prediction = self.model.predict(data)
        return prediction
    
    async def aggregate_result(
        self,
        results
    ):
        np_res = np.median(results)
        int_res = float(np_res)
        return int_res
    
    async def predict(
        self,
        file: UploadFile = File(...),
    ):
        uprocessed_data = await self.read_file(file)
        pd_data: pd.DataFrame = await self._format_data(uprocessed_data)
        processed_data = await self.__segmentize(pd_data)
        result = self._predict(processed_data)
        return await self.aggregate_result(result)
    