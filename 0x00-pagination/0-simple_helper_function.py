#!/usr/bin/env python3
"""
A helper function that returns range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page and page_size and returns a tuple of size
    two containing a start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination parameters.
    """

    start_i = page * page_size
    end_i = start_i + page_size

    return (start_i, end_i)
