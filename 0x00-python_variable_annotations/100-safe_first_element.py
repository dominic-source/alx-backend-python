#!/usr/bin/env python3

"""This module using python type annotation to add values"""
from types import NoneType
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Dock type annotation implementation"""
    if lst:
        return lst[0]
    else:
        return None
