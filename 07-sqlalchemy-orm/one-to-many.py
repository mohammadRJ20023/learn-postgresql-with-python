"""
===========================================
Chapter 07
Relationships
One To Many Example

User 1 -----> Many Orders
===========================================
"""

from sqlalchemy import (
    create_engine,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)

DATABASE_URL = "postgresql+psycopg://postgres:password@localhost:5432/bookstore"

engine = create_engine(DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    orders: Mapped[list["Order"]] = relationship(
        back_populates="user"
    )


class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(100))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user: Mapped["User"] = relationship(
        back_populates="orders"
    )


Base.metadata.create_all(engine)