#!/usr/bin/env python3
"""python Asynchronous"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Asynchronous coroutine that spawns wait_random n
    times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Return:
        List[float]: List of delays in ascending order.
    """

    temp_list = []
    for _ in range(n):
        temp_list.append(await wait_random(max_delay))
    return sorted(temp_list)
