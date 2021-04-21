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


class DWDMInterface(object):
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
        'channels_100_g': 'list[OpticalChannel]',
        'corrected_bit_error_rate': 'int',
        'rx_power': 'float',
        'rx_power_100_g': 'float',
        'tx_power': 'float',
        'tx_power_100_g': 'float',
        'uncorrected_bit_error_rate': 'int'
    }

    attribute_map = {
        'channels': 'channels',
        'channels_100_g': 'channels_100_g',
        'corrected_bit_error_rate': 'corrected_bit_error_rate',
        'rx_power': 'rx_power',
        'rx_power_100_g': 'rx_power_100_g',
        'tx_power': 'tx_power',
        'tx_power_100_g': 'tx_power_100_g',
        'uncorrected_bit_error_rate': 'uncorrected_bit_error_rate'
    }

    def __init__(self, channels=None, channels_100_g=None, corrected_bit_error_rate=None, rx_power=None, rx_power_100_g=None, tx_power=None, tx_power_100_g=None, uncorrected_bit_error_rate=None, _configuration=None):  # noqa: E501
        """DWDMInterface - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channels = None
        self._channels_100_g = None
        self._corrected_bit_error_rate = None
        self._rx_power = None
        self._rx_power_100_g = None
        self._tx_power = None
        self._tx_power_100_g = None
        self._uncorrected_bit_error_rate = None
        self.discriminator = None

        if channels is not None:
            self.channels = channels
        if channels_100_g is not None:
            self.channels_100_g = channels_100_g
        if corrected_bit_error_rate is not None:
            self.corrected_bit_error_rate = corrected_bit_error_rate
        if rx_power is not None:
            self.rx_power = rx_power
        if rx_power_100_g is not None:
            self.rx_power_100_g = rx_power_100_g
        if tx_power is not None:
            self.tx_power = tx_power
        if tx_power_100_g is not None:
            self.tx_power_100_g = tx_power_100_g
        if uncorrected_bit_error_rate is not None:
            self.uncorrected_bit_error_rate = uncorrected_bit_error_rate

    @property
    def channels(self):
        """Gets the channels of this DWDMInterface.  # noqa: E501


        :return: The channels of this DWDMInterface.  # noqa: E501
        :rtype: list[OpticalChannel]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this DWDMInterface.


        :param channels: The channels of this DWDMInterface.  # noqa: E501
        :type: list[OpticalChannel]
        """

        self._channels = channels

    @property
    def channels_100_g(self):
        """Gets the channels_100_g of this DWDMInterface.  # noqa: E501


        :return: The channels_100_g of this DWDMInterface.  # noqa: E501
        :rtype: list[OpticalChannel]
        """
        return self._channels_100_g

    @channels_100_g.setter
    def channels_100_g(self, channels_100_g):
        """Sets the channels_100_g of this DWDMInterface.


        :param channels_100_g: The channels_100_g of this DWDMInterface.  # noqa: E501
        :type: list[OpticalChannel]
        """

        self._channels_100_g = channels_100_g

    @property
    def corrected_bit_error_rate(self):
        """Gets the corrected_bit_error_rate of this DWDMInterface.  # noqa: E501


        :return: The corrected_bit_error_rate of this DWDMInterface.  # noqa: E501
        :rtype: int
        """
        return self._corrected_bit_error_rate

    @corrected_bit_error_rate.setter
    def corrected_bit_error_rate(self, corrected_bit_error_rate):
        """Sets the corrected_bit_error_rate of this DWDMInterface.


        :param corrected_bit_error_rate: The corrected_bit_error_rate of this DWDMInterface.  # noqa: E501
        :type: int
        """

        self._corrected_bit_error_rate = corrected_bit_error_rate

    @property
    def rx_power(self):
        """Gets the rx_power of this DWDMInterface.  # noqa: E501


        :return: The rx_power of this DWDMInterface.  # noqa: E501
        :rtype: float
        """
        return self._rx_power

    @rx_power.setter
    def rx_power(self, rx_power):
        """Sets the rx_power of this DWDMInterface.


        :param rx_power: The rx_power of this DWDMInterface.  # noqa: E501
        :type: float
        """

        self._rx_power = rx_power

    @property
    def rx_power_100_g(self):
        """Gets the rx_power_100_g of this DWDMInterface.  # noqa: E501


        :return: The rx_power_100_g of this DWDMInterface.  # noqa: E501
        :rtype: float
        """
        return self._rx_power_100_g

    @rx_power_100_g.setter
    def rx_power_100_g(self, rx_power_100_g):
        """Sets the rx_power_100_g of this DWDMInterface.


        :param rx_power_100_g: The rx_power_100_g of this DWDMInterface.  # noqa: E501
        :type: float
        """

        self._rx_power_100_g = rx_power_100_g

    @property
    def tx_power(self):
        """Gets the tx_power of this DWDMInterface.  # noqa: E501


        :return: The tx_power of this DWDMInterface.  # noqa: E501
        :rtype: float
        """
        return self._tx_power

    @tx_power.setter
    def tx_power(self, tx_power):
        """Sets the tx_power of this DWDMInterface.


        :param tx_power: The tx_power of this DWDMInterface.  # noqa: E501
        :type: float
        """

        self._tx_power = tx_power

    @property
    def tx_power_100_g(self):
        """Gets the tx_power_100_g of this DWDMInterface.  # noqa: E501


        :return: The tx_power_100_g of this DWDMInterface.  # noqa: E501
        :rtype: float
        """
        return self._tx_power_100_g

    @tx_power_100_g.setter
    def tx_power_100_g(self, tx_power_100_g):
        """Sets the tx_power_100_g of this DWDMInterface.


        :param tx_power_100_g: The tx_power_100_g of this DWDMInterface.  # noqa: E501
        :type: float
        """

        self._tx_power_100_g = tx_power_100_g

    @property
    def uncorrected_bit_error_rate(self):
        """Gets the uncorrected_bit_error_rate of this DWDMInterface.  # noqa: E501


        :return: The uncorrected_bit_error_rate of this DWDMInterface.  # noqa: E501
        :rtype: int
        """
        return self._uncorrected_bit_error_rate

    @uncorrected_bit_error_rate.setter
    def uncorrected_bit_error_rate(self, uncorrected_bit_error_rate):
        """Sets the uncorrected_bit_error_rate of this DWDMInterface.


        :param uncorrected_bit_error_rate: The uncorrected_bit_error_rate of this DWDMInterface.  # noqa: E501
        :type: int
        """

        self._uncorrected_bit_error_rate = uncorrected_bit_error_rate

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
        if issubclass(DWDMInterface, dict):
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
        if not isinstance(other, DWDMInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DWDMInterface):
            return True

        return self.to_dict() != other.to_dict()