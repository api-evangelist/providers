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
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Bespoke REST API for opendata.gov.al at same-origin /api, with action-style routes. Known endpoints include POST /api/Dataset/filter (dataset search/listing), GET /api/Dataset/get/{slug}, GET /api/Dca
  name: Open Data Albania REST API
  slug: rest
- description: SPARQL query endpoint for the linked-data / DCAT-AP graph powering the portal.
  name: Open Data Albania SPARQL endpoint
  slug: sparql
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-gov-al-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.gov.al/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: opendata.gov.al is the national government open-data portal for Albania (Open Data Albania). It is a custom, DCAT-AP-compliant platform (an Angular single-page-app front end over a bespoke REST API) with a dedicated SPARQL query endpoint, and it is harvested into the EU data portal (data.europa.eu). It is not CKAN or DKAN. Read endpoints live under the /api prefix using PascalCase, action-style routes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-gov-al.png
layout: provider
modified: '2026-06-23'
name: opendata.gov.al (Open Data Albania)
nav: Providers
network: true
overview: opendata.gov.al (Open Data Albania) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, Custom Platform, DCAT-AP, SPARQL, and Linked Data.
random_paper: 31
score:
  band: minimal
  composite: 7.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-gov-al/refs/heads/main/screenshots/opendata-gov-al-2026-08-07T190550.png
security:
- kind: domain-security
  name: Opendata Gov Al Domain Security
  slug: opendata-gov-al-domain-security
  summary_line: TLSv1.2
slug: opendata-gov-al
tags:
- Open Data
- Custom Platform
- DCAT-AP
- SPARQL
- Linked Data
- Government Data
- National Government
- Albania
- Europe
website: https://opendata.gov.al/
---
