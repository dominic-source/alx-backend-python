#!/usr/bin/env python3

"""This module houses a coroutine that behaves like a generator

"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of the async generator"""

    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    time_count = time.perf_counter() - s

    return time_count
