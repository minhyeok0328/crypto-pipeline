import asyncio
from dependency_injector.wiring import inject, Provide

from app import AppContainer

async def main() -> None:
    container = AppContainer()
    container.wire(modules=[__name__])

    bybit = container.exchange_module.bybit
    
    async def run_bybit():
        bybit()
    
    await asyncio.gather(
        run_bybit() # 임시
    )
    print('Exchanges are running')

if __name__ == "__main__":
    asyncio.run(main())
