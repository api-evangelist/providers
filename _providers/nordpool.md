---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nordpool Agentic Access
  operation_count: 59
  slug: nordpool-agentic-access
  summary_line: 59 operations
api_count: 10
apis:
- description: WebSocket API for continuous intraday power trading - clients speak STOMP over secure WebSocket (port 443) to parallel Market Data and Trading services for streaming contracts, order books, and capaci
  name: Nord Pool Intraday Trading API
  slug: nordpool-intraday-trading-api
- description: JSON REST API for day-ahead auction trading - integrated order submission and trade capture across the Nordic and Baltic auctions, CWE auctions, Poland, the GB Half Hourly Auction, and SEM-GB intraday
  name: Nord Pool Auction API
  slug: nordpool-auction-trading-api
- description: The Auction API from Nord Pool — 14 operation(s) for auction.
  name: Nord Pool Auction API
  slug: nordpool-auction-api
- description: The BalanceMarket API from Nord Pool — 2 operation(s) for balancemarket.
  name: Nord Pool BalanceMarket API
  slug: nordpool-balancemarket-api
- description: Public day-ahead auction prices and price indices.
  name: Nord Pool Day-Ahead Prices API
  slug: nordpool-day-ahead-prices-api
- description: The ExchangeRate API from Nord Pool — 2 operation(s) for exchangerate.
  name: Nord Pool ExchangeRate API
  slug: nordpool-exchangerate-api
- description: The Intraday API from Nord Pool — 17 operation(s) for intraday.
  name: Nord Pool Intraday API
  slug: nordpool-intraday-api
- description: The PowerSystem API from Nord Pool — 17 operation(s) for powersystem.
  name: Nord Pool PowerSystem API
  slug: nordpool-powersystem-api
- description: The PriceCurves API from Nord Pool — 1 operation(s) for pricecurves.
  name: Nord Pool PriceCurves API
  slug: nordpool-pricecurves-api
- description: The System API from Nord Pool — 4 operation(s) for system.
  name: Nord Pool System API
  slug: nordpool-system-api
artifact_total: 30
asyncapis:
- description: Nord Pool's Intraday Trading API is a genuine WebSocket API. Clients open secure WebSocket connections (port 443) and speak STOMP over them to two web services - a Market Data service (public market d
  name: Nord Pool Intraday Trading API (WebSocket/STOMP)
  slug: nordpool-intraday-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction API
  slug: open-nordpool-auction-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction BalanceMarket API
  slug: open-nordpool-balancemarket-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction Day-Ahead Prices API
  slug: open-nordpool-day-ahead-prices-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction ExchangeRate API
  slug: open-nordpool-exchangerate-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction Intraday API
  slug: open-nordpool-intraday-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction PowerSystem API
  slug: open-nordpool-powersystem-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction PriceCurves API
  slug: open-nordpool-pricecurves-api
- collection_type: open
  name: Nord Pool Data Portal API (Public) Auction System API
  slug: open-nordpool-system-api
- collection_type: open
  name: Nord Pool Market Data API
  slug: open-nordpool
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nordpool-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nordpool-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nordpool-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nordpool-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nordpool-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.nordpoolgroup.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.nordpoolgroup.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nord-pool
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NordPool
- group: docs
  title: ''
  type: Documentation
  url: https://www.nordpoolgroup.com/en/trading/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/nordpool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nordpool-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nordpool-finops.yml
created: '2026-07-11'
description: Nord Pool, part of the Euronext group, operates Europe's leading power exchange, running day-ahead auctions and continuous intraday electricity markets across the Nordics, Baltics, Central Western Europe, and the UK. Its Market Data API delivers day-ahead prices, kWh-level electricity rates by bidding area, volumes, capacities, flows, and power system data, while WebSocket and REST trading APIs serve exchange members.
finops:
- name: Nordpool Finops
  service_category: Market Data and Financial Services
  slug: nordpool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nordpool.png
layout: provider
modified: '2026-07-11'
name: Nord Pool
nav: Providers
network: true
overview: 'Nord Pool publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Intraday Trading API, Auction API, BalanceMarket API, and 6 more. Tagged areas include Day-Ahead Prices, Electricity, Energy Markets, Power Exchange, and Intraday Trading.


  The Nord Pool catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nord Pool''s developer surface includes authentication, developer portal, documentation, and 10 more developer resources.'
plans:
- name: Nordpool Plans Pricing
  plan_count: 5
  slug: nordpool-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Nordpool Rate Limits
  slug: nordpool-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Nord Pool API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: nordpool-asyncapi-spectral-rules
scopes:
- name: Nordpool Scopes
  scope_count: 1
  slug: nordpool-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 60.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 47.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nordpool/refs/heads/main/screenshots/nordpool-2026-08-07T185517.png
security:
- kind: authentication
  name: Nordpool Authentication
  slug: nordpool-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nordpool Domain Security
  slug: nordpool-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nordpool Vulnerability Disclosure
  slug: nordpool-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nordpool
tags:
- Day-Ahead Prices
- Electricity
- Energy Markets
- Power Exchange
- Intraday Trading
- Market Data
- Europe
website: https://www.nordpoolgroup.com/
---
