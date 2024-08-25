from fastapi import APIRouter, Body, File, UploadFile,Depends
from fastapi.encoders import jsonable_encoder
import csv
import io

from ..authentication.jwttoken import verify_jwt_token
from ..models.User import UserSchema
from ..handlers.user_handler import add_user
from ..controllers.InterestControllers import predict_from_csv_file

router = APIRouter()

@router.post("/update")
async def update_using_csv(csv_file: UploadFile = File(...), user_id: str = Depends(verify_jwt_token)):
    await predict_from_csv_file(user_id, csv_file)
    return {"status":"success"}

@router.post("/add-user")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return new_user
    