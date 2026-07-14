from database import get_connection


def add_course(title, course_code, credits, department, description):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses (title, course_code, credits, department, description) VALUES (?, ?, ?, ?, ?)',
            (title, course_code, credits, department, description)
        )

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def get_course_by_id(id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses WHERE id = ?', (id,)).fetchone()

def update_course(id, title, course_code, credits, department, description):
    with get_connection() as connection:
        connection.execute(
            'UPDATE courses SET title=?, course_code=?, credits=?, department=?, description=? WHERE id=?',
            (title, course_code, credits, department, description, id)
        )

def delete_course(id):
    with get_connection()as connection:
        connection.execute(
            "DELETE FROM courses WHERE id=?",
        (id,)
        )