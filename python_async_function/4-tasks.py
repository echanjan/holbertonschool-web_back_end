#!/usr/bin/env python3
"""Python asíncrono."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Launch multiple tasks in parallel.

        Args:
            n (int): The number of times the task should be executed.
            max_delay (int): Upper limit for random delay.

        Returns:
            List[float]: A list with wait times.
    """
    list_task = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*list_task))
