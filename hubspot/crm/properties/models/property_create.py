# coding: utf-8

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.properties.configuration import Configuration


class PropertyCreate(object):
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
        'name': 'str',
        'label': 'str',
        'type': 'str',
        'field_type': 'str',
        'group_name': 'str',
        'description': 'str',
        'options': 'list[OptionInput]',
        'display_order': 'int',
        'has_unique_value': 'bool',
        'hidden': 'bool',
        'form_field': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'type': 'type',
        'field_type': 'fieldType',
        'group_name': 'groupName',
        'description': 'description',
        'options': 'options',
        'display_order': 'displayOrder',
        'has_unique_value': 'hasUniqueValue',
        'hidden': 'hidden',
        'form_field': 'formField'
    }

    def __init__(self, name=None, label=None, type=None, field_type=None, group_name=None, description=None, options=None, display_order=None, has_unique_value=None, hidden=None, form_field=None, local_vars_configuration=None):  # noqa: E501
        """PropertyCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._label = None
        self._type = None
        self._field_type = None
        self._group_name = None
        self._description = None
        self._options = None
        self._display_order = None
        self._has_unique_value = None
        self._hidden = None
        self._form_field = None
        self.discriminator = None

        self.name = name
        self.label = label
        self.type = type
        self.field_type = field_type
        self.group_name = group_name
        if description is not None:
            self.description = description
        if options is not None:
            self.options = options
        if display_order is not None:
            self.display_order = display_order
        if has_unique_value is not None:
            self.has_unique_value = has_unique_value
        if hidden is not None:
            self.hidden = hidden
        if form_field is not None:
            self.form_field = form_field

    @property
    def name(self):
        """Gets the name of this PropertyCreate.  # noqa: E501

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :return: The name of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyCreate.

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :param name: The name of this PropertyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this PropertyCreate.  # noqa: E501

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PropertyCreate.

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this PropertyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def type(self):
        """Gets the type of this PropertyCreate.  # noqa: E501

        The data type of the property.  # noqa: E501

        :return: The type of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyCreate.

        The data type of the property.  # noqa: E501

        :param type: The type of this PropertyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "number", "date", "datetime", "enumeration"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def field_type(self):
        """Gets the field_type of this PropertyCreate.  # noqa: E501

        Controls how the property appears in HubSpot.  # noqa: E501

        :return: The field_type of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this PropertyCreate.

        Controls how the property appears in HubSpot.  # noqa: E501

        :param field_type: The field_type of this PropertyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501
        allowed_values = ["textarea", "text", "date", "file", "number", "select", "radio", "checkbox", "booleancheckbox"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `field_type` ({0}), must be one of {1}"  # noqa: E501
                .format(field_type, allowed_values)
            )

        self._field_type = field_type

    @property
    def group_name(self):
        """Gets the group_name of this PropertyCreate.  # noqa: E501

        The name of the property group the property belongs to.  # noqa: E501

        :return: The group_name of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PropertyCreate.

        The name of the property group the property belongs to.  # noqa: E501

        :param group_name: The group_name of this PropertyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def description(self):
        """Gets the description of this PropertyCreate.  # noqa: E501

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :return: The description of this PropertyCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PropertyCreate.

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :param description: The description of this PropertyCreate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def options(self):
        """Gets the options of this PropertyCreate.  # noqa: E501

        A list of valid options for the property. This field is required for enumerated properties.  # noqa: E501

        :return: The options of this PropertyCreate.  # noqa: E501
        :rtype: list[OptionInput]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PropertyCreate.

        A list of valid options for the property. This field is required for enumerated properties.  # noqa: E501

        :param options: The options of this PropertyCreate.  # noqa: E501
        :type: list[OptionInput]
        """

        self._options = options

    @property
    def display_order(self):
        """Gets the display_order of this PropertyCreate.  # noqa: E501

        Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values.  # noqa: E501

        :return: The display_order of this PropertyCreate.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PropertyCreate.

        Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values.  # noqa: E501

        :param display_order: The display_order of this PropertyCreate.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def has_unique_value(self):
        """Gets the has_unique_value of this PropertyCreate.  # noqa: E501

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :return: The has_unique_value of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._has_unique_value

    @has_unique_value.setter
    def has_unique_value(self, has_unique_value):
        """Sets the has_unique_value of this PropertyCreate.

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :param has_unique_value: The has_unique_value of this PropertyCreate.  # noqa: E501
        :type: bool
        """

        self._has_unique_value = has_unique_value

    @property
    def hidden(self):
        """Gets the hidden of this PropertyCreate.  # noqa: E501

        If true, the property won't be visible and can't be used in HubSpot.  # noqa: E501

        :return: The hidden of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this PropertyCreate.

        If true, the property won't be visible and can't be used in HubSpot.  # noqa: E501

        :param hidden: The hidden of this PropertyCreate.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def form_field(self):
        """Gets the form_field of this PropertyCreate.  # noqa: E501

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :return: The form_field of this PropertyCreate.  # noqa: E501
        :rtype: bool
        """
        return self._form_field

    @form_field.setter
    def form_field(self, form_field):
        """Sets the form_field of this PropertyCreate.

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :param form_field: The form_field of this PropertyCreate.  # noqa: E501
        :type: bool
        """

        self._form_field = form_field

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
        if not isinstance(other, PropertyCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyCreate):
            return True

        return self.to_dict() != other.to_dict()
