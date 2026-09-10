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
@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db_connection)
):
    try:
        return student_crud.create_student(db, student)

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="National ID or email already exists"
        )

# Endpoint for GET_ALL Students
@router.get("/", response_model=list[StudentResponse])
def get_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db_connection)
):
    return student_crud.get_all_students(db, skip, limit)


# Endpoint for GET/Search Student by national ID
@router.get(
    "/search/national-id/{national_id}",
    response_model=StudentResponse
)
def search_by_national_id(
    national_id: str,
    db: Session = Depends(get_db_connection)
):
    student = student_crud.search_student_by_national_id(
        db,
        national_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Endpoint for GET/Search Student by Email
@router.get(
    "/search/email",
    response_model=StudentResponse
)
def search_by_email(
    email: str,
    db: Session = Depends(get_db_connection)
):
    student = student_crud.search_student_by_email(
        db,
        email
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Endpoint for GET Student by national ID
@router.get(
    "/{national_id}",
    response_model=StudentResponse
)
def get_student(
    national_id: str,
    db: Session = Depends(get_db_connection)
):
    student = student_crud.get_student(
        db,
        national_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# Endpoint for UPDATE Student
@router.put(
    "/{national_id}",
    response_model=StudentResponse
)
def update_student(
    national_id: str,
    student: StudentCreate,
    db: Session = Depends(get_db_connection)
):
    updated_student = student_crud.update_student(
        db,
        national_id,
        student
    )

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student

# Endpoint for DELETE Student
@router.delete("/{national_id}")
def delete_student(
    national_id: str,
    db: Session = Depends(get_db_connection)
):
    student = student_crud.delete_student(
        db,
        national_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }