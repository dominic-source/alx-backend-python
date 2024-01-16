#!/usr/bin/env python3

"""This module houses a coroutine that behaves like a generator

"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Iterate through a generator"""

    result = [n async for n in async_generator()]

    return result
