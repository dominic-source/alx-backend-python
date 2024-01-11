#!/usr/bin/env python3

"""This module using python type annotation to add values"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float"""
    def func(num: float) -> float:
        """The function that multipies a float with a multiplie"""
        return num * multiplier
    return func
