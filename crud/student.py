from sqlalchemy.orm import Session
from models.student import Student
from schemas.student import StudentCreate

# Create student
def create_student(db:Session,data:StudentCreate):

    db_student=Student(name=data.name,email=data.email,gpa=data.gpa,course_id=data.course_id)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

# get specific student
def get_student(db:Session,id:int):

    return (db.query(Student).filter(Student.id==id).first())

# get all students
def get_all_students(db:Session,skip:int=0,limit:int=100):

    return (db.query(Student).offset(skip).limit(limit).all())

# update student
def update_student(db:Session,student_id:int,data:StudentCreate):

    getStudent=get_student(db,student_id)

    if not getStudent:
        return None

    
    db_student=Student(name=data.name,email=data.email,gpa=data.gpa,course_id=data.course_id)

    getStudent.name=data.name
    getStudent.email=data.email
    getStudent.gpa=data.gpa
    getStudent.course_id=data.course_id

    db.commit()
    db.refresh(getStudent)

    return getStudent


# delete student
def delete_student(db:Session,student_id:int):

    getStudent=get_student(db,student_id)

    if not getStudent:
            return None

    db.delete(getStudent)
    db.commit()

    return getStudent

