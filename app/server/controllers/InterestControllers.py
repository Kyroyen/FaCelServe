from bson.objectid import ObjectId

from ..database import user_database
from ..serializers.user_serializer import userReponseEntity

user_collection = user_database.get_collection("users_collection")

async def retrieve_user(id:str):
    user = await user_database.find_one({"_id": ObjectId(id)})
    if user:
        return userReponseEntity(user)
