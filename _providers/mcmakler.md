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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcmakler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mcmakler.de/
created: '2026-07-17'
description: McMakler is a German hybrid residential real-estate brokerage (proptech) headquartered in Berlin, combining local human agents with in-house technology to list, market, and sell homes across Germany, Austria, and France. It was surfaced as a portfolio company of balderton-capital and added to the API Evangelist network as a stub for enrichment. An enrichment pass on 2026-07-20 probed the public surface and found no public developer API, developer portal, documentation, or well-known discovery catalog; an internal backend host (api.mcmakler.de) exists but returns 403 and is not a published API. Domain transport/email security was probed and recorded.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcmakler.png
layout: provider
modified: '2026-07-20'
name: mcmakler
nav: Providers
network: true
overview: mcmakler is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Proptech, Germany, and Brokerage.
random_paper: 99
score:
  band: minimal
  composite: 5.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mcmakler/refs/heads/main/screenshots/mcmakler-2026-08-07T172248.png
security:
- kind: domain-security
  name: Mcmakler Domain Security
  slug: mcmakler-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mcmakler
tags:
- Company
- Real Estate
- Proptech
- Germany
- Brokerage
- Housing
website: https://www.mcmakler.de/
---
