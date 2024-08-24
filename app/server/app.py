from fastapi import FastAPI

from server.routes.student_router import router as StudentRouter
from server.routes.interest_router import router as InterestRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(InterestRouter, tags=["Interest"], prefix="/gyro")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

