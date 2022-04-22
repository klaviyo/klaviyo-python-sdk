from __future__ import absolute_import

from __future__ import print_function
import time
import swagger_client
import inspect
import tenacity
import klaviyo_sdk.custom_retry as custom_retry
import json
import base64
import requests


class Client:

    def __init__(self, api_key,test_host=None, max_delay=60, max_retries=3):

        configuration = swagger_client.Configuration()

        self.api_key = api_key

        self.retry_codes = [429,503,504]

        self.retry_logic = tenacity.retry(
            reraise=True,
            retry=custom_retry.retry_if_qualifies(self.retry_codes),
            wait=tenacity.wait.wait_random_exponential(multiplier = 1, max = max_delay/max_retries),
            stop=tenacity.stop.stop_after_attempt(max_retries)
        )

        configuration.api_key["api_key"] = api_key
        if test_host:
            configuration.host = test_host

        subclient_names = [item_name for item_name in dir(swagger_client.api) if inspect.isclass(getattr(swagger_client.api,item_name)) and 'with_http_info' not in item_name]

        for subclient_name in subclient_names:

            setattr(self,subclient_name,eval(f'swagger_client.{subclient_name}(swagger_client.ApiClient(configuration))'))

            subclient = eval(f'self.{subclient_name}')

            for attribute_name in dir(subclient):

                if f'{attribute_name}_with_http_info' in dir(subclient):

                    endpoint = eval(f'subclient.{attribute_name}')

                    endpoint = self.retry_logic(endpoint)

                    setattr(subclient,attribute_name,endpoint)

        self.TrackIdentifyApi.track_post = self.post_update(self.TrackIdentifyApi.track_post)
        self.TrackIdentifyApi.identify_post = self.post_update(self.TrackIdentifyApi.identify_post)
        self.TrackIdentifyApi.track_get = self.get_update(self.TrackIdentifyApi.track_get)
        self.TrackIdentifyApi.identify_get = self.get_update(self.TrackIdentifyApi.identify_get)

        self.ProfilesApi.update_profile = self.update_profile_fix(self.ProfilesApi.update_profile)

        # last step: drop 'Api' suffix from sublient name
        for subclient_name in subclient_names:

            setattr(self,subclient_name[:-3],eval(f'self.{subclient_name}'))


    def is_error(self, status):

        return not (200 <= status <= 299)

    def update_profile_fix(self, func):
        def wrapped_func(person_id='PERSON_ID', params={}):

            url = f"https://a.klaviyo.com/api/v1/person/{person_id}"

            querystring = {"api_key":self.api_key}

            for key in params:

                querystring[str(key)] = str(params[key])

            headers = {
                "Accept": "application/json",
                "user-agent" : "klaviyo-python-sdk/1.0.3.20220329"
                }

            response = requests.request("PUT", url, headers=headers, params=querystring)

            if self.is_error(response.status_code):

                e = swagger_client.rest.ApiException(status=response.status_code, reason=response.reason, http_resp=response)
                raise(e)

            return response.json()

        return wrapped_func



    def post_update(self, func):
        def wrapped_func(data={}):
            if type(data) is not str:
                data = json.dumps(data)
            return func(data=data)
        return wrapped_func


    def get_update(self, func):
        def wrapped_func(data={}):        

            if type(data) is dict:
                json_string = json.dumps(data)
                utf = json_string.encode('utf-8')
                data = base64.b64encode(utf)

                return func(data)

            elif type(data) is str:
                utf = data.encode('utf-8')
                data = base64.b64encode(utf)

                return func(data)

            elif type(data) is bytes:

                if b'{' in data:
                    data = base64.b64encode(data)

                return func(data)

        return wrapped_func
        
        