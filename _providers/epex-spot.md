---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 4
apis:
- description: 'Read-only API subscription (Day-Ahead and pan-EU Intraday API Read-only, EUR 1,040.00/month for internal usage) delivering day-ahead and intraday auction results - prices and volumes - for all market '
  name: EPEX SPOT Day-Ahead and Intraday Auction Market Data API
  slug: epex-spot-day-ahead-intraday-auction-market-data-api
- description: Read-only API subscription (Continuous API Read-only, EUR 3,360.00/month for internal usage) giving real-time access to production data - all trades and orders - on the continuous intraday market oper
  name: EPEX SPOT Continuous Intraday Market Data API
  slug: epex-spot-continuous-intraday-market-data-api
- description: Member trading API for the Multiple Auction Trading System (MATS), the platform that replaced the legacy ETS system for all EPEX SPOT auction markets. Supports submission of linear, block, scalable co
  name: EPEX SPOT MATS Auction Trading API
  slug: epex-spot-mats-auction-trading-api
- description: Member trading API for the M7 trading system that runs all EPEX SPOT continuous intraday markets. Clients exchange standardized messages with M7 over an AMQP (Advanced Message Queuing Protocol) server
  name: EPEX SPOT M7 Intraday Trading API
  slug: epex-spot-m7-intraday-trading-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epex-spot-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epex-spot
- group: company
  title: ''
  type: Website
  url: https://www.epexspot.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.epexspot.com/en/marketdataservices
- group: other
  title: ''
  type: Downloads
  url: https://www.epexspot.com/en/downloads
- group: other
  title: ''
  type: MarketResults
  url: https://www.epexspot.com/en/market-results
- group: commercial
  title: ''
  type: Pricing
  url: https://webshop.eex-group.com/epex-spot-public-market-data
- group: commercial
  title: ''
  type: Plans
  url: plans/epex-spot-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.epexspot.com/en/news
created: '2026-07-11'
description: EPEX SPOT SE, the European Power Exchange, operates the organised short-term electricity markets across thirteen European countries - day-ahead and intraday auctions on the MATS trading system and continuous intraday trading on the M7 trading system. Day-ahead prices set on EPEX SPOT are the reference for much of the European power sector. EPEX SPOT exposes real machine-readable interfaces, but none of them are open self-serve APIs - trading APIs (MATS, M7) require exchange membership, and read-only market data APIs and SFTP file feeds require a paid Market Data Services subscription ordered through the EEX Group Webshop.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epex-spot.png
layout: provider
modified: '2026-07-11'
name: EPEX SPOT
nav: Providers
network: true
overview: 'EPEX SPOT publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Day-Ahead Prices, Electricity, Energy Markets, Power Exchange, and Intraday Trading.


  EPEX SPOT''s developer surface includes documentation, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Epex Spot Plans Pricing
  plan_count: 10
  slug: epex-spot-plans-pricing
random_paper: 53
score:
  band: emerging
  composite: 15.7
  delta: -2.7
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Epex Spot Domain Security
  slug: epex-spot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: epex-spot
tags:
- Day-Ahead Prices
- Electricity
- Energy Markets
- Power Exchange
- Intraday Trading
- Market Data
- Auctions
- Europe
website: https://www.epexspot.com
---
