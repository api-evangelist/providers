---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.ledgerx.com
  baseurl_source: declared
  description: Public and authenticated REST API on api.ledgerx.com covering exchange contracts, traded contracts, contract tickers, positions, trades (own and global), upcoming exchange holidays and account balance
  name: MIAXdx Market Data and Account API
  slug: market-data
- description: Authenticated order-entry REST API on trade.ledgerx.com for listing resting limit orders, placing orders, cancelling a single order or all orders for an MPID, atomically cancel-replacing an order, and
  name: MIAXdx Trading API
  slug: trading
artifact_total: 6
asyncapis:
- description: WebSocket market data and account feed for MIAX Derivatives Exchange (LedgerX). NOT A PROVIDER-PUBLISHED SPEC. MIAXdx publishes no AsyncAPI document. This description was derived by API Evangelist fro
  name: MIAXdx (LedgerX) Market Data Feed
  slug: ledgerx-market-data-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://app.ledgerx.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.miaxdx.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.miaxdx.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.miaxdx.com/docs/api-key
- group: operate
  title: ''
  type: Support
  url: https://support.miaxdx.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.ledgerx.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.miaxdx.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ledgerx-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ledgerx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ledgerx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ledgerx-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ledgerx-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ledgerx-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ledgerx-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ledgerx-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ledgerx-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/ledgerx-market-data-asyncapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/ledgerx-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ledgerx-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ledgerx-domain-security.yml
created: '2026-07-17'
description: LedgerX LLC, doing business as MIAX Derivatives Exchange (MIAXdx), is a CFTC-regulated derivatives venue registered as a Designated Contract Market (DCM), Swap Execution Facility (SEF) and Derivatives Clearing Organization (DCO). Founded in 2014 under Ledger Holdings Inc. and backed by GV and Lightspeed Venture Partners, it pioneered physically settled, federally regulated Bitcoin options and swaps for institutional and retail traders. Ledger Holdings was acquired by West Realm Shires (FTX.US) in 2021; after the FTX bankruptcy, Miami International Holdings acquired MIAXdx in May 2023, and in November 2025 MIAX agreed to sell 90% of the exchange to Robinhood Markets in partnership with Susquehanna International Group. The exchange published a public REST API for contracts, positions, trades, balances and order entry, plus a WebSocket market data feed carrying action reports, top-of-book updates and exchange heartbeats, authenticated with JWT API keys. Its physically settled DCM/SEF
  products were delisted in July 2024 and the public developer surface (docs, api and trade hosts, status page) is currently unreachable or inactive.
image: https://app.ledgerx.com/icon-192x192.png
layout: provider
modified: '2026-07-19'
name: LedgerX (MIAX Derivatives Exchange)
nav: Providers
network: true
overview: 'LedgerX (MIAX Derivatives Exchange) publishes 1 API on the [APIs.io](https://apis.io/) network: MIAXdx Market Data and Account API. Tagged areas include Company, Enterprise, Financial-Services, Derivatives, and Trading.


  The LedgerX (MIAX Derivatives Exchange) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LedgerX (MIAX Derivatives Exchange)''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 13 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Ledgerx Rate Limits
  slug: ledgerx-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 44.8
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 33.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 36.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ledgerx/refs/heads/main/screenshots/ledgerx-2026-07-25T224817.png
security:
- kind: authentication
  name: Ledgerx Authentication
  slug: ledgerx-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ledgerx Domain Security
  slug: ledgerx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ledgerx
tags:
- Company
- Enterprise
- Financial-Services
- Derivatives
- Trading
- Cryptocurrency
- Bitcoin
- Exchange
- Market Data
- WebSockets
- Regulated Markets
website: https://app.ledgerx.com
---
