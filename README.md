# Klaviyo Python SDK (Legacy)

## Legacy Notice

This SDK is set to be deprecated + retired on 2024-06-30.

We have a NEW python SDK to go along with our [new API](https://developers.klaviyo.com/en/reference/api_overview).

We recommend migrating over to our [newest SDK](https://github.com/klaviyo/klaviyo-api-python).

You can read more about our SDK release history and support [here](https://developers.klaviyo.com/en/docs/sdk_overview)

For a comparison between our old and new APIs, check out [this guide](https://developers.klaviyo.com/en/docs/apis_comparison_chart).

# Klaviyo Python SDK

- SDK version: 1.0.7.20220329

## Helpful Resources

- [API Reference](https://developers.klaviyo.com/en/reference/api-overview)
- [API Guides](https://developers.klaviyo.com/en/docs)
- [Postman Workspace](https://www.postman.com/klaviyo/workspace/klaviyo-developers)

## Design & Approach

This SDK is a thin wrapper around our API. See our API Reference for full documentation on API behavior.

This SDK exactly mirrors the organization and naming convention of the above language-agnostic resources, with a few namespace changes to make it Pythonic (details in Appendix).

## Organization

This SDK is organized into the following resources:

- Campaigns
- DataPrivacy
- ListsSegments
- Metrics
- Profiles
- Templates
- TrackIdentify

# Installation

## pip

You can install this library using [`pip`](https://pypi.org/project/klaviyo-sdk/).

Depending on your system configuration, you will need to run *one* of the following shell commands:

`pip install klaviyo-sdk`

OR 

`pip3 install klaviyo-sdk`

## source code

*Alternatively*, you can also run this using this repo as source code, by running *one* of the following shell commands within the cloned repo:

`pip install -r requirements.txt`

OR

`pip3 install -r requirements.txt`


and then running python from the cloned repo.

# Usage Example

### To instantiate the client

```python
from klaviyo_sdk import Client

client = Client( "YOUR API KEY HERE", max_delay=60, max_retries=3)
```

NOTE: 
* The SDK retries on resolvable errors, namely: rate limits (common) and server errors on klaviyo (rare).
* The keyword arguments define retry behavior; the example is populated with the default values.
* `max_delay` denotes total delay (in seconds) across all attempts.

### To call the `metric-export` operation:

```python
metric_id = "METRIC_ID"
count = 100

client.Metrics.metric_export(metric_id, count=count) 
```

# Error Handling

This SDK throws an `ApiException` error when the server returns a non-`2XX` response. 

An `ApiException` consists of the following attributes:

* `status` : `int`
* `reason` : `str`
* `body` : `bytes`
    * this can be decoded into a native python dictionary as follows:
        ```python
        # to decode to a dictionary
        import json
        BODY_DICT = json.loads(YOUR_EXCEPTION.body)

        # to decode to a string
        BODY_STRING = YOUR_EXCEPTION.body.decode('utf-8')
        ```
* `headers` : [class 'urllib3._collections.HTTPHeaderDict'](https://urllib3.readthedocs.io/en/stable/user-guide.html?highlight=httpheaderdict#response-content)
    * This can be interacted with as a normal dictionary:
        * ex:
            ```
            date = YOUR_EXCEPTION.headers['Date']
            keys = YOUR_EXCEPTION.headers.keys()
            values = YOUR_EXCEPTION.headers.values()
            ```

# Comprehensive list of Operations & Parameters

_**NOTE:**_
- Organization: Resource groups and operation_ids are listed in alphabetical order, first by Resource name, then by **OpenAPI Summary**. Operation summaries are those listed in the right side bar of the [API Reference](https://developers.klaviyo.com/en/reference/track-post).
- For example values / data types, as well as whether parameters are required/optional, please reference the corresponding API Reference link.
- Some keyword args are required for the API call to succeed, the API docs above are the source of truth regarding which keyword params are required.
- JSON payloads should be passed in as native python dictionaries.



## Campaigns


#### [Cancel a Campaign](https://developers.klaviyo.com/en/reference/cancel-campaign)

```python
client.Campaigns.cancel_campaign(campaign_id)
```




#### [Clone a Campaign](https://developers.klaviyo.com/en/reference/clone-campaign)

```python
client.Campaigns.clone_campaign(campaign_id, name=name, list_id=list_id)
```




#### [Create New Campaign](https://developers.klaviyo.com/en/reference/create-campaign)

```python
client.Campaigns.create_campaign(list_id=list_id, template_id=template_id, from_email=from_email, from_name=from_name, subject=subject, name=name, use_smart_sending=use_smart_sending, add_google_analytics=add_google_analytics)
```




#### [Get Campaign Info](https://developers.klaviyo.com/en/reference/get-campaign-info)

```python
client.Campaigns.get_campaign_info(campaign_id)
```




#### [Get Campaign Recipients](https://developers.klaviyo.com/en/reference/get-campaign-recipients)

```python
client.Campaigns.get_campaign_recipients(campaign_id, count=count, sort=sort, offset=offset)
```




#### [Get Campaigns](https://developers.klaviyo.com/en/reference/get-campaigns)

```python
client.Campaigns.get_campaigns(page=page, count=count)
```




#### [Schedule a Campaign](https://developers.klaviyo.com/en/reference/schedule-campaign)

```python
client.Campaigns.schedule_campaign(campaign_id, send_time=send_time)
```




#### [Send a Campaign Immediately](https://developers.klaviyo.com/en/reference/send-campaign)

```python
client.Campaigns.send_campaign(campaign_id)
```




#### [Update Campaign](https://developers.klaviyo.com/en/reference/update-campaign)

```python
client.Campaigns.update_campaign(campaign_id, list_id=list_id, template_id=template_id, from_email=from_email, from_name=from_name, subject=subject, name=name, use_smart_sending=use_smart_sending, add_google_analytics=add_google_analytics)
```



## DataPrivacy


#### [Request a Deletion](https://developers.klaviyo.com/en/reference/request-deletion)

```python
client.DataPrivacy.request_deletion(body=body)
```



## ListsSegments


#### [Add Members to a List](https://developers.klaviyo.com/en/reference/add-members)

```python
client.ListsSegments.add_members(list_id, body=body)
```




#### [Create List](https://developers.klaviyo.com/en/reference/create-list)

```python
client.ListsSegments.create_list(list_name=list_name)
```




#### [Delete List](https://developers.klaviyo.com/en/reference/delete-list)

```python
client.ListsSegments.delete_list(list_id)
```




#### [Exclude Profile From All Email](https://developers.klaviyo.com/en/reference/exclude-globally)

```python
client.ListsSegments.exclude_globally(email=email)
```




#### [Get Global Exclusions & Unsubscribes](https://developers.klaviyo.com/en/reference/get-global-exclusions)

```python
client.ListsSegments.get_global_exclusions(reason=reason, sort=sort, count=count, page=page)
```




#### [Get All Exclusions for a List](https://developers.klaviyo.com/en/reference/get-list-exclusions)

```python
client.ListsSegments.get_list_exclusions(list_id, marker=marker)
```




#### [Get List Info](https://developers.klaviyo.com/en/reference/get-list-info)

```python
client.ListsSegments.get_list_info(list_id)
```




#### [Check if Profiles Are in a List](https://developers.klaviyo.com/en/reference/get-list-members)

```python
client.ListsSegments.get_list_members(list_id, body=body)
```




#### [Check if Profiles Are in a List and not Suppressed](https://developers.klaviyo.com/en/reference/get-list-subscriptions)

```python
client.ListsSegments.get_list_subscriptions(list_id, body=body)
```




#### [Get Lists](https://developers.klaviyo.com/en/reference/get-lists)

```python
client.ListsSegments.get_lists()
```




#### [Get List and Segment Members](https://developers.klaviyo.com/en/reference/get-members)

```python
client.ListsSegments.get_members(list_or_segment_id, marker=marker)
```




#### [Check if Profiles Are in a Segment](https://developers.klaviyo.com/en/reference/get-segment-members)

```python
client.ListsSegments.get_segment_members(segment_id, body=body)
```




#### [Remove Profiles From List](https://developers.klaviyo.com/en/reference/remove-members)

```python
client.ListsSegments.remove_members(list_id, body=body)
```




#### [Subscribe Profiles to List](https://developers.klaviyo.com/en/reference/subscribe)

```python
client.ListsSegments.subscribe(list_id, body=body)
```




#### [Unsubscribe Profiles From List](https://developers.klaviyo.com/en/reference/unsubscribe)

```python
client.ListsSegments.unsubscribe(list_id, body=body)
```




#### [Update List Name](https://developers.klaviyo.com/en/reference/update-list-name)

```python
client.ListsSegments.update_list_name(list_id, list_name=list_name)
```



## Metrics


#### [Get Metrics Info](https://developers.klaviyo.com/en/reference/get-metrics)

```python
client.Metrics.get_metrics(page=page, count=count)
```




#### [Query Event Data](https://developers.klaviyo.com/en/reference/metric-export)

```python
client.Metrics.metric_export(metric_id, start_date=start_date, end_date=end_date, unit=unit, measurement=measurement, where=where, by=by, count=count)
```




#### [Get Events for a Specific Metric](https://developers.klaviyo.com/en/reference/metric-timeline)

```python
client.Metrics.metric_timeline(metric_id, since=since, count=count, sort=sort)
```




#### [Get Events for All Metrics](https://developers.klaviyo.com/en/reference/metrics-timeline)

```python
client.Metrics.metrics_timeline(since=since, count=count, sort=sort)
```



## Profiles


#### [Exchange ID for Profile ID](https://developers.klaviyo.com/en/reference/exchange)

```python
client.Profiles.exchange(body=body)
```




#### [Get Profile](https://developers.klaviyo.com/en/reference/get-profile)

```python
client.Profiles.get_profile(person_id)
```




#### [Get Profile ID](https://developers.klaviyo.com/en/reference/get-profile-id)

```python
client.Profiles.get_profile_id(email=email, phone_number=phone_number, external_id=external_id)
```




#### [Get Profile's Events for a Specific Metric](https://developers.klaviyo.com/en/reference/profile-metric-timeline)

```python
client.Profiles.profile_metric_timeline(person_id, metric_id, since=since, count=count, sort=sort)
```




#### [Get Profile's Events for all Metrics](https://developers.klaviyo.com/en/reference/profile-metrics-timeline)

```python
client.Profiles.profile_metrics_timeline(person_id, since=since, count=count, sort=sort)
```




#### [Update Profile](https://developers.klaviyo.com/en/reference/update-profile)

```python
client.Profiles.update_profile(person_id, params=params)
```



## Templates


#### [Clone Template](https://developers.klaviyo.com/en/reference/clone-template)

```python
client.Templates.clone_template(template_id, name=name)
```




#### [Create New Template](https://developers.klaviyo.com/en/reference/create-template)

```python
client.Templates.create_template(name=name, html=html)
```




#### [Delete Template](https://developers.klaviyo.com/en/reference/delete-template)

```python
client.Templates.delete_template(template_id)
```




#### [Get All Templates](https://developers.klaviyo.com/en/reference/get-templates)

```python
client.Templates.get_templates(page=page, count=count)
```




#### [Render Template](https://developers.klaviyo.com/en/reference/render-template)

```python
client.Templates.render_template(template_id, context=context)
```




#### [Render and Send Template](https://developers.klaviyo.com/en/reference/send-template)

```python
client.Templates.send_template(template_id, from_email=from_email, from_name=from_name, subject=subject, to=to, context=context)
```




#### [Update Template](https://developers.klaviyo.com/en/reference/update-template)

```python
client.Templates.update_template(template_id, name=name, html=html)
```



## TrackIdentify


#### [Identify Profile (Legacy)](https://developers.klaviyo.com/en/reference/identify-get)

```python
client.TrackIdentify.identify_get(data)
```




#### [Identify Profile](https://developers.klaviyo.com/en/reference/identify-post)

```python
client.TrackIdentify.identify_post(data=data)
```




#### [Track Profile Activity (Legacy)](https://developers.klaviyo.com/en/reference/track-get)

```python
client.TrackIdentify.track_get(data)
```




#### [Track Profile Activity](https://developers.klaviyo.com/en/reference/track-post)

```python
client.TrackIdentify.track_post(data=data)
```



# Appendix

## Limitations

- The `api_key` is set at the global level: this means that if you manage multiple stores, you will need to run the code for each store in a different environment 

## Refresher on catching exceptions:

```python
try:
    YOUR_CALL
except Exception as e:
    print(e.status)
    print(e.reason)
    print(e.body)
    print(e.headers)
```

## Namespace

In the interest of making the SDK Pythonic, we made the following namespace changes *relative* to the language agnostic resources up top.

1. dashes `-` become underscores `_`
2. all other non-alphanumeric symbols, including spaces, are removed.

For example:
* `get-campaigns` becomes `get_campaigns`
* `Track & Identify` becomes `TrackIdentify`

## Parameters & Arguments

The parameters follow the same naming conventions as the resource groups and operations.

We stick to the following convention for parameters/arguments

1. All parameters are passed as function args.
2. All optional params, as well as all Body and Form Data params (including required ones), are passed as keyword args.
3. All query and path params that are tagged as `required` in the docs are passed as positional args.
4. There is no need to pass in your private `api_key` for any operations, as it is defined upon client instantiation; public key is still required where.
