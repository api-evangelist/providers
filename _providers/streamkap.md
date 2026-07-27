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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Streamkap Agentic Access
  operation_count: 32
  slug: streamkap-agentic-access
  summary_line: 32 operations · 17 acting
api_count: 9
apis:
- description: Obtain and refresh access tokens and manage credentials.
  name: Streamkap Authentication API
  slug: streamkap-authentication-api
- description: Discover available connector types.
  name: Streamkap Connectors API
  slug: streamkap-connectors-api
- description: Configure and manage sink destinations.
  name: Streamkap Destinations API
  slug: streamkap-destinations-api
- description: Manage Kafka users and permissions.
  name: Streamkap Kafka Access API
  slug: streamkap-kafka-access-api
- description: Manage CDC pipelines and their lifecycle.
  name: Streamkap Pipelines API
  slug: streamkap-pipelines-api
- description: Configure source connectors and snapshots.
  name: Streamkap Sources API
  slug: streamkap-sources-api
- description: Create and manage resource tags.
  name: Streamkap Tags API
  slug: streamkap-tags-api
- description: Manage underlying Kafka topics.
  name: Streamkap Topics API
  slug: streamkap-topics-api
- description: Deploy and manage in-stream transforms.
  name: Streamkap Transforms API
  slug: streamkap-transforms-api
artifact_total: 17
collections:
- collection_type: open
  name: Streamkap API
  slug: open-streamkap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/streamkap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/streamkap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamkap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streamkap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streamkap-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/streamkap
- group: company
  title: ''
  type: Website
  url: https://streamkap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamkap.com
- group: commercial
  title: ''
  type: Plans
  url: plans/streamkap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/streamkap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/streamkap-finops.yml
created: '2026-07-01'
description: Streamkap is a real-time streaming ETL and change data capture (CDC) platform built on Apache Kafka and Apache Flink. It streams data from operational databases (PostgreSQL, MySQL, MongoDB, SQL Server, Oracle) to cloud warehouses, lakes, and other destinations with sub-second latency, and its REST API lets teams provision and operate sources, destinations, pipelines, transforms, and Kafka access programmatically.
finops:
- name: Streamkap Finops
  service_category: Analytics
  slug: streamkap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streamkap.png
layout: provider
modified: '2026-07-01'
name: Streamkap
nav: Providers
network: true
overview: 'Streamkap publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Connectors API, Destinations API, and 6 more. Tagged areas include Streaming, ETL, CDC, Kafka, and Flink.


  Streamkap''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Streamkap Plans Pricing
  plan_count: 4
  slug: streamkap-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Streamkap Rate Limits
  slug: streamkap-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Streamkap Authentication
  slug: streamkap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Streamkap Domain Security
  slug: streamkap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Streamkap Trust Center
  slug: streamkap-trust-center
  summary_line: SOC 2, ISO 27001
slug: streamkap
tags:
- Streaming
- ETL
- CDC
- Kafka
- Flink
- Data Integration
- Real Time
website: https://streamkap.com/
---
