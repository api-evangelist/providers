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
- acting_count: 0
  human_in_the_loop: 0
  name: Gridstatus Agentic Access
  operation_count: 25
  slug: gridstatus-agentic-access
  summary_line: 25 operations
api_count: 11
apis:
- description: API name and version.
  name: Grid Status API Info API
  slug: gridstatus-api-info-api
- description: Usage and limits for the current user or organization.
  name: Grid Status API Usage API
  slug: gridstatus-api-usage-api
- description: Block-averaged prices for an ISO.
  name: Grid Status Block Pricing Data API
  slug: gridstatus-block-pricing-data-api
- description: Transmission constraints, binding activity, and shift factors.
  name: Grid Status Constraints API
  slug: gridstatus-constraints-api
- description: Bulk per-day CSV export files on S3.
  name: Grid Status CSV Exports API
  slug: gridstatus-csv-exports-api
- description: Ingest audit history for a dataset.
  name: Grid Status Dataset Audit API
  slug: gridstatus-dataset-audit-api
- description: List datasets and fetch per-dataset metadata.
  name: Grid Status Dataset Metadata API
  slug: gridstatus-dataset-metadata-api
- description: Recent row insert/update activity for a dataset.
  name: Grid Status Dataset Updates API
  slug: gridstatus-dataset-updates-api
- description: Nodes, hubs, and zones behind LMP datasets.
  name: Grid Status Pricing Locations API
  slug: gridstatus-pricing-locations-api
- description: Query dataset rows with filters, resampling, and pagination.
  name: Grid Status Query Data API
  slug: gridstatus-query-data-api
- description: Daily peak reports (paid plans).
  name: Grid Status Reports API
  slug: gridstatus-reports-api
artifact_total: 18
collections:
- collection_type: open
  name: Grid Status API
  slug: open-gridstatus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gridstatus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridstatus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gridstatus-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gridstatus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grid-status
- group: company
  title: ''
  type: Website
  url: https://www.gridstatus.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gridstatus.io
- group: commercial
  title: ''
  type: Plans
  url: plans/gridstatus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gridstatus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gridstatus-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.gridstatus.io/rss/
created: '2026-07-11'
description: Grid Status is a United States electricity grid and power market data platform. The hosted Grid Status API (api.gridstatus.io) exposes hundreds of curated datasets - day-ahead and real-time LMP and settlement point prices, load and load forecasts, fuel mix, ancillary services, storage, and transmission constraints - across CAISO, ERCOT, PJM, MISO, NYISO, SPP, ISONE, and IESO through a uniform dataset query model authenticated with an API key. Grid Status also maintains the open-source gridstatus Python library (BSD-3-Clause) for pulling raw data directly from ISO/RTO sources, and the gridstatusio client for the hosted API.
finops:
- name: Gridstatus Finops
  service_category: Analytics and Data
  slug: gridstatus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gridstatus.png
layout: provider
modified: '2026-07-11'
name: Grid Status
nav: Providers
network: true
overview: 'Grid Status publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Info API, API Usage API, Block Pricing Data API, and 8 more. Tagged areas include Day-Ahead Prices, Electricity, Grid Data, Energy Markets, and LMP.


  Grid Status'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Gridstatus Plans Pricing
  plan_count: 4
  slug: gridstatus-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 7
  name: Gridstatus Rate Limits
  slug: gridstatus-rate-limits
score:
  band: thin
  composite: 42.4
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.6
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gridstatus/refs/heads/main/screenshots/gridstatus-2026-07-25T220330.png
security:
- kind: authentication
  name: Gridstatus Authentication
  slug: gridstatus-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Gridstatus Domain Security
  slug: gridstatus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gridstatus
tags:
- Day-Ahead Prices
- Electricity
- Grid Data
- Energy Markets
- LMP
- Load
- Fuel Mix
- Open Source
website: https://www.gridstatus.io
---
