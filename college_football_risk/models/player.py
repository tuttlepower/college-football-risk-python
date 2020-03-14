# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from college_football_risk.configuration import Configuration


class Player(object):
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
        'name': 'str',
        'team': 'PlayerTeam',
        'ratings': 'PlayerRatings',
        'stats': 'PlayerStats',
        'turns': 'list[PlayerTurns]'
    }

    attribute_map = {
        'name': 'name',
        'team': 'team',
        'ratings': 'ratings',
        'stats': 'stats',
        'turns': 'turns'
    }

    def __init__(self, name=None, team=None, ratings=None, stats=None, turns=None, local_vars_configuration=None):  # noqa: E501
        """Player - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._team = None
        self._ratings = None
        self._stats = None
        self._turns = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if team is not None:
            self.team = team
        if ratings is not None:
            self.ratings = ratings
        if stats is not None:
            self.stats = stats
        if turns is not None:
            self.turns = turns

    @property
    def name(self):
        """Gets the name of this Player.  # noqa: E501


        :return: The name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Player.


        :param name: The name of this Player.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team(self):
        """Gets the team of this Player.  # noqa: E501


        :return: The team of this Player.  # noqa: E501
        :rtype: PlayerTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Player.


        :param team: The team of this Player.  # noqa: E501
        :type: PlayerTeam
        """

        self._team = team

    @property
    def ratings(self):
        """Gets the ratings of this Player.  # noqa: E501


        :return: The ratings of this Player.  # noqa: E501
        :rtype: PlayerRatings
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this Player.


        :param ratings: The ratings of this Player.  # noqa: E501
        :type: PlayerRatings
        """

        self._ratings = ratings

    @property
    def stats(self):
        """Gets the stats of this Player.  # noqa: E501


        :return: The stats of this Player.  # noqa: E501
        :rtype: PlayerStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Player.


        :param stats: The stats of this Player.  # noqa: E501
        :type: PlayerStats
        """

        self._stats = stats

    @property
    def turns(self):
        """Gets the turns of this Player.  # noqa: E501


        :return: The turns of this Player.  # noqa: E501
        :rtype: list[PlayerTurns]
        """
        return self._turns

    @turns.setter
    def turns(self, turns):
        """Sets the turns of this Player.


        :param turns: The turns of this Player.  # noqa: E501
        :type: list[PlayerTurns]
        """

        self._turns = turns

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
        if not isinstance(other, Player):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Player):
            return True

        return self.to_dict() != other.to_dict()