"""
===========================================
Chapter 06
Database Manager
===========================================
"""

import psycopg


connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="bookstore",
    user="postgres",
    password="pg_82.dev"
)


def get_users():

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT *
            FROM users
            ORDER BY id;
        """)

        return cursor.fetchall()


def create_user(first_name, last_name, email, phone):

    with connection.cursor() as cursor:

        cursor.execute(
            """
            INSERT INTO users
            (
                first_name,
                last_name,
                email,
                phone
            )
            VALUES
            (%s,%s,%s,%s)
            """,
            (first_name, last_name, email, phone)
        )

        connection.commit()


def update_user(user_id, first_name):

    with connection.cursor() as cursor:

        cursor.execute(
            """
            UPDATE users
            SET first_name=%s
            WHERE id=%s
            """,
            (first_name, user_id)
        )

        connection.commit()


def delete_user(user_id):

    with connection.cursor() as cursor:

        cursor.execute(
            """
            DELETE FROM users
            WHERE id=%s
            """,
            (user_id,)
        )

        connection.commit()


print(get_users())