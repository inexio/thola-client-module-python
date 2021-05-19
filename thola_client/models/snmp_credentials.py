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


class SNMPCredentials(object):
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
        'community': 'str',
        'port': 'int',
        'v3_context_name': 'str',
        'v3_level': 'str',
        'version': 'str'
    }

    attribute_map = {
        'community': 'community',
        'port': 'port',
        'v3_context_name': 'v3ContextName',
        'v3_level': 'v3Level',
        'version': 'version'
    }

    def __init__(self, community=None, port=None, v3_context_name=None, v3_level=None, version=None, _configuration=None):  # noqa: E501
        """SNMPCredentials - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._community = None
        self._port = None
        self._v3_context_name = None
        self._v3_level = None
        self._version = None
        self.discriminator = None

        if community is not None:
            self.community = community
        if port is not None:
            self.port = port
        if v3_context_name is not None:
            self.v3_context_name = v3_context_name
        if v3_level is not None:
            self.v3_level = v3_level
        if version is not None:
            self.version = version

    @property
    def community(self):
        """Gets the community of this SNMPCredentials.  # noqa: E501


        :return: The community of this SNMPCredentials.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SNMPCredentials.


        :param community: The community of this SNMPCredentials.  # noqa: E501
        :type: str
        """

        self._community = community

    @property
    def port(self):
        """Gets the port of this SNMPCredentials.  # noqa: E501


        :return: The port of this SNMPCredentials.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SNMPCredentials.


        :param port: The port of this SNMPCredentials.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def v3_context_name(self):
        """Gets the v3_context_name of this SNMPCredentials.  # noqa: E501


        :return: The v3_context_name of this SNMPCredentials.  # noqa: E501
        :rtype: str
        """
        return self._v3_context_name

    @v3_context_name.setter
    def v3_context_name(self, v3_context_name):
        """Sets the v3_context_name of this SNMPCredentials.


        :param v3_context_name: The v3_context_name of this SNMPCredentials.  # noqa: E501
        :type: str
        """

        self._v3_context_name = v3_context_name

    @property
    def v3_level(self):
        """Gets the v3_level of this SNMPCredentials.  # noqa: E501


        :return: The v3_level of this SNMPCredentials.  # noqa: E501
        :rtype: str
        """
        return self._v3_level

    @v3_level.setter
    def v3_level(self, v3_level):
        """Sets the v3_level of this SNMPCredentials.


        :param v3_level: The v3_level of this SNMPCredentials.  # noqa: E501
        :type: str
        """

        self._v3_level = v3_level

    @property
    def version(self):
        """Gets the version of this SNMPCredentials.  # noqa: E501


        :return: The version of this SNMPCredentials.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SNMPCredentials.


        :param version: The version of this SNMPCredentials.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(SNMPCredentials, dict):
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
        if not isinstance(other, SNMPCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SNMPCredentials):
            return True

        return self.to_dict() != other.to_dict()
