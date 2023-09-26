from pydantic import BaseModel, EmailStr


class Team(BaseModel):
    team_id: int
    name: str
    scheduling_timezone: str
    email: EmailStr
    slack_channel: str


class User(BaseModel):
    user_id: int
    team_id: int
    name: str
    full_name: str
    phone_number: str
    email: EmailStr


class Duty(BaseModel):
    duty_id: int
    user_id: int
    date: str
    role: str