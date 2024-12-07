from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict



class ProductEntity(BaseModel):
    id: int
    product_id: str
    product_name: str
    product_price: int


class StoreEntity(BaseModel):
    products: Optional[List[ProductEntity]]