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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The US Census Bureau provides various APIs and data sets on demographics and businesses
  name: Census.gov
  slug: censusgov
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/census-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.census.gov/data/developers/data-sets.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: The US Census Bureau provides various APIs and data sets on demographics and businesses
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/census-gov.png
layout: provider
modified: '2026-05-28'
name: Census.gov
nav: Providers
network: true
overview: Census.gov publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 106
score:
  band: minimal
  composite: 6.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/census-gov/refs/heads/main/screenshots/census-gov-2026-06-20T174118.png
security:
- kind: domain-security
  name: Census Gov Domain Security
  slug: census-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: census-gov
tags:
- Government
- Public APIs
website: https://www.census.gov/data/developers/data-sets.html
---
