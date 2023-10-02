from datetime import datetime

from pydantic import BaseModel, EmailStr, validator


class Shift(BaseModel):
    date: datetime
    role: str

    @validator("date", pre=True)
    def is_formated(cls, v):
        format = "%d/%m/%Y"
        return datetime.strptime(v, format)
    
    class Config:
        json_encoders = {
            datetime: lambda d: int(d.timestamp())
        }


class User(BaseModel):
    name: str
    full_name: str
    phone_number: str
    email: EmailStr
    duty: list[Shift]


class Team(BaseModel):
    name: str
    scheduling_timezone: str
    email: EmailStr
    slack_channel: str
    users: list[User]


class Teams(BaseModel):
    teams: list[Team]