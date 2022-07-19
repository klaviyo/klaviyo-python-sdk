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

        self.retry_codes = [429,503,504,524]

        self.retry_logic = tenacity.retry(
            reraise=True,
            retry=custom_retry.retry_if_qualifies(self.retry_codes),
            wait=tenacity.wait.wait_random_exponential(multiplier = 1, max = max_delay/max_retries),
            stop=tenacity.stop.stop_after_attempt(max_retries)
        )

        configuration.api_key["api_key"] = api_key
        if test_host:
            configuration.host = test_host

        ## Adding Campaigns to Client
        self.Campaigns=swagger_client.CampaignsApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in Campaigns
        self.Campaigns.cancel_campaign=self.retry_logic(self.Campaigns.cancel_campaign)
        self.Campaigns.clone_campaign=self.retry_logic(self.Campaigns.clone_campaign)
        self.Campaigns.create_campaign=self.retry_logic(self.Campaigns.create_campaign)
        self.Campaigns.get_campaign_info=self.retry_logic(self.Campaigns.get_campaign_info)
        self.Campaigns.get_campaign_recipients=self.retry_logic(self.Campaigns.get_campaign_recipients)
        self.Campaigns.get_campaigns=self.retry_logic(self.Campaigns.get_campaigns)
        self.Campaigns.schedule_campaign=self.retry_logic(self.Campaigns.schedule_campaign)
        self.Campaigns.send_campaign=self.retry_logic(self.Campaigns.send_campaign)
        self.Campaigns.update_campaign=self.retry_logic(self.Campaigns.update_campaign)
        
        ## Adding DataPrivacy to Client
        self.DataPrivacy=swagger_client.DataPrivacyApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in DataPrivacy
        self.DataPrivacy.request_deletion=self.retry_logic(self.DataPrivacy.request_deletion)
        
        ## Adding ListsSegments to Client
        self.ListsSegments=swagger_client.ListsSegmentsApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in ListsSegments
        self.ListsSegments.add_members=self.retry_logic(self.ListsSegments.add_members)
        self.ListsSegments.create_list=self.retry_logic(self.ListsSegments.create_list)
        self.ListsSegments.delete_list=self.retry_logic(self.ListsSegments.delete_list)
        self.ListsSegments.exclude_globally=self.retry_logic(self.ListsSegments.exclude_globally)
        self.ListsSegments.get_global_exclusions=self.retry_logic(self.ListsSegments.get_global_exclusions)
        self.ListsSegments.get_list_exclusions=self.retry_logic(self.ListsSegments.get_list_exclusions)
        self.ListsSegments.get_list_info=self.retry_logic(self.ListsSegments.get_list_info)
        self.ListsSegments.get_list_members=self.retry_logic(self.ListsSegments.get_list_members)
        self.ListsSegments.get_list_subscriptions=self.retry_logic(self.ListsSegments.get_list_subscriptions)
        self.ListsSegments.get_lists=self.retry_logic(self.ListsSegments.get_lists)
        self.ListsSegments.get_members=self.retry_logic(self.ListsSegments.get_members)
        self.ListsSegments.get_segment_members=self.retry_logic(self.ListsSegments.get_segment_members)
        self.ListsSegments.remove_members=self.retry_logic(self.ListsSegments.remove_members)
        self.ListsSegments.subscribe=self.retry_logic(self.ListsSegments.subscribe)
        self.ListsSegments.unsubscribe=self.retry_logic(self.ListsSegments.unsubscribe)
        self.ListsSegments.update_list_name=self.retry_logic(self.ListsSegments.update_list_name)
        
        ## Adding Metrics to Client
        self.Metrics=swagger_client.MetricsApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in Metrics
        self.Metrics.get_metrics=self.retry_logic(self.Metrics.get_metrics)
        self.Metrics.metric_export=self.retry_logic(self.Metrics.metric_export)
        self.Metrics.metric_timeline=self.retry_logic(self.Metrics.metric_timeline)
        self.Metrics.metrics_timeline=self.retry_logic(self.Metrics.metrics_timeline)
        
        ## Adding Profiles to Client
        self.Profiles=swagger_client.ProfilesApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in Profiles
        self.Profiles.exchange=self.retry_logic(self.Profiles.exchange)
        self.Profiles.get_profile=self.retry_logic(self.Profiles.get_profile)
        self.Profiles.get_profile_id=self.retry_logic(self.Profiles.get_profile_id)
        self.Profiles.profile_metric_timeline=self.retry_logic(self.Profiles.profile_metric_timeline)
        self.Profiles.profile_metrics_timeline=self.retry_logic(self.Profiles.profile_metrics_timeline)
        self.Profiles.update_profile=self.retry_logic(self.Profiles.update_profile)
        
        ## Adding Templates to Client
        self.Templates=swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in Templates
        self.Templates.clone_template=self.retry_logic(self.Templates.clone_template)
        self.Templates.create_template=self.retry_logic(self.Templates.create_template)
        self.Templates.delete_template=self.retry_logic(self.Templates.delete_template)
        self.Templates.get_templates=self.retry_logic(self.Templates.get_templates)
        self.Templates.render_template=self.retry_logic(self.Templates.render_template)
        self.Templates.send_template=self.retry_logic(self.Templates.send_template)
        self.Templates.update_template=self.retry_logic(self.Templates.update_template)
        
        ## Adding TrackIdentify to Client
        self.TrackIdentify=swagger_client.TrackIdentifyApi(swagger_client.ApiClient(configuration))

        ## Applying tenacity retry decorator to each endpoint in TrackIdentify
        self.TrackIdentify.identify_get=self.retry_logic(self.TrackIdentify.identify_get)
        self.TrackIdentify.identify_post=self.retry_logic(self.TrackIdentify.identify_post)
        self.TrackIdentify.track_get=self.retry_logic(self.TrackIdentify.track_get)
        self.TrackIdentify.track_post=self.retry_logic(self.TrackIdentify.track_post)
        

        self.TrackIdentify.track_post = self.post_update(self.TrackIdentify.track_post)
        self.TrackIdentify.identify_post = self.post_update(self.TrackIdentify.identify_post)
        self.TrackIdentify.track_get = self.get_update(self.TrackIdentify.track_get)
        self.TrackIdentify.identify_get = self.get_update(self.TrackIdentify.identify_get)

        self.Profiles.update_profile = self.update_profile_fix(self.Profiles.update_profile)

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
                "user-agent" : "klaviyo-python-sdk/1.0.5.20220329"
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
        
        