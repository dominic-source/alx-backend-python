#!/usr/bin/env python3

"""This module returns an asynio without using async keyword on the coroutines
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Learn some more secret"""
    return asyncio.create_task(wait_random(max_delay))
