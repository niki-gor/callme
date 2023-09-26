import asyncio

import asyncpg

from callme import config


async def _get_connections_pool():
    connections_pool = await asyncpg.create_pool(
        str(config.dsn),
        min_size=config.min_connection_count,
        max_size=config.max_connection_count,
    )
    return connections_pool


def get_connections_pool(config: config.Config):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(_get_connections_pool())