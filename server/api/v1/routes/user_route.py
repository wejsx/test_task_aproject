from typing import TYPE_CHECKING
from fastapi import APIRouter, Request, Depends, HTTPException

from dependency_injector.wiring import inject, Provide

from infra.di.main_container import MainContainer
from infra.exceptions import AppExceptions

from schemas.main_schemas import (
    BuyProductSchema,
    AddProductCartSchema,
    DeleteProductCartSchema,
    RegisterSchema,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession
    from domain.services import UserService


user_router = APIRouter(
    prefix='/api/v1'
)

async def session(request: Request):
    async for session in request.app.db.get_session():
        yield session


@user_router.post('/buy/product')
@inject
async def buy_product(
    request: Request,
    data: BuyProductSchema,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.buy_product(data.tg_id, data.product_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
    

@user_router.post('/add/product/cart')
@inject
async def buy_product(
    request: Request,
    data: AddProductCartSchema,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.add_cart(data.tg_id, data.product_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
    

@user_router.post('/delete/product/cart')
@inject
async def buy_product(
    request: Request,
    data: DeleteProductCartSchema,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.delete_product_cart(data.tg_id, data.product_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
    
@user_router.get('/get/purchase')
@inject
async def get_purchase(
    request: Request,
    tg_id: int,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.get_purchase(tg_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
    

@user_router.get('/get/cart')
@inject
async def register(
    request: Request,
    tg_id: int,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.get_cart(tg_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )


@user_router.post('/register')
@inject
async def register(
    request: Request,
    data: RegisterSchema,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.register(data.tg_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )
    

@user_router.get('/get/user')
@inject
async def register(
    request: Request,
    tg_id: int,
    service: "UserService" = Depends(Provide[MainContainer.user_service]),
    session: "AsyncSession" = Depends(session)
):
    try:
        result = await service.get_user(tg_id, session)
        return result 
    except AppExceptions as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.message,
        )