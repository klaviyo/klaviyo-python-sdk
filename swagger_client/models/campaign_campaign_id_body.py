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

class CampaignCampaignIdBody(object):
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
        'list_id': 'str',
        'template_id': 'str',
        'from_email': 'str',
        'from_name': 'str',
        'subject': 'str',
        'name': 'str',
        'use_smart_sending': 'bool',
        'add_google_analytics': 'bool'
    }

    attribute_map = {
        'list_id': 'list_id',
        'template_id': 'template_id',
        'from_email': 'from_email',
        'from_name': 'from_name',
        'subject': 'subject',
        'name': 'name',
        'use_smart_sending': 'use_smart_sending',
        'add_google_analytics': 'add_google_analytics'
    }

    def __init__(self, list_id=None, template_id=None, from_email=None, from_name=None, subject=None, name=None, use_smart_sending=None, add_google_analytics=None):  # noqa: E501
        """CampaignCampaignIdBody - a model defined in Swagger"""  # noqa: E501
        self._list_id = None
        self._template_id = None
        self._from_email = None
        self._from_name = None
        self._subject = None
        self._name = None
        self._use_smart_sending = None
        self._add_google_analytics = None
        self.discriminator = None
        if list_id is not None:
            self.list_id = list_id
        if template_id is not None:
            self.template_id = template_id
        if from_email is not None:
            self.from_email = from_email
        if from_name is not None:
            self.from_name = from_name
        if subject is not None:
            self.subject = subject
        if name is not None:
            self.name = name
        if use_smart_sending is not None:
            self.use_smart_sending = use_smart_sending
        if add_google_analytics is not None:
            self.add_google_analytics = add_google_analytics

    @property
    def list_id(self):
        """Gets the list_id of this CampaignCampaignIdBody.  # noqa: E501

        The list you will send the campaign to.  # noqa: E501

        :return: The list_id of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this CampaignCampaignIdBody.

        The list you will send the campaign to.  # noqa: E501

        :param list_id: The list_id of this CampaignCampaignIdBody.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def template_id(self):
        """Gets the template_id of this CampaignCampaignIdBody.  # noqa: E501

        The ID of the Email Template object that will be the content of this campaign. Note the Email Template is copied when creating this campaign, so future changes to that Email Template will not alter the content of this campaign.  # noqa: E501

        :return: The template_id of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CampaignCampaignIdBody.

        The ID of the Email Template object that will be the content of this campaign. Note the Email Template is copied when creating this campaign, so future changes to that Email Template will not alter the content of this campaign.  # noqa: E501

        :param template_id: The template_id of this CampaignCampaignIdBody.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def from_email(self):
        """Gets the from_email of this CampaignCampaignIdBody.  # noqa: E501

        The email address your email will be sent from and will be used in the reply-to header.  # noqa: E501

        :return: The from_email of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this CampaignCampaignIdBody.

        The email address your email will be sent from and will be used in the reply-to header.  # noqa: E501

        :param from_email: The from_email of this CampaignCampaignIdBody.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

    @property
    def from_name(self):
        """Gets the from_name of this CampaignCampaignIdBody.  # noqa: E501

        The name or label associated with the email address you're sending from.  # noqa: E501

        :return: The from_name of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this CampaignCampaignIdBody.

        The name or label associated with the email address you're sending from.  # noqa: E501

        :param from_name: The from_name of this CampaignCampaignIdBody.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def subject(self):
        """Gets the subject of this CampaignCampaignIdBody.  # noqa: E501

        The email subject of the campaign  # noqa: E501

        :return: The subject of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CampaignCampaignIdBody.

        The email subject of the campaign  # noqa: E501

        :param subject: The subject of this CampaignCampaignIdBody.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def name(self):
        """Gets the name of this CampaignCampaignIdBody.  # noqa: E501

        A name for this campaign. If not specified, this will default to the subject of the campaign.  # noqa: E501

        :return: The name of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CampaignCampaignIdBody.

        A name for this campaign. If not specified, this will default to the subject of the campaign.  # noqa: E501

        :param name: The name of this CampaignCampaignIdBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def use_smart_sending(self):
        """Gets the use_smart_sending of this CampaignCampaignIdBody.  # noqa: E501

        If set, limits the number of emails sent to an individual within a short period. Campaigns initially default to `true`.  # noqa: E501

        :return: The use_smart_sending of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._use_smart_sending

    @use_smart_sending.setter
    def use_smart_sending(self, use_smart_sending):
        """Sets the use_smart_sending of this CampaignCampaignIdBody.

        If set, limits the number of emails sent to an individual within a short period. Campaigns initially default to `true`.  # noqa: E501

        :param use_smart_sending: The use_smart_sending of this CampaignCampaignIdBody.  # noqa: E501
        :type: bool
        """

        self._use_smart_sending = use_smart_sending

    @property
    def add_google_analytics(self):
        """Gets the add_google_analytics of this CampaignCampaignIdBody.  # noqa: E501

        If specified, adds Google Analytics tracking tags to links. Campaigns initially default to `false`.  # noqa: E501

        :return: The add_google_analytics of this CampaignCampaignIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._add_google_analytics

    @add_google_analytics.setter
    def add_google_analytics(self, add_google_analytics):
        """Sets the add_google_analytics of this CampaignCampaignIdBody.

        If specified, adds Google Analytics tracking tags to links. Campaigns initially default to `false`.  # noqa: E501

        :param add_google_analytics: The add_google_analytics of this CampaignCampaignIdBody.  # noqa: E501
        :type: bool
        """

        self._add_google_analytics = add_google_analytics

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
        if issubclass(CampaignCampaignIdBody, dict):
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
        if not isinstance(other, CampaignCampaignIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
