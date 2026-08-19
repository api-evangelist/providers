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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Public access to a database of IIN/BIN information
  name: Binlist
  slug: binlist
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/binlist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://binlist.net/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Public access to a database of IIN/BIN information
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/binlist.png
layout: provider
modified: '2026-05-28'
name: Binlist
nav: Providers
network: true
overview: Binlist publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 12
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/binlist/refs/heads/main/screenshots/binlist-2026-06-20T173247.png
security:
- kind: domain-security
  name: Binlist Domain Security
  slug: binlist-domain-security
  summary_line: TLSv1.3
slug: binlist
tags:
- Finance
- Public APIs
website: https://binlist.net/
---
