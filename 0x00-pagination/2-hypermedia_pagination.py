#!/usr/bin/env python3
"""
A helper function that returns range
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """extact page content from dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        prange = index_range(page, page_size)
        dataset = self.dataset()
        page = dataset[prange[0]: prange[1]]
        return page

    def get_hyper(
            self, page: int = 1, page_size: int = 10
            ) -> Dict:
        """Get hypermedia
        """

        hypermedia = {"page_size": page_size,
                      "page": page,
                      "data": self.get_page(page, page_size),
                      "next_page": page + 1 if len(
                          self.get_page(page + 1, page_size)) else None,
                      "prev_page": page - 1 if page > 1 else None,
                      "total_pages": math.ceil(
                          len(self.dataset()) / page_size),
                      }

        return hypermedia


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page and page_size and returns a tuple of size
    two containing a start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination parameters.
    """

    start_i = (page - 1) * page_size
    end_i = start_i + page_size

    return (start_i, end_i)
