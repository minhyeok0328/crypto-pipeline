import asyncio
from dependency_injector.wiring import inject, Provide

from app import AppContainer

@inject
async def main() -> None:
    print('test')

if __name__ == "__main__":
    container = AppContainer()
    container.wire(modules=[__name__])

    asyncio.run(main())
