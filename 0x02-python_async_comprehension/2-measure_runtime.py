#!/usr/bin/env python3
"""measure_runtime"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function measure_runtime"""
    temps = time.time()
    all = [async_comprehension() for i in range(4)]
    await asyncio.gather(*all)

    return time.time() - temps
