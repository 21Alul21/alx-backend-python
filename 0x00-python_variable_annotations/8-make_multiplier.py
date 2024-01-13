#!/usr/bin/env python3
"""module contains a type annotated function
and returns a function that multiplies a float
by its float parameter"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that implements the module docstring"""

    def func_multiplieer(x: float) -> float:
        return x * multiplier
    return func_multiplieer
