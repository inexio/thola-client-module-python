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


class SBCComponent(object):
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
        'active_local_contacts': 'int',
        'agents': 'list[SBCComponentAgent]',
        'global_call_per_second': 'int',
        'global_concurrent_sessions_': 'int',
        'license_capacity': 'int',
        'realms': 'list[SBCComponentRealm]',
        'system_health_score': 'int',
        'system_redundancy': 'int',
        'transcoding_capacity': 'int'
    }

    attribute_map = {
        'active_local_contacts': 'active_local_contacts',
        'agents': 'agents',
        'global_call_per_second': 'global_call_per_second',
        'global_concurrent_sessions_': 'global_concurrent_sessions ',
        'license_capacity': 'license_capacity',
        'realms': 'realms',
        'system_health_score': 'system_health_score',
        'system_redundancy': 'system_redundancy',
        'transcoding_capacity': 'transcoding_capacity'
    }

    def __init__(self, active_local_contacts=None, agents=None, global_call_per_second=None, global_concurrent_sessions_=None, license_capacity=None, realms=None, system_health_score=None, system_redundancy=None, transcoding_capacity=None, _configuration=None):  # noqa: E501
        """SBCComponent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_local_contacts = None
        self._agents = None
        self._global_call_per_second = None
        self._global_concurrent_sessions_ = None
        self._license_capacity = None
        self._realms = None
        self._system_health_score = None
        self._system_redundancy = None
        self._transcoding_capacity = None
        self.discriminator = None

        if active_local_contacts is not None:
            self.active_local_contacts = active_local_contacts
        if agents is not None:
            self.agents = agents
        if global_call_per_second is not None:
            self.global_call_per_second = global_call_per_second
        if global_concurrent_sessions_ is not None:
            self.global_concurrent_sessions_ = global_concurrent_sessions_
        if license_capacity is not None:
            self.license_capacity = license_capacity
        if realms is not None:
            self.realms = realms
        if system_health_score is not None:
            self.system_health_score = system_health_score
        if system_redundancy is not None:
            self.system_redundancy = system_redundancy
        if transcoding_capacity is not None:
            self.transcoding_capacity = transcoding_capacity

    @property
    def active_local_contacts(self):
        """Gets the active_local_contacts of this SBCComponent.  # noqa: E501


        :return: The active_local_contacts of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._active_local_contacts

    @active_local_contacts.setter
    def active_local_contacts(self, active_local_contacts):
        """Sets the active_local_contacts of this SBCComponent.


        :param active_local_contacts: The active_local_contacts of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._active_local_contacts = active_local_contacts

    @property
    def agents(self):
        """Gets the agents of this SBCComponent.  # noqa: E501


        :return: The agents of this SBCComponent.  # noqa: E501
        :rtype: list[SBCComponentAgent]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this SBCComponent.


        :param agents: The agents of this SBCComponent.  # noqa: E501
        :type: list[SBCComponentAgent]
        """

        self._agents = agents

    @property
    def global_call_per_second(self):
        """Gets the global_call_per_second of this SBCComponent.  # noqa: E501


        :return: The global_call_per_second of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._global_call_per_second

    @global_call_per_second.setter
    def global_call_per_second(self, global_call_per_second):
        """Sets the global_call_per_second of this SBCComponent.


        :param global_call_per_second: The global_call_per_second of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._global_call_per_second = global_call_per_second

    @property
    def global_concurrent_sessions_(self):
        """Gets the global_concurrent_sessions_ of this SBCComponent.  # noqa: E501


        :return: The global_concurrent_sessions_ of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._global_concurrent_sessions_

    @global_concurrent_sessions_.setter
    def global_concurrent_sessions_(self, global_concurrent_sessions_):
        """Sets the global_concurrent_sessions_ of this SBCComponent.


        :param global_concurrent_sessions_: The global_concurrent_sessions_ of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._global_concurrent_sessions_ = global_concurrent_sessions_

    @property
    def license_capacity(self):
        """Gets the license_capacity of this SBCComponent.  # noqa: E501


        :return: The license_capacity of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._license_capacity

    @license_capacity.setter
    def license_capacity(self, license_capacity):
        """Sets the license_capacity of this SBCComponent.


        :param license_capacity: The license_capacity of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._license_capacity = license_capacity

    @property
    def realms(self):
        """Gets the realms of this SBCComponent.  # noqa: E501


        :return: The realms of this SBCComponent.  # noqa: E501
        :rtype: list[SBCComponentRealm]
        """
        return self._realms

    @realms.setter
    def realms(self, realms):
        """Sets the realms of this SBCComponent.


        :param realms: The realms of this SBCComponent.  # noqa: E501
        :type: list[SBCComponentRealm]
        """

        self._realms = realms

    @property
    def system_health_score(self):
        """Gets the system_health_score of this SBCComponent.  # noqa: E501


        :return: The system_health_score of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._system_health_score

    @system_health_score.setter
    def system_health_score(self, system_health_score):
        """Sets the system_health_score of this SBCComponent.


        :param system_health_score: The system_health_score of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._system_health_score = system_health_score

    @property
    def system_redundancy(self):
        """Gets the system_redundancy of this SBCComponent.  # noqa: E501


        :return: The system_redundancy of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._system_redundancy

    @system_redundancy.setter
    def system_redundancy(self, system_redundancy):
        """Sets the system_redundancy of this SBCComponent.


        :param system_redundancy: The system_redundancy of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._system_redundancy = system_redundancy

    @property
    def transcoding_capacity(self):
        """Gets the transcoding_capacity of this SBCComponent.  # noqa: E501


        :return: The transcoding_capacity of this SBCComponent.  # noqa: E501
        :rtype: int
        """
        return self._transcoding_capacity

    @transcoding_capacity.setter
    def transcoding_capacity(self, transcoding_capacity):
        """Sets the transcoding_capacity of this SBCComponent.


        :param transcoding_capacity: The transcoding_capacity of this SBCComponent.  # noqa: E501
        :type: int
        """

        self._transcoding_capacity = transcoding_capacity

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
        if issubclass(SBCComponent, dict):
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
        if not isinstance(other, SBCComponent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SBCComponent):
            return True

        return self.to_dict() != other.to_dict()