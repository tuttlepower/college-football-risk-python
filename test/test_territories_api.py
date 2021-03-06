# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import college_football_risk
from college_football_risk.api.territories_api import TerritoriesApi  # noqa: E501
from college_football_risk.rest import ApiException


class TestTerritoriesApi(unittest.TestCase):
    """TerritoriesApi unit test stubs"""

    def setUp(self):
        self.api = college_football_risk.api.territories_api.TerritoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_territories(self):
        """Test case for get_territories

        Get list of territories  # noqa: E501
        """
        pass

    def test_get_territory_history(self):
        """Test case for get_territory_history

        Get historical territory data  # noqa: E501
        """
        pass

    def test_get_territory_turn(self):
        """Test case for get_territory_turn

        Get teritory statistics for a specific turn  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
