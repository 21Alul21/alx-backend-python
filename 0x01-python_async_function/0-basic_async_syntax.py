#!/usr/bin/env python3
""" module containing an asynchronous
coroutine that and returns it using
the 'random' module
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """ coroutine for the implementation """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(1)
    return delay
