# coding: utf-8

"""
    Klaviyo API

    Empowering creators to own their destiny  # noqa: E501

    OpenAPI spec version: 2021.11.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CampaignTemplate(object):
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
        'html': 'str'
    }

    attribute_map = {
        'object': 'object',
        'id': 'id',
        'html': 'html'
    }

    def __init__(self, object=None, id=None, html=None):  # noqa: E501
        """CampaignTemplate - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._id = None
        self._html = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if id is not None:
            self.id = id
        if html is not None:
            self.html = html

    @property
    def object(self):
        """Gets the object of this CampaignTemplate.  # noqa: E501


        :return: The object of this CampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CampaignTemplate.


        :param object: The object of this CampaignTemplate.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def id(self):
        """Gets the id of this CampaignTemplate.  # noqa: E501


        :return: The id of this CampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CampaignTemplate.


        :param id: The id of this CampaignTemplate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def html(self):
        """Gets the html of this CampaignTemplate.  # noqa: E501


        :return: The html of this CampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this CampaignTemplate.


        :param html: The html of this CampaignTemplate.  # noqa: E501
        :type: str
        """

        self._html = html

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
        if issubclass(CampaignTemplate, dict):
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
        if not isinstance(other, CampaignTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
