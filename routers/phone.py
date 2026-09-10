from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db_connection
from crud import phone as phone_crud
from schemas.phone import (
    PhoneCreate,
    PhoneUpdate,
    PhoneResponse
)


router = APIRouter(
    prefix="/phones",
    tags=["Phones"]
)

# Endpoint for CREATE Phone
@router.post(
    "/",
    response_model=PhoneResponse
)
def create_phone(
    phone: PhoneCreate,
    db: Session = Depends(get_db_connection)
):
    result = phone_crud.create_phone(
        db,
        phone
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if result == "already_exists":
        raise HTTPException(
            status_code=400,
            detail="Phone number already exists"
        )

    return result

# Endpoint for GET all Phones
@router.get(
    "/",
    response_model=list[PhoneResponse]
)
def get_phones(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db_connection)
):
    return phone_crud.get_phones(
        db,
        skip,
        limit
    )

# Endpoint for GET Phone by ID
@router.get(
    "/{phone_id}",
    response_model=PhoneResponse
)
def get_phone(
    phone_id: int,
    db: Session = Depends(get_db_connection)
):
    phone = phone_crud.get_phone(
        db,
        phone_id
    )

    if not phone:
        raise HTTPException(
            status_code=404,
            detail="Phone not found"
        )

    return phone

# Endpoint for PUT Phone
@router.put(
    "/{phone_id}",
    response_model=PhoneResponse
)
def update_phone(
    phone_id: int,
    phone: PhoneUpdate,
    db: Session = Depends(get_db_connection)
):
    result = phone_crud.update_phone(
        db,
        phone_id,
        phone
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Phone not found"
        )

    if result == "already_exists":
        raise HTTPException(
            status_code=400,
            detail="Phone number already exists"
        )

    return result

# Endpoint for DELETE Phone
@router.delete("/{phone_id}")
def delete_phone(
    phone_id: int,
    db: Session = Depends(get_db_connection)
):
    phone = phone_crud.delete_phone(
        db,
        phone_id
    )

    if not phone:
        raise HTTPException(
            status_code=404,
            detail="Phone not found"
        )

    return {
        "message": "Phone deleted successfully"
    }