import asyncio

from app import AppContainer
from app.exchange.exchange_container import ExchangeContainer


async def main() -> None:
    container = AppContainer()
    container.wire(modules=[__name__])

    exchange_module: ExchangeContainer = container.exchange_module()
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
