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


class DeviceData(object):
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
        'connection_data': 'ConnectionData',
        'ip_address': 'str'
    }

    attribute_map = {
        'connection_data': 'connection_data',
        'ip_address': 'ip_address'
    }

    def __init__(self, connection_data=None, ip_address=None, _configuration=None):  # noqa: E501
        """DeviceData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_data = None
        self._ip_address = None
        self.discriminator = None

        if connection_data is not None:
            self.connection_data = connection_data
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def connection_data(self):
        """Gets the connection_data of this DeviceData.  # noqa: E501


        :return: The connection_data of this DeviceData.  # noqa: E501
        :rtype: ConnectionData
        """
        return self._connection_data

    @connection_data.setter
    def connection_data(self, connection_data):
        """Sets the connection_data of this DeviceData.


        :param connection_data: The connection_data of this DeviceData.  # noqa: E501
        :type: ConnectionData
        """

        self._connection_data = connection_data

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceData.  # noqa: E501

        The IP of the device  # noqa: E501

        :return: The ip_address of this DeviceData.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceData.

        The IP of the device  # noqa: E501

        :param ip_address: The ip_address of this DeviceData.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

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
        if issubclass(DeviceData, dict):
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
        if not isinstance(other, DeviceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceData):
            return True

        return self.to_dict() != other.to_dict()
