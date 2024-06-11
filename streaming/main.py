import asyncio

from app import AppContainer
from app.exchange.exchange_module import ExchangeModule

async def main() -> None:
    container = AppContainer()
    container.wire(modules=[__name__])

    exchange_module: ExchangeModule = container.exchange_module()
    bybit = exchange_module.bybit()

    async def run_crypto():
        await bybit.run()

    await asyncio.gather(
        run_crypto()
    )

if __name__ == "__main__":
    asyncio.run(main())
