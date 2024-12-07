from typing import TYPE_CHECKING
from fastapi import APIRouter, Request, Depends, HTTPException

from dependency_injector.wiring import inject, Provide

from infra.di.main_container import MainContainer
from infra.exceptions import AppExceptions

from schemas.main_schemas import (
    StoreAddProductSchema,
    StoreGetProductsSchema,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession
    from domain.services import StoreService


store_router = APIRouter(
    prefix='/api/v1'
)

async def session(request: Request):
    async for session in request.app.db.get_session():
        yield session


@store_router.post('/add/product')
@inject
async def buy_product(
    request: Request,
    data: StoreAddProductSchema,
    service: "StoreService" = Depends(Provide[MainContainer.store_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.add(data.name, data.price, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )

@store_router.get('/get/product')
@inject
async def buy_product(
    request: Request,
    product_id: str,
    service: "StoreService" = Depends(Provide[MainContainer.store_service]),
    session: "AsyncSession" = Depends(session)
):
    print(f'product_id = {product_id}')
    try:
        result = await service.get_product(product_id, session)
        print(result)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
    

@store_router.get('/get/products')
@inject
async def get_products(
    request: Request,
    service: "StoreService" = Depends(Provide[MainContainer.store_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.get_products(session)
        print(result)
        return result
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )