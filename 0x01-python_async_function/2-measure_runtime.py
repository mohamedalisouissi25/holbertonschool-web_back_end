#!/usr/bin/env python3
"""function with arguments that measures the total execution time"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function measure_time"""
    temps = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - temps) / n)
