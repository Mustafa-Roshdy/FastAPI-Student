from pydantic import BaseModel, ConfigDict


class PhoneCreate(BaseModel):
    student_id: str
    phone_number: str


class PhoneUpdate(BaseModel):
    phone_number: str


class PhoneResponse(BaseModel):
    id: int
    student_id: str
    phone_number: str

    model_config = ConfigDict(from_attributes=True)