#!/usr/bin/env python3
""" imports wait_random from previous
module for asyn operations
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ implementation coroutine """

    delay_list = list()
    for i in range(n):
        value = await wait_random(max_delay)
        delay_list.append(value)
    new_delay_list = sorted(delay_list.copy())
    return new_delay_list
