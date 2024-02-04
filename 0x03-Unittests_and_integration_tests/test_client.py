#!/usr/bin/env python3

"""
This module is used to test client
"""

import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_method):
        """Test the public repos"""
        payload = TEST_PAYLOAD[0][1]
        mock_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_met:
            mock_met.return_value = TEST_PAYLOAD[0][0]

            production = GithubOrgClient("google")
            production.public_repos()

        mock_met.assert_called_once()
        mock_method.assert_called_once()

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
    def test_has_license(self, data, license, result):
        """Test that license is true or false"""
        production = GithubOrgClient.has_license(data, license)
        self.assertEqual(production, result)


@parameterized_class((), [])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """PERFORM INTEGRATION TESTING"""

    @patch()
    def setUpClasss(self):
        """The setup method for our integration testing"""
        self.mock_request = MagicMock()
        self.mock_request.requests.get.return_value = TEST_PAYLOAD[0][1]

    def tearDownClass(self):
        """The tear down method for our integration testing"""

        pass
