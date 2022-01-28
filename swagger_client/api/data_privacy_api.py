# coding: utf-8

"""
    Klaviyo API

    Empowering creators to own their destiny  # noqa: E501

    OpenAPI spec version: 2021.11.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DataPrivacyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.warned = []

    def request_deletion(self, **kwargs):  # noqa: E501
        """Request a Deletion  # noqa: E501

        Request a data privacy-compliant deletion for the person record corresponding to an email address, phone number, or person identifier.   **If multiple person records exist for the provided identifier, only one of them will be deleted.**  The arguments should be sent as content type application/json.           Note that only **one** identifier (email, phone_number, or person_id) can be specified.  In addition to your API key, you need to set exactly one of the following parameters: `email`, `phone_number`, `or person_id`, along with the associated `string` value.   Examples:  Email:    `{\"email\":\"abraham.lincoln@klaviyo.com\"}`    Phone Number:      `{\"phone_number\":\"+13239169023\"}`    Person ID:      `{\"person_id\":\"PERSON_ID\"}`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_deletion(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_deletion_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.request_deletion_with_http_info(**kwargs)  # noqa: E501
            return data

    def request_deletion_with_http_info(self, **kwargs):  # noqa: E501
        """Request a Deletion  # noqa: E501

        Request a data privacy-compliant deletion for the person record corresponding to an email address, phone number, or person identifier.   **If multiple person records exist for the provided identifier, only one of them will be deleted.**  The arguments should be sent as content type application/json.           Note that only **one** identifier (email, phone_number, or person_id) can be specified.  In addition to your API key, you need to set exactly one of the following parameters: `email`, `phone_number`, `or person_id`, along with the associated `string` value.   Examples:  Email:    `{\"email\":\"abraham.lincoln@klaviyo.com\"}`    Phone Number:      `{\"phone_number\":\"+13239169023\"}`    Person ID:      `{\"person_id\":\"PERSON_ID\"}`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_deletion_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_deletion" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/data-privacy/deletion-request', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)