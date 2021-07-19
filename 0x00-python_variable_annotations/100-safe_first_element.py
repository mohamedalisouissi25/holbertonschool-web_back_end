#!/usr/bin/env python3
'''Augment with duck-typed annotations'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''function safe_first_elements'''
    if lst:
        return lst[0]
    else:
        return None
