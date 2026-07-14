from fastapi import APIRouter
from schemas.course import Course
from repositories.course import (
    add_course,
    get_courses,
    get_course_by_id,
    update_course,
    delete_course
)

router= APIRouter (prefix="/courses", tags= ["courses"])

@router.post("")
def register_course(course: Course):
    add_course(course.title, course.course_code, course.credits, course.department, course.description)
    return {"message": "Course created successfully!", "course": course}

@router.get("")
def get_all_courses():
    courses = get_courses()
    return courses

@router.get("/{id}")
def course_details(id: int):
    course = get_course_by_id(id)
    return course

@router.put("/{id}")
def edit_course(id: int, course: Course):
    update_course(id, course.title, course.course_code, course.credits, course.department, course.description)
    return {"message": "Course updated successfully"}

@router.delete("/{id}")
def remove_course(id: int):
    delete_course(id)
    return {"message": "Course deleted successfully"}