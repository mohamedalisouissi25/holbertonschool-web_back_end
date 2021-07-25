#!/usr/bin/env python3
"""Caching"""


BasicCaching = __import__('base_caching').BaseCaching


class BasicCache(BasicCaching):
    """cache class"""
    def __init__(self):
    """constructor func init"""
        super().__init__()

def put(self, key, item):
        """function put"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """function get"""
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
