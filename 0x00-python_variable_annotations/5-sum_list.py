#!/usr/bin/env python3

"""This module using python type annotation to add values"""
from typing import List


def sum_list(sum_list: List[float]) -> float:
    """return a sum of a list of float"""

    return sum(sum_list)
