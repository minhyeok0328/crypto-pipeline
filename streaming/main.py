import asyncio
from dependency_injector.wiring import inject, Provide

from app import AppContainer

async def main() -> None:
    container = AppContainer()
    container.wire(modules=[__name__])

    bybit = container.exchange_module.bybit
    
    await asyncio.gather(
        bybit() # 임시
    )
    print('Exchanges are running')

if __name__ == "__main__":
    asyncio.run(main())
