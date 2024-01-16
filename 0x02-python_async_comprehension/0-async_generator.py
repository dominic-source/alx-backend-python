#!/user/bin/env python3

"""This module houses a coroutine that behaves like a generator
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ A generator function """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
