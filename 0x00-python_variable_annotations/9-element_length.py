#!/usr/bin/env python3
'''Annotate function’s parameters and return values with types'''

from typing import List, Union, Tuple, Callable, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''function element_lenght'''
    return [(i, len(i)) for i in lst]
