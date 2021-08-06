import sqlite3


def drop_table():
    with sqlite3.connect('users.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS users;""")
    return True


def create_db():
    with sqlite3.connect('users.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
        c.execute(table)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()