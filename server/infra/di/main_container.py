from dependency_injector import containers, providers

from core.settings import settings

from domain.services import UserService, StoreService

from infra.database.manager import DataBaseManager
from infra.repository import UserRepository, StoreRepository


class MainContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['api.v1.routes.user_route', 'api.v1.routes.store_route'])

    db = providers.Singleton(DataBaseManager, url=str(settings.db.url))

    user_repository = providers.Factory(
        UserRepository
    )
    store_repository = providers.Factory(
        StoreRepository
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
        store_repository=store_repository,
    )
    store_service = providers.Factory(
        StoreService,
        store_repository=store_repository,
    )