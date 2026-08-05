"""
===========================================
Chapter 07
Session And CRUD
===========================================
"""

from sqlalchemy import create_engine, String, Integer, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


DATABASE_URL = ( "postgresql+psycopg://postgres:pg_82.dev@localhost:5432/bookstore" )


engine = create_engine( DATABASE_URL, echo=True )


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


# CREATE TABLE
Base.metadata.create_all(engine)


# =========================
# CREATE
# =========================

with Session(engine) as session:

    product = Product(
        name="Laptop",
        price=50000
    )

    session.add(product)

    session.commit()

    print("Product created ✅")


# =========================
# READ
# =========================

with Session(engine) as session:

    statement = select(Product)

    products = session.execute(statement)

    for product in products.scalars():

        print(
            product.id,
            product.name,
            product.price
        )


# =========================
# UPDATE
# =========================

with Session(engine) as session:

    product = session.get( Product, 1 )

    if product:

        product.price = 60000

        session.commit()

        print("Product updated ✅")


# =========================
# DELETE
# =========================

with Session(engine) as session:

    product = session.get( Product, 1)

    if product:

        session.delete(product)

        session.commit()

        print("Product deleted ✅")