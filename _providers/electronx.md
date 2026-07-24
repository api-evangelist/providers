---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'The ElectronX FIX API provides programmatic access to the exchange through three session types: Order Entry (submit, modify, cancel orders and receive execution reports), Market Data (real-time prices'
  name: ElectronX FIX API
  slug: electronx-fix-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electronx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.electronx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.electronx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.electronx.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.electronx.com/fix-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.electronx.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.electronx.com/news-insights-collections
- group: operate
  title: ''
  type: Support
  url: https://www.electronx.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.electronx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.electronx.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.electronx.com/regulatory
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/electronx-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/electronx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/electronx-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/electronx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/electronx-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/electronx-changelog.yml
created: '2026-07-17'
description: ElectronX is a CFTC-regulated financial exchange (Designated Contract Market) and clearinghouse (Derivatives Clearing Organization) operating the first U.S.-regulated, direct-access power derivatives market. It offers 1MW hourly bounded futures and binary options that let energy market participants hedge intraday electricity price volatility across ISOs including ERCOT, PJM, MISO, and CAISO. Traders connect through a browser-based platform or programmatically via a FIX API providing order entry, market data, and drop copy sessions. ElectronX is backed by DCVC and has raised more than $55M across seed and Series A rounds to democratize access to electricity risk-management tools for battery storage operators, distributed energy resource aggregators, trading firms, and commercial power consumers.
image: https://docs.electronx.com/assets/og/electronx-logo.jpg
layout: provider
modified: '2026-07-19'
name: Electronx
nav: Providers
network: true
overview: 'Electronx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Power Derivatives, and Trading.


  Electronx''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 10 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 32.1
  delta: 5.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 26.3
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Electronx Authentication
  slug: electronx-authentication
  summary_line: fix-session/mutualTLS · 2 schemes
- kind: domain-security
  name: Electronx Domain Security
  slug: electronx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: electronx
tags:
- Company
- Energy
- Electricity
- Power Derivatives
- Trading
- Exchange
- Financial Services
- FIX API
- Market Data
- Futures
- Options
- CFTC
website: https://www.electronx.com/
---
