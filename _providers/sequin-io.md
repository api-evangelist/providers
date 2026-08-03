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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Sequin Io Agentic Access
  operation_count: 25
  slug: sequin-io-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 5
apis:
- description: Replay existing Postgres rows into a sink.
  name: Sequin Backfills API
  slug: sequin-io-backfills-api
- description: Reusable HTTP endpoint destinations used by webhook sinks.
  name: Sequin HTTP Endpoints API
  slug: sequin-io-http-endpoints-api
- description: Source Postgres database connections Sequin replicates from.
  name: Sequin Postgres Databases API
  slug: sequin-io-postgres-databases-api
- description: Destinations that stream Postgres changes to external systems.
  name: Sequin Sink Consumers API
  slug: sequin-io-sink-consumers-api
- description: HTTP pull consumption for the Sequin Stream sink.
  name: Sequin Stream Pull API
  slug: sequin-io-stream-pull-api
artifact_total: 12
collections:
- collection_type: open
  name: Sequin Management API
  slug: open-sequin-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sequin-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sequin-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sequin-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sequinstream
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sequin-io
- group: company
  title: ''
  type: Website
  url: https://sequinstream.com
- group: docs
  title: ''
  type: Documentation
  url: https://sequinstream.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/sequin-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sequin-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sequin-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.sequinstream.com/feed
created: '2026-07-01'
description: Sequin is an open-source Postgres change data capture (CDC) engine that streams Postgres rows and changes to streams, queues, and search indexes - Kafka, SQS, SNS, Kinesis, Redis, NATS, RabbitMQ, Elasticsearch, Typesense, GCP Pub/Sub, Azure Event Hubs, and HTTP/webhook endpoints - with exactly-once processing, backfills, and low-latency delivery. Sequin is self-hostable and also available as Sequin Cloud. Resources are configured declaratively via a sequin.yaml file or programmatically through the Management API; consumers can pull changes over HTTP via the Sequin Stream sink.
finops:
- name: Sequin Io Finops
  service_category: Analytics and Data Streaming
  slug: sequin-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sequin-io.png
layout: provider
modified: '2026-07-01'
name: Sequin
nav: Providers
network: true
overview: 'Sequin publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Backfills API, HTTP Endpoints API, Postgres Databases API, and 2 more. Tagged areas include Change Data Capture, CDC, Postgres, Streaming, and Open Source.


  Sequin''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sequin Io Plans Pricing
  plan_count: 4
  slug: sequin-io-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Sequin Io Rate Limits
  slug: sequin-io-rate-limits
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Sequin Io Authentication
  slug: sequin-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sequin Io Domain Security
  slug: sequin-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sequin-io
tags:
- Change Data Capture
- CDC
- Postgres
- Streaming
- Open Source
- Data Pipeline
website: https://sequinstream.com
---
