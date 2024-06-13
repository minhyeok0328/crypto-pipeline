from dependency_injector import containers, providers

from app.websocket.websocket_service import WebSocketService


class WebSocketContainer(containers.DeclarativeContainer):
    websocket_service_factory = providers.Factory(WebSocketService)
