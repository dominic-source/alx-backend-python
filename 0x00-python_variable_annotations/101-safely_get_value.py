#!/usr/bin/env python3

"""This module using python type annotation to add values"""

from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely get value using this function"""
    if key in dct:
        return dct[key]
    else:
        return default
