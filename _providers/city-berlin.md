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
- description: Berlin(DE) City Open Data
  name: City, Berlin
  slug: city-berlin
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/city-berlin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/city-berlin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daten.berlin.de/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Berlin(DE) City Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/city-berlin.png
layout: provider
modified: '2026-05-28'
name: City, Berlin
nav: Providers
network: true
overview: City, Berlin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 78
score:
  band: minimal
  composite: 8.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: City Berlin Domain Security
  slug: city-berlin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: City Berlin Vulnerability Disclosure
  slug: city-berlin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: city-berlin
tags:
- Government
- Public APIs
website: https://daten.berlin.de/
---
