from pydantic import BaseModel, Field
from typing import Optional

class UserSchema(BaseModel):
    id: str = Field(..., alias="_id")
    interest:float = Field(..., lt=1.0, gt=0.0)
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example" : {
                "id" : "23456789tyuio",
                "interest" : 0.5
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message" : message
    }
    
def ErrorResponseModel(error, code, message):
    return {
        "error" : error,
        "code" : code, 
        "message" : message,
    }