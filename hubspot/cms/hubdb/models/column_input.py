# coding: utf-8

"""
    HubDB endpoints

    HubDB is a relational data store that presents data as rows, columns, and cells in a table, much like a spreadsheet. HubDB tables can be added or modified [in the HubSpot CMS](https://knowledge.hubspot.com/cos-general/how-to-edit-hubdb-tables), but you can also use the API endpoints documented here. For more information on HubDB tables and using their data on a HubSpot site, see the [CMS developers site](https://designers.hubspot.com/docs/tools/hubdb). You can also see the [documentation for dynamic pages](https://designers.hubspot.com/docs/tutorials/how-to-build-dynamic-pages-with-hubdb) for more details about the `useForPages` field.  HubDB tables support `draft` and `live` versions and you can publish and unpublish the live version. This allows you to update data in the table, either for testing or to allow for a manual approval process, without affecting any live pages using the existing data. Draft data can be reviewed, pushed to live version, and published by a user working in HubSpot or published via the API. Draft data can also be discarded, allowing users to go back to the live version of the data without disrupting it. If a table is set to be `allowed for public access`, you can access the published version of the table and rows without any authentication.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.hubdb.configuration import Configuration


class ColumnInput(object):
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
        "archived": "bool",
        "name": "str",
        "options": "list[Option]",
        "width": "int",
        "label": "str",
        "id": "int",
        "type": "str",
    }

    attribute_map = {
        "archived": "archived",
        "name": "name",
        "options": "options",
        "width": "width",
        "label": "label",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self,
        archived=None,
        name=None,
        options=None,
        width=None,
        label=None,
        id=None,
        type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ColumnInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._archived = None
        self._name = None
        self._options = None
        self._width = None
        self._label = None
        self._id = None
        self._type = None
        self.discriminator = None

        if archived is not None:
            self.archived = archived
        self.name = name
        if options is not None:
            self.options = options
        if width is not None:
            self.width = width
        self.label = label
        if id is not None:
            self.id = id
        self.type = type

    @property
    def archived(self):
        """Gets the archived of this ColumnInput.  # noqa: E501

        Specifies whether the column is archived  # noqa: E501

        :return: The archived of this ColumnInput.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ColumnInput.

        Specifies whether the column is archived  # noqa: E501

        :param archived: The archived of this ColumnInput.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def name(self):
        """Gets the name of this ColumnInput.  # noqa: E501

        Name of the column  # noqa: E501

        :return: The name of this ColumnInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ColumnInput.

        Name of the column  # noqa: E501

        :param name: The name of this ColumnInput.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def options(self):
        """Gets the options of this ColumnInput.  # noqa: E501

        Options to choose for select and multi-select columns  # noqa: E501

        :return: The options of this ColumnInput.  # noqa: E501
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ColumnInput.

        Options to choose for select and multi-select columns  # noqa: E501

        :param options: The options of this ColumnInput.  # noqa: E501
        :type: list[Option]
        """

        self._options = options

    @property
    def width(self):
        """Gets the width of this ColumnInput.  # noqa: E501

        Column width for HubDB UI  # noqa: E501

        :return: The width of this ColumnInput.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ColumnInput.

        Column width for HubDB UI  # noqa: E501

        :param width: The width of this ColumnInput.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def label(self):
        """Gets the label of this ColumnInput.  # noqa: E501

        Label of the column  # noqa: E501

        :return: The label of this ColumnInput.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ColumnInput.

        Label of the column  # noqa: E501

        :param label: The label of this ColumnInput.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label`, must not be `None`"
            )  # noqa: E501

        self._label = label

    @property
    def id(self):
        """Gets the id of this ColumnInput.  # noqa: E501

        Column Id  # noqa: E501

        :return: The id of this ColumnInput.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ColumnInput.

        Column Id  # noqa: E501

        :param id: The id of this ColumnInput.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ColumnInput.  # noqa: E501

        Type of the column  # noqa: E501

        :return: The type of this ColumnInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ColumnInput.

        Type of the column  # noqa: E501

        :param type: The type of this ColumnInput.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

        self._type = type

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
        if not isinstance(other, ColumnInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ColumnInput):
            return True

        return self.to_dict() != other.to_dict()
