from fastapi import APIRouter 
from schemas.student import Student
from repositories.student import(
    add_student,
    get_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter(prefix="/students", tags=["students"])

@router.post("")
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "User registered successfully!", "student": student}

@router.get("")
def get_all_students():
    students = get_students()
    return students

@router.get("/{id}")
def student_details(id: int):
    student = get_student_by_id(id)
    return student

@router.put("/{id}")
def edit_student(id: int, student: Student):
    update_student(id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully"}

@router.delete("/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": "Student deleted successfully"}