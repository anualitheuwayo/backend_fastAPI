from database import get_connection



def add_teacher(name, course_id, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, course_id, email, country, id_number) VALUES (?, ?, ?, ?, ?)',
            (name, course_id, email, country, id_number)
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def get_teacher_by_id(id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers WHERE id = ?', (id,)).fetchone()

def update_teacher(id, name, course_id, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'UPDATE teachers SET name=?, course_id=?, email=?, country=?, id_number=? WHERE id=?',
            (name, course_id, email, country, id_number, id)
        )

def delete_teacher(id):
    with get_connection()as connection:
        connection.execute(
            "DELETE FROM teachers WHERE id=?",
            (id,)
        )