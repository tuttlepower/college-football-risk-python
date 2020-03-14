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


class TeamHistoryStarBreakdown(object):
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
        'ones': 'int',
        'twos': 'int',
        'threes': 'int',
        'fours': 'int',
        'fives': 'int'
    }

    attribute_map = {
        'ones': 'ones',
        'twos': 'twos',
        'threes': 'threes',
        'fours': 'fours',
        'fives': 'fives'
    }

    def __init__(self, ones=None, twos=None, threes=None, fours=None, fives=None, local_vars_configuration=None):  # noqa: E501
        """TeamHistoryStarBreakdown - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ones = None
        self._twos = None
        self._threes = None
        self._fours = None
        self._fives = None
        self.discriminator = None

        if ones is not None:
            self.ones = ones
        if twos is not None:
            self.twos = twos
        if threes is not None:
            self.threes = threes
        if fours is not None:
            self.fours = fours
        if fives is not None:
            self.fives = fives

    @property
    def ones(self):
        """Gets the ones of this TeamHistoryStarBreakdown.  # noqa: E501


        :return: The ones of this TeamHistoryStarBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._ones

    @ones.setter
    def ones(self, ones):
        """Sets the ones of this TeamHistoryStarBreakdown.


        :param ones: The ones of this TeamHistoryStarBreakdown.  # noqa: E501
        :type: int
        """

        self._ones = ones

    @property
    def twos(self):
        """Gets the twos of this TeamHistoryStarBreakdown.  # noqa: E501


        :return: The twos of this TeamHistoryStarBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._twos

    @twos.setter
    def twos(self, twos):
        """Sets the twos of this TeamHistoryStarBreakdown.


        :param twos: The twos of this TeamHistoryStarBreakdown.  # noqa: E501
        :type: int
        """

        self._twos = twos

    @property
    def threes(self):
        """Gets the threes of this TeamHistoryStarBreakdown.  # noqa: E501


        :return: The threes of this TeamHistoryStarBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._threes

    @threes.setter
    def threes(self, threes):
        """Sets the threes of this TeamHistoryStarBreakdown.


        :param threes: The threes of this TeamHistoryStarBreakdown.  # noqa: E501
        :type: int
        """

        self._threes = threes

    @property
    def fours(self):
        """Gets the fours of this TeamHistoryStarBreakdown.  # noqa: E501


        :return: The fours of this TeamHistoryStarBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._fours

    @fours.setter
    def fours(self, fours):
        """Sets the fours of this TeamHistoryStarBreakdown.


        :param fours: The fours of this TeamHistoryStarBreakdown.  # noqa: E501
        :type: int
        """

        self._fours = fours

    @property
    def fives(self):
        """Gets the fives of this TeamHistoryStarBreakdown.  # noqa: E501


        :return: The fives of this TeamHistoryStarBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._fives

    @fives.setter
    def fives(self, fives):
        """Sets the fives of this TeamHistoryStarBreakdown.


        :param fives: The fives of this TeamHistoryStarBreakdown.  # noqa: E501
        :type: int
        """

        self._fives = fives

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
        if not isinstance(other, TeamHistoryStarBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamHistoryStarBreakdown):
            return True

        return self.to_dict() != other.to_dict()
