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


class HubDbTableCloneRequest(object):
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
        'new_name': 'str',
        'new_label': 'str',
        'copy_rows': 'bool'
    }

    attribute_map = {
        'new_name': 'newName',
        'new_label': 'newLabel',
        'copy_rows': 'copyRows'
    }

    def __init__(self, new_name=None, new_label=None, copy_rows=None, local_vars_configuration=None):  # noqa: E501
        """HubDbTableCloneRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._new_name = None
        self._new_label = None
        self._copy_rows = None
        self.discriminator = None

        self.new_name = new_name
        self.new_label = new_label
        if copy_rows is not None:
            self.copy_rows = copy_rows

    @property
    def new_name(self):
        """Gets the new_name of this HubDbTableCloneRequest.  # noqa: E501

        The new name for the cloned table  # noqa: E501

        :return: The new_name of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this HubDbTableCloneRequest.

        The new name for the cloned table  # noqa: E501

        :param new_name: The new_name of this HubDbTableCloneRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_name is None:  # noqa: E501
            raise ValueError("Invalid value for `new_name`, must not be `None`")  # noqa: E501

        self._new_name = new_name

    @property
    def new_label(self):
        """Gets the new_label of this HubDbTableCloneRequest.  # noqa: E501

        The new label for the cloned table  # noqa: E501

        :return: The new_label of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_label

    @new_label.setter
    def new_label(self, new_label):
        """Sets the new_label of this HubDbTableCloneRequest.

        The new label for the cloned table  # noqa: E501

        :param new_label: The new_label of this HubDbTableCloneRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_label is None:  # noqa: E501
            raise ValueError("Invalid value for `new_label`, must not be `None`")  # noqa: E501

        self._new_label = new_label

    @property
    def copy_rows(self):
        """Gets the copy_rows of this HubDbTableCloneRequest.  # noqa: E501

        Specifies whether to copy the rows during clone  # noqa: E501

        :return: The copy_rows of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: bool
        """
        return self._copy_rows

    @copy_rows.setter
    def copy_rows(self, copy_rows):
        """Sets the copy_rows of this HubDbTableCloneRequest.

        Specifies whether to copy the rows during clone  # noqa: E501

        :param copy_rows: The copy_rows of this HubDbTableCloneRequest.  # noqa: E501
        :type: bool
        """

        self._copy_rows = copy_rows

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
        if not isinstance(other, HubDbTableCloneRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubDbTableCloneRequest):
            return True

        return self.to_dict() != other.to_dict()
