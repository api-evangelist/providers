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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gridstatus Agentic Access
  operation_count: 25
  slug: gridstatus-agentic-access
  summary_line: 25 operations
api_count: 1
apis:
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: API name and version.
  name: Grid Status API Info API
  slug: gridstatus-api-info-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Usage and limits for the current user or organization.
  name: Grid Status API Usage API
  slug: gridstatus-api-usage-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Block-averaged prices for an ISO.
  name: Grid Status Block Pricing Data API
  slug: gridstatus-block-pricing-data-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Transmission constraints, binding activity, and shift factors.
  name: Grid Status Constraints API
  slug: gridstatus-constraints-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Bulk per-day CSV export files on S3.
  name: Grid Status CSV Exports API
  slug: gridstatus-csv-exports-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Ingest audit history for a dataset.
  name: Grid Status Dataset Audit API
  slug: gridstatus-dataset-audit-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: List datasets and fetch per-dataset metadata.
  name: Grid Status Dataset Metadata API
  slug: gridstatus-dataset-metadata-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Recent row insert/update activity for a dataset.
  name: Grid Status Dataset Updates API
  slug: gridstatus-dataset-updates-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Nodes, hubs, and zones behind LMP datasets.
  name: Grid Status Pricing Locations API
  slug: gridstatus-pricing-locations-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Query dataset rows with filters, resampling, and pagination.
  name: Grid Status Query Data API
  slug: gridstatus-query-data-api
- baseURL: https://api.gridstatus.io/v1
  baseurl_source: declared
  description: Daily peak reports (paid plans).
  name: Grid Status Reports API
  slug: gridstatus-reports-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grid Status API Info API
  slug: open-gridstatus-api-info-api
- collection_type: open
  name: Grid Status API Info API Usage API
  slug: open-gridstatus-api-usage-api
- collection_type: open
  name: Grid Status API Info Block Pricing Data API
  slug: open-gridstatus-block-pricing-data-api
- collection_type: open
  name: Grid Status API Info Constraints API
  slug: open-gridstatus-constraints-api
- collection_type: open
  name: Grid Status API Info CSV Exports API
  slug: open-gridstatus-csv-exports-api
- collection_type: open
  name: Grid Status API Info Dataset Audit API
  slug: open-gridstatus-dataset-audit-api
- collection_type: open
  name: Grid Status API Info Dataset Metadata API
  slug: open-gridstatus-dataset-metadata-api
- collection_type: open
  name: Grid Status API Info Dataset Updates API
  slug: open-gridstatus-dataset-updates-api
- collection_type: open
  name: Grid Status API Info Pricing Locations API
  slug: open-gridstatus-pricing-locations-api
- collection_type: open
  name: Grid Status API Info Query Data API
  slug: open-gridstatus-query-data-api
- collection_type: open
  name: Grid Status API Info Reports API
  slug: open-gridstatus-reports-api
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
random_paper: 6
rate_limits:
- limit_count: 7
  name: Gridstatus Rate Limits
  slug: gridstatus-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
website: https://www.gridstatus.io
---
