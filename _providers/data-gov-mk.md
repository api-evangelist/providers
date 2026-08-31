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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: CKAN Action API for data.gov.mk, a consistent JSON-over-HTTP interface over the national catalog. Standard actions include package_search, package_show, package_list, organization_list, group_list, an
  name: data.gov.mk CKAN Action API
  slug: catalog
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://data.gov.mk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: data.gov.mk is the national government open-data portal for North Macedonia, operated by the Ministry of Digital Transformation. It runs CKAN and exposes the standard CKAN Action API over roughly 280+ datasets from 50+ public institutions, supporting programmatic dataset search, metadata retrieval, and resource access, plus DCAT exports (N3, TTL, XML, JSON-LD).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-mk.png
layout: provider
modified: '2026-06-23'
name: data.gov.mk
nav: Providers
network: true
overview: 'data.gov.mk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  data.gov.mk''s developer surface includes documentation and 2 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 0.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: data-gov-mk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- North Macedonia
- Europe
website: https://data.gov.mk/
---
