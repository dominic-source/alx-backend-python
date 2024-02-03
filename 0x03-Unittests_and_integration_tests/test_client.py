#!/usr/bin/env python3

"""
This module is used to test client
"""

import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test github organisation client"""

    @parameterized.expand([('google'), ('abc')])
    @patch("client.get_json")
    def test_org(self, org, mock_method):
        """Test organisation"""
        mock_method.return_value = {"working": None}
        production = GithubOrgClient(org)
        production.org
        mock_method.assert_called_once()

    def test_public_repos_url(self):
        """Test public repos url"""

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_method:
            mock_method.return_value = {"repos_url": True}
            production = GithubOrgClient("google")
            self.assertEqual(production._public_repos_url,
                             mock_method()["repos_url"])
