#!/usr/bin/env python3
"""module containing a type annotateed
fuction that takes a string and and an
int of float as arguments and
returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that implements
    the module docstring
    """

    return k, float(v ** 2)
