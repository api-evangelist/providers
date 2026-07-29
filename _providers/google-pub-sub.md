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
- acting_count: 12
  human_in_the_loop: 0
  name: Google Pub Sub Agentic Access
  operation_count: 19
  slug: google-pub-sub-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 6
apis:
- description: Publish messages to topics
  name: Google Pub/Sub Publish API
  slug: google-pub-sub-publish-api
- description: Manage Pub/Sub schemas
  name: Google Pub/Sub Schemas API
  slug: google-pub-sub-schemas-api
- description: Manage subscription snapshots
  name: Google Pub/Sub Snapshots API
  slug: google-pub-sub-snapshots-api
- description: Pull and acknowledge messages
  name: Google Pub/Sub Subscribe API
  slug: google-pub-sub-subscribe-api
- description: Manage Pub/Sub subscriptions
  name: Google Pub/Sub Subscriptions API
  slug: google-pub-sub-subscriptions-api
- description: Manage Pub/Sub topics
  name: Google Pub/Sub Topics API
  slug: google-pub-sub-topics-api
artifact_total: 18
asyncapis:
- description: Google Cloud Pub/Sub is a fully managed real-time messaging service that allows you to send and receive messages between independent applications. This AsyncAPI spec describes the event-driven messagi
  name: Google Cloud Pub/Sub
  slug: google-pub-sub-asyncapi
collections:
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub API
  slug: open-google-pub-sub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-pub-sub-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-pub-sub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-pub-sub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-pub-sub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-pub-sub-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/pubsub
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/pubsub/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/pubsub/docs/quickstarts
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/pubsub/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/googleapis/google-cloud-go
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog
created: '2026-03-26'
description: Google Cloud Pub/Sub is a fully managed, real-time messaging service that allows you to send and receive messages between independent applications, providing reliable, many-to-many, asynchronous messaging for event ingestion, streaming analytics, and event-driven computing.
finops:
- name: Google Pub Sub Finops
  service_category: API
  slug: google-pub-sub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-pub-sub.png
layout: provider
modified: '2026-05-19'
name: Google Pub/Sub
nav: Providers
network: true
overview: 'Google Pub/Sub publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Publish API, Schemas API, Snapshots API, and 3 more. Tagged areas include Cloud, Event-Driven, Google Cloud, Messaging, and Pub/Sub.


  The Google Pub/Sub catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Google Pub/Sub''s developer surface includes authentication, documentation, getting-started guide, pricing, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Google Pub Sub Plans Pricing
  plan_count: 3
  slug: google-pub-sub-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Google Pub Sub Rate Limits
  slug: google-pub-sub-rate-limits
rules:
- name: Google Pub/Sub API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: google-pub-sub-asyncapi-spectral-rules
- name: Google Pub/Sub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-pub-sub-jsonschema-spectral-rules
scopes:
- name: Google Pub Sub Scopes
  scope_count: 2
  slug: google-pub-sub-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 52.2
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 77.1
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 48.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-pub-sub/refs/heads/main/screenshots/google-pub-sub-2026-06-20T182227.png
security:
- kind: authentication
  name: Google Pub Sub Authentication
  slug: google-pub-sub-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Google Pub Sub Domain Security
  slug: google-pub-sub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Pub Sub Vulnerability Disclosure
  slug: google-pub-sub-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-pub-sub
tags:
- Cloud
- Event-Driven
- Google Cloud
- Messaging
- Pub/Sub
- Streaming
website: https://cloud.google.com/pubsub
---
