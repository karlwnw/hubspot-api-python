# coding: utf-8

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.schemas.configuration import Configuration


class AssociationDefinitionEgg(object):
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
        'from_object_type_id': 'str',
        'to_object_type_id': 'str',
        'name': 'str',
        'cardinality': 'str',
        'inverse_cardinality': 'str'
    }

    attribute_map = {
        'from_object_type_id': 'fromObjectTypeId',
        'to_object_type_id': 'toObjectTypeId',
        'name': 'name',
        'cardinality': 'cardinality',
        'inverse_cardinality': 'inverseCardinality'
    }

    def __init__(self, from_object_type_id=None, to_object_type_id=None, name=None, cardinality=None, inverse_cardinality=None, local_vars_configuration=None):  # noqa: E501
        """AssociationDefinitionEgg - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_object_type_id = None
        self._to_object_type_id = None
        self._name = None
        self._cardinality = None
        self._inverse_cardinality = None
        self.discriminator = None

        self.from_object_type_id = from_object_type_id
        self.to_object_type_id = to_object_type_id
        if name is not None:
            self.name = name
        self.cardinality = cardinality
        self.inverse_cardinality = inverse_cardinality

    @property
    def from_object_type_id(self):
        """Gets the from_object_type_id of this AssociationDefinitionEgg.  # noqa: E501

        ID of the primary object type to link from.  # noqa: E501

        :return: The from_object_type_id of this AssociationDefinitionEgg.  # noqa: E501
        :rtype: str
        """
        return self._from_object_type_id

    @from_object_type_id.setter
    def from_object_type_id(self, from_object_type_id):
        """Sets the from_object_type_id of this AssociationDefinitionEgg.

        ID of the primary object type to link from.  # noqa: E501

        :param from_object_type_id: The from_object_type_id of this AssociationDefinitionEgg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and from_object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `from_object_type_id`, must not be `None`")  # noqa: E501

        self._from_object_type_id = from_object_type_id

    @property
    def to_object_type_id(self):
        """Gets the to_object_type_id of this AssociationDefinitionEgg.  # noqa: E501

        ID of the target object type ID to link to.  # noqa: E501

        :return: The to_object_type_id of this AssociationDefinitionEgg.  # noqa: E501
        :rtype: str
        """
        return self._to_object_type_id

    @to_object_type_id.setter
    def to_object_type_id(self, to_object_type_id):
        """Sets the to_object_type_id of this AssociationDefinitionEgg.

        ID of the target object type ID to link to.  # noqa: E501

        :param to_object_type_id: The to_object_type_id of this AssociationDefinitionEgg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to_object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `to_object_type_id`, must not be `None`")  # noqa: E501

        self._to_object_type_id = to_object_type_id

    @property
    def name(self):
        """Gets the name of this AssociationDefinitionEgg.  # noqa: E501

        A unique name for this association.  # noqa: E501

        :return: The name of this AssociationDefinitionEgg.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssociationDefinitionEgg.

        A unique name for this association.  # noqa: E501

        :param name: The name of this AssociationDefinitionEgg.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cardinality(self):
        """Gets the cardinality of this AssociationDefinitionEgg.  # noqa: E501


        :return: The cardinality of this AssociationDefinitionEgg.  # noqa: E501
        :rtype: str
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """Sets the cardinality of this AssociationDefinitionEgg.


        :param cardinality: The cardinality of this AssociationDefinitionEgg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cardinality is None:  # noqa: E501
            raise ValueError("Invalid value for `cardinality`, must not be `None`")  # noqa: E501
        allowed_values = ["ONE_TO_ONE", "ONE_TO_MANY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cardinality not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cardinality` ({0}), must be one of {1}"  # noqa: E501
                .format(cardinality, allowed_values)
            )

        self._cardinality = cardinality

    @property
    def inverse_cardinality(self):
        """Gets the inverse_cardinality of this AssociationDefinitionEgg.  # noqa: E501


        :return: The inverse_cardinality of this AssociationDefinitionEgg.  # noqa: E501
        :rtype: str
        """
        return self._inverse_cardinality

    @inverse_cardinality.setter
    def inverse_cardinality(self, inverse_cardinality):
        """Sets the inverse_cardinality of this AssociationDefinitionEgg.


        :param inverse_cardinality: The inverse_cardinality of this AssociationDefinitionEgg.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inverse_cardinality is None:  # noqa: E501
            raise ValueError("Invalid value for `inverse_cardinality`, must not be `None`")  # noqa: E501
        allowed_values = ["ONE_TO_ONE", "ONE_TO_MANY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and inverse_cardinality not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `inverse_cardinality` ({0}), must be one of {1}"  # noqa: E501
                .format(inverse_cardinality, allowed_values)
            )

        self._inverse_cardinality = inverse_cardinality

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
        if not isinstance(other, AssociationDefinitionEgg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssociationDefinitionEgg):
            return True

        return self.to_dict() != other.to_dict()
