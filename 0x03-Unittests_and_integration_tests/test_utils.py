#!/usr/bin/env python3

"""This module is used to test our classes and functions
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """The test access nested map class"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, result):
        """This will test the application"""
        self.assertEqual(access_nested_map(nested_map=nested_map,
                                           path=path), result)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))
                           ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test if an exception would be raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)
