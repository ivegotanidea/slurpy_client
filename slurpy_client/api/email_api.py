"""
    Slurpy

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from slurpy_client.api_client import ApiClient, Endpoint
from slurpy_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from slurpy_client.model.http_validation_error import HTTPValidationError


class EmailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_email(
            self,
            email,
            password,
            folder,
            timeout,
            **kwargs
        ):
            """Get Mail  # noqa: E501

            Get email  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_email(email, password, folder, timeout, async_req=True)
            >>> result = thread.get()

            Args:
                email (str):
                password (str):
                folder (str):
                timeout (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['email'] = \
                email
            kwargs['password'] = \
                password
            kwargs['folder'] = \
                folder
            kwargs['timeout'] = \
                timeout
            return self.call_with_http_info(**kwargs)

        self.get_email = Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/api/v1.0/email/mail/{email}/{password}/{folder}/{timeout}',
                'operation_id': 'get_email',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                    'password',
                    'folder',
                    'timeout',
                ],
                'required': [
                    'email',
                    'password',
                    'folder',
                    'timeout',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'email':
                        (str,),
                    'password':
                        (str,),
                    'folder':
                        (str,),
                    'timeout':
                        (int,),
                },
                'attribute_map': {
                    'email': 'email',
                    'password': 'password',
                    'folder': 'folder',
                    'timeout': 'timeout',
                },
                'location_map': {
                    'email': 'path',
                    'password': 'path',
                    'folder': 'path',
                    'timeout': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_email
        )

        def __get_inbox_folders(
            self,
            email,
            password,
            **kwargs
        ):
            """Get Folders  # noqa: E501

            Get inbox folders  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_inbox_folders(email, password, async_req=True)
            >>> result = thread.get()

            Args:
                email (str):
                password (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['email'] = \
                email
            kwargs['password'] = \
                password
            return self.call_with_http_info(**kwargs)

        self.get_inbox_folders = Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/api/v1.0/email/folders/{email}/{password}',
                'operation_id': 'get_inbox_folders',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                    'password',
                ],
                'required': [
                    'email',
                    'password',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'email':
                        (str,),
                    'password':
                        (str,),
                },
                'attribute_map': {
                    'email': 'email',
                    'password': 'password',
                },
                'location_map': {
                    'email': 'path',
                    'password': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_inbox_folders
        )

        def __get_unseen(
            self,
            email,
            password,
            limit,
            **kwargs
        ):
            """Get Unseen  # noqa: E501

            Get unseen email  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_unseen(email, password, limit, async_req=True)
            >>> result = thread.get()

            Args:
                email (str):
                password (str):
                limit (int):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['email'] = \
                email
            kwargs['password'] = \
                password
            kwargs['limit'] = \
                limit
            return self.call_with_http_info(**kwargs)

        self.get_unseen = Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/api/v1.0/email/unseen/{email}/{password}/{limit}',
                'operation_id': 'get_unseen',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'email',
                    'password',
                    'limit',
                ],
                'required': [
                    'email',
                    'password',
                    'limit',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'email':
                        (str,),
                    'password':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'email': 'email',
                    'password': 'password',
                    'limit': 'limit',
                },
                'location_map': {
                    'email': 'path',
                    'password': 'path',
                    'limit': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_unseen
        )
