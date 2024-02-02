#!/usr/bin/env python3

"""Further improve on asynchronous coroutines"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Learn how to spawn another coroutine"""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    result = []

    for task in asyncio.as_completed(tasks):
        result.append(await task)
    return result
