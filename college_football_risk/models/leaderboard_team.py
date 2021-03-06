# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from college_football_risk.configuration import Configuration


class LeaderboardTeam(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'rank': 'int',
        'name': 'str',
        'logo': 'str',
        'territory_count': 'int',
        'player_count': 'int',
        'merc_count': 'int',
        'star_power': 'float'
    }

    attribute_map = {
        'rank': 'rank',
        'name': 'name',
        'logo': 'logo',
        'territory_count': 'territoryCount',
        'player_count': 'playerCount',
        'merc_count': 'mercCount',
        'star_power': 'starPower'
    }

    def __init__(self, rank=None, name=None, logo=None, territory_count=None, player_count=None, merc_count=None, star_power=None, local_vars_configuration=None):  # noqa: E501
        """LeaderboardTeam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rank = None
        self._name = None
        self._logo = None
        self._territory_count = None
        self._player_count = None
        self._merc_count = None
        self._star_power = None
        self.discriminator = None

        if rank is not None:
            self.rank = rank
        if name is not None:
            self.name = name
        if logo is not None:
            self.logo = logo
        if territory_count is not None:
            self.territory_count = territory_count
        if player_count is not None:
            self.player_count = player_count
        if merc_count is not None:
            self.merc_count = merc_count
        if star_power is not None:
            self.star_power = star_power

    @property
    def rank(self):
        """Gets the rank of this LeaderboardTeam.  # noqa: E501


        :return: The rank of this LeaderboardTeam.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this LeaderboardTeam.


        :param rank: The rank of this LeaderboardTeam.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def name(self):
        """Gets the name of this LeaderboardTeam.  # noqa: E501


        :return: The name of this LeaderboardTeam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LeaderboardTeam.


        :param name: The name of this LeaderboardTeam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this LeaderboardTeam.  # noqa: E501


        :return: The logo of this LeaderboardTeam.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this LeaderboardTeam.


        :param logo: The logo of this LeaderboardTeam.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def territory_count(self):
        """Gets the territory_count of this LeaderboardTeam.  # noqa: E501


        :return: The territory_count of this LeaderboardTeam.  # noqa: E501
        :rtype: int
        """
        return self._territory_count

    @territory_count.setter
    def territory_count(self, territory_count):
        """Sets the territory_count of this LeaderboardTeam.


        :param territory_count: The territory_count of this LeaderboardTeam.  # noqa: E501
        :type: int
        """

        self._territory_count = territory_count

    @property
    def player_count(self):
        """Gets the player_count of this LeaderboardTeam.  # noqa: E501


        :return: The player_count of this LeaderboardTeam.  # noqa: E501
        :rtype: int
        """
        return self._player_count

    @player_count.setter
    def player_count(self, player_count):
        """Sets the player_count of this LeaderboardTeam.


        :param player_count: The player_count of this LeaderboardTeam.  # noqa: E501
        :type: int
        """

        self._player_count = player_count

    @property
    def merc_count(self):
        """Gets the merc_count of this LeaderboardTeam.  # noqa: E501


        :return: The merc_count of this LeaderboardTeam.  # noqa: E501
        :rtype: int
        """
        return self._merc_count

    @merc_count.setter
    def merc_count(self, merc_count):
        """Sets the merc_count of this LeaderboardTeam.


        :param merc_count: The merc_count of this LeaderboardTeam.  # noqa: E501
        :type: int
        """

        self._merc_count = merc_count

    @property
    def star_power(self):
        """Gets the star_power of this LeaderboardTeam.  # noqa: E501


        :return: The star_power of this LeaderboardTeam.  # noqa: E501
        :rtype: float
        """
        return self._star_power

    @star_power.setter
    def star_power(self, star_power):
        """Sets the star_power of this LeaderboardTeam.


        :param star_power: The star_power of this LeaderboardTeam.  # noqa: E501
        :type: float
        """

        self._star_power = star_power

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LeaderboardTeam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LeaderboardTeam):
            return True

        return self.to_dict() != other.to_dict()
