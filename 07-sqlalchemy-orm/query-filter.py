"""
===========================================
Chapter 07
Query And Filter
===========================================
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Product


DATABASE_URL = (
    "postgresql+psycopg://postgres:pg_82.dev@localhost:5432/bookstore"
)


engine = create_engine(
    DATABASE_URL,
    echo=True
)


# =========================
# GET ALL PRODUCTS
# =========================

with Session(engine) as session:

    query = select(Product)

    result = session.execute(query)

    products = result.scalars().all()

    for product in products:
        print(
            product.id,
            product.name,
            product.price
        )


# =========================
# FILTER
# =========================

with Session(engine) as session:

    query = select(Product).where(
        Product.price > 1000
    )

    result = session.execute(query)

    products = result.scalars().all()

    for product in products:
        print(product.name)


# =========================
# SEARCH
# =========================

with Session(engine) as session:

    query = select(Product).where(
        Product.name.ilike("%phone%")
    )

    result = session.execute(query)

    products = result.scalars().all()

    for product in products:
        print(product.name)


# =========================
# ORDER BY
# =========================

with Session(engine) as session:

    query = select(Product).order_by(
        Product.price.desc()
    )

    result = session.execute(query)

    products = result.scalars().all()

    for product in products:
        print(
            product.name,
            product.price
        )


# =========================
# PAGINATION
# =========================

with Session(engine) as session:

    query = (
        select(Product)
        .limit(10)
        .offset(0)
    )

    result = session.execute(query)

    products = result.scalars().all()

    for product in products:
        print(product.name)