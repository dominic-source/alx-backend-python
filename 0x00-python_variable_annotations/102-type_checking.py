#!/usr/bin/env python3

"""This module using python type annotation to add values"""

from typing import Tuple, TypeVar, List, Any, cast


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(cast(Tuple, array))

zoom_3x = zoom_array(cast(Tuple, array), cast(int, 3))