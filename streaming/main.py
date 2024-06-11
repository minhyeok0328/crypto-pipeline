import asyncio
from dependency_injector.wiring import inject, Provide

from app import AppContainer

async def main() -> None:
    container = AppContainer()
    container.wire(modules=[__name__])

    bybit = container.exchange_module.bybit()

    async def run_crypto():
        await bybit.run()

    await asyncio.gather(
        run_crypto() # 임시
    )

if __name__ == "__main__":
    asyncio.run(main())
