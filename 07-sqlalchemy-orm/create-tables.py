
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean


DATABASE_URL = ("postgresql+psycopg://postgres:pg_82.dev@localhost:5432/bookstore")


engine = create_engine(DATABASE_URL, echo=True )


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    price: Mapped[int] = mapped_column(
        Integer
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


Base.metadata.create_all(engine)

print("Tables created successfully ✅")