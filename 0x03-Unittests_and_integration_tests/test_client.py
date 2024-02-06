#!/usr/bin/env python3

"""
This module is used to test client
"""

import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import requests


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


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """PERFORM INTEGRATION TESTING"""

    @classmethod
    def setUpClass(cls):
        """The setup method for our integration testing"""

        def side_effect(url):
            """Use the url to get information"""

            mock_json = MagicMock()
            mock_get = Mock()
            mock_get.get.return_value = TEST_PAYLOAD
            for data in mock_get.get():
                if url.endswith(
                    cls.repos_payload[0]["owner"]["login"]
                                ) and url.startswith(
                                    "https://api.github.com/orgs/"):

                    mock_json.json.return_value = data[0]
                    return mock_json
                elif url.endswith("/repos") and url == data[0]["repos_url"]:
                    mock_json.json.return_value = data[1]
                    return mock_json
            mock_json.json.return_value = {"repos_url": ""}
            return mock_json

        cls.get_patcher = patch('requests.get', side_effect=side_effect)

        cls.mock_req = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """The tear down method for our integration testing"""

        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos"""

        url_2 = self.repos_payload[0]["owner"]["login"]
        p_rep = GithubOrgClient(url_2)
        self.assertEqual(p_rep.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public repos with licence"""

        url_2 = self.repos_payload[0]["owner"]["login"]
        p_rep = GithubOrgClient(url_2)
        self.assertEqual(p_rep.public_repos(license="apache-2.0"),
                         self.apache2_repos)
