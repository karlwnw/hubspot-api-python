# coding: utf-8

"""
    Blog Post endpoints

    \"Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags\"  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.blog_posts.configuration import Configuration


class VersionUser(object):
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
    openapi_types = {"id": "str", "email": "str", "full_name": "str"}

    attribute_map = {"id": "id", "email": "email", "full_name": "fullName"}

    def __init__(
        self, id=None, email=None, full_name=None, local_vars_configuration=None
    ):  # noqa: E501
        """VersionUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._full_name = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.full_name = full_name

    @property
    def id(self):
        """Gets the id of this VersionUser.  # noqa: E501

        The unique ID of the User.  # noqa: E501

        :return: The id of this VersionUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionUser.

        The unique ID of the User.  # noqa: E501

        :param id: The id of this VersionUser.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this VersionUser.  # noqa: E501

        The email address of the user.  # noqa: E501

        :return: The email of this VersionUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this VersionUser.

        The email address of the user.  # noqa: E501

        :param email: The email of this VersionUser.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and email is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `email`, must not be `None`"
            )  # noqa: E501

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this VersionUser.  # noqa: E501

        The first and last name of the User.  # noqa: E501

        :return: The full_name of this VersionUser.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this VersionUser.

        The first and last name of the User.  # noqa: E501

        :param full_name: The full_name of this VersionUser.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and full_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `full_name`, must not be `None`"
            )  # noqa: E501

        self._full_name = full_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, VersionUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VersionUser):
            return True

        return self.to_dict() != other.to_dict()
