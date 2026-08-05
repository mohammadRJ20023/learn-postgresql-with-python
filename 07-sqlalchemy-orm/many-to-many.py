from sqlalchemy import (
    create_engine,
    String,
    Integer,
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


class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_name: Mapped[str] = mapped_column(String(100))

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order"
    )


class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    price: Mapped[int] = mapped_column(Integer)

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )


class OrderItem(Base):

    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id")
    )

    quantity: Mapped[int] = mapped_column(Integer)

    price: Mapped[int] = mapped_column(Integer)

    order: Mapped["Order"] = relationship(
        back_populates="items"
    )

    product: Mapped["Product"] = relationship(
        back_populates="items"
    )


Base.metadata.create_all(engine)