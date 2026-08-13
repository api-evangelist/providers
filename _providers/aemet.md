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
api_count: 1
apis:
- description: Weather and forecast data from Spain
  name: Aemet
  slug: aemet
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aemet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.aemet.es/centrodedescargas/inicio
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Weather and forecast data from Spain
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aemet.png
layout: provider
modified: '2026-05-28'
name: Aemet
nav: Providers
network: true
overview: Aemet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 44
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aemet/refs/heads/main/screenshots/aemet-2026-06-20T165442.png
security:
- kind: domain-security
  name: Aemet Domain Security
  slug: aemet-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aemet
tags:
- Weather
- Public APIs
website: https://opendata.aemet.es/centrodedescargas/inicio
---
