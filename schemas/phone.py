from pydantic import BaseModel, ConfigDict


class PhoneCreate(BaseModel):
    student_id: int
    phone_number: str


class PhoneUpdate(BaseModel):
    phone_number: str


class PhoneResponse(BaseModel):
    id: int
    student_id: int
    phone_number: str

    model_config = ConfigDict(from_attributes=True)