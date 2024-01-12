#!/usr/bin/env python3
"""module which contains a typed annotated
function that takes a list of integers and
floats and returns their sum
"""


def sum_mixed_list(mxd_lst: list(int | float)) -> float:
    """function for the modul0x00-python_variable_annotationse
    implementation
    """

    sum = 0
    for i in mxd_lst:
        sum += i
        sum = float(sum)
    return sum
