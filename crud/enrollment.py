from sqlalchemy.orm import Session

from models.enrollment import Enrollment
from models.student import Student
from models.course import Course
from schemas.enrollment import EnrollmentCreate, EnrollmentUpdate

# Create enrollment for student by national_id in specific course by id
def create_enrollment(
    db: Session,
    data: EnrollmentCreate
):
    student = (
        db.query(Student)
        .filter(Student.national_id == data.student_id)
        .first()
    )

    if not student:
        return None

    course = (
        db.query(Course)
        .filter(Course.id == data.course_id)
        .first()
    )

    if not course:
        return None

    existing = (
        db.query(Enrollment)
        .filter(
            Enrollment.student_id == data.student_id,
            Enrollment.course_id == data.course_id
        )
        .first()
    )

    if existing:
        return "already_exists"

    enrollment = Enrollment(
        student_id=data.student_id,
        course_id=data.course_id,
        grade=data.grade,
        enrollment_date=data.enrollment_date
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment

# GET specific enrollment
def get_enrollment(
    db: Session,
    enrollment_id: int
):
    return (
        db.query(Enrollment)
        .filter(Enrollment.id == enrollment_id)
        .first()
    )

# GET all enrollments
def get_enrollments(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Enrollment)
        .offset(skip)
        .limit(limit)
        .all()
    )

# UPDATE specific enrollment data
def update_enrollment(
    db: Session,
    enrollment_id: int,
    data: EnrollmentUpdate
):
    enrollment = get_enrollment(db, enrollment_id)

    if not enrollment:
        return None

    enrollment.grade = data.grade
    enrollment.enrollment_date = data.enrollment_date

    db.commit()
    db.refresh(enrollment)

    return enrollment

# DELETE enrollment
def delete_enrollment(
    db: Session,
    enrollment_id: int
):
    enrollment = get_enrollment(db, enrollment_id)

    if not enrollment:
        return None

    db.delete(enrollment)
    db.commit()

    return enrollment