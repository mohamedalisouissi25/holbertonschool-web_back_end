#!/usr/bin/env python3
"""simple helper fun"""


def index_range(page, page_size):
    """ function index_range"""

    size = (page - 1) * page_size

    return(size, size + page_size)
