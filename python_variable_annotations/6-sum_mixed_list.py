#!/usr/bin/env python3
"""Anotaciones complejas en Python"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Suma una lista de enteros y flotantes."""
    return float(sum(mxd_list))
