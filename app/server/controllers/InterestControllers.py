from fastapi import File, UploadFile

async def predict_from_csv_file(csv_file:UploadFile = File(...)):
    print(csv_file.content_type)
    