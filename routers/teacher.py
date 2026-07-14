from fastapi import APIRouter 
from schemas.teacher import Teacher
from repositories. teacher import(
    add_teacher,
    get_teachers,
    get_teacher_by_id,
    update_teacher,
    delete_teacher
)

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.post("")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.course_id, teacher.email, teacher.country, teacher.id_number)
    return {"message": "Teacher registered successfully!", "teacher": teacher}

@router.get("")
def get_all_teachers():
    teachers = get_teachers()
    return teachers

@router.get("/{id}")
def teacher_details(id: int):
    teacher = get_teacher_by_id(id)
    return teacher

@router.put("/{id}")
def edit_teacher(id: int, teacher: Teacher):
    update_teacher(id, teacher.name, teacher.course_id, teacher.email, teacher.country, teacher.id_number)
    return {"message": "Teacher updated successfully"}

@router.delete("/{id}")
def remove_teacher(id: int):
    delete_teacher(id)
    return {"message": "Teacher deleted successfully"}