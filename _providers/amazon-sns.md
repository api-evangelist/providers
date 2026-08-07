---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Amazon Sns Agentic Access
  operation_count: 20
  slug: amazon-sns-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 8
apis:
- description: The ?Action=ListTagsForResource API from Amazon SNS — 1 operation(s) for ?action=listtagsforresource.
  name: Amazon SNS ?Action=ListTagsForResource API
  slug: amazon-sns-action-listtagsforresource-api
- description: The ?Action=TagResource API from Amazon SNS — 1 operation(s) for ?action=tagresource.
  name: Amazon SNS ?Action=TagResource API
  slug: amazon-sns-action-tagresource-api
- description: The ?Action=UntagResource API from Amazon SNS — 1 operation(s) for ?action=untagresource.
  name: Amazon SNS ?Action=UntagResource API
  slug: amazon-sns-action-untagresource-api
- description: Operations for managing platform applications used for mobile push notifications via APNs, FCM, and other push services.
  name: Amazon SNS Platform Applications API
  slug: amazon-sns-platform-applications-api
- description: Operations for publishing messages to SNS topics or directly to endpoints. Messages can be plain text or structured JSON for per-protocol delivery.
  name: Amazon SNS Publishing API
  slug: amazon-sns-publishing-api
- description: Operations for managing SMS messaging attributes and phone number opt-out lists.
  name: Amazon SNS SMS API
  slug: amazon-sns-sms-api
- description: Operations for subscribing endpoints to topics, confirming subscriptions, listing subscriptions, and unsubscribing. Subscriptions define which endpoints receive messages published to a topic.
  name: Amazon SNS Subscriptions API
  slug: amazon-sns-subscriptions-api
- description: Operations for creating, listing, configuring, and deleting SNS topics. Topics are communication channels to which messages are published and from which notifications are delivered to subscribers.
  name: Amazon SNS Topics API
  slug: amazon-sns-topics-api
artifact_total: 123
asyncapis:
- description: 'Amazon Simple Notification Service (SNS) delivers notifications to subscribed endpoints when messages are published to topics. This AsyncAPI specification describes the notification messages that SNS '
  name: Amazon SNS Notifications
  slug: amazon-sns-notifications-asyncapi
collections:
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource ?Action=ListTagsForResource API
  slug: postman-amazon-sns-action-listtagsforresource-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource ?Action=TagResource API
  slug: postman-amazon-sns-action-tagresource-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource ?Action=UntagResource API
  slug: postman-amazon-sns-action-untagresource-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource Platform Applications API
  slug: postman-amazon-sns-platform-applications-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource Publishing API
  slug: postman-amazon-sns-publishing-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource SMS API
  slug: postman-amazon-sns-sms-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource Subscriptions API
  slug: postman-amazon-sns-subscriptions-api
- collection_type: postman
  name: Amazon SNS Amazon Simple Notification Service (SNS) ?Action=ListTagsForResource ?Action=ListTagsForResource Topics API
  slug: postman-amazon-sns-topics-api
- collection_type: open
  name: Amazon SNS Amazon Simple Notification Service (SNS) API
  slug: open-amazon-sns-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-sns/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-sns-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-sns-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-sns-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-sns-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-sns-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/messaging-and-targeting/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/sns/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/services-in-scope/
- group: operate
  title: ''
  type: Support
  url: https://console.aws.amazon.com/support/home
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://aws.amazon.com/premiumsupport/knowledge-center/#Amazon_Simple_Notification_Service
- group: company
  title: ''
  type: Partners
  url: https://aws.amazon.com/sns/partners/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/awsdocs/amazon-sns-developer-guide
created: '2024-01-01'
description: Amazon Simple Notification Service (SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. It enables pub/sub, SMS, email, and mobile push notifications.
examples:
- key_count: 1
  name: Amazon Sns Check If Phone Number Is Opted Out Response Example
  slug: amazon-sns-check-if-phone-number-is-opted-out-response-example
- key_count: 1
  name: Amazon Sns Confirm Subscription Response Example
  slug: amazon-sns-confirm-subscription-response-example
- key_count: 1
  name: Amazon Sns Create Platform Application Response Example
  slug: amazon-sns-create-platform-application-response-example
- key_count: 1
  name: Amazon Sns Create Topic Response Example
  slug: amazon-sns-create-topic-response-example
- key_count: 0
  name: Amazon Sns Delete Topic Response Example
  slug: amazon-sns-delete-topic-response-example
- key_count: 2
  name: Amazon Sns Error Response Example
  slug: amazon-sns-error-response-example
- key_count: 1
  name: Amazon Sns Get Sms Attributes Response Example
  slug: amazon-sns-get-sms-attributes-response-example
- key_count: 1
  name: Amazon Sns Get Subscription Attributes Response Example
  slug: amazon-sns-get-subscription-attributes-response-example
- key_count: 1
  name: Amazon Sns Get Topic Attributes Response Example
  slug: amazon-sns-get-topic-attributes-response-example
- key_count: 1
  name: Amazon Sns List Subscriptions By Topic Response Example
  slug: amazon-sns-list-subscriptions-by-topic-response-example
- key_count: 1
  name: Amazon Sns List Subscriptions Response Example
  slug: amazon-sns-list-subscriptions-response-example
- key_count: 1
  name: Amazon Sns List Tags For Resource Response Example
  slug: amazon-sns-list-tags-for-resource-response-example
- key_count: 1
  name: Amazon Sns List Topics Response Example
  slug: amazon-sns-list-topics-response-example
- key_count: 3
  name: Amazon Sns Message Attribute Value Example
  slug: amazon-sns-message-attribute-value-example
- key_count: 7
  name: Amazon Sns Publish Batch Request Entry Example
  slug: amazon-sns-publish-batch-request-entry-example
- key_count: 1
  name: Amazon Sns Publish Batch Response Example
  slug: amazon-sns-publish-batch-response-example
- key_count: 1
  name: Amazon Sns Publish Response Example
  slug: amazon-sns-publish-response-example
- key_count: 1
  name: Amazon Sns Response Metadata Example
  slug: amazon-sns-response-metadata-example
- key_count: 0
  name: Amazon Sns Set Subscription Attributes Response Example
  slug: amazon-sns-set-subscription-attributes-response-example
- key_count: 0
  name: Amazon Sns Set Topic Attributes Response Example
  slug: amazon-sns-set-topic-attributes-response-example
- key_count: 1
  name: Amazon Sns Subscribe Response Example
  slug: amazon-sns-subscribe-response-example
- key_count: 5
  name: Amazon Sns Subscription Member Example
  slug: amazon-sns-subscription-member-example
- key_count: 2
  name: Amazon Sns Tag Example
  slug: amazon-sns-tag-example
- key_count: 0
  name: Amazon Sns Tag Resource Response Example
  slug: amazon-sns-tag-resource-response-example
- key_count: 1
  name: Amazon Sns Topic Member Example
  slug: amazon-sns-topic-member-example
- key_count: 0
  name: Amazon Sns Unsubscribe Response Example
  slug: amazon-sns-unsubscribe-response-example
- key_count: 0
  name: Amazon Sns Untag Resource Response Example
  slug: amazon-sns-untag-resource-response-example
features:
- description: Fan-out messages to multiple subscribers through topics supporting HTTP/S, email, SQS, Lambda, and SMS protocols.
  name: Pub/Sub Messaging
- description: Strict message ordering and exactly-once delivery for use cases requiring sequence-preserving fan-out.
  name: FIFO Topics
- description: Subscription filter policies enabling subscribers to receive only the messages relevant to them.
  name: Message Filtering
- description: Cross-platform mobile push via APNs, FCM, and other push services through platform applications.
  name: Mobile Push Notifications
- description: Direct SMS text messaging to phone numbers worldwide with support for transactional and promotional messages.
  name: SMS Messaging
- description: Capture undeliverable messages for analysis and reprocessing to ensure no messages are lost.
  name: Dead-Letter Queues
finops:
- name: Amazon Sns Finops
  service_category: API
  slug: amazon-sns-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: CheckIfPhoneNumberIsOptedOutResponse
  property_count: 1
  slug: amazon-sns-check-if-phone-number-is-opted-out-response
- name: ConfirmSubscriptionResponse
  property_count: 1
  slug: amazon-sns-confirm-subscription-response
- name: CreatePlatformApplicationResponse
  property_count: 1
  slug: amazon-sns-create-platform-application-response
- name: CreateTopicResponse
  property_count: 1
  slug: amazon-sns-create-topic-response
- name: DeleteTopicResponse
  property_count: 0
  slug: amazon-sns-delete-topic-response
- name: ErrorResponse
  property_count: 2
  slug: amazon-sns-error-response
- name: GetSMSAttributesResponse
  property_count: 1
  slug: amazon-sns-get-sms-attributes-response
- name: GetSubscriptionAttributesResponse
  property_count: 1
  slug: amazon-sns-get-subscription-attributes-response
- name: GetTopicAttributesResponse
  property_count: 1
  slug: amazon-sns-get-topic-attributes-response
- name: ListSubscriptionsByTopicResponse
  property_count: 1
  slug: amazon-sns-list-subscriptions-by-topic-response
- name: ListSubscriptionsResponse
  property_count: 1
  slug: amazon-sns-list-subscriptions-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-sns-list-tags-for-resource-response
- name: ListTopicsResponse
  property_count: 1
  slug: amazon-sns-list-topics-response
- name: MessageAttributeValue
  property_count: 3
  slug: amazon-sns-message-attribute-value
- name: Amazon SNS Notification Message
  property_count: 0
  slug: amazon-sns-notification
- name: PublishBatchRequestEntry
  property_count: 7
  slug: amazon-sns-publish-batch-request-entry
- name: PublishBatchResponse
  property_count: 1
  slug: amazon-sns-publish-batch-response
- name: PublishResponse
  property_count: 1
  slug: amazon-sns-publish-response
- name: ResponseMetadata
  property_count: 1
  slug: amazon-sns-response-metadata
- name: SetSubscriptionAttributesResponse
  property_count: 0
  slug: amazon-sns-set-subscription-attributes-response
- name: SetTopicAttributesResponse
  property_count: 0
  slug: amazon-sns-set-topic-attributes-response
- name: SubscribeResponse
  property_count: 1
  slug: amazon-sns-subscribe-response
- name: SubscriptionMember
  property_count: 5
  slug: amazon-sns-subscription-member
- name: TagResourceResponse
  property_count: 0
  slug: amazon-sns-tag-resource-response
- name: Tag
  property_count: 2
  slug: amazon-sns-tag
- name: TopicMember
  property_count: 1
  slug: amazon-sns-topic-member
- name: UnsubscribeResponse
  property_count: 0
  slug: amazon-sns-unsubscribe-response
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-sns-untag-resource-response
json_structures:
- name: Amazon Sns Check If Phone Number Is Opted Out Response Structure
  property_count: 1
  slug: amazon-sns-check-if-phone-number-is-opted-out-response-structure
- name: Amazon Sns Confirm Subscription Response Structure
  property_count: 1
  slug: amazon-sns-confirm-subscription-response-structure
- name: Amazon Sns Create Platform Application Response Structure
  property_count: 1
  slug: amazon-sns-create-platform-application-response-structure
- name: Amazon Sns Create Topic Response Structure
  property_count: 1
  slug: amazon-sns-create-topic-response-structure
- name: Amazon Sns Delete Topic Response Structure
  property_count: 0
  slug: amazon-sns-delete-topic-response-structure
- name: Amazon Sns Error Response Structure
  property_count: 2
  slug: amazon-sns-error-response-structure
- name: Amazon Sns Get Sms Attributes Response Structure
  property_count: 1
  slug: amazon-sns-get-sms-attributes-response-structure
- name: Amazon Sns Get Subscription Attributes Response Structure
  property_count: 1
  slug: amazon-sns-get-subscription-attributes-response-structure
- name: Amazon Sns Get Topic Attributes Response Structure
  property_count: 1
  slug: amazon-sns-get-topic-attributes-response-structure
- name: Amazon Sns List Subscriptions By Topic Response Structure
  property_count: 1
  slug: amazon-sns-list-subscriptions-by-topic-response-structure
- name: Amazon Sns List Subscriptions Response Structure
  property_count: 1
  slug: amazon-sns-list-subscriptions-response-structure
- name: Amazon Sns List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-sns-list-tags-for-resource-response-structure
- name: Amazon Sns List Topics Response Structure
  property_count: 1
  slug: amazon-sns-list-topics-response-structure
- name: Amazon Sns Message Attribute Value Structure
  property_count: 3
  slug: amazon-sns-message-attribute-value-structure
- name: Amazon Sns Publish Batch Request Entry Structure
  property_count: 7
  slug: amazon-sns-publish-batch-request-entry-structure
- name: Amazon Sns Publish Batch Response Structure
  property_count: 1
  slug: amazon-sns-publish-batch-response-structure
- name: Amazon Sns Publish Response Structure
  property_count: 1
  slug: amazon-sns-publish-response-structure
- name: Amazon Sns Response Metadata Structure
  property_count: 1
  slug: amazon-sns-response-metadata-structure
- name: Amazon Sns Set Subscription Attributes Response Structure
  property_count: 0
  slug: amazon-sns-set-subscription-attributes-response-structure
- name: Amazon Sns Set Topic Attributes Response Structure
  property_count: 0
  slug: amazon-sns-set-topic-attributes-response-structure
- name: Amazon Sns Subscribe Response Structure
  property_count: 1
  slug: amazon-sns-subscribe-response-structure
- name: Amazon Sns Subscription Member Structure
  property_count: 5
  slug: amazon-sns-subscription-member-structure
- name: Amazon Sns Tag Resource Response Structure
  property_count: 0
  slug: amazon-sns-tag-resource-response-structure
- name: Amazon Sns Tag Structure
  property_count: 2
  slug: amazon-sns-tag-structure
- name: Amazon Sns Topic Member Structure
  property_count: 1
  slug: amazon-sns-topic-member-structure
- name: Amazon Sns Unsubscribe Response Structure
  property_count: 0
  slug: amazon-sns-unsubscribe-response-structure
- name: Amazon Sns Untag Resource Response Structure
  property_count: 0
  slug: amazon-sns-untag-resource-response-structure
jsonld:
- class_count: 0
  name: Amazon Sns Context
  property_count: 0
  slug: amazon-sns-context
layout: provider
modified: '2026-05-19'
name: Amazon SNS
nav: Providers
network: true
overview: 'Amazon SNS publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ?Action=ListTagsForResource API, ?Action=TagResource API, ?Action=UntagResource API, and 5 more. Tagged areas include Email, Messaging, Notifications, Pub/Sub, and Push Notifications.


  The Amazon SNS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Amazon SNS''s developer surface includes authentication, engineering blog, developer console, support, and 12 more developer resources.'
plans:
- name: Amazon Sns Plans Pricing
  plan_count: 3
  slug: amazon-sns-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Amazon Sns Rate Limits
  slug: amazon-sns-rate-limits
rules:
- name: Amazon SNS API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: amazon-sns-asyncapi-spectral-rules
- name: Amazon SNS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-sns-jsonschema-spectral-rules
- name: Amazon SNS API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 9
  slug: amazon-sns-spectral-rules
score:
  band: strong
  composite: 57.7
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 78.3
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 47.4
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-sns/refs/heads/main/screenshots/amazon-sns-2026-06-20T171830.png
security:
- kind: authentication
  name: Amazon Sns Authentication
  slug: amazon-sns-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amazon Sns Domain Security
  slug: amazon-sns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Sns Vulnerability Disclosure
  slug: amazon-sns-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Sns Trust Center
  slug: amazon-sns-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-sns
tags:
- Email
- Messaging
- Notifications
- Pub/Sub
- Push Notifications
- SMS
use_cases:
- description: Broadcast application events to multiple microservices simultaneously using pub/sub topic subscriptions.
  name: Application Event Fan-Out
- description: Send targeted push notifications to mobile applications across iOS and Android platforms.
  name: Mobile Push Campaigns
- description: Deliver operational alerts via SMS, email, and HTTP endpoints for infrastructure monitoring.
  name: Alert and Monitoring Systems
- description: Send transactional notifications for order confirmations, shipping updates, and account activity.
  name: Order Confirmation Notifications
- description: Share events across AWS accounts using SNS topic policies for multi-account architectures.
  name: Cross-Account Event Distribution
---
