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

class MetricIntegration(object):
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
        'object': 'str',
        'id': 'str',
        'name': 'str',
        'category': 'str'
    }

    attribute_map = {
        'object': 'object',
        'id': 'id',
        'name': 'name',
        'category': 'category'
    }

    def __init__(self, object=None, id=None, name=None, category=None):  # noqa: E501
        """MetricIntegration - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._id = None
        self._name = None
        self._category = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category

    @property
    def object(self):
        """Gets the object of this MetricIntegration.  # noqa: E501


        :return: The object of this MetricIntegration.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this MetricIntegration.


        :param object: The object of this MetricIntegration.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def id(self):
        """Gets the id of this MetricIntegration.  # noqa: E501


        :return: The id of this MetricIntegration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricIntegration.


        :param id: The id of this MetricIntegration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MetricIntegration.  # noqa: E501


        :return: The name of this MetricIntegration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricIntegration.


        :param name: The name of this MetricIntegration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this MetricIntegration.  # noqa: E501


        :return: The category of this MetricIntegration.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this MetricIntegration.


        :param category: The category of this MetricIntegration.  # noqa: E501
        :type: str
        """

        self._category = category

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
        if issubclass(MetricIntegration, dict):
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
        if not isinstance(other, MetricIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
