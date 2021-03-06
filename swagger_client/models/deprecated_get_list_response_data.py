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

class DeprecatedGetListResponseData(object):
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
        'type': 'str',
        'created': 'str',
        'updated': 'str',
        'person_count': 'int'
    }

    attribute_map = {
        'object': 'object',
        'id': 'id',
        'type': 'type',
        'created': 'created',
        'updated': 'updated',
        'person_count': 'person_count'
    }

    def __init__(self, object=None, id=None, type=None, created=None, updated=None, person_count=None):  # noqa: E501
        """DeprecatedGetListResponseData - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._id = None
        self._type = None
        self._created = None
        self._updated = None
        self._person_count = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if person_count is not None:
            self.person_count = person_count

    @property
    def object(self):
        """Gets the object of this DeprecatedGetListResponseData.  # noqa: E501


        :return: The object of this DeprecatedGetListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this DeprecatedGetListResponseData.


        :param object: The object of this DeprecatedGetListResponseData.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def id(self):
        """Gets the id of this DeprecatedGetListResponseData.  # noqa: E501


        :return: The id of this DeprecatedGetListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeprecatedGetListResponseData.


        :param id: The id of this DeprecatedGetListResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this DeprecatedGetListResponseData.  # noqa: E501


        :return: The type of this DeprecatedGetListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeprecatedGetListResponseData.


        :param type: The type of this DeprecatedGetListResponseData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created(self):
        """Gets the created of this DeprecatedGetListResponseData.  # noqa: E501


        :return: The created of this DeprecatedGetListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DeprecatedGetListResponseData.


        :param created: The created of this DeprecatedGetListResponseData.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this DeprecatedGetListResponseData.  # noqa: E501


        :return: The updated of this DeprecatedGetListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this DeprecatedGetListResponseData.


        :param updated: The updated of this DeprecatedGetListResponseData.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def person_count(self):
        """Gets the person_count of this DeprecatedGetListResponseData.  # noqa: E501


        :return: The person_count of this DeprecatedGetListResponseData.  # noqa: E501
        :rtype: int
        """
        return self._person_count

    @person_count.setter
    def person_count(self, person_count):
        """Sets the person_count of this DeprecatedGetListResponseData.


        :param person_count: The person_count of this DeprecatedGetListResponseData.  # noqa: E501
        :type: int
        """

        self._person_count = person_count

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
        if issubclass(DeprecatedGetListResponseData, dict):
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
        if not isinstance(other, DeprecatedGetListResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
