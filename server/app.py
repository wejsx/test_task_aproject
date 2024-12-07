import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.routes import store_router, user_router

from infra.di.main_container import MainContainer


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = MainContainer()
    db = container.db()
    await db.create_table()
    app.db = db
    yield
    await app.db.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    title='BOT API',
    version='0.0.1',
    description='API FOR PURCHASES WATERMELON',
    lifespan=lifespan,
)
app.include_router(user_router)
app.include_router(store_router)