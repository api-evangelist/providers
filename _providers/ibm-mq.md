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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Ibm Mq Agentic Access
  operation_count: 28
  slug: ibm-mq-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 11
apis:
- description: Java Message Service API for IBM MQ.
  name: IBM MQ JMS API
  slug: ibm-mq-jms-api
- description: Native procedural API for IBM MQ (MQI).
  name: IBM MQ Native API
  slug: ibm-mq-native-api
- description: Manage and query channel objects and status
  name: IBM MQ Channels API
  slug: ibm-mq-channels-api
- description: Query MQ installation information
  name: IBM MQ Installations API
  slug: ibm-mq-installations-api
- description: Authentication token management
  name: IBM MQ Login API
  slug: ibm-mq-login-api
- description: Manage and query queue manager objects and status
  name: IBM MQ Queue Managers API
  slug: ibm-mq-queue-managers-api
- description: Send and receive messages on queues
  name: IBM MQ Queue Messaging API
  slug: ibm-mq-queue-messaging-api
- description: Manage and query queue objects and status
  name: IBM MQ Queues API
  slug: ibm-mq-queues-api
- description: Manage and query subscription objects
  name: IBM MQ Subscriptions API
  slug: ibm-mq-subscriptions-api
- description: Publish messages to topics
  name: IBM MQ Topic Messaging API
  slug: ibm-mq-topic-messaging-api
- description: Manage and query topic objects
  name: IBM MQ Topics API
  slug: ibm-mq-topics-api
artifact_total: 27
asyncapis:
- description: Asynchronous messaging interface for IBM MQ, supporting point-to-point queue-based messaging and publish/subscribe topic-based messaging. Defines the channels, operations, and message formats for appl
  name: IBM MQ Messaging
  slug: ibm-mq-messaging-asyncapi
collections:
- collection_type: open
  name: IBM MQ Administration REST API
  slug: open-ibm-mq-admin-rest
- collection_type: open
  name: IBM MQ Messaging REST API
  slug: open-ibm-mq-messaging-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ibm-mq-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-mq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-mq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ibm-mq-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ibm-messaging
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibm.com/docs/en/ibm-mq/latest?topic=mq-getting-started
- group: learn
  title: ''
  type: tutorials
  url: https://developer.ibm.com/tutorials/?s=mq
- group: other
  title: ''
  type: downloads
  url: https://www.ibm.com/support/pages/downloading-ibm-mq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/products/mq/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: company
  title: ''
  type: Blog
  url: https://community.ibm.com/community/user/integration/communities/community-home?CommunityKey=183ec850-4947-49c8-9a2e-8e7c7fc46c64
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ibm-mq-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ibm-mq-queue-manager-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ibm-mq-queue-schema.json
- group: design
  title: ''
  type: Rules
  url: rules/ibm-mq-rules.yml
created: '2024-01-20'
description: APIs for IBM MQ messaging middleware for enterprise integration.
finops:
- name: Ibm Mq Finops
  service_category: Messaging + Integration
  slug: ibm-mq-finops
image: https://www.ibm.com/brand/experience-guides/developer/8f4e3cc842d31b9a55e57cb2b0e49605/02_8-bar-positive.svg
json_schemas:
- name: IBM MQ Queue Manager
  property_count: 14
  slug: ibm-mq-queue-manager
- name: IBM MQ Queue
  property_count: 23
  slug: ibm-mq-queue
jsonld:
- class_count: 0
  name: Ibm Mq Context
  property_count: 7
  slug: ibm-mq-context
layout: provider
modified: '2026-05-19'
name: IBM MQ
nav: Providers
network: true
overview: 'IBM MQ publishes 10 APIs on the [APIs.io](https://apis.io/) network, including JMS API, Channels API, Installations API, and 7 more. Tagged areas include Async, Enterprise, Integration, Messaging, and Middleware.


  The IBM MQ catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  IBM MQ''s developer surface includes authentication, getting-started guide, pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Ibm Mq Plans Pricing
  plan_count: 3
  slug: ibm-mq-plans-pricing
random_paper: 115
rate_limits:
- limit_count: 3
  name: Ibm Mq Rate Limits
  slug: ibm-mq-rate-limits
rules:
- name: IBM MQ API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: ibm-mq-asyncapi-spectral-rules
- name: IBM MQ API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: ibm-mq-jsonschema-spectral-rules
- name: IBM MQ API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ibm-mq-rules
score:
  band: developing
  composite: 43.3
  delta: -5.5
  facets:
    commercial_clarity: 26.3
    contract_quality: 72.5
    developer_ergonomics: 28.3
    discoverability: 63.0
    governance: 52.1
    operational_transparency: 13.2
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-mq/refs/heads/main/screenshots/ibm-mq-2026-06-20T183135.png
security:
- kind: authentication
  name: Ibm Mq Authentication
  slug: ibm-mq-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ibm Mq Domain Security
  slug: ibm-mq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm Mq Vulnerability Disclosure
  slug: ibm-mq-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-mq
tags:
- Async
- Enterprise
- Integration
- Messaging
- Middleware
- Queue
website: https://www.ibm.com/products/mq
---
