from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ProductsModel(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=True)
    product_name: Mapped[str] = mapped_column(String(100))
    product_price: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f'<ProductsModel(id={self.id}, product_id={self.product_id}\n' \
        f'product_name={self.product_name}\n' \
        f'product_price={self.product_price})>'
