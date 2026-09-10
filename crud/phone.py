from sqlalchemy.orm import Session

from models.phone import Phone
from models.student import Student
from schemas.phone import PhoneCreate, PhoneUpdate

# Create phone for student by national_id
def create_phone(
    db: Session,
    data: PhoneCreate
):
    student = (
        db.query(Student)
        .filter(Student.national_id == data.student_id)
        .first()
    )

    if not student:
        return None

    existing = (
        db.query(Phone)
        .filter(Phone.phone_number == data.phone_number)
        .first()
    )

    if existing:
        return "already_exists"

    phone = Phone(
        student_id=data.student_id,
        phone_number=data.phone_number
    )

    db.add(phone)
    db.commit()
    db.refresh(phone)

    return phone

# Get specific phone
def get_phone(
    db: Session,
    phone_id: int
):
    return (
        db.query(Phone)
        .filter(Phone.id == phone_id)
        .first()
    )

# Get All phones
def get_phones(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Phone)
        .offset(skip)
        .limit(limit)
        .all()
    )

# Update phone data
def update_phone(
    db: Session,
    phone_id: int,
    data: PhoneUpdate
):
    phone = get_phone(db, phone_id)

    if not phone:
        return None

    existing = (
        db.query(Phone)
        .filter(
            Phone.phone_number == data.phone_number,
            Phone.id != phone_id
        )
        .first()
    )

    if existing:
        return "already_exists"

    phone.phone_number = data.phone_number

    db.commit()
    db.refresh(phone)

    return phone

# Delete phone 
def delete_phone(
    db: Session,
    phone_id: int
):
    phone = get_phone(db, phone_id)

    if not phone:
        return None

    db.delete(phone)
    db.commit()

    return phone


def search_by_phone(
    db: Session,
    phone_number: str
):
    return (
        db.query(Student)
        .join(Phone)
        .filter(Phone.phone_number == phone_number)
        .first()
    )