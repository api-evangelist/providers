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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Google Cloud Pubsub Agentic Access
  operation_count: 13
  slug: google-cloud-pubsub-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 3
apis:
- description: Operations for managing Pub/Sub schemas
  name: Google Cloud Pub/Sub Schemas API
  slug: google-cloud-pubsub-schemas-api
- description: Operations for managing Pub/Sub subscriptions
  name: Google Cloud Pub/Sub Subscriptions API
  slug: google-cloud-pubsub-subscriptions-api
- description: Operations for managing Pub/Sub topics
  name: Google Cloud Pub/Sub Topics API
  slug: google-cloud-pubsub-topics-api
artifact_total: 17
asyncapis:
- description: Google Cloud Pub/Sub is a fully managed, real-time messaging service for sending and receiving messages between independent applications. This AsyncAPI document describes Pub/Sub's event-driven surfac
  name: Google Cloud Pub/Sub Messaging Surface
  slug: google-cloud-pubsub-asyncapi
collections:
- collection_type: open
  name: Google Cloud Pub/Sub API
  slug: open-google-cloud-pubsub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-pubsub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-pubsub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-pubsub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-pubsub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-pubsub-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/pubsub/docs/quickstarts
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/pubsub/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-pubsub-context.jsonld
created: '2026-03-13'
description: Google Cloud Pub/Sub is a fully managed, real-time messaging service that allows you to send and receive messages between independent applications. It provides reliable, many-to-many, asynchronous messaging that decouples senders and receivers.
finops:
- name: Google Cloud Pubsub Finops
  service_category: API
  slug: google-cloud-pubsub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-pubsub.png
json_schemas:
- name: Google Cloud Pub/Sub Topic
  property_count: 7
  slug: google-cloud-pubsub-topic
jsonld:
- class_count: 15
  name: Google Cloud Pubsub Context
  property_count: 1
  slug: google-cloud-pubsub-context
layout: provider
modified: '2026-05-30'
name: Google Cloud Pub/Sub
nav: Providers
network: true
overview: 'Google Cloud Pub/Sub publishes 3 APIs on the [APIs.io](https://apis.io/) network: Schemas API, Subscriptions API, and Topics API. Tagged areas include Event-Driven, Google Cloud, Messaging, and Pub/Sub.


  The Google Cloud Pub/Sub catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Google Cloud Pub/Sub''s developer surface includes authentication, getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Google Cloud Pubsub Plans Pricing
  plan_count: 3
  slug: google-cloud-pubsub-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Google Cloud Pubsub Rate Limits
  slug: google-cloud-pubsub-rate-limits
rules:
- name: Google Cloud Pub/Sub API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: google-cloud-pubsub-asyncapi-spectral-rules
- name: Google Cloud Pub/Sub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-pubsub-jsonschema-spectral-rules
scopes:
- name: Google Cloud Pubsub Scopes
  scope_count: 2
  slug: google-cloud-pubsub-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 52.1
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 80.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 55.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-pubsub/refs/heads/main/screenshots/google-cloud-pubsub-2026-06-20T182128.png
security:
- kind: authentication
  name: Google Cloud Pubsub Authentication
  slug: google-cloud-pubsub-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Pubsub Domain Security
  slug: google-cloud-pubsub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Pubsub Vulnerability Disclosure
  slug: google-cloud-pubsub-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-pubsub
tags:
- Event-Driven
- Google Cloud
- Messaging
- Pub/Sub
---
