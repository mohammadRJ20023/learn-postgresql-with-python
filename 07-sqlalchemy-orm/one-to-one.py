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

    profile: Mapped["Profile"] = relationship(
        back_populates="user"
    )


class Profile(Base):

    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)

    bio: Mapped[str] = mapped_column(String(255))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    user: Mapped["User"] = relationship(
        back_populates="profile"
    )


Base.metadata.create_all(engine)