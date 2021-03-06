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

class CampaignIdScheduleBody(object):
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
        'send_time': 'str'
    }

    attribute_map = {
        'send_time': 'send_time'
    }

    def __init__(self, send_time='2022-01-13 00:00:00'):  # noqa: E501
        """CampaignIdScheduleBody - a model defined in Swagger"""  # noqa: E501
        self._send_time = None
        self.discriminator = None
        self.send_time = send_time

    @property
    def send_time(self):
        """Gets the send_time of this CampaignIdScheduleBody.  # noqa: E501

         A timestamp of the format `%Y-%m-%d %H:%M:%S` in the UTC timezone.  Ex:  `2022-01-13 00:00:00`   # noqa: E501

        :return: The send_time of this CampaignIdScheduleBody.  # noqa: E501
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this CampaignIdScheduleBody.

         A timestamp of the format `%Y-%m-%d %H:%M:%S` in the UTC timezone.  Ex:  `2022-01-13 00:00:00`   # noqa: E501

        :param send_time: The send_time of this CampaignIdScheduleBody.  # noqa: E501
        :type: str
        """
        if send_time is None:
            raise ValueError("Invalid value for `send_time`, must not be `None`")  # noqa: E501

        self._send_time = send_time

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
        if issubclass(CampaignIdScheduleBody, dict):
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
        if not isinstance(other, CampaignIdScheduleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
