from dependency_injector import containers, providers

from domain.services import UserService, StoreService

from infra.repository import UserRepository, StoreRepository
from infra.clients import ApiV1Client, HTTPClient


class MainContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['api.handlers'])

    http_client = providers.Singleton(HTTPClient)
    api_v1_client = providers.Singleton(
        ApiV1Client,
        http_client=http_client,
    )

    user_repository = providers.Factory(
        UserRepository,
        api_client=api_v1_client,
    )
    store_repository = providers.Factory(
        StoreRepository,
        api_client=api_v1_client,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
    store_service = providers.Factory(
        StoreService,
        store_repository=store_repository,
    )