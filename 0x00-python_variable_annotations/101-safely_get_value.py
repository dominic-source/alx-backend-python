#!/usr/bin/env python3

"""This module using python type annotation to add values"""

from typing import Any, Union, TypeVar, Mapping, Optional

K = TypeVar('K')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[K, None] = None) -> Union[Any, K]:
    if key in dct:
        return dct[key]
    else:
        return default
