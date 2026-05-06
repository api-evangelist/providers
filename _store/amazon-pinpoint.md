---
name: Amazon Pinpoint
description: Amazon Pinpoint is a flexible and scalable outbound and inbound marketing communications service that enables you to engage with customers across multiple messaging channels including email, SMS, push notifications, and voice messages. Note - AWS will end support for Amazon Pinpoint on October 30, 2026. SMS, voice, mobile push, OTP, and phone number validation APIs will continue through AWS End User Messaging.
url: https://raw.githubusercontent.com/api-evangelist/amazon-pinpoint/refs/heads/main/apis.yml
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Campaigns
  - Communications
  - Email
  - Marketing
  - Messaging
  - Push Notifications
  - SMS
  - Voice
  - Customer Engagement
  - Segmentation
  - Journeys
  - Analytics
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Pinpoint API
    description: The Amazon Pinpoint API enables you to create and manage marketing campaigns, send transactional messages, define audience segments, manage message templates, configure messaging channels (email, SMS, push, voice), and analyze engagement metrics for multi-channel communications.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/pinpoint/
    baseURL: https://pinpoint.amazonaws.com
    tags:
      - Communications
      - Marketing
      - Messaging
      - Campaigns
      - Segmentation
      - Journeys
      - Analytics
      - Email
      - SMS
      - Push Notifications
      - Voice
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html
      - type: APIReference
        url: https://docs.aws.amazon.com/pinpoint/latest/apireference/welcome.html
      - type: OpenAPI
        url: openapi/amazon-pinpoint-openapi.yml
      - type: OpenAPI
        url: openapi/amazon-pinpoint-openapi-original.yaml
      - type: Pricing
        url: https://aws.amazon.com/pinpoint/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/pinpoint/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/pinpoint/faqs/
      - type: Features
        url: https://aws.amazon.com/pinpoint/features/
      - type: Quotas
        url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html
common:
  - type: Portal
    url: https://console.aws.amazon.com/pinpoint/
  - type: Blog
    url: https://aws.amazon.com/blogs/messaging-and-targeting/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/pinpoint/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Documentation
    url: https://docs.aws.amazon.com/pinpoint/
  - type: Pricing
    url: https://aws.amazon.com/pinpoint/pricing/
  - type: GettingStarted
    url: https://aws.amazon.com/pinpoint/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/pinpoint/faqs/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-pinpoint
  - type: CodeExamples
    url: https://docs.aws.amazon.com/code-library/latest/ug/pinpoint_code_examples.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: SpectralRules
    url: rules/amazon-pinpoint-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/customer-engagement.yaml
  - type: Vocabulary
    url: vocabulary/amazon-pinpoint-vocabulary.yaml
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-message-request-schema.json
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-campaigns-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-segments-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-journeys-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-messages-context.jsonld
  - type: Features
    data:
      - name: Multi-Channel Messaging
        description: Send messages via email, SMS, push notifications, and voice through a unified API.
      - name: Audience Segmentation
        description: Create dynamic segments based on app data or import static segments from external sources.
      - name: Messaging Campaigns
        description: Schedule targeted campaigns with A/B testing and detailed analytics reporting.
      - name: Customer Journeys
        description: Build multi-step automated engagement workflows triggered by customer events.
      - name: Transactional Messaging
        description: Send real-time transactional messages such as account confirmations, order updates, and password resets.
      - name: Message Templates
        description: Create reusable email, SMS, push, voice, and in-app message templates with personalization.
      - name: Analytics and Metrics
        description: Track engagement trends, open rates, delivery rates, and campaign performance across all channels.
      - name: Endpoint Management
        description: Manage customer endpoint profiles including device tokens, email addresses, and phone numbers.
  - type: UseCases
    data:
      - name: Marketing Campaigns
        description: Run scheduled, targeted promotional campaigns across email, SMS, and push channels.
      - name: Customer Onboarding
        description: Automate welcome sequences and onboarding journeys for new users.
      - name: Transactional Notifications
        description: Deliver order confirmations, shipping updates, and account alerts in real time.
      - name: Re-engagement Campaigns
        description: Win back inactive users with targeted re-engagement messages and offers.
      - name: A/B Testing
        description: Experiment with different message content, timing, and channels to optimize engagement.
      - name: Event-Based Messaging
        description: Trigger personalized messages based on in-app events and user behaviors.
  - type: Integrations
    data:
      - name: Amazon Kinesis
        description: Stream Pinpoint analytics data to Kinesis for real-time processing and external storage.
      - name: Amazon S3
        description: Import and export endpoint data and segment definitions using S3 bucket storage.
      - name: AWS Lambda
        description: Trigger Lambda functions from Pinpoint journey actions and campaign events.
      - name: Amazon CloudWatch
        description: Monitor Pinpoint service metrics and set alarms using CloudWatch.
      - name: AWS End User Messaging
        description: The successor service for SMS, voice, push, OTP, and phone number validation APIs continuing after Pinpoint deprecation.
      - name: Amazon SES
        description: Amazon Simple Email Service provides the email delivery infrastructure for Pinpoint email campaigns.
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-analytics-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-apps-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-channels-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-endpoints-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-general-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-pinpoint-templates-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-action-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-activities-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-activity-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-address-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-adm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-adm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-adm-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-alignment-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-android-push-notification-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-push-notification-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-voip-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-voip-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-voip-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-apns-voip-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-application-date-range-kpi-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-application-settings-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-applications-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-attribute-dimension-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-attribute-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-attributes-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-baidu-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-baidu-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-baidu-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-base-kpi-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-button-action-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-custom-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-date-range-kpi-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-email-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-event-filter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-hook-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-in-app-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-limits-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-sms-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-state-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaign-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-campaigns-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-channel-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-channels-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-closed-days-rule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-closed-days-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-condition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-conditional-split-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-contact-center-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-app-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-app-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-campaign-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-campaign-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-email-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-email-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-export-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-export-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-import-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-import-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-in-app-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-in-app-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-journey-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-journey-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-push-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-push-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-recommender-configuration-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-recommender-configuration-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-recommender-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-segment-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-segment-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-sms-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-sms-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-template-message-body-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-voice-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-create-voice-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-custom-delivery-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-custom-message-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-day-of-week-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-default-button-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-default-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-default-push-notification-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-default-push-notification-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-adm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-adm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-voip-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-voip-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-voip-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-apns-voip-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-app-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-app-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-baidu-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-baidu-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-campaign-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-campaign-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-email-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-email-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-email-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-email-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-event-stream-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-event-stream-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-gcm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-gcm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-in-app-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-in-app-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-journey-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-journey-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-push-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-push-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-recommender-configuration-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-recommender-configuration-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-segment-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-segment-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-sms-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-sms-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-sms-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-sms-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-user-endpoints-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-user-endpoints-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-voice-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-voice-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-voice-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delete-voice-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-delivery-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-direct-message-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-duration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-email-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-email-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-email-message-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-email-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-email-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-email-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-batch-item-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-batch-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-demographic-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-item-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-location-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-message-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-send-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoint-user-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-endpoints-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-condition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-dimensions-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-filter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-item-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-start-condition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-event-stream-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-events-batch-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-events-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-events-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-export-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-export-job-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-export-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-export-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-frequency-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-gcm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-gcm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-gcm-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-adm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-adm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-voip-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-voip-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-voip-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apns-voip-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-app-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-app-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-application-date-range-kpi-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-application-date-range-kpi-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-application-settings-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-application-settings-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apps-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-apps-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-baidu-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-baidu-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-activities-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-activities-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-date-range-kpi-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-date-range-kpi-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-version-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-version-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-versions-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaign-versions-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaigns-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-campaigns-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-channels-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-channels-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-email-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-email-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-email-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-email-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-event-stream-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-event-stream-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-export-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-export-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-export-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-export-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-gcm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-gcm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-import-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-import-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-import-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-import-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-in-app-messages-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-in-app-messages-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-in-app-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-in-app-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-date-range-kpi-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-date-range-kpi-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-execution-activity-metrics-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-execution-activity-metrics-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-execution-metrics-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-execution-metrics-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-journey-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-push-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-push-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-recommender-configuration-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-recommender-configuration-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-recommender-configurations-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-recommender-configurations-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-export-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-export-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-import-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-import-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-version-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-version-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-versions-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segment-versions-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segments-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-segments-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-sms-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-sms-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-sms-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-sms-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-user-endpoints-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-user-endpoints-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-voice-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-voice-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-voice-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-get-voice-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-gps-coordinates-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-gps-point-dimension-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-holdout-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-import-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-import-job-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-import-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-import-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-campaign-schedule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-message-body-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-message-button-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-message-campaign-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-message-content-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-message-header-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-messages-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-in-app-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-include-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-item-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-job-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-channel-settings-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-custom-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-date-range-kpi-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-email-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-execution-activity-metrics-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-execution-metrics-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-limits-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-push-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-schedule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-sms-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journey-state-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-journeys-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-layout-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-journeys-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-journeys-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-recommender-configurations-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-tags-for-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-tags-for-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-template-versions-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-template-versions-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-templates-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-list-templates-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-message-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-message-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-message-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-metric-dimension-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-multi-conditional-branch-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-multi-conditional-split-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-number-validate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-number-validate-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-open-hours-rule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-open-hours-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-override-button-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-phone-number-validate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-phone-number-validate-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-public-endpoint-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-push-message-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-push-notification-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-push-notification-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-put-event-stream-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-put-event-stream-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-put-events-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-put-events-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-quiet-time-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-random-split-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-random-split-entry-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-raw-email-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-recency-dimension-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-recommender-configuration-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-remove-attributes-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-remove-attributes-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-result-row-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-result-row-value-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-schedule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-behaviors-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-condition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-demographics-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-dimensions-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-group-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-group-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-import-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-location-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segment-reference-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-segments-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-messages-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-messages-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-otp-message-request-parameters-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-otp-message-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-otp-message-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-users-message-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-users-message-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-users-messages-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-send-users-messages-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-session-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-set-dimension-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-simple-condition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-simple-email-part-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-simple-email-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-sms-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-sms-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-sms-message-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-sms-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-sms-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-sms-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-source-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-start-condition-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-state-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-tag-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-tags-model-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-active-version-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-create-message-body-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-version-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-template-versions-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-templates-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-treatment-resource-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-untag-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-adm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-adm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-voip-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-voip-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-voip-sandbox-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-apns-voip-sandbox-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-application-settings-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-application-settings-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-attributes-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-baidu-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-baidu-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-campaign-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-campaign-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-email-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-email-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-email-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-email-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-endpoints-batch-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-endpoints-batch-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-gcm-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-gcm-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-in-app-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-in-app-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-journey-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-journey-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-journey-state-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-journey-state-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-push-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-push-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-recommender-configuration-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-recommender-configuration-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-recommender-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-segment-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-segment-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-sms-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-sms-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-sms-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-sms-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-template-active-version-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-template-active-version-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-voice-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-voice-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-voice-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-update-voice-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-verification-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-verify-otp-message-request-parameters-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-verify-otp-message-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-verify-otp-message-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-voice-channel-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-voice-channel-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-voice-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-voice-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-voice-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-wait-activity-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-wait-time-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-write-application-settings-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-write-campaign-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-write-event-stream-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-write-journey-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-write-segment-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-pinpoint-write-treatment-resource-schema.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-action-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-activities-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-activity-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-address-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-adm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-adm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-adm-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-alignment-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-android-push-notification-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-push-notification-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-voip-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-voip-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-voip-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-apns-voip-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-application-date-range-kpi-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-application-settings-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-applications-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-attribute-dimension-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-attribute-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-attributes-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-baidu-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-baidu-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-baidu-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-base-kpi-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-button-action-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-custom-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-date-range-kpi-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-email-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-event-filter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-hook-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-in-app-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-limits-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-sms-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-state-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaign-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-campaigns-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-channel-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-channels-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-closed-days-rule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-closed-days-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-condition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-conditional-split-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-contact-center-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-app-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-app-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-campaign-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-campaign-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-email-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-email-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-export-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-export-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-import-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-import-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-in-app-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-in-app-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-journey-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-journey-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-push-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-push-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-recommender-configuration-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-recommender-configuration-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-recommender-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-segment-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-segment-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-sms-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-sms-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-template-message-body-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-voice-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-create-voice-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-custom-delivery-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-custom-message-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-day-of-week-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-default-button-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-default-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-default-push-notification-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-default-push-notification-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-adm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-adm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-voip-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-voip-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-voip-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-apns-voip-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-app-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-app-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-baidu-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-baidu-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-campaign-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-campaign-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-email-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-email-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-email-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-email-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-event-stream-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-event-stream-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-gcm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-gcm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-in-app-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-in-app-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-journey-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-journey-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-push-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-push-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-recommender-configuration-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-recommender-configuration-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-segment-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-segment-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-sms-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-sms-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-sms-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-sms-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-user-endpoints-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-user-endpoints-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-voice-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-voice-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-voice-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delete-voice-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-delivery-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-direct-message-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-duration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-email-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-email-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-email-message-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-email-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-email-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-email-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-batch-item-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-batch-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-demographic-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-item-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-location-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-message-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-send-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoint-user-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-endpoints-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-condition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-dimensions-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-filter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-item-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-start-condition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-stream-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-event-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-events-batch-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-events-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-events-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-export-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-export-job-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-export-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-export-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-frequency-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-gcm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-gcm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-gcm-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-adm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-adm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-voip-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-voip-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-voip-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apns-voip-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-app-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-app-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-application-date-range-kpi-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-application-date-range-kpi-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-application-settings-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-application-settings-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apps-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-apps-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-baidu-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-baidu-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-activities-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-activities-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-date-range-kpi-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-date-range-kpi-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-version-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-version-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-versions-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaign-versions-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaigns-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-campaigns-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-channels-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-channels-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-email-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-email-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-email-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-email-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-event-stream-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-event-stream-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-export-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-export-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-export-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-export-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-gcm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-gcm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-import-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-import-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-import-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-import-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-in-app-messages-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-in-app-messages-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-in-app-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-in-app-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-date-range-kpi-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-date-range-kpi-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-execution-activity-metrics-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-execution-activity-metrics-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-execution-metrics-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-execution-metrics-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-journey-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-push-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-push-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-recommender-configuration-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-recommender-configuration-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-recommender-configurations-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-recommender-configurations-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-export-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-export-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-import-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-import-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-version-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-version-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-versions-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segment-versions-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segments-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-segments-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-sms-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-sms-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-sms-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-sms-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-user-endpoints-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-user-endpoints-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-voice-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-voice-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-voice-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-get-voice-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-gps-coordinates-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-gps-point-dimension-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-holdout-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-import-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-import-job-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-import-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-import-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-campaign-schedule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-message-body-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-message-button-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-message-campaign-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-message-content-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-message-header-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-messages-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-in-app-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-include-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-item-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-job-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-channel-settings-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-custom-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-date-range-kpi-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-email-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-execution-activity-metrics-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-execution-metrics-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-limits-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-push-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-schedule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-sms-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journey-state-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-journeys-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-layout-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-journeys-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-journeys-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-recommender-configurations-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-tags-for-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-tags-for-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-template-versions-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-template-versions-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-templates-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-list-templates-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-message-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-message-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-message-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-message-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-metric-dimension-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-multi-conditional-branch-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-multi-conditional-split-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-number-validate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-number-validate-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-open-hours-rule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-open-hours-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-override-button-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-phone-number-validate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-phone-number-validate-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-public-endpoint-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-push-message-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-push-notification-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-push-notification-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-put-event-stream-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-put-event-stream-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-put-events-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-put-events-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-quiet-time-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-random-split-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-random-split-entry-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-raw-email-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-recency-dimension-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-recommender-configuration-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-remove-attributes-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-remove-attributes-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-result-row-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-result-row-value-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-schedule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-behaviors-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-condition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-demographics-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-dimensions-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-group-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-group-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-import-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-location-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-reference-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segment-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-segments-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-messages-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-messages-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-otp-message-request-parameters-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-otp-message-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-otp-message-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-users-message-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-users-message-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-users-messages-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-send-users-messages-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-session-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-set-dimension-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-simple-condition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-simple-email-part-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-simple-email-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-sms-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-sms-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-sms-message-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-sms-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-sms-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-sms-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-source-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-start-condition-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-state-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-tag-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-tags-model-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-active-version-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-create-message-body-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-version-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-template-versions-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-templates-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-treatment-resource-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-untag-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-adm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-adm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-voip-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-voip-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-voip-sandbox-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-apns-voip-sandbox-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-application-settings-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-application-settings-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-attributes-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-baidu-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-baidu-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-campaign-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-campaign-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-email-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-email-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-email-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-email-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-endpoints-batch-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-endpoints-batch-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-gcm-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-gcm-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-in-app-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-in-app-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-journey-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-journey-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-journey-state-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-journey-state-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-push-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-push-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-recommender-configuration-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-recommender-configuration-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-recommender-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-segment-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-segment-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-sms-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-sms-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-sms-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-sms-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-template-active-version-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-template-active-version-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-voice-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-voice-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-voice-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-update-voice-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-verification-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-verify-otp-message-request-parameters-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-verify-otp-message-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-verify-otp-message-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-voice-channel-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-voice-channel-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-voice-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-voice-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-voice-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-wait-activity-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-wait-time-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-write-application-settings-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-write-campaign-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-write-event-stream-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-write-journey-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-write-segment-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-pinpoint-write-treatment-resource-structure.json
  - type: Example
    url: examples/amazon-pinpoint-activity-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-android-push-notification-template-example.json
  - type: Example
    url: examples/amazon-pinpoint-apns-channel-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-applications-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-attributes-resource-example.json
  - type: Example
    url: examples/amazon-pinpoint-baidu-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-campaign-date-range-kpi-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-campaign-hook-example.json
  - type: Example
    url: examples/amazon-pinpoint-campaign-state-example.json
  - type: Example
    url: examples/amazon-pinpoint-create-campaign-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-create-sms-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-create-voice-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-delete-campaign-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-delete-email-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-delete-journey-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-delete-sms-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-delete-voice-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-direct-message-configuration-example.json
  - type: Example
    url: examples/amazon-pinpoint-email-message-activity-example.json
  - type: Example
    url: examples/amazon-pinpoint-email-template-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-endpoint-demographic-example.json
  - type: Example
    url: examples/amazon-pinpoint-endpoint-message-result-example.json
  - type: Example
    url: examples/amazon-pinpoint-events-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-export-jobs-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-gcm-message-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-adm-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-apns-voip-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-apns-voip-sandbox-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-campaign-activities-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-campaign-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-campaigns-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-email-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-gcm-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-import-jobs-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-in-app-messages-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-push-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-recommender-configurations-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-segment-versions-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-get-sms-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-gps-coordinates-example.json
  - type: Example
    url: examples/amazon-pinpoint-holdout-activity-example.json
  - type: Example
    url: examples/amazon-pinpoint-import-job-resource-example.json
  - type: Example
    url: examples/amazon-pinpoint-in-app-messages-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-journey-email-message-example.json
  - type: Example
    url: examples/amazon-pinpoint-journey-execution-activity-metrics-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-journey-limits-example.json
  - type: Example
    url: examples/amazon-pinpoint-journey-state-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-list-journeys-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-list-recommender-configurations-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-message-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-number-validate-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-open-hours-example.json
  - type: Example
    url: examples/amazon-pinpoint-open-hours-rule-example.json
  - type: Example
    url: examples/amazon-pinpoint-phone-number-validate-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-random-split-entry-example.json
  - type: Example
    url: examples/amazon-pinpoint-result-row-value-example.json
  - type: Example
    url: examples/amazon-pinpoint-segment-group-example.json
  - type: Example
    url: examples/amazon-pinpoint-segment-location-example.json
  - type: Example
    url: examples/amazon-pinpoint-send-messages-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-send-otp-message-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-send-otp-message-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-send-users-message-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-session-example.json
  - type: Example
    url: examples/amazon-pinpoint-set-dimension-example.json
  - type: Example
    url: examples/amazon-pinpoint-simple-condition-example.json
  - type: Example
    url: examples/amazon-pinpoint-tag-resource-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-template-versions-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-treatment-resource-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-apns-channel-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-campaign-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-email-channel-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-email-template-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-in-app-template-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-journey-response-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-recommender-configuration-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-recommender-configuration-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-update-sms-template-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-verify-otp-message-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-voice-template-request-example.json
  - type: Example
    url: examples/amazon-pinpoint-wait-time-example.json
  - type: Example
    url: examples/amazon-pinpoint-write-event-stream-example.json
  - type: Example
    url: examples/amazon-pinpoint-write-segment-request-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-pinpoint.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
