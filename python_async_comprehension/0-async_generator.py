#!/usr/bin/python3
"""Comprensión asíncrona y generadores asíncronos."""

import asyncio
import random


async def async_generator():
    """
    Coroutina que genera valores aleatorios entre 0 y 10
    de manera asíncrona.

    Cada iteración espera 1 segundo para producir el siguiente número.

    Yields:
        float: Float entre 0 y 10.
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
