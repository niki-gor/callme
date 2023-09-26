from pydantic import BaseModel, EmailStr, validator
from datetime import datetime


class TeamCreate(BaseModel):
    name: str
    scheduling_timezone: str
    email: EmailStr
    slack_channel: str


class UserCreate(BaseModel):
    team_id: int
    name: str
    full_name: str
    phone_number: str
    email: EmailStr


class DutyCreate(BaseModel):
    user_id: int
    date: str
    role: str

    @validator("date")
    def is_formated(v):
        format = "%d/%m/%Y"
        datetime.strptime(v, format)
        return v