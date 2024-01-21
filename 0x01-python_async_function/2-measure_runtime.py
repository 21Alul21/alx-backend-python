#!/usr/bin/env python3
""" module that implements coroutine
that implements a coroutine from a
previous file
"""
import asyncio
import random
import time
import typing


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ coroutine for execution time measurement
    """

    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = float(start_time - end_time)
    return total_time/n
