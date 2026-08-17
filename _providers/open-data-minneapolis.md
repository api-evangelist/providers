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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Spatial (GIS) and non-spatial city data for Minneapolis
  name: Open Data Minneapolis
  slug: open-data-minneapolis
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-data-minneapolis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-data-minneapolis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.minneapolismn.gov/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Spatial (GIS) and non-spatial city data for Minneapolis
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-data-minneapolis.png
layout: provider
modified: '2026-05-28'
name: Open Data Minneapolis
nav: Providers
network: true
overview: Open Data Minneapolis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 31
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
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-data-minneapolis/refs/heads/main/screenshots/open-data-minneapolis-2026-06-20T190743.png
security:
- kind: domain-security
  name: Open Data Minneapolis Domain Security
  slug: open-data-minneapolis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Open Data Minneapolis Vulnerability Disclosure
  slug: open-data-minneapolis-vulnerability-disclosure
  summary_line: disclosure policy published
slug: open-data-minneapolis
tags:
- Open Data
- Public APIs
website: https://opendata.minneapolismn.gov/
---
