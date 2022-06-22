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

class InlineResponse2009Records(object):
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
        'id': 'str',
        'email': 'str',
        'phone_number': 'str',
        'push_token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'phone_number': 'phone_number',
        'push_token': 'push_token'
    }

    def __init__(self, id=None, email=None, phone_number=None, push_token=None):  # noqa: E501
        """InlineResponse2009Records - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._email = None
        self._phone_number = None
        self._push_token = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if push_token is not None:
            self.push_token = push_token

    @property
    def id(self):
        """Gets the id of this InlineResponse2009Records.  # noqa: E501


        :return: The id of this InlineResponse2009Records.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2009Records.


        :param id: The id of this InlineResponse2009Records.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this InlineResponse2009Records.  # noqa: E501


        :return: The email of this InlineResponse2009Records.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse2009Records.


        :param email: The email of this InlineResponse2009Records.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse2009Records.  # noqa: E501


        :return: The phone_number of this InlineResponse2009Records.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse2009Records.


        :param phone_number: The phone_number of this InlineResponse2009Records.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def push_token(self):
        """Gets the push_token of this InlineResponse2009Records.  # noqa: E501


        :return: The push_token of this InlineResponse2009Records.  # noqa: E501
        :rtype: str
        """
        return self._push_token

    @push_token.setter
    def push_token(self, push_token):
        """Sets the push_token of this InlineResponse2009Records.


        :param push_token: The push_token of this InlineResponse2009Records.  # noqa: E501
        :type: str
        """

        self._push_token = push_token

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
        if issubclass(InlineResponse2009Records, dict):
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
        if not isinstance(other, InlineResponse2009Records):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
