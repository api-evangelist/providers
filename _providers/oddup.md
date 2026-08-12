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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oddup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oddup.com
- group: company
  title: ''
  type: Website
  url: https://oddup.app
created: '2026-07-17'
description: 'Oddup (now operating as Oddup Markets) is a Singapore-based platform founded in 2015 by James Giancotti. It began as a data-driven startup-rating and intelligence service — a 500 Global portfolio company scoring startups and crypto projects — and has since pivoted to prediction markets, letting users trade on real-world outcomes across crypto, FX, indices, and commodities using a distinctive Yes / No / Maybe outcome model. The current product is a client-side single-page web application hosted on Vercel at oddup.app (and oddup.com). As of this enrichment pass the live site is geo-restricted (HTTP 451, x-blocked-country: US) and exposes no public developer, API, documentation, or .well-known surface — no OpenAPI, no API subdomains, and no published packages were discoverable. This profile therefore captures verified company identity and a domain-security probe only; it will be re-enriched if a public API surface appears.'
image: https://oddup.app/favicon.png
layout: provider
modified: '2026-07-20'
name: Oddup
nav: Providers
network: true
overview: Oddup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Prediction Markets, Trading, Cryptocurrency, and Fintech.
random_paper: 76
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
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Oddup Domain Security
  slug: oddup-domain-security
  summary_line: TLSv1.3
slug: oddup
tags:
- Company
- Prediction Markets
- Trading
- Cryptocurrency
- Fintech
- Startup Intelligence
- Singapore
website: https://oddup.com
---
