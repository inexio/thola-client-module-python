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
        'corrected_fec': 'list[Rate]',
        'rx_power': 'float',
        'tx_power': 'float',
        'uncorrected_fec': 'list[Rate]'
    }

    attribute_map = {
        'channels': 'channels',
        'corrected_fec': 'corrected_fec',
        'rx_power': 'rx_power',
        'tx_power': 'tx_power',
        'uncorrected_fec': 'uncorrected_fec'
    }

    def __init__(self, channels=None, corrected_fec=None, rx_power=None, tx_power=None, uncorrected_fec=None, _configuration=None):  # noqa: E501
        """DWDMInterface - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channels = None
        self._corrected_fec = None
        self._rx_power = None
        self._tx_power = None
        self._uncorrected_fec = None
        self.discriminator = None

        if channels is not None:
            self.channels = channels
        if corrected_fec is not None:
            self.corrected_fec = corrected_fec
        if rx_power is not None:
            self.rx_power = rx_power
        if tx_power is not None:
            self.tx_power = tx_power
        if uncorrected_fec is not None:
            self.uncorrected_fec = uncorrected_fec

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
    def corrected_fec(self):
        """Gets the corrected_fec of this DWDMInterface.  # noqa: E501


        :return: The corrected_fec of this DWDMInterface.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._corrected_fec

    @corrected_fec.setter
    def corrected_fec(self, corrected_fec):
        """Sets the corrected_fec of this DWDMInterface.


        :param corrected_fec: The corrected_fec of this DWDMInterface.  # noqa: E501
        :type: list[Rate]
        """

        self._corrected_fec = corrected_fec

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
    def uncorrected_fec(self):
        """Gets the uncorrected_fec of this DWDMInterface.  # noqa: E501


        :return: The uncorrected_fec of this DWDMInterface.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._uncorrected_fec

    @uncorrected_fec.setter
    def uncorrected_fec(self, uncorrected_fec):
        """Sets the uncorrected_fec of this DWDMInterface.


        :param uncorrected_fec: The uncorrected_fec of this DWDMInterface.  # noqa: E501
        :type: list[Rate]
        """

        self._uncorrected_fec = uncorrected_fec

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
