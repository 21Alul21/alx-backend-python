#!/usr/bin/env python3
"""module for augmenting the code given with
duck type annotation
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """this returns the first element of
    the input listif it exits otherwise returns none
    """

    if lst:
        return lst[0]
    else:
        return None
