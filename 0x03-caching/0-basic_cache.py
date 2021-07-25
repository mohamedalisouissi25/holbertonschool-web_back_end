#!/usr/bin/python3
"""Caching"""


BasicCaching = __import__('base_caching').BaseCaching


class BasicCache(BasicCaching):
    """cache class"""

    def put(self, key, item):
        """function put"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """function get"""
        return self.cache_data.get(key)
