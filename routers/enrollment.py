from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db_connection
from crud import enrollment as enrollment_crud
from schemas.enrollment import (
    EnrollmentCreate,
    EnrollmentUpdate,
    EnrollmentResponse
)


router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

# Endpoint for CREATE Enrollment
@router.post(
    "/",
    response_model=EnrollmentResponse
)

def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db_connection)
):
    result = enrollment_crud.create_enrollment(
        db,
        enrollment
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student or Course not found"
        )

    if result == "already_exists":
        raise HTTPException(
            status_code=400,
            detail="Student is already enrolled in this course"
        )

    return result

# Endpoint for GET Enrollments
@router.get(
    "/",
    response_model=list[EnrollmentResponse]
)
def get_enrollments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db_connection)
):
    return enrollment_crud.get_enrollments(
        db,
        skip,
        limit
    )

# Endpoint for GET Enrollment by ID
@router.get(
    "/{enrollment_id}",
    response_model=EnrollmentResponse
)
def get_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db_connection)
):
    enrollment = enrollment_crud.get_enrollment(
        db,
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment

# Endpoint for PUT Enrollment
@router.put(
    "/{enrollment_id}",
    response_model=EnrollmentResponse
)
def update_enrollment(
    enrollment_id: int,
    enrollment: EnrollmentUpdate,
    db: Session = Depends(get_db_connection)
):
    updated = enrollment_crud.update_enrollment(
        db,
        enrollment_id,
        enrollment
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return updated

# Endpoint for DELETE Enrollment
@router.delete("/{enrollment_id}")
def delete_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db_connection)
):
    enrollment = enrollment_crud.delete_enrollment(
        db,
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return {
        "message": "Enrollment deleted successfully"
    }