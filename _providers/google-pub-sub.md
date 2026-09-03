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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Google Pub Sub Agentic Access
  operation_count: 19
  slug: google-pub-sub-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 1
apis:
- baseURL: https://pubsub.googleapis.com
  baseurl_source: spec
  description: Publish messages to topics
  name: Google Pub/Sub Publish API
  slug: google-pub-sub-publish-api
- baseURL: https://pubsub.googleapis.com
  baseurl_source: spec
  description: Manage Pub/Sub schemas
  name: Google Pub/Sub Schemas API
  slug: google-pub-sub-schemas-api
- baseURL: https://pubsub.googleapis.com
  baseurl_source: spec
  description: Manage subscription snapshots
  name: Google Pub/Sub Snapshots API
  slug: google-pub-sub-snapshots-api
- baseURL: https://pubsub.googleapis.com
  baseurl_source: spec
  description: Pull and acknowledge messages
  name: Google Pub/Sub Subscribe API
  slug: google-pub-sub-subscribe-api
- baseURL: https://pubsub.googleapis.com
  baseurl_source: spec
  description: Manage Pub/Sub subscriptions
  name: Google Pub/Sub Subscriptions API
  slug: google-pub-sub-subscriptions-api
- baseURL: https://pubsub.googleapis.com
  baseurl_source: spec
  description: Manage Pub/Sub topics
  name: Google Pub/Sub Topics API
  slug: google-pub-sub-topics-api
artifact_total: 25
asyncapis:
- description: Google Cloud Pub/Sub is a fully managed real-time messaging service that allows you to send and receive messages between independent applications. This AsyncAPI spec describes the event-driven messagi
  name: Google Cloud Pub/Sub
  slug: google-pub-sub-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub Publish API
  slug: open-google-pub-sub-publish-api
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub Publish Schemas API
  slug: open-google-pub-sub-schemas-api
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub Publish Snapshots API
  slug: open-google-pub-sub-snapshots-api
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub Publish Subscribe API
  slug: open-google-pub-sub-subscribe-api
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub Publish Subscriptions API
  slug: open-google-pub-sub-subscriptions-api
- collection_type: open
  name: Google Pub/Sub Google Cloud Pub/Sub Publish Topics API
  slug: open-google-pub-sub-topics-api
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
overview: 'Google Pub/Sub publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Publish API, Schemas API, Snapshots API, and 3 more. Tagged areas include Cloud, Event-Driven, Google Cloud, Messaging, and Pub-Sub.


  The Google Pub/Sub catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Google Pub/Sub''s developer surface includes authentication, documentation, getting-started guide, pricing, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Google Pub Sub Plans Pricing
  plan_count: 3
  slug: google-pub-sub-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Google Pub Sub Rate Limits
  slug: google-pub-sub-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Google Pub/Sub API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: google-pub-sub-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Google Pub/Sub API Rules
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
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 68.5
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Pub-Sub
- Streaming
website: https://cloud.google.com/pubsub
---
