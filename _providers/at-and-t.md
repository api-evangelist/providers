---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: At And T Agentic Access
  operation_count: 26
  slug: at-and-t-agentic-access
  summary_line: 26 operations · 14 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: 'AT&T OAuth 2.0 authentication API providing access tokens for all AT&T REST APIs. Supports Authorization Code, Client Credentials, and Refresh Token grant types. Scopes include ADS, MMS, SMS, SPEECH, '
  name: AT&T OAuth 2.0 API
  slug: att-oauth-api
- description: 'Wireline business APIs enabling partners to expedite quoting, service qualification, and ordering of AT&T wireline products. Includes Quick Quote, Product Catalog, Service Qualification, Price Offer, '
  name: AT&T Alliance Wireline APIs
  slug: att-alliance-wireline-apis
- description: The Authentication API from AT&T — 1 operation(s) for authentication.
  name: AT&T Authentication API
  slug: at-and-t-authentication-api
- description: The Balance Management API from AT&T — 1 operation(s) for balance management.
  name: AT&T Balance Management API
  slug: at-and-t-balance-management-api
- description: The Device Management API from AT&T — 2 operation(s) for device management.
  name: AT&T Device Management API
  slug: at-and-t-device-management-api
- description: The Geographic Sites API from AT&T — 1 operation(s) for geographic sites.
  name: AT&T Geographic Sites API
  slug: at-and-t-geographic-sites-api
- description: The Inbox Management API from AT&T — 2 operation(s) for inbox management.
  name: AT&T Inbox Management API
  slug: at-and-t-inbox-management-api
- description: The Messages API from AT&T — 2 operation(s) for messages.
  name: AT&T Messages API
  slug: at-and-t-messages-api
- description: The Number Management API from AT&T — 2 operation(s) for number management.
  name: AT&T Number Management API
  slug: at-and-t-number-management-api
- description: The Porting API from AT&T — 3 operation(s) for porting.
  name: AT&T Porting API
  slug: at-and-t-porting-api
- description: The Product Orders API from AT&T — 1 operation(s) for product orders.
  name: AT&T Product Orders API
  slug: at-and-t-product-orders-api
- description: The Service Management API from AT&T — 1 operation(s) for service management.
  name: AT&T Service Management API
  slug: at-and-t-service-management-api
- description: The SMS Messaging API from AT&T — 3 operation(s) for sms messaging.
  name: AT&T SMS Messaging API
  slug: at-and-t-sms-messaging-api
- description: The Subscriber Management API from AT&T — 1 operation(s) for subscriber management.
  name: AT&T Subscriber Management API
  slug: at-and-t-subscriber-management-api
artifact_total: 138
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/at-and-t-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/at-and-t-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/at-and-t-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/at-and-t-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/att
- group: company
  title: ''
  type: Website
  url: https://www.att.com
- group: start
  title: ''
  type: Portal
  url: https://developer.att.com/s/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devex-web.att.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.att.com/s/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.att.com/oauth-2/docs
- group: operate
  title: ''
  type: Support
  url: https://developer.att.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://developer.att.com/support/faqs/att-developer-program-and-api-platform-faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.att.com/gen/general?pid=11561
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.att.com/gen/privacy-policy?pid=2506
- group: start
  title: ''
  type: Signup
  url: https://developer.att.com/developer/manageMyAccount.jsp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attdevsupport
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/att
- group: design
  title: ''
  type: SpectralRules
  url: rules/at-and-t-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/at-and-t-vocabulary.yaml
created: '2026-03-21'
description: AT&T is a multinational telecommunications holding company providing wireless and wireline telecommunications services, broadband, and digital entertainment to consumers and businesses worldwide. AT&T offers a suite of developer APIs spanning messaging, speech, mobile virtual network operations, business voice, wholesale service qualification, enterprise wireline ordering, and mobility management, enabling developers and enterprise partners to integrate AT&T network capabilities into applications and systems.
examples:
- key_count: 1
  name: In App Messaging Api Delta Response Example
  slug: in-app-messaging-api-delta-response-example
- key_count: 1
  name: In App Messaging Api Message Detail Example
  slug: in-app-messaging-api-message-detail-example
- key_count: 1
  name: In App Messaging Api Message Index Response Example
  slug: in-app-messaging-api-message-index-response-example
- key_count: 1
  name: In App Messaging Api Message List Response Example
  slug: in-app-messaging-api-message-list-response-example
- key_count: 8
  name: In App Messaging Api Message Summary Example
  slug: in-app-messaging-api-message-summary-example
- key_count: 1
  name: In App Messaging Api Send Message Request Example
  slug: in-app-messaging-api-send-message-request-example
- key_count: 2
  name: In App Messaging Api Send Message Response Example
  slug: in-app-messaging-api-send-message-response-example
- key_count: 1
  name: In App Messaging Api Update Message Request Example
  slug: in-app-messaging-api-update-message-request-example
- key_count: 1
  name: In App Messaging Api Update Message Response Example
  slug: in-app-messaging-api-update-message-response-example
- key_count: 2
  name: Mvnx Api Cancel Portability Order Example
  slug: mvnx-api-cancel-portability-order-example
- key_count: 4
  name: Mvnx Api Geographic Site Example
  slug: mvnx-api-geographic-site-example
- key_count: 3
  name: Mvnx Api Portability Order Cancellation Example
  slug: mvnx-api-portability-order-cancellation-example
- key_count: 1
  name: Mvnx Api Portability Order Create Example
  slug: mvnx-api-portability-order-create-example
- key_count: 4
  name: Mvnx Api Portability Order Example
  slug: mvnx-api-portability-order-example
- key_count: 1
  name: Mvnx Api Portability Order Update Example
  slug: mvnx-api-portability-order-update-example
- key_count: 4
  name: Mvnx Api Product Example
  slug: mvnx-api-product-example
- key_count: 2
  name: Mvnx Api Product Order Create Example
  slug: mvnx-api-product-order-create-example
- key_count: 4
  name: Mvnx Api Product Order Example
  slug: mvnx-api-product-order-example
- key_count: 5
  name: Mvnx Api Resource Example
  slug: mvnx-api-resource-example
- key_count: 1
  name: Mvnx Api Resource Reservation Create Example
  slug: mvnx-api-resource-reservation-create-example
- key_count: 4
  name: Mvnx Api Resource Reservation Example
  slug: mvnx-api-resource-reservation-example
- key_count: 1
  name: Mvnx Api Resource Reservation Update Example
  slug: mvnx-api-resource-reservation-update-example
- key_count: 1
  name: Mvnx Api Resource Update Example
  slug: mvnx-api-resource-update-example
- key_count: 4
  name: Mvnx Api Service Example
  slug: mvnx-api-service-example
- key_count: 3
  name: Mvnx Api Topup Balance Create Example
  slug: mvnx-api-topup-balance-create-example
- key_count: 3
  name: Mvnx Api Topup Balance Example
  slug: mvnx-api-topup-balance-example
- key_count: 2
  name: Sms Api Delivery Info Example
  slug: sms-api-delivery-info-example
- key_count: 1
  name: Sms Api Delivery Info Response Example
  slug: sms-api-delivery-info-response-example
- key_count: 5
  name: Sms Api Inbound Sms Message Example
  slug: sms-api-inbound-sms-message-example
- key_count: 1
  name: Sms Api Inbound Sms Response Example
  slug: sms-api-inbound-sms-response-example
- key_count: 1
  name: Sms Api Send Sms Request Example
  slug: sms-api-send-sms-request-example
- key_count: 1
  name: Sms Api Send Sms Response Example
  slug: sms-api-send-sms-response-example
- key_count: 6
  name: Sms Api Token Request Example
  slug: sms-api-token-request-example
- key_count: 4
  name: Sms Api Token Response Example
  slug: sms-api-token-response-example
features:
- 'AT&T: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- AT&T Business APIs (Network APIs, IoT Connectivity, etc.) are sold via partner program with custom contracts.
finops:
- name: At And T Finops
  service_category: Telecommunications
  slug: at-and-t-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/at-and-t.png
integrations:
- description: AT&T API Platform Adapters for IBM Worklight mobile development platform.
  name: IBM Worklight
- description: AT&T Toolkit for Salesforce enabling speech and messaging API integration in Salesforce apps.
  name: Salesforce Platform
- description: MVNX APIs align with TM Forum Open API standards including TMF 622, 637, 639, 640, 654, 674, 689, 702, 716, and 761.
  name: TM Forum APIs
json_schemas:
- name: DeltaResponse
  property_count: 1
  slug: in-app-messaging-api-delta-response
- name: MessageDetail
  property_count: 1
  slug: in-app-messaging-api-message-detail
- name: MessageIndexResponse
  property_count: 1
  slug: in-app-messaging-api-message-index-response
- name: MessageListResponse
  property_count: 1
  slug: in-app-messaging-api-message-list-response
- name: MessageSummary
  property_count: 8
  slug: in-app-messaging-api-message-summary
- name: SendMessageRequest
  property_count: 1
  slug: in-app-messaging-api-send-message-request
- name: SendMessageResponse
  property_count: 2
  slug: in-app-messaging-api-send-message-response
- name: UpdateMessageRequest
  property_count: 1
  slug: in-app-messaging-api-update-message-request
- name: UpdateMessageResponse
  property_count: 1
  slug: in-app-messaging-api-update-message-response
- name: CancelPortabilityOrder
  property_count: 2
  slug: mvnx-api-cancel-portability-order
- name: GeographicSite
  property_count: 4
  slug: mvnx-api-geographic-site
- name: PortabilityOrderCancellation
  property_count: 3
  slug: mvnx-api-portability-order-cancellation
- name: PortabilityOrderCreate
  property_count: 1
  slug: mvnx-api-portability-order-create
- name: PortabilityOrder
  property_count: 4
  slug: mvnx-api-portability-order
- name: PortabilityOrderUpdate
  property_count: 1
  slug: mvnx-api-portability-order-update
- name: ProductOrderCreate
  property_count: 2
  slug: mvnx-api-product-order-create
- name: ProductOrder
  property_count: 4
  slug: mvnx-api-product-order
- name: Product
  property_count: 4
  slug: mvnx-api-product
- name: ResourceReservationCreate
  property_count: 1
  slug: mvnx-api-resource-reservation-create
- name: ResourceReservation
  property_count: 4
  slug: mvnx-api-resource-reservation
- name: ResourceReservationUpdate
  property_count: 1
  slug: mvnx-api-resource-reservation-update
- name: Resource
  property_count: 5
  slug: mvnx-api-resource
- name: ResourceUpdate
  property_count: 1
  slug: mvnx-api-resource-update
- name: Service
  property_count: 4
  slug: mvnx-api-service
- name: TopupBalanceCreate
  property_count: 3
  slug: mvnx-api-topup-balance-create
- name: TopupBalance
  property_count: 3
  slug: mvnx-api-topup-balance
- name: DeliveryInfoResponse
  property_count: 1
  slug: sms-api-delivery-info-response
- name: DeliveryInfo
  property_count: 2
  slug: sms-api-delivery-info
- name: InboundSmsMessage
  property_count: 5
  slug: sms-api-inbound-sms-message
- name: InboundSmsResponse
  property_count: 1
  slug: sms-api-inbound-sms-response
- name: SendSmsRequest
  property_count: 1
  slug: sms-api-send-sms-request
- name: SendSmsResponse
  property_count: 1
  slug: sms-api-send-sms-response
- name: TokenRequest
  property_count: 6
  slug: sms-api-token-request
- name: TokenResponse
  property_count: 4
  slug: sms-api-token-response
json_structures:
- name: In App Messaging Api Delta Response Structure
  property_count: 1
  slug: in-app-messaging-api-delta-response-structure
- name: In App Messaging Api Message Detail Structure
  property_count: 1
  slug: in-app-messaging-api-message-detail-structure
- name: In App Messaging Api Message Index Response Structure
  property_count: 1
  slug: in-app-messaging-api-message-index-response-structure
- name: In App Messaging Api Message List Response Structure
  property_count: 1
  slug: in-app-messaging-api-message-list-response-structure
- name: In App Messaging Api Message Summary Structure
  property_count: 8
  slug: in-app-messaging-api-message-summary-structure
- name: In App Messaging Api Send Message Request Structure
  property_count: 1
  slug: in-app-messaging-api-send-message-request-structure
- name: In App Messaging Api Send Message Response Structure
  property_count: 2
  slug: in-app-messaging-api-send-message-response-structure
- name: In App Messaging Api Update Message Request Structure
  property_count: 1
  slug: in-app-messaging-api-update-message-request-structure
- name: In App Messaging Api Update Message Response Structure
  property_count: 1
  slug: in-app-messaging-api-update-message-response-structure
- name: Mvnx Api Cancel Portability Order Structure
  property_count: 2
  slug: mvnx-api-cancel-portability-order-structure
- name: Mvnx Api Geographic Site Structure
  property_count: 4
  slug: mvnx-api-geographic-site-structure
- name: Mvnx Api Portability Order Cancellation Structure
  property_count: 3
  slug: mvnx-api-portability-order-cancellation-structure
- name: Mvnx Api Portability Order Create Structure
  property_count: 1
  slug: mvnx-api-portability-order-create-structure
- name: Mvnx Api Portability Order Structure
  property_count: 4
  slug: mvnx-api-portability-order-structure
- name: Mvnx Api Portability Order Update Structure
  property_count: 1
  slug: mvnx-api-portability-order-update-structure
- name: Mvnx Api Product Order Create Structure
  property_count: 2
  slug: mvnx-api-product-order-create-structure
- name: Mvnx Api Product Order Structure
  property_count: 4
  slug: mvnx-api-product-order-structure
- name: Mvnx Api Product Structure
  property_count: 4
  slug: mvnx-api-product-structure
- name: Mvnx Api Resource Reservation Create Structure
  property_count: 1
  slug: mvnx-api-resource-reservation-create-structure
- name: Mvnx Api Resource Reservation Structure
  property_count: 4
  slug: mvnx-api-resource-reservation-structure
- name: Mvnx Api Resource Reservation Update Structure
  property_count: 1
  slug: mvnx-api-resource-reservation-update-structure
- name: Mvnx Api Resource Structure
  property_count: 5
  slug: mvnx-api-resource-structure
- name: Mvnx Api Resource Update Structure
  property_count: 1
  slug: mvnx-api-resource-update-structure
- name: Mvnx Api Service Structure
  property_count: 4
  slug: mvnx-api-service-structure
- name: Mvnx Api Topup Balance Create Structure
  property_count: 3
  slug: mvnx-api-topup-balance-create-structure
- name: Mvnx Api Topup Balance Structure
  property_count: 3
  slug: mvnx-api-topup-balance-structure
- name: Sms Api Delivery Info Response Structure
  property_count: 1
  slug: sms-api-delivery-info-response-structure
- name: Sms Api Delivery Info Structure
  property_count: 2
  slug: sms-api-delivery-info-structure
- name: Sms Api Inbound Sms Message Structure
  property_count: 5
  slug: sms-api-inbound-sms-message-structure
- name: Sms Api Inbound Sms Response Structure
  property_count: 1
  slug: sms-api-inbound-sms-response-structure
- name: Sms Api Send Sms Request Structure
  property_count: 1
  slug: sms-api-send-sms-request-structure
- name: Sms Api Send Sms Response Structure
  property_count: 1
  slug: sms-api-send-sms-response-structure
- name: Sms Api Token Request Structure
  property_count: 6
  slug: sms-api-token-request-structure
- name: Sms Api Token Response Structure
  property_count: 4
  slug: sms-api-token-response-structure
jsonld:
- class_count: 9
  name: At And T In App Messaging Api Context
  property_count: 28
  slug: at-and-t-in-app-messaging-api-context
- class_count: 18
  name: At And T Mvnx Api Context
  property_count: 30
  slug: at-and-t-mvnx-api-context
- class_count: 8
  name: At And T Sms Api Context
  property_count: 27
  slug: at-and-t-sms-api-context
layout: provider
modified: '2026-05-19'
name: AT&T
nav: Providers
network: true
overview: 'AT&T publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balance Management API, Device Management API, and 9 more. Tagged areas include Fortune 100, Telecommunications, Wireless, Wireline, and Messaging.


  The AT&T catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  AT&T''s developer surface includes authentication, developer portal, documentation, support, FAQ, signup flow, and 13 more developer resources.'
plans:
- name: At And T Plans Pricing
  plan_count: 1
  slug: at-and-t-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: At And T Rate Limits
  slug: at-and-t-rate-limits
rules:
- name: AT&T API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: at-and-t-jsonschema-spectral-rules
- name: AT&T API Rules
  rule_count: 44
  severity_counts:
    error: 16
    hint: 0
    info: 5
    warn: 23
  slug: at-and-t-spectral-rules
scopes:
- name: At And T Scopes
  scope_count: 8
  slug: at-and-t-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 57.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.7
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 26.3
  previous_composite: 57.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: At And T Authentication
  slug: at-and-t-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: At And T Domain Security
  slug: at-and-t-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: at-and-t
tags:
- Fortune 100
- Telecommunications
- Wireless
- Wireline
- Messaging
- Speech
- Mobile
- Broadband
- Enterprise
use_cases:
- description: Send security verification codes, appointment reminders, promotional offers, and customer feedback requests via SMS short code.
  name: SMS Alerts and Notifications
- description: Embed MMS and SMS messaging directly into mobile applications with full inbox management capabilities.
  name: In-App Messaging Integration
- description: Launch and operate MVNO services using AT&T's network with automated subscriber onboarding, porting, and lifecycle management.
  name: Mobile Virtual Network Operations
- description: Automate service qualification, quoting, and order submission for enterprise connectivity services.
  name: Enterprise Wireline Ordering
website: https://www.att.com
---
