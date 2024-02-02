#!/usr/bin/env python3

"""This module is used to test our classes and functions
"""

import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json
import json


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


class TestGetJson(unittest.TestCase):
    """Mock a test to get json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("utils.requests")
    def test_get_json(self, test_url, test_payload, mock_req):
        """The test for getting json"""

        mock_res = MagicMock()
        mock_res.json.return_value = test_payload

        mock_req.get.return_value = mock_res

        self.assertEqual(get_json(test_url), test_payload)

        mock_req.get.assert_called_once()
