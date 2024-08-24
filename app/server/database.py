import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.environ.get("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

stud_database = client.students

user_database = client.users

