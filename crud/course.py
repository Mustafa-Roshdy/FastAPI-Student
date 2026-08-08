from sqlalchemy.orm import Session

from models.course import Course
from schemas.course import CourseCreate

# create course
def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        name=course.name
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course

# get specific course
def get_course(db: Session, course_id: int):
    return (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

# get all courses
def get_courses(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Course)
        .offset(skip)
        .limit(limit)
        .all()
    )


# update course
def update_course(
    db: Session,
    course_id: int,
    course_data: CourseCreate
):
    db_course = get_course(db, course_id)

    if not db_course:
        return None

    db_course.name = course_data.name

    db.commit()
    db.refresh(db_course)

    return db_course

# delete course
def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)

    if not db_course:
        return None

    db.delete(db_course)
    db.commit()

    return db_course