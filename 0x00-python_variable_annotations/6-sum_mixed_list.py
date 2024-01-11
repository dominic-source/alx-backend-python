#!/usr/bin/env python3

"""This module using python type annotation to add values"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float: 
    """Sum a list of integers and float"""
    return sum(mxd_lst)
