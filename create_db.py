from models import Student,Course
from core.database import base,engine

base.metadata.create_all(bind=engine)

print("Database created successfully")