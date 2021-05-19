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


class SNMPv3ConnectionData(object):
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
        'auth_key': 'str',
        'auth_protocol': 'str',
        'context_name': 'str',
        'level': 'str',
        'priv_key': 'str',
        'priv_protocol': 'str',
        'user': 'str'
    }

    attribute_map = {
        'auth_key': 'auth_key',
        'auth_protocol': 'auth_protocol',
        'context_name': 'context_name',
        'level': 'level',
        'priv_key': 'priv_key',
        'priv_protocol': 'priv_protocol',
        'user': 'user'
    }

    def __init__(self, auth_key=None, auth_protocol=None, context_name=None, level=None, priv_key=None, priv_protocol=None, user=None, _configuration=None):  # noqa: E501
        """SNMPv3ConnectionData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_key = None
        self._auth_protocol = None
        self._context_name = None
        self._level = None
        self._priv_key = None
        self._priv_protocol = None
        self._user = None
        self.discriminator = None

        if auth_key is not None:
            self.auth_key = auth_key
        if auth_protocol is not None:
            self.auth_protocol = auth_protocol
        if context_name is not None:
            self.context_name = context_name
        if level is not None:
            self.level = level
        if priv_key is not None:
            self.priv_key = priv_key
        if priv_protocol is not None:
            self.priv_protocol = priv_protocol
        if user is not None:
            self.user = user

    @property
    def auth_key(self):
        """Gets the auth_key of this SNMPv3ConnectionData.  # noqa: E501

        The authentication protocol passphrase of the SNMP connection.  # noqa: E501

        :return: The auth_key of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this SNMPv3ConnectionData.

        The authentication protocol passphrase of the SNMP connection.  # noqa: E501

        :param auth_key: The auth_key of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._auth_key = auth_key

    @property
    def auth_protocol(self):
        """Gets the auth_protocol of this SNMPv3ConnectionData.  # noqa: E501

        The authentication protocol of the SNMP connection.  # noqa: E501

        :return: The auth_protocol of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_protocol):
        """Sets the auth_protocol of this SNMPv3ConnectionData.

        The authentication protocol of the SNMP connection.  # noqa: E501

        :param auth_protocol: The auth_protocol of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._auth_protocol = auth_protocol

    @property
    def context_name(self):
        """Gets the context_name of this SNMPv3ConnectionData.  # noqa: E501

        The context name of the SNMP connection.  # noqa: E501

        :return: The context_name of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._context_name

    @context_name.setter
    def context_name(self, context_name):
        """Sets the context_name of this SNMPv3ConnectionData.

        The context name of the SNMP connection.  # noqa: E501

        :param context_name: The context_name of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._context_name = context_name

    @property
    def level(self):
        """Gets the level of this SNMPv3ConnectionData.  # noqa: E501

        The security level of the SNMP connection.  # noqa: E501

        :return: The level of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SNMPv3ConnectionData.

        The security level of the SNMP connection.  # noqa: E501

        :param level: The level of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def priv_key(self):
        """Gets the priv_key of this SNMPv3ConnectionData.  # noqa: E501

        The privacy protocol passphrase of the SNMP connection.  # noqa: E501

        :return: The priv_key of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._priv_key

    @priv_key.setter
    def priv_key(self, priv_key):
        """Sets the priv_key of this SNMPv3ConnectionData.

        The privacy protocol passphrase of the SNMP connection.  # noqa: E501

        :param priv_key: The priv_key of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._priv_key = priv_key

    @property
    def priv_protocol(self):
        """Gets the priv_protocol of this SNMPv3ConnectionData.  # noqa: E501

        The privacy protocol of the SNMP connection.  # noqa: E501

        :return: The priv_protocol of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._priv_protocol

    @priv_protocol.setter
    def priv_protocol(self, priv_protocol):
        """Sets the priv_protocol of this SNMPv3ConnectionData.

        The privacy protocol of the SNMP connection.  # noqa: E501

        :param priv_protocol: The priv_protocol of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._priv_protocol = priv_protocol

    @property
    def user(self):
        """Gets the user of this SNMPv3ConnectionData.  # noqa: E501

        The user of the SNMP connection.  # noqa: E501

        :return: The user of this SNMPv3ConnectionData.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SNMPv3ConnectionData.

        The user of the SNMP connection.  # noqa: E501

        :param user: The user of this SNMPv3ConnectionData.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(SNMPv3ConnectionData, dict):
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
        if not isinstance(other, SNMPv3ConnectionData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SNMPv3ConnectionData):
            return True

        return self.to_dict() != other.to_dict()
