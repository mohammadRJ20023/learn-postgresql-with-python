import psycopg 



connection = psycopg.connect(
    host = "localhost",
    port=5432,
    dbname="bookstore",
    user="postgres",
    password="pg_82.dev"
)
print("Connected Successfully ✅")

connection.close()

print("Connection Closed 🔒")