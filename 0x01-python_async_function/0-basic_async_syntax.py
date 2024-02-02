#!/usr/bin/env python3

"""A python module to practice how to use async and asyncio
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ A coroutine that delays for a set number of time"""
    sleep: float = random.uniform(0, max_delay)

    await asyncio.sleep(sleep)
    return sleep
