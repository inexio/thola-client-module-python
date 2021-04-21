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


class ResponseInfo(object):
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
        'messages': 'list[OutputMessage]',
        'performance_data': 'list[PerformanceDataPoint]',
        'raw_output': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'messages': 'messages',
        'performance_data': 'performance_data',
        'raw_output': 'raw_output',
        'status_code': 'status_code'
    }

    def __init__(self, messages=None, performance_data=None, raw_output=None, status_code=None, _configuration=None):  # noqa: E501
        """ResponseInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._messages = None
        self._performance_data = None
        self._raw_output = None
        self._status_code = None
        self.discriminator = None

        if messages is not None:
            self.messages = messages
        if performance_data is not None:
            self.performance_data = performance_data
        if raw_output is not None:
            self.raw_output = raw_output
        if status_code is not None:
            self.status_code = status_code

    @property
    def messages(self):
        """Gets the messages of this ResponseInfo.  # noqa: E501


        :return: The messages of this ResponseInfo.  # noqa: E501
        :rtype: list[OutputMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ResponseInfo.


        :param messages: The messages of this ResponseInfo.  # noqa: E501
        :type: list[OutputMessage]
        """

        self._messages = messages

    @property
    def performance_data(self):
        """Gets the performance_data of this ResponseInfo.  # noqa: E501


        :return: The performance_data of this ResponseInfo.  # noqa: E501
        :rtype: list[PerformanceDataPoint]
        """
        return self._performance_data

    @performance_data.setter
    def performance_data(self, performance_data):
        """Sets the performance_data of this ResponseInfo.


        :param performance_data: The performance_data of this ResponseInfo.  # noqa: E501
        :type: list[PerformanceDataPoint]
        """

        self._performance_data = performance_data

    @property
    def raw_output(self):
        """Gets the raw_output of this ResponseInfo.  # noqa: E501


        :return: The raw_output of this ResponseInfo.  # noqa: E501
        :rtype: str
        """
        return self._raw_output

    @raw_output.setter
    def raw_output(self, raw_output):
        """Sets the raw_output of this ResponseInfo.


        :param raw_output: The raw_output of this ResponseInfo.  # noqa: E501
        :type: str
        """

        self._raw_output = raw_output

    @property
    def status_code(self):
        """Gets the status_code of this ResponseInfo.  # noqa: E501


        :return: The status_code of this ResponseInfo.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ResponseInfo.


        :param status_code: The status_code of this ResponseInfo.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(ResponseInfo, dict):
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
        if not isinstance(other, ResponseInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseInfo):
            return True

        return self.to_dict() != other.to_dict()
