from bson.objectid import ObjectId

from ..database import user_database
from ..serializers.user_serializer import userReponseEntity

from ..handlers.student_handler import student_collection

user_collection = user_database.get_collection("user_collection")

def user_helper(user):
    return {
        "id" : str(user['_id']),
        "interest" : user["interest"],
    }

async def update_user(id:str, data:dict):
    updated_user = await user_collection.find_one_and_update(
        {
            "_id" : ObjectId(id)
        },
        {
            "$set" : data
        }
    )
    return True

async def add_user(user_data:dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id":user.inserted_id})
    return user_helper(new_user)

async def retrieve_user(id:str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return userReponseEntity(user)
    return None
