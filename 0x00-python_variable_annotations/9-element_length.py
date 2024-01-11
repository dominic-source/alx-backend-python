#!/usr/bin/env python3

"""This module using python type annotation to add values"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the function using Iterable, Sequence, List, and Turple"""
    return [(i, len(i)) for i in lst]
