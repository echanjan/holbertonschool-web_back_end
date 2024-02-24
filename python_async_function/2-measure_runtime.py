#!/usr/bin/env python3
"""Script for measuring the average time taken by the wait_n coroutine"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """Measures the average time taken by the wait_n coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.
        n (int): Number of times to run the wait_n coroutine.

    Returns:
        float: The average time taken per iteration.
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n
    return total_time
