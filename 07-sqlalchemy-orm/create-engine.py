from sqlalchemy import create_engine

DATABASE_URL = ("postgresql+psycopg://postgres:pg_82.dev@localhost:5432/bookstore")



engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as connection:
    print("Connected Successfully ✅")