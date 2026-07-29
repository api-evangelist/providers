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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exegy-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exegy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/exegy-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.exegy.com/
- group: start
  title: ''
  type: Portal
  url: https://exegy.com/portal
- group: company
  title: ''
  type: Blog
  url: https://www.exegy.com/category/insights/
- group: operate
  title: ''
  type: Support
  url: https://www.exegy.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exegy.com/legal-patents-privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exegy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exegy
created: '2026-07-21'
description: Exegy is a St. Louis-based provider of low-latency market data infrastructure, trading platforms, and predictive trading signals for capital markets, backed by Marlin Equity Partners after its 2021 merger with Vela Trading Systems and subsequent acquisitions of Enyx and NovaSparks. The firm sells managed FPGA ticker plants (Exegy Nexus), software feed handlers (SMDS, nxFeed), the Axiom normalized data feed, the Metro options trading platform, and market access products (nxAccess, FrontTrade, SREX). Client access to normalized real-time and historical market data is delivered through the proprietary Exegy Client API (XCAPI), a C++/C#/Java library for Linux and Windows, while Metro exposes the Subway socket API and Freeway algorithmic API - none of which are publicly documented HTTP APIs. All developer documentation sits behind customer logins (Exegy Customer Portal, Object Trading DMA portal, MarketDataPeaks), making this an entirely sales-gated, entitlement-managed offering
  with no self-serve API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exegy.png
layout: provider
modified: '2026-07-22'
name: Exegy
nav: Providers
network: true
overview: 'Exegy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Trading, Real-Time, and Low Latency.


  Exegy''s developer surface includes developer portal, engineering blog, support, and 7 more developer resources.'
random_paper: 60
score:
  band: emerging
  composite: 13.3
  delta: -0.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exegy/refs/heads/main/screenshots/exegy-2026-07-22T202414.png
security:
- kind: domain-security
  name: Exegy Domain Security
  slug: exegy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: exegy
tags:
- Financial
- Market Data
- Trading
- Real-Time
- Low Latency
- FPGA
- Options
- Feed Handlers
- Order Book
website: https://www.exegy.com/
---
