#!/usr/bin/env python3
'''concurrency'''

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''function wait_n'''

    conc = []
    coroutines = []

    for i in range(n):
        conc.append(wait_random(max_delay))
    for i in asyncio.as_completed(conc):
        coroutines.append(await i)
    return coroutines
