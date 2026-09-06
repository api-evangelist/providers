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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Custom Laravel REST API for data.egov.bg with action-named endpoints under /api, almost all POST with JSON bodies. Public read methods include listDatasets, getDatasetDetails, listResources, getResour
  name: data.egov.bg REST API
  slug: rest
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-egov-bg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.egov.bg/
- group: docs
  title: ''
  type: Documentation
  url: https://data.egov.bg/document
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: data.egov.bg is the national government open-data portal for Bulgaria, operated by the Ministry of e-Government (Министерство на електронното управление). It is a custom Laravel application exposing a REST API with action-style endpoints (predominantly POST with JSON bodies) under the /api prefix. It is not CKAN. Public read endpoints require no key; write/admin endpoints require an api_key obtained via a free account.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-egov-bg.png
layout: provider
modified: '2026-06-23'
name: data.egov.bg (Open Data Portal of Bulgaria)
nav: Providers
network: true
overview: 'data.egov.bg (Open Data Portal of Bulgaria) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, Custom Platform, REST, Government Data, and National Government.


  data.egov.bg (Open Data Portal of Bulgaria)''s developer surface includes documentation and 3 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 1
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Data Egov Bg Domain Security
  slug: data-egov-bg-domain-security
  summary_line: TLSv1.2 · DMARC
slug: data-egov-bg
tags:
- Open Data
- Custom Platform
- REST
- Government Data
- National Government
- Bulgaria
- Europe
website: https://data.egov.bg/
---
