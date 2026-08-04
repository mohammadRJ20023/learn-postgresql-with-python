import psycopg




connection = psycopg.connect(
    host = "localhost",
    port = "5432",
    dbname = "bookstore",
    user="postgres",
    password="pg_82.dev"
    
)

cursor = connection.cursor()


query = """
SELECT * FROM users
"""

cursor.execute(query)

users = cursor.fetchall()

for user in users:
    print(user)
    
cursor.close()
connection.close() 