---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Quickwit Agentic Access
  operation_count: 26
  slug: quickwit-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Monitor cluster state and node health
  name: Quickwit Cluster API
  slug: quickwit-cluster-api
- description: Remove documents matching queries from indexes
  name: Quickwit Delete Tasks API
  slug: quickwit-delete-tasks-api
- description: Manage index templates for automatic index creation
  name: Quickwit Index Templates API
  slug: quickwit-index-templates-api
- description: Create, update, retrieve, and manage search indexes
  name: Quickwit Indexes API
  slug: quickwit-indexes-api
- description: Add documents to indexes via NDJSON format
  name: Quickwit Ingest API
  slug: quickwit-ingest-api
- description: Query documents across indexes using full-text and aggregation queries
  name: Quickwit Search API
  slug: quickwit-search-api
- description: Configure data sources such as Kafka, Kinesis, and Pulsar
  name: Quickwit Sources API
  slug: quickwit-sources-api
artifact_total: 12
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/quickwit-oss/quickwit/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quickwit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quickwit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quickwit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://quickwit.io/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/quickwit-oss
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/quickwit-oss/quickwit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quickwit-inc/
- group: company
  title: ''
  type: Blog
  url: https://quickwit.io/blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/quickwit_inc
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/MT27AG5EVE
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@quickwit8103
- group: commercial
  title: ''
  type: Pricing
  url: https://quickwit.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/quickwit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quickwit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quickwit-finops.yml
created: '2026-06-13'
description: Cloud-native search engine for log management and full-text search with a REST API for indexing documents, running queries, and managing search indexes at petabyte scale. Quickwit decouples compute from storage, enabling sub-second search and analytics directly on cloud object storage (S3, GCS, Azure Blob). It is open-source (Apache 2.0), written in Rust, and supports OpenTelemetry, Jaeger tracing, and an Elasticsearch-compatible API. Quickwit joined Datadog in January 2025.
finops:
- name: Quickwit Finops
  service_category: ''
  slug: quickwit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quickwit.png
layout: provider
modified: '2026-06-13'
name: Quickwit
nav: Providers
network: true
overview: 'Quickwit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Delete Tasks API, Index Templates API, and 4 more. Tagged areas include Search, Log Management, Observability, Full-Text Search, and Cloud Native.


  Quickwit''s developer surface includes documentation, engineering blog, YouTube channel, pricing, and 12 more developer resources.'
plans:
- name: Quickwit Plans Pricing
  plan_count: 1
  slug: quickwit-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 4
  name: Quickwit Rate Limits
  slug: quickwit-rate-limits
score:
  band: thin
  composite: 36.0
  delta: 0.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.5
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quickwit/refs/heads/main/screenshots/quickwit-2026-06-20T192434.png
security:
- kind: domain-security
  name: Quickwit Domain Security
  slug: quickwit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: quickwit
tags:
- Search
- Log Management
- Observability
- Full-Text Search
- Cloud Native
- Open Source
- Distributed Tracing
- Analytics
website: https://quickwit.io/
---
