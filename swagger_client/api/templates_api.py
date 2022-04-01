# coding: utf-8

"""
    Klaviyo API

    Empowering creators to own their destiny  # noqa: E501

    OpenAPI spec version: 2022.03.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TemplatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.warned = []

    def clone_template(self, template_id, **kwargs):  # noqa: E501
        """Clone Template  # noqa: E501

        Creates a copy of a given template with a new name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clone_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str name:
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clone_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.clone_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def clone_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Clone Template  # noqa: E501

        Creates a copy of a given template with a new name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clone_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str name:
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['template_id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clone_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `clone_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-template/{template_id}/clone', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Template',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_template(self, **kwargs):  # noqa: E501
        """Create New Template  # noqa: E501

        Creates a new email template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_template(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str html:
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_template_with_http_info(self, **kwargs):  # noqa: E501
        """Create New Template  # noqa: E501

        Creates a new email template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_template_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str html:
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['name', 'html']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'html' in params:
            form_params.append(('html', params['html']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-templates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Template',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_template(self, template_id, **kwargs):  # noqa: E501
        """Delete Template  # noqa: E501

        Deletes a given template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def delete_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Delete Template  # noqa: E501

        Deletes a given template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `delete_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-template/{template_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_templates(self, **kwargs):  # noqa: E501
        """Get All Templates  # noqa: E501

        Returns a list of all the email templates you've created. The templates are returned in sorted order by `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: For pagination, which page of results to return. Default = 0
        :param int count: For pagination, the number of results to return. Max = 100
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_templates_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Templates  # noqa: E501

        Returns a list of all the email templates you've created. The templates are returned in sorted order by `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: For pagination, which page of results to return. Default = 0
        :param int count: For pagination, the number of results to return. Max = 100
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_templates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}


        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_template(self, template_id, **kwargs):  # noqa: E501
        """Render Template  # noqa: E501

        Renders the specified template with the provided data and return HTML and text versions of the email.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.render_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str context:
        :return: RenderedTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.render_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.render_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def render_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Render Template  # noqa: E501

        Renders the specified template with the provided data and return HTML and text versions of the email.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.render_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str context:
        :return: RenderedTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['template_id', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `render_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}
        if 'context' in params:
            form_params.append(('context', params['context']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-template/{template_id}/render', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderedTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_template(self, template_id, **kwargs):  # noqa: E501
        """Render and Send Template  # noqa: E501

        Renders the specified template with the provided data and send the contents in an email via the service specified. This API is intended to test templates only, and is rate limited to the following thresholds: 100/hour, 1,000/day.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str from_email:
        :param str from_name:
        :param str subject:
        :param str to:
        :param str context:
        :return: RenderedTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.send_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def send_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Render and Send Template  # noqa: E501

        Renders the specified template with the provided data and send the contents in an email via the service specified. This API is intended to test templates only, and is rate limited to the following thresholds: 100/hour, 1,000/day.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str from_email:
        :param str from_name:
        :param str subject:
        :param str to:
        :param str context:
        :return: RenderedTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['template_id', 'from_email', 'from_name', 'subject', 'to', 'context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `send_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}
        if 'from_email' in params:
            form_params.append(('from_email', params['from_email']))  # noqa: E501
        if 'from_name' in params:
            form_params.append(('from_name', params['from_name']))  # noqa: E501
        if 'subject' in params:
            form_params.append(('subject', params['subject']))  # noqa: E501
        if 'to' in params:
            form_params.append(('to', params['to']))  # noqa: E501
        if 'context' in params:
            form_params.append(('context', params['context']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-template/{template_id}/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderedTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_template(self, template_id, **kwargs):  # noqa: E501
        """Update Template  # noqa: E501

        Updates the name and/or HTML content of a template. Only updates imported HTML templates; does not currently update drag & drop templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str name:
        :param str html:
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def update_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Update Template  # noqa: E501

        Updates the name and/or HTML content of a template. Only updates imported HTML templates; does not currently update drag & drop templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str name:
        :param str html:
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """


        all_params = ['template_id', 'name', 'html']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `update_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}


        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'html' in params:
            form_params.append(('html', params['html']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/email-template/{template_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Template',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
