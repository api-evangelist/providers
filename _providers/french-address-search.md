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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Address search via the French Government
  name: French Address Search
  slug: french-address-search
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/french-address-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geo.api.gouv.fr/adresse
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://ghost.adresse.data.gouv.fr/rss/
created: '2026-05-28'
description: Address search via the French Government
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/french-address-search.png
layout: provider
modified: '2026-05-28'
name: French Address Search
nav: Providers
network: true
overview: 'French Address Search publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.


  French Address Search''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/french-address-search/refs/heads/main/screenshots/french-address-search-2026-06-20T181536.png
security:
- kind: domain-security
  name: French Address Search Domain Security
  slug: french-address-search-domain-security
  summary_line: TLSv1.3 · DMARC
slug: french-address-search
tags:
- Open Data
- Public APIs
website: https://geo.api.gouv.fr/adresse
---
