from pydantic import BaseModel


class Teacher(BaseModel):
    name: str
    course_id: int
    email: str
    country: str
    id_number: int