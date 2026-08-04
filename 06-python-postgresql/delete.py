"""
===========================================
Chapter 06
Delete Data
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

cursor = connection.cursor()

query = """
DELETE FROM users
WHERE id = %s;
"""

user_id = (4,)

cursor.execute(query, user_id)

connection.commit()

if cursor.rowcount:
    print("User deleted successfully ✅")
else:
    print("User not found ❌")

cursor.close()
connection.close()