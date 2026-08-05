from sqlalchemy import create_engine, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)


DATABASE_URL = (
    "postgresql+psycopg://postgres:password@localhost:5432/bookstore"
)


engine = create_engine(
    DATABASE_URL,
    echo=True
)


class Base(DeclarativeBase):
    pass


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )


Base.metadata.create_all(engine)


# =========================
# TRANSACTION
# =========================

with Session(engine) as session:

    try:

        user = User(
            name="Ali"
        )


        session.add(user)


        session.commit()


        print(
            "Saved Successfully ✅"
        )


    except Exception as error:


        session.rollback()


        print(
            "Error:",
            error
        )