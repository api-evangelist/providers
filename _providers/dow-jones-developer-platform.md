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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Dow Jones Developer Platform provides developers with access to Dow Jones' news, business intelligence, and market data through a catalog of APIs and data feeds. It supports use cases across newsr
  name: Dow Jones Developer Platform
  slug: dow-jones-developer-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dow-jones-developer-platform-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dowjones
- group: company
  title: ''
  type: Website
  url: https://www.dowjones.com
- group: other
  title: ''
  type: Developer
  url: https://developer.dowjones.com/
created: '2025-03-01'
description: Dow Jones is a financial news and information provider that publishes The Wall Street Journal, Barron's, MarketWatch, and Financial News, and operates a portfolio of professional information services including Factiva, Dow Jones Newswires, and Dow Jones Risk and Compliance. The Dow Jones Developer Platform exposes APIs and data services that give developers programmatic access to Dow Jones content, market data, company and people intelligence, and risk and compliance datasets.
finops:
- name: Dow Jones Developer Platform Finops
  service_category: API
  slug: dow-jones-developer-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dow-jones-developer-platform.png
layout: provider
modified: '2026-04-28'
name: Dow Jones Developer Platform
nav: Providers
network: true
overview: Dow Jones Developer Platform publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Data, Financial, Market Data, News, and Risk and Compliance.
plans:
- name: Dow Jones Developer Platform Plans Pricing
  plan_count: 3
  slug: dow-jones-developer-platform-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Dow Jones Developer Platform Rate Limits
  slug: dow-jones-developer-platform-rate-limits
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dow-jones-developer-platform/refs/heads/main/screenshots/dow-jones-developer-platform-2026-06-20T180207.png
security:
- kind: domain-security
  name: Dow Jones Developer Platform Domain Security
  slug: dow-jones-developer-platform-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dow-jones-developer-platform
tags:
- Business Data
- Financial
- Market Data
- News
- Risk and Compliance
website: https://www.dowjones.com
---
