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
- description: CTS Realtime API
  name: CTS
  slug: cts
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.cts-strasbourg.eu/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: CTS Realtime API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cts.png
layout: provider
modified: '2026-05-28'
name: CTS
nav: Providers
network: true
overview: CTS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 104
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
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cts/refs/heads/main/screenshots/cts-2026-06-20T175323.png
security:
- kind: domain-security
  name: Cts Domain Security
  slug: cts-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cts
tags:
- Transportation
- Public APIs
website: https://api.cts-strasbourg.eu/
---
