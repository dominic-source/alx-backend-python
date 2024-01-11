#!/usr/bin/env python3

"""This module using python type annotation to add values"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a turple of the string and the square of the int or float"""

    return k, v**2
