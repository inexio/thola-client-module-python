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


class ReadCPULoadResponse(object):
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
        'cpu_load': 'list[float]'
    }

    attribute_map = {
        'cpu_load': 'cpu_load'
    }

    def __init__(self, cpu_load=None, _configuration=None):  # noqa: E501
        """ReadCPULoadResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpu_load = None
        self.discriminator = None

        if cpu_load is not None:
            self.cpu_load = cpu_load

    @property
    def cpu_load(self):
        """Gets the cpu_load of this ReadCPULoadResponse.  # noqa: E501


        :return: The cpu_load of this ReadCPULoadResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._cpu_load

    @cpu_load.setter
    def cpu_load(self, cpu_load):
        """Sets the cpu_load of this ReadCPULoadResponse.


        :param cpu_load: The cpu_load of this ReadCPULoadResponse.  # noqa: E501
        :type: list[float]
        """

        self._cpu_load = cpu_load

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
        if issubclass(ReadCPULoadResponse, dict):
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
        if not isinstance(other, ReadCPULoadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadCPULoadResponse):
            return True

        return self.to_dict() != other.to_dict()