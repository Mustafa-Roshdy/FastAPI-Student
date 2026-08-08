from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db_connection
from crud import student as student_crud
from schemas.student import StudentCreate, StudentResponse


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Endpoint for CREATE Student
@router.post("/",response_model=StudentResponse)
def create_student(student: StudentCreate,db: Session = Depends(get_db_connection)):

    return student_crud.create_student(db,student)

# Endpoint for GET_ALL Students
@router.get("/",response_model=list[StudentResponse])
def get_students(skip: int = 0,limit: int = 100,db: Session = Depends(get_db_connection)):

    return student_crud.get_students(db,skip,limit)

# Endpoint for GET Student
@router.get("/{student_id}",response_model=StudentResponse)
def get_student(student_id: int,db: Session = Depends(get_db_connection)):

    student = student_crud.get_student(db,student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# Endpoint for UPDATE Student
@router.put("/{student_id}",response_model=StudentResponse)
def update_student(student_id: int,student: StudentCreate,db: Session = Depends(get_db_connection)):

    updated_student = student_crud.update_student(db,student_id,student)

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student

# Endpoint for DELETE Student
@router.delete("/{student_id}")
def delete_student(student_id: int,db: Session = Depends(get_db_connection)):

    student = student_crud.delete_student(db,student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }