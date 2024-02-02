#!/usr/bin/env python3

"""This module houses a coroutine that behaves like a generator

"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ A generator function that return a random float value"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
