"""
===========================================
Chapter 06
Insert Data
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
INSERT INTO users (
    first_name,
    last_name,
    email,
    phone
)
VALUES (%s, %s, %s, %s);
"""

user = (
    "Mohammadreza",
    "Jafari",
    "mohammadreza@example.com",
    "09125557788"
)

cursor.execute(query, user)

connection.commit()

print("User created successfully ✅")

cursor.close()
connection.close()