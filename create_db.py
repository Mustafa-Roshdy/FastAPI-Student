from core.database import engine, base

from models.student import Student
from models.course import Course
from models.enrollment import Enrollment
from models.phone import Phone


base.metadata.create_all(bind=engine)

print("Database created successfully")