#!/usr/bin/env python3
"""module that contains the values and type
annotations
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Safely retrieves the value associated
    with key from dct.
    if the key is not present, it returns the specified
    default
    """

    if key in dct:
        return dct[key]
    else:
        return default
