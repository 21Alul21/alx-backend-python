#!/usr/bin/env python3
"""module containing a type anotated
funcrion that takes a list of floats
as argument and returns their sum as
floats
"""


def sum_list(input_list: list[float]) -> float:
    """function that takes a list of floats
    as argumentn and returns their sum
    """

    sum: float = 0.0
    for i in input_list:
        sum += i
        sum = float(sum)
    return sum
