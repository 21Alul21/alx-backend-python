#!/usr/bin/env python3
"""module for annotating function
parameters and return value
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function for the implementation of
    the module docstring specification
    """
    return [(i, len(i) for i in lst)]
