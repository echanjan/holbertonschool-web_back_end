#!/usr/bin/env python3
"""Anotaciones de tipos complejos en Python."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplica un número por el multiplicador dado."""
    def multiplier_function(number: float) -> float:
        return number * multiplier
    return multiplier_function
