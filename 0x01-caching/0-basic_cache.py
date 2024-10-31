#!/usr/bin/python3
"""
Basic dictionary charis version
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary. charis version
    """

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
