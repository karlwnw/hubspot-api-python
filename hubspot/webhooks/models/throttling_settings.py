# coding: utf-8

"""
    Webhooks API

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.webhooks.configuration import Configuration


class ThrottlingSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'max_concurrent_requests': 'int',
        'period': 'str'
    }

    attribute_map = {
        'max_concurrent_requests': 'maxConcurrentRequests',
        'period': 'period'
    }

    def __init__(self, max_concurrent_requests=None, period=None, local_vars_configuration=None):  # noqa: E501
        """ThrottlingSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_concurrent_requests = None
        self._period = None
        self.discriminator = None

        self.max_concurrent_requests = max_concurrent_requests
        self.period = period

    @property
    def max_concurrent_requests(self):
        """Gets the max_concurrent_requests of this ThrottlingSettings.  # noqa: E501

        The maximum number of HTTP requests HubSpot will attempt to make to your app in a given time frame determined by `period`.  # noqa: E501

        :return: The max_concurrent_requests of this ThrottlingSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrent_requests

    @max_concurrent_requests.setter
    def max_concurrent_requests(self, max_concurrent_requests):
        """Sets the max_concurrent_requests of this ThrottlingSettings.

        The maximum number of HTTP requests HubSpot will attempt to make to your app in a given time frame determined by `period`.  # noqa: E501

        :param max_concurrent_requests: The max_concurrent_requests of this ThrottlingSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_concurrent_requests is None:  # noqa: E501
            raise ValueError("Invalid value for `max_concurrent_requests`, must not be `None`")  # noqa: E501

        self._max_concurrent_requests = max_concurrent_requests

    @property
    def period(self):
        """Gets the period of this ThrottlingSettings.  # noqa: E501

        Time scale for this setting. Can be either `SECONDLY` (per second) or `ROLLING_MINUTE` (per minute).  # noqa: E501

        :return: The period of this ThrottlingSettings.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ThrottlingSettings.

        Time scale for this setting. Can be either `SECONDLY` (per second) or `ROLLING_MINUTE` (per minute).  # noqa: E501

        :param period: The period of this ThrottlingSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and period is None:  # noqa: E501
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501
        allowed_values = ["SECONDLY", "ROLLING_MINUTE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and period not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"  # noqa: E501
                .format(period, allowed_values)
            )

        self._period = period

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThrottlingSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThrottlingSettings):
            return True

        return self.to_dict() != other.to_dict()
