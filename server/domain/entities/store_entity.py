from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class ProductEntity(BaseModel):
    id: Optional[int] = None
    product_id: str
    product_name: str
    product_price: int

    model_config = ConfigDict(
        from_attributes=True
    )
    

class ProductsEntity(BaseModel):
    products: List[ProductEntity]

    model_config = ConfigDict(
        from_attributes=True
    )