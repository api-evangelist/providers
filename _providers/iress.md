---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'QuantFeed is Iress''s signature end-to-end ultra-low latency market data API. Built to deliver an unmatched level of performance and quality of normalisation, QuantFeed connects 240+ normalised market '
  name: Iress QuantFeed
  slug: iress-quantfeed
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iress-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iress
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iress
- group: company
  title: ''
  type: Website
  url: https://www.iress.com/
created: '2025-02-12'
description: Iress is a technology company providing software for financial markets, wealth management, and trading. Iress QuantFeed is a signature end-to-end ultra-low latency market data API that connects over 240 normalized market data feeds from 80+ sources.
finops:
- name: Iress Finops
  service_category: API
  slug: iress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iress.png
layout: provider
modified: '2026-04-28'
name: Iress
nav: Providers
network: true
overview: Iress publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Data, Market Data, Trading, and Wealth Management.
plans:
- name: Iress Plans Pricing
  plan_count: 3
  slug: iress-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 5
  name: Iress Rate Limits
  slug: iress-rate-limits
score:
  band: emerging
  composite: 18.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 18.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iress/refs/heads/main/screenshots/iress-2026-06-20T183604.png
security:
- kind: domain-security
  name: Iress Domain Security
  slug: iress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iress
tags:
- Financial Data
- Market Data
- Trading
- Wealth Management
website: https://www.iress.com/
---
