---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: uData REST API for data.gov.rs, a consistent JSON-over-HTTP interface over a catalog of roughly 3,452 datasets. Standard endpoints under /api/1/ include /datasets/ (search and listing), /organizations
  name: data.gov.rs uData REST API
  slug: catalog
- description: Paginated dataset search and listing endpoint returning dataset metadata, organizations, and resource references as JSON.
  name: data.gov.rs Datasets endpoint
  slug: datasets
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-rs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.rs/en/
- group: docs
  title: ''
  type: Documentation
  url: https://udata.readthedocs.io/en/stable/api/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: data.gov.rs is the national government open-data portal for the Republic of Serbia, operated by the Office for IT and eGovernment. It runs the uData platform and exposes the uData REST API over approximately 3,452 datasets, supporting programmatic dataset search, metadata retrieval, organization listings, and resource access. The API provides a consistent JSON-over-HTTP interface and is harvested into the EU data portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-rs.png
layout: provider
modified: '2026-06-23'
name: data.gov.rs
nav: Providers
network: true
overview: 'data.gov.rs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, uData, Data Catalog, DCAT, and Government Data.


  data.gov.rs'' developer surface includes documentation and 3 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 9.0
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-rs/refs/heads/main/screenshots/data-gov-rs-2026-07-25T211244.png
security:
- kind: domain-security
  name: Data Gov Rs Domain Security
  slug: data-gov-rs-domain-security
  summary_line: TLSv1.2
slug: data-gov-rs
tags:
- Open Data
- uData
- Data Catalog
- DCAT
- Government Data
- National Government
- Serbia
- Europe
website: https://data.gov.rs/en/
---
