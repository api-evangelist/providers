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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
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
random_paper: 4
score:
  band: minimal
  composite: 9.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
