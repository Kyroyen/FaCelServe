from pydantic import BaseModel, Field
from typing import Optional

class UserSchema(BaseModel):
    interest:float = Field(..., le=1.0, ge=0.0)
    
    class Config:
        schema_extra = {
            "example" : {
                "interest" : 0.5
            }
        }

class UpdateUserModel(BaseModel):
    interest: Optional[float]
    class Config:
        schema_extra = {
            "example" :{
                "interest":"0.5"
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