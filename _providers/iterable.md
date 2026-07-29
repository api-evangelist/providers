---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Iterable Agentic Access
  operation_count: 48
  slug: iterable-agentic-access
  summary_line: 48 operations · 25 acting
api_count: 23
apis:
- description: The Iterable Export API enables developers to extract data from Iterable projects for analytics, reporting, and data warehousing purposes. It provides asynchronous export endpoints that allow bulk ret
  name: Iterable Export API
  slug: export-api
- description: The Iterable Web SDK enables developers to integrate Iterable's marketing automation capabilities directly into JavaScript and Node.js applications. It provides functions for tracking user events, man
  name: Iterable Web SDK
  slug: web-sdk
- description: The Iterable iOS SDK allows developers to integrate Iterable's marketing automation features into native iOS applications built with Swift or Objective-C. It supports push notifications, in-app messag
  name: Iterable iOS SDK
  slug: ios-sdk
- description: The Iterable Android SDK provides native integration between Android applications and the Iterable marketing automation platform. It supports push notifications, in-app messages, deep links, and Mobil
  name: Iterable Android SDK
  slug: android-sdk
- description: The Iterable React Native SDK enables developers to integrate Iterable's marketing automation capabilities into cross-platform mobile applications built with React Native. It wraps Iterable's native i
  name: Iterable React Native SDK
  slug: react-native-sdk
- description: Create, retrieve, and manage marketing campaigns. Access campaign metrics and trigger campaign sends.
  name: Iterable Campaigns API
  slug: iterable-campaigns-api
- description: Manage product catalogs and catalog items used for personalization and recommendation in campaigns.
  name: Iterable Catalogs API
  slug: iterable-catalogs-api
- description: Retrieve and manage messaging channels and message types used for organizing campaigns and templates.
  name: Iterable Channels API
  slug: iterable-channels-api
- description: Track purchase events, update cart data, and manage commerce-related user activity for revenue attribution.
  name: Iterable Commerce API
  slug: iterable-commerce-api
- description: Send transactional emails and manage email-specific delivery settings.
  name: Iterable Email API
  slug: iterable-email-api
- description: Track custom events, retrieve event data for users, and manage event metadata used for segmentation and campaign triggering.
  name: Iterable Events API
  slug: iterable-events-api
- description: Export experiment and A/B test metrics as CSV for analysis.
  name: Iterable ExperimentMetrics API
  slug: iterable-experimentmetrics-api
- description: Retrieve experiment configurations and metrics for A/B tests running across campaigns.
  name: Iterable Experiments API
  slug: iterable-experiments-api
- description: Manage in-app messages and retrieve in-app message content for mobile and web clients.
  name: Iterable InApp API
  slug: iterable-inapp-api
- description: Create and manage subscriber lists. Subscribe and unsubscribe users from lists. Retrieve list metadata and membership.
  name: Iterable Lists API
  slug: iterable-lists-api
- description: Manage message types that categorize the kinds of messages sent through channels.
  name: Iterable MessageTypes API
  slug: iterable-messagetypes-api
- description: Store and retrieve key-value metadata tables for use in personalization and campaign logic.
  name: Iterable Metadata API
  slug: iterable-metadata-api
- description: Send push notifications and manage push notification delivery settings and tokens.
  name: Iterable Push API
  slug: iterable-push-api
- description: Send SMS messages and manage SMS-specific delivery settings.
  name: Iterable SMS API
  slug: iterable-sms-api
- description: Manage email, push, SMS, and in-app message templates. Retrieve template content and metadata.
  name: Iterable Templates API
  slug: iterable-templates-api
- description: Manage user profiles, update user fields, bulk update users, get user data by email or userId, and delete users.
  name: Iterable Users API
  slug: iterable-users-api
- description: Send web push notifications and manage web push subscription tokens.
  name: Iterable WebPush API
  slug: iterable-webpush-api
- description: Trigger workflow enrollments and manage journey-based automation workflows.
  name: Iterable Workflows API
  slug: iterable-workflows-api
artifact_total: 90
asyncapis:
- description: Iterable system webhooks send real-time event data from an Iterable project to external systems via HTTP POST requests whenever specified events occur. System webhooks can be configured to fire on ema
  name: Iterable System Webhooks
  slug: iterable-system-webhooks-asyncapi
collections:
- collection_type: postman
  name: Iterable Export Campaigns API
  slug: postman-iterable-campaigns-api
- collection_type: postman
  name: Iterable Export Campaigns Catalogs API
  slug: postman-iterable-catalogs-api
- collection_type: postman
  name: Iterable Export Campaigns Channels API
  slug: postman-iterable-channels-api
- collection_type: postman
  name: Iterable Export Campaigns Commerce API
  slug: postman-iterable-commerce-api
- collection_type: postman
  name: Iterable Export Campaigns Email API
  slug: postman-iterable-email-api
- collection_type: postman
  name: Iterable Export Campaigns Events API
  slug: postman-iterable-events-api
- collection_type: postman
  name: Iterable Export Campaigns ExperimentMetrics API
  slug: postman-iterable-experimentmetrics-api
- collection_type: postman
  name: Iterable Export Campaigns Experiments API
  slug: postman-iterable-experiments-api
- collection_type: postman
  name: Iterable Campaigns Export API
  slug: postman-iterable-export-api
- collection_type: postman
  name: Iterable Export Campaigns InApp API
  slug: postman-iterable-inapp-api
- collection_type: postman
  name: Iterable Export Campaigns Lists API
  slug: postman-iterable-lists-api
- collection_type: postman
  name: Iterable Export Campaigns MessageTypes API
  slug: postman-iterable-messagetypes-api
- collection_type: postman
  name: Iterable Export Campaigns Metadata API
  slug: postman-iterable-metadata-api
- collection_type: postman
  name: Iterable Export Campaigns Push API
  slug: postman-iterable-push-api
- collection_type: postman
  name: Iterable Export Campaigns SMS API
  slug: postman-iterable-sms-api
- collection_type: postman
  name: Iterable Export Campaigns Templates API
  slug: postman-iterable-templates-api
- collection_type: postman
  name: Iterable Export Campaigns Users API
  slug: postman-iterable-users-api
- collection_type: postman
  name: Iterable Export Campaigns WebPush API
  slug: postman-iterable-webpush-api
- collection_type: postman
  name: Iterable Export Campaigns Workflows API
  slug: postman-iterable-workflows-api
- collection_type: open
  name: Iterable Export API
  slug: open-iterable-export-api
- collection_type: open
  name: Iterable REST API
  slug: open-iterable-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/iterable/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iterable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/iterable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iterable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iterable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iterable
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/iterable-system-webhooks-asyncapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/iterable-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-campaign-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-commerce-item-schema.json
- group: company
  title: ''
  type: Website
  url: https://iterable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.iterable.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://support.iterable.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://iterable.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.iterable.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iterable.com/trust/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iterable.com/trust/terms-of-service/
created: '2026-03-20'
description: Iterable is an AI customer engagement platform that powers unified cross-channel marketing experiences and empowers marketers to create, optimize, and measure relevant interactions across email, push, SMS, in-app, and web channels. Their developer platform provides REST APIs, export APIs, AsyncAPI webhooks, and native SDKs for web, iOS, Android, and React Native.
features:
- 'Growth: $3K-$5K/mo for 10K-50K MAUs'
- 'Premier: $6K-$15K/mo for 50K-200K MAUs'
- 'Enterprise: $20K+/mo for 200K+ MAUs'
- Multi-year + volume discounts
- Email + Push + SMS + In-App + Web Push + Direct Mail channels
- Workflow Studio for journey orchestration
- AI Optimization for send-time and channel selection (Premier+)
- REST API at api.iterable.com
- Default 30 req/sec; bulk endpoints up to 1K events/req
- OAuth + API keys (project-scoped)
- Webhooks for events and campaign data
- User profile and event tracking
- Cross-channel campaigns
- Smart Ingest for data lake/warehouse loading
- Real-time event triggers
- Iterable AI for content suggestions
finops:
- name: Iterable Finops
  service_category: Marketing Automation
  slug: iterable-finops
graphqls:
- description: Iterable is a cross-channel marketing automation platform. The API covers user management, event tracking, email/SMS/push campaigns, workflows, A/B testing, audience segmentation, catalog items, and e
  name: Iterable GraphQL API
  slug: iterable-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iterable.png
json_schemas:
- name: Iterable Campaign
  property_count: 15
  slug: iterable-campaign
- name: CampaignCreateRequest
  property_count: 6
  slug: iterable-campaigncreaterequest
- name: Channel
  property_count: 4
  slug: iterable-channel
- name: Iterable Commerce Item
  property_count: 10
  slug: iterable-commerce-item
- name: CommerceItem
  property_count: 10
  slug: iterable-commerceitem
- name: EmailTemplate
  property_count: 11
  slug: iterable-emailtemplate
- name: EmailTemplateUpdate
  property_count: 8
  slug: iterable-emailtemplateupdate
- name: ErrorResponse
  property_count: 2
  slug: iterable-errorresponse
- name: Iterable Event
  property_count: 7
  slug: iterable-event
- name: ExportedEvent
  property_count: 15
  slug: iterable-exportedevent
- name: IterableResponse
  property_count: 3
  slug: iterable-iterableresponse
- name: List
  property_count: 5
  slug: iterable-list
- name: PurchaseRequest
  property_count: 7
  slug: iterable-purchaserequest
- name: TrackEventRequest
  property_count: 7
  slug: iterable-trackeventrequest
- name: Iterable User
  property_count: 10
  slug: iterable-user
- name: UserResponse
  property_count: 1
  slug: iterable-userresponse
- name: UserUpdateRequest
  property_count: 5
  slug: iterable-userupdaterequest
json_structures:
- name: Iterable Structure
  property_count: 0
  slug: iterable-structure
jsonld:
- class_count: 0
  name: Iterable Context
  property_count: 8
  slug: iterable-context
layout: provider
modified: '2026-05-19'
name: Iterable
nav: Providers
network: true
overview: 'Iterable publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Export API, Campaigns API, Catalogs API, and 16 more. Tagged areas include Cross-Channel Messaging, Customer Engagement, Email, Marketing Automation, and Push Notifications.


  The Iterable catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Iterable''s developer surface includes authentication, documentation, support, engineering blog, and 15 more developer resources.'
plans:
- name: Iterable Plans Pricing
  plan_count: 3
  slug: iterable-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Iterable Rate Limits
  slug: iterable-rate-limits
rules:
- name: Iterable API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: iterable-asyncapi-spectral-rules
- name: Iterable API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: iterable-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.9
  delta: -4.8
  facets:
    commercial_clarity: 81.6
    contract_quality: 79.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 31.6
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iterable/refs/heads/main/screenshots/iterable-2026-06-20T183630.png
security:
- kind: authentication
  name: Iterable Authentication
  slug: iterable-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Iterable Domain Security
  slug: iterable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Iterable Trust Center
  slug: iterable-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: iterable
tags:
- Cross-Channel Messaging
- Customer Engagement
- Email
- Marketing Automation
- Push Notifications
- SMS
website: https://iterable.com/
---
