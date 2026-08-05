"""
===========================================
Chapter 07
Create Model
===========================================
"""

from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100)
    )

    last_name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(20)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )