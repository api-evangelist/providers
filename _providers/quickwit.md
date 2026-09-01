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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Quickwit Agentic Access
  operation_count: 26
  slug: quickwit-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quickwit REST Cluster API
  slug: open-quickwit-cluster-api
- collection_type: open
  name: Quickwit REST Cluster Delete Tasks API
  slug: open-quickwit-delete-tasks-api
- collection_type: open
  name: Quickwit REST Cluster Index Templates API
  slug: open-quickwit-index-templates-api
- collection_type: open
  name: Quickwit REST Cluster Indexes API
  slug: open-quickwit-indexes-api
- collection_type: open
  name: Quickwit REST Cluster Ingest API
  slug: open-quickwit-ingest-api
- collection_type: open
  name: Quickwit REST Cluster Search API
  slug: open-quickwit-search-api
- collection_type: open
  name: Quickwit REST Cluster Sources API
  slug: open-quickwit-sources-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/quickwit-oss/quickwit/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/quickwit-oss/quickwit/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/quickwit-oss/quickwit/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/quickwit-oss/quickwit/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/quickwit-oss/quickwit/blob/main/CONTRIBUTING.md
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
overview: 'Quickwit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Delete Tasks API, Index Templates API, and 4 more. Tagged areas include Search, Log Management, Observability, Full-Text Search, and Cloud-Native.


  Quickwit''s developer surface includes documentation, engineering blog, YouTube channel, pricing, and 17 more developer resources.'
plans:
- name: Quickwit Plans Pricing
  plan_count: 1
  slug: quickwit-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Quickwit Rate Limits
  slug: quickwit-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.9
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 63.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Cloud-Native
- Open-Source
- Distributed Tracing
- Analytics
website: https://quickwit.io/
---
