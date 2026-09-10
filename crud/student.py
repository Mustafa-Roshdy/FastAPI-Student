from sqlalchemy.orm import Session, joinedload

from models.student import Student
from schemas.student import StudentCreate

# Create student
def create_student(
    db: Session,
    data: StudentCreate
):
    db_student = Student(
        national_id=data.national_id,
        name=data.name,
        email=data.email
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

# get specific student by national ID
def get_student(
    db: Session,
    national_id: int
):
    return (
        db.query(Student)
        .options(
            joinedload(Student.phones),
            joinedload(Student.enrollments)
        )
        .filter(Student.national_id == national_id)
        .first()
    )

# get all students
def get_all_students(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Student)
        .options(
            joinedload(Student.phones),
            joinedload(Student.enrollments)
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
# search specific student by national ID
def search_student_by_national_id(
    db: Session,
    national_id: int
):
    return get_student(db, national_id)

# search specific student by Email
def search_student_by_email(
    db: Session,
    email: str
):
    return (
        db.query(Student)
        .options(
            joinedload(Student.phones),
            joinedload(Student.enrollments)
        )
        .filter(Student.email == email)
        .first()
    )

# update student
def update_student(
    db: Session,
    national_id: int,
    data: StudentCreate
):
    student = get_student(db, national_id)

    if not student:
        return None

    student.name = data.name
    student.email = data.email

    db.commit()
    db.refresh(student)

    return student


# delete student
def delete_student(
    db: Session,
    national_id: int
):
    student = get_student(db, national_id)

    if not student:
        return None

    db.delete(student)
    db.commit()

    return student

