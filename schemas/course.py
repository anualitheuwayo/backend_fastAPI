from pydantic import BaseModel


class Course(BaseModel):
    title: str
    course_code: str
    credits: int
    department: str
    description: str