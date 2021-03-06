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
import datetime

import college_football_risk
from college_football_risk.models.player_turns import PlayerTurns  # noqa: E501
from college_football_risk.rest import ApiException

class TestPlayerTurns(unittest.TestCase):
    """PlayerTurns unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlayerTurns
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = college_football_risk.models.player_turns.PlayerTurns()  # noqa: E501
        if include_optional :
            return PlayerTurns(
                season = 56, 
                day = 56, 
                stars = 56, 
                mvp = True, 
                territory = '0', 
                team = '0'
            )
        else :
            return PlayerTurns(
        )

    def testPlayerTurns(self):
        """Test PlayerTurns"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
