# coding: utf-8

"""
    Thola

    REST API for Thola.  For more information look at our Github : https://github.com/inexio/thola  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from thola_client.configuration import Configuration


class ReadHardwareHealthResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'environment_monitor_state': 'int',
        'fans': 'list[HardwareHealthComponentFan]',
        'power_supply': 'list[HardwareHealthComponentPowerSupply]'
    }

    attribute_map = {
        'environment_monitor_state': 'environment_monitor_state',
        'fans': 'fans',
        'power_supply': 'power_supply'
    }

    def __init__(self, environment_monitor_state=None, fans=None, power_supply=None, _configuration=None):  # noqa: E501
        """ReadHardwareHealthResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._environment_monitor_state = None
        self._fans = None
        self._power_supply = None
        self.discriminator = None

        if environment_monitor_state is not None:
            self.environment_monitor_state = environment_monitor_state
        if fans is not None:
            self.fans = fans
        if power_supply is not None:
            self.power_supply = power_supply

    @property
    def environment_monitor_state(self):
        """Gets the environment_monitor_state of this ReadHardwareHealthResponse.  # noqa: E501


        :return: The environment_monitor_state of this ReadHardwareHealthResponse.  # noqa: E501
        :rtype: int
        """
        return self._environment_monitor_state

    @environment_monitor_state.setter
    def environment_monitor_state(self, environment_monitor_state):
        """Sets the environment_monitor_state of this ReadHardwareHealthResponse.


        :param environment_monitor_state: The environment_monitor_state of this ReadHardwareHealthResponse.  # noqa: E501
        :type: int
        """

        self._environment_monitor_state = environment_monitor_state

    @property
    def fans(self):
        """Gets the fans of this ReadHardwareHealthResponse.  # noqa: E501


        :return: The fans of this ReadHardwareHealthResponse.  # noqa: E501
        :rtype: list[HardwareHealthComponentFan]
        """
        return self._fans

    @fans.setter
    def fans(self, fans):
        """Sets the fans of this ReadHardwareHealthResponse.


        :param fans: The fans of this ReadHardwareHealthResponse.  # noqa: E501
        :type: list[HardwareHealthComponentFan]
        """

        self._fans = fans

    @property
    def power_supply(self):
        """Gets the power_supply of this ReadHardwareHealthResponse.  # noqa: E501


        :return: The power_supply of this ReadHardwareHealthResponse.  # noqa: E501
        :rtype: list[HardwareHealthComponentPowerSupply]
        """
        return self._power_supply

    @power_supply.setter
    def power_supply(self, power_supply):
        """Sets the power_supply of this ReadHardwareHealthResponse.


        :param power_supply: The power_supply of this ReadHardwareHealthResponse.  # noqa: E501
        :type: list[HardwareHealthComponentPowerSupply]
        """

        self._power_supply = power_supply

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ReadHardwareHealthResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReadHardwareHealthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadHardwareHealthResponse):
            return True

        return self.to_dict() != other.to_dict()
