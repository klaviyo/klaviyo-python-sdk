# coding: utf-8

# flake8: noqa
"""
    Klaviyo API

    Empowering creators to own their destiny  # noqa: E501

    OpenAPI spec version: 2022.03.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.ascending import Ascending
from swagger_client.models.campaign import Campaign
from swagger_client.models.campaign_campaign_id_body import CampaignCampaignIdBody
from swagger_client.models.campaign_id_clone_body import CampaignIdCloneBody
from swagger_client.models.campaign_id_schedule_body import CampaignIdScheduleBody
from swagger_client.models.campaign_template import CampaignTemplate
from swagger_client.models.check_membership_request import CheckMembershipRequest
from swagger_client.models.check_membership_response import CheckMembershipResponse
from swagger_client.models.check_membership_response_inner import CheckMembershipResponseInner
from swagger_client.models.delete_email import DeleteEmail
from swagger_client.models.delete_person import DeletePerson
from swagger_client.models.delete_phone import DeletePhone
from swagger_client.models.deprecated_get_list_response import DeprecatedGetListResponse
from swagger_client.models.deprecated_get_list_response_data import DeprecatedGetListResponseData
from swagger_client.models.descending import Descending
from swagger_client.models.emailtemplate_template_id_body import EmailtemplateTemplateIdBody
from swagger_client.models.global_exclusion_response_data import GlobalExclusionResponseData
from swagger_client.models.global_exclusion_response_data_data import GlobalExclusionResponseDataData
from swagger_client.models.identify_payload import IdentifyPayload
from swagger_client.models.identify_payload_post import IdentifyPayloadPost
from swagger_client.models.identify_payload_properties import IdentifyPayloadProperties
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response20010 import InlineResponse20010
from swagger_client.models.inline_response20011 import InlineResponse20011
from swagger_client.models.inline_response20011_data import InlineResponse20011Data
from swagger_client.models.inline_response20012 import InlineResponse20012
from swagger_client.models.inline_response20013 import InlineResponse20013
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response2005 import InlineResponse2005
from swagger_client.models.inline_response2006 import InlineResponse2006
from swagger_client.models.inline_response2007 import InlineResponse2007
from swagger_client.models.inline_response2007_records import InlineResponse2007Records
from swagger_client.models.inline_response2008 import InlineResponse2008
from swagger_client.models.inline_response2008_records import InlineResponse2008Records
from swagger_client.models.inline_response2009 import InlineResponse2009
from swagger_client.models.list_id_members_body import ListIdMembersBody
from swagger_client.models.list_id_members_body1 import ListIdMembersBody1
from swagger_client.models.list_id_subscribe_body import ListIdSubscribeBody
from swagger_client.models.list_id_subscribe_body1 import ListIdSubscribeBody1
from swagger_client.models.list_list_id_body import ListListIdBody
from swagger_client.models.list_subscribe_post_response_data import ListSubscribePostResponseData
from swagger_client.models.list_subscribe_post_response_data_inner import ListSubscribePostResponseDataInner
from swagger_client.models.measurement_count import MeasurementCount
from swagger_client.models.measurement_sum import MeasurementSum
from swagger_client.models.measurement_unique import MeasurementUnique
from swagger_client.models.measurement_value import MeasurementValue
from swagger_client.models.metric import Metric
from swagger_client.models.metric_export import MetricExport
from swagger_client.models.metric_export_data import MetricExportData
from swagger_client.models.metric_export_metric import MetricExportMetric
from swagger_client.models.metric_export_results import MetricExportResults
from swagger_client.models.metric_integration import MetricIntegration
from swagger_client.models.metric_timeline import MetricTimeline
from swagger_client.models.metric_timeline_data import MetricTimelineData
from swagger_client.models.metric_timeline_event_properties import MetricTimelineEventProperties
from swagger_client.models.metric_timeline_person import MetricTimelinePerson
from swagger_client.models.model200ok import Model200ok
from swagger_client.models.one_ofidentify_payload_properties_your_custom_field import OneOfidentifyPayloadPropertiesYourCustomField
from swagger_client.models.one_oftrack_payload_properties_your_custom_field import OneOftrackPayloadPropertiesYourCustomField
from swagger_client.models.one_oftrack_payload_time import OneOftrackPayloadTime
from swagger_client.models.people_exchange_body import PeopleExchangeBody
from swagger_client.models.people_exclusions_body import PeopleExclusionsBody
from swagger_client.models.person import Person
from swagger_client.models.privacy_email import PrivacyEmail
from swagger_client.models.privacy_id import PrivacyId
from swagger_client.models.privacy_phone import PrivacyPhone
from swagger_client.models.reason_bounced import ReasonBounced
from swagger_client.models.reason_invalid_email import ReasonInvalidEmail
from swagger_client.models.reason_manually_excluded import ReasonManuallyExcluded
from swagger_client.models.reason_reported_spam import ReasonReportedSpam
from swagger_client.models.reason_unsubscribed import ReasonUnsubscribed
from swagger_client.models.rendered_template import RenderedTemplate
from swagger_client.models.renderedtemplate_data import RenderedtemplateData
from swagger_client.models.since_integer import SinceInteger
from swagger_client.models.since_string import SinceString
from swagger_client.models.string_array import StringArray
from swagger_client.models.template import Template
from swagger_client.models.template_id_clone_body import TemplateIdCloneBody
from swagger_client.models.template_id_render_body import TemplateIdRenderBody
from swagger_client.models.template_id_send_body import TemplateIdSendBody
from swagger_client.models.track_payload import TrackPayload
from swagger_client.models.track_payload_customer_properties import TrackPayloadCustomerProperties
from swagger_client.models.track_payload_post import TrackPayloadPost
from swagger_client.models.track_payload_properties import TrackPayloadProperties
from swagger_client.models.unit_day import UnitDay
from swagger_client.models.unit_month import UnitMonth
from swagger_client.models.unit_week import UnitWeek
from swagger_client.models.v1_campaigns_body import V1CampaignsBody
from swagger_client.models.v1_emailtemplates_body import V1EmailtemplatesBody
from swagger_client.models.v2_lists_body import V2ListsBody
