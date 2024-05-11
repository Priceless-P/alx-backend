#!/usr/bin/python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start index and an end index """
    start_index = (page - 1) * page_size if page > 1 else 0

    end_index = start_index + page_size

    return start_index, end_index
