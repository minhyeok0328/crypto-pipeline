import asyncio

from app import AppContainer
from app.exchange.exchange_module import ExchangeModule


async def main() -> None:
    container = AppContainer()
    container.wire(modules=[__name__])

    exchange_module: ExchangeModule = container.exchange_module()
    bybit = exchange_module.bybit()
    upbit = exchange_module.upbit()

    async def run_crypto():
        await asyncio.gather(
            bybit.run(),
            upbit.run()
        )

    await run_crypto()


if __name__ == "__main__":
    asyncio.run(main())
