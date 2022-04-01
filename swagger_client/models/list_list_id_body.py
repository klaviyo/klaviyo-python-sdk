# coding: utf-8

"""
    Klaviyo API

    Empowering creators to own their destiny  # noqa: E501

    OpenAPI spec version: 2022.03.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ListListIdBody(object):
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
        'list_name': 'str'
    }

    attribute_map = {
        'list_name': 'list_name'
    }

    def __init__(self, list_name='MyRenamedList'):  # noqa: E501
        """ListListIdBody - a model defined in Swagger"""  # noqa: E501
        self._list_name = None
        self.discriminator = None
        self.list_name = list_name

    @property
    def list_name(self):
        """Gets the list_name of this ListListIdBody.  # noqa: E501


        :return: The list_name of this ListListIdBody.  # noqa: E501
        :rtype: str
        """
        return self._list_name

    @list_name.setter
    def list_name(self, list_name):
        """Sets the list_name of this ListListIdBody.


        :param list_name: The list_name of this ListListIdBody.  # noqa: E501
        :type: str
        """
        if list_name is None:
            raise ValueError("Invalid value for `list_name`, must not be `None`")  # noqa: E501

        self._list_name = list_name

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
        if issubclass(ListListIdBody, dict):
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
        if not isinstance(other, ListListIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
