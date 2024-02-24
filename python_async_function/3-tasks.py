#!/usr/bin/env python3
"""Script for creating an asyncio Task for the wait_random coroutine"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Creates an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: representing the execution of wait_random.
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
