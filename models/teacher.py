from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course_id TEXT,
            email TEXT NOT NULL,
            country TEXT NOT NULL,
            id_number INTEGER NOT NULL,
            FOREIGN KEY(course_id) REFERENCES courses(course_code) ON DELETE SET NULL
        )''')
