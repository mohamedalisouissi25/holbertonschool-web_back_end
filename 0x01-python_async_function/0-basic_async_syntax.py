#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function wait_random"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
