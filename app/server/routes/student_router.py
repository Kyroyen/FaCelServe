from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.handlers.student_handler import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully")
