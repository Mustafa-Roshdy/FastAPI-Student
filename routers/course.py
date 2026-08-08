from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db_connection
from crud import course as course_crud
from schemas.course import CourseCreate, CourseResponse


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

# Endpoint for CREATE Course
@router.post("/",response_model=CourseResponse)
def create_course(course: CourseCreate,db: Session = Depends(get_db_connection)):

    return course_crud.create_course(db, course)

# Endpoint for GET_ALL Courses
@router.get("/",response_model=list[CourseResponse])
def get_courses(skip: int = 0,limit: int = 100,db: Session = Depends(get_db_connection)):

    return course_crud.get_courses(db,skip,limit)

# Endpoint for GET Course
@router.get("/{course_id}",response_model=CourseResponse)
def get_course(course_id: int,db: Session = Depends(get_db_connection)):
    course = course_crud.get_course(db,course_id)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course

# Endpoint for UPDATE Course
@router.put("/{course_id}",response_model=CourseResponse)
def update_course(course_id: int,course: CourseCreate,db: Session = Depends(get_db_connection)):

    updated_course = course_crud.update_course(db,course_id,course)

    if not updated_course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated_course

# Endpoint for DELETE Course
@router.delete("/{course_id}")
def delete_course(course_id: int,db: Session = Depends(get_db_connection)):

    course = course_crud.delete_course(db,course_id)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "message": "Course deleted successfully"
    }