from fastapi import File, UploadFile

from ..errors import FileTypeNotACsv
from ..celery_task_app.ml.model import ChurnModel
from ..handlers.user_handler import update_user

async def predict_from_csv_file(user_id: str, csv_file:UploadFile = File(...)):
    if csv_file.content_type!="text/csv":
        raise FileTypeNotACsv
    xf = ChurnModel()
    new_interest = await xf.predict(csv_file)
    await update_user(user_id, {"interest" : new_interest})
    
    