#!/usr/bin/env python3
"""Anotaciones en Python de tipos complejos."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Eleva al cuadrado el segundo argumento."""
    return (k, v ** 2)
