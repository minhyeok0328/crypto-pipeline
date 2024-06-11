from dependency_injector import containers, providers

from app.websocket.websocket_service import WebSocketService

class WebSocketModule(containers.DeclarativeContainer):
    websocket_service = providers.Singleton(WebSocketService)