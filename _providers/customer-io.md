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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Customer Io Agentic Access
  operation_count: 52
  slug: customer-io-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 23
apis:
- description: The Customer.io Track API allows developers to send behavioral data and customer profile information into Customer.io. It provides endpoints for identifying customers, tracking events, managing device
  name: Customer.io Track API
  slug: track-api
- description: Retrieve activity logs for your workspace.
  name: Customer.io Activities API
  slug: customer-io-activities-api
- description: Merge two user identities by creating an alias linking a new identity to an existing one.
  name: Customer.io Alias API
  slug: customer-io-alias-api
- description: Send multiple API calls in a single request for improved performance.
  name: Customer.io Batch API
  slug: customer-io-batch-api
- description: Trigger API-triggered broadcasts to send messages to groups of people based on segments or filters.
  name: Customer.io Broadcasts API
  slug: customer-io-broadcasts-api
- description: Retrieve information about campaigns, campaign actions, and campaign metrics in your workspace.
  name: Customer.io Campaigns API
  slug: customer-io-campaigns-api
- description: Manage collections of data used in message personalization.
  name: Customer.io Collections API
  slug: customer-io-collections-api
- description: Look up customer profiles, search for customers, and retrieve customer attributes and activity data.
  name: Customer.io Customers API
  slug: customer-io-customers-api
- description: Manage push notification devices associated with customer profiles.
  name: Customer.io Devices API
  slug: customer-io-devices-api
- description: Track API v2 entity endpoint for creating and managing people and objects using a unified request format.
  name: Customer.io Entity API
  slug: customer-io-entity-api
- description: Track customer events and anonymous events to record behavioral data and trigger messaging workflows.
  name: Customer.io Events API
  slug: customer-io-events-api
- description: Export customer data, deliveries, and other information from your workspace.
  name: Customer.io Exports API
  slug: customer-io-exports-api
- description: Associate people with groups or organizations.
  name: Customer.io Group API
  slug: customer-io-group-api
- description: Identify people and set their profile attributes. The identify call tells Customer.io who the current user is and assigns traits to them.
  name: Customer.io Identify API
  slug: customer-io-identify-api
- description: Merge two customer profiles into a single profile.
  name: Customer.io Merge API
  slug: customer-io-merge-api
- description: Retrieve information about individual messages sent to customers.
  name: Customer.io Messages API
  slug: customer-io-messages-api
- description: Retrieve information about newsletters and newsletter variants.
  name: Customer.io Newsletters API
  slug: customer-io-newsletters-api
- description: Record page views from web applications.
  name: Customer.io Page API
  slug: customer-io-page-api
- description: Record screen views from mobile applications.
  name: Customer.io Screen API
  slug: customer-io-screen-api
- description: Create and manage manual segments, and retrieve segment membership information.
  name: Customer.io Segments API
  slug: customer-io-segments-api
- description: Manage sender identities used for sending messages.
  name: Customer.io Sender Identities API
  slug: customer-io-sender-identities-api
- description: Manage reusable content snippets for use in messages.
  name: Customer.io Snippets API
  slug: customer-io-snippets-api
- description: Send transactional messages such as password resets, purchase receipts, and other important notifications triggered by user actions.
  name: Customer.io Transactional API
  slug: customer-io-transactional-api
artifact_total: 43
asyncapis:
- description: Customer.io Reporting Webhooks send real-time message activity events as JSON payloads via HTTP POST to a configured endpoint. These events include message sends, deliveries, opens, clicks, bounces, u
  name: Customer.io Reporting Webhooks
  slug: customer-io-reporting-webhooks-asyncapi
collections:
- collection_type: open
  name: Customer.io App API
  slug: open-customer-io-app-api
- collection_type: open
  name: Customer.io Pipelines API
  slug: open-customer-io-pipelines-api
- collection_type: open
  name: Customer.io Track API
  slug: open-customer-io-track-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customer-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/customer-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/customer-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customer-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/customer-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customerio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customer-io
- group: company
  title: ''
  type: Website
  url: https://customer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.customer.io
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/customer-io-reporting-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-customer-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-webhook-payload-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/customer-io-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/customer-io-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/customer-io-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/customer-io-capabilities.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.customer.io/llms.txt
created: '2024-01-01'
description: Customer.io is a customer engagement platform that combines a customer data platform, marketing automation, and messaging delivery to send behavior-triggered email, push, SMS, and in-app messages. Its API surface includes the Track API for sending behavioral data and customer profile updates, the App API for managing workspace resources and sending transactional and broadcast messages, the Pipelines API which is a Segment-spec data ingestion interface, and outbound reporting webhooks that deliver message lifecycle events.
finops:
- name: Customer Io Finops
  service_category: Marketing Automation
  slug: customer-io-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Customer.io messaging and marketing automation platform. Customer.io provides APIs for tracking behavioral data, managing customer profiles and segments, '
  name: Customer.io GraphQL Schema
  slug: customer-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customer-io.png
json_schemas:
- name: Customer.io Customer
  property_count: 8
  slug: customer-io-customer
- name: Customer.io Event
  property_count: 7
  slug: customer-io-event
- name: Customer.io Reporting Webhook Payload
  property_count: 4
  slug: customer-io-webhook-payload
jsonld:
- class_count: 0
  name: Customer Io Context
  property_count: 11
  slug: customer-io-context
layout: provider
modified: '2026-05-19'
name: Customer.io
nav: Providers
network: true
overview: 'Customer.io publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Track API, Activities API, Alias API, and 20 more. Tagged areas include Behavioral Data, Broadcasts, Campaigns, CDP, and Customer Data.


  The Customer.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Customer.io''s developer surface includes authentication, documentation, and 16 more developer resources.'
plans:
- name: Customer Io Plans Pricing
  plan_count: 3
  slug: customer-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Customer Io Rate Limits
  slug: customer-io-rate-limits
rules:
- name: Customer.io API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: customer-io-asyncapi-spectral-rules
- name: Customer.io API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: customer-io-jsonschema-spectral-rules
- name: Customer.io API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: customer-io-rules
score:
  band: developing
  composite: 52.3
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 77.9
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 52.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/screenshots/customer-io-2026-06-20T175348.png
security:
- kind: authentication
  name: Customer Io Authentication
  slug: customer-io-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Customer Io Domain Security
  slug: customer-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Customer Io Vulnerability Disclosure
  slug: customer-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Customer Io Trust Center
  slug: customer-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: customer-io
tags:
- Behavioral Data
- Broadcasts
- Campaigns
- CDP
- Customer Data
- Customer Data Platform
- Data Ingestion
- Email
- Event Tracking
- Marketing Automation
- Messaging
- Push Notifications
- Segments
- SMS
- Transactional Email
website: https://customer.io
---
