#!/usr/bin/env python3

"""This module introduces further development of understand on async/await

"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time"""

    time1 = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_t = time.perf_counter() - time1
    return total_t / n
