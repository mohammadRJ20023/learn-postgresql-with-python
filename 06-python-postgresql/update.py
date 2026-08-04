"""
===========================================
Chapter 06
Update Data
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
UPDATE users
SET
    first_name = %s,
    last_name = %s,
    email = %s,
    phone = %s
WHERE id = %s;
"""

user = (
    "Mohammad",
    "Jafari",
    "m.jafari@example.com",
    "09129998877",
    1
)

cursor.execute(query, user)

connection.commit()

print(f"{cursor.rowcount} row updated ✅")

cursor.close()
connection.close()