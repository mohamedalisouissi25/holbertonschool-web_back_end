#!/usr/bin/env python3
"""hypermedia pagination"""


import csv
import math
from typing import List,Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby name
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """fun dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """fun get_page"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        index, indexes = index_range(page, page_size)
        if index > len(self.dataset()):
            return []
        data = self.dataset()
        return data[index:indexes]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        '''fun get_hyper'''
        index, indexes = index_range(page, page_size)
        if index > 0:
            previous_page = page - 1
        else:
            previous_page = None
        pagelist = math.ceil(len(self.dataset()) / page_size)

        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                "next_page": page + 1 if page + 1 < pagelist else None,
                "prev_page": page - 1 if page > 1 else None,
                'total_pages': pagelist}
