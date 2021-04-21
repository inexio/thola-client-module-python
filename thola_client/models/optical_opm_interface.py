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


class OpticalOPMInterface(object):
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
        'channels': 'list[OpticalChannel]',
        'identifier': 'str',
        'label': 'str',
        'rx_power': 'float'
    }

    attribute_map = {
        'channels': 'channels',
        'identifier': 'identifier',
        'label': 'label',
        'rx_power': 'rx_power'
    }

    def __init__(self, channels=None, identifier=None, label=None, rx_power=None, _configuration=None):  # noqa: E501
        """OpticalOPMInterface - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channels = None
        self._identifier = None
        self._label = None
        self._rx_power = None
        self.discriminator = None

        if channels is not None:
            self.channels = channels
        if identifier is not None:
            self.identifier = identifier
        if label is not None:
            self.label = label
        if rx_power is not None:
            self.rx_power = rx_power

    @property
    def channels(self):
        """Gets the channels of this OpticalOPMInterface.  # noqa: E501


        :return: The channels of this OpticalOPMInterface.  # noqa: E501
        :rtype: list[OpticalChannel]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this OpticalOPMInterface.


        :param channels: The channels of this OpticalOPMInterface.  # noqa: E501
        :type: list[OpticalChannel]
        """

        self._channels = channels

    @property
    def identifier(self):
        """Gets the identifier of this OpticalOPMInterface.  # noqa: E501


        :return: The identifier of this OpticalOPMInterface.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this OpticalOPMInterface.


        :param identifier: The identifier of this OpticalOPMInterface.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def label(self):
        """Gets the label of this OpticalOPMInterface.  # noqa: E501


        :return: The label of this OpticalOPMInterface.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this OpticalOPMInterface.


        :param label: The label of this OpticalOPMInterface.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def rx_power(self):
        """Gets the rx_power of this OpticalOPMInterface.  # noqa: E501


        :return: The rx_power of this OpticalOPMInterface.  # noqa: E501
        :rtype: float
        """
        return self._rx_power

    @rx_power.setter
    def rx_power(self, rx_power):
        """Sets the rx_power of this OpticalOPMInterface.


        :param rx_power: The rx_power of this OpticalOPMInterface.  # noqa: E501
        :type: float
        """

        self._rx_power = rx_power

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
        if issubclass(OpticalOPMInterface, dict):
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
        if not isinstance(other, OpticalOPMInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpticalOPMInterface):
            return True

        return self.to_dict() != other.to_dict()
