---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Real-time datafeeds (OMD-C SS, SP, SF tiers) for all securities traded on the Stock Exchange of Hong Kong, published in a proprietary binary message format over one-to-many IP multicast/UDP for high t
  name: HKEX Orion Market Data Platform - Securities Market (OMD-C)
  slug: hkex-orion-market-data-securities-omd-c
- description: Real-time datafeeds (OMD-D DS, DP, DF tiers) for futures and options traded on the Hong Kong Futures Exchange, delivered in binary format over IP multicast/UDP with separate channel sets for stock opt
  name: HKEX Orion Market Data Platform - Derivatives Market (OMD-D)
  slug: hkex-orion-market-data-derivatives-omd-d
- description: Web-based storefront for HKEX historical and reference data straight from the exchange - historical full order book tick data for securities and derivatives (CSV), CCASS shareholding data, and securit
  name: HKEX Data Marketplace Historical Data
  slug: hkex-data-marketplace-historical-data
- description: The FINI (Fast Interface for New Issuance) API Gateway offers RESTful JSON endpoints (e.g. GET /api/ipos/list/v1, GET /api/ipos/refdata/v1) for market participants to automate IPO workflows - IPO refe
  name: HKEX FINI API
  slug: hkex-fini-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/hkex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hkex-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hkex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hkex-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hkex-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hkex-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hkex-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hkex-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hkex-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hkex-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hkex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hkex.com.hk/
- group: start
  title: ''
  type: Portal
  url: https://data.hkex.com.hk/catalog
- group: docs
  title: ''
  type: Documentation
  url: https://www.hkex.com.hk/Services/Market-Data-Services?sc_lang=en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hkex
- group: company
  title: ''
  type: Blog
  url: https://www.hkexgroup.com/Media-Centre/Insight?sc_lang=en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hkex.com.hk/Services/Rules-and-Forms-and-Fees/Fees/Overview?sc_lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hkex.com.hk/Global/Exchange/Terms-of-Use?sc_lang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hkex.com.hk/Global/Exchange/HKEX-Privacy-Notices?sc_lang=en
- group: operate
  title: ''
  type: Support
  url: https://www.hkex.com.hk/Global/Exchange/Contact?sc_lang=en
created: '2026-07-21'
description: HKEX (Hong Kong Exchanges and Clearing Limited, SEHK 388) operates the Stock Exchange of Hong Kong, the Hong Kong Futures Exchange, and their clearing houses, and also owns the London Metal Exchange. As an exchange data arm it sells real-time securities and derivatives market data through the sales-gated HKEX Orion Market Data (OMD) platform - binary multicast datafeeds licensed to vendors and subscribers rather than a self-serve HTTP API - plus historical tick, full order book, and CCASS shareholding reference data through the HKEX Data Marketplace, delivered via SFTP, cloud-to-cloud transfer, and direct download. Its one publicly documented RESTful JSON API is the FINI API Gateway for IPO settlement workflows, restricted to registered market participants using OAuth 2.0 JWT credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hkex.png
layout: provider
modified: '2026-07-22'
name: HKEX
nav: Providers
network: true
overview: 'HKEX publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Stocks, Derivatives, and Exchange.


  HKEX''s developer surface includes authentication, changelog, developer portal, documentation, engineering blog, pricing, support, and 13 more developer resources.'
random_paper: 37
rate_limits:
- limit_count: 2
  name: Hkex Rate Limits
  slug: hkex-rate-limits
scopes:
- name: Hkex Scopes
  scope_count: 0
  slug: hkex-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.5
  delta: -1.7
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 34.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hkex/refs/heads/main/screenshots/hkex-2026-07-22T202427.png
security:
- kind: authentication
  name: Hkex Authentication
  slug: hkex-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hkex Domain Security
  slug: hkex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hkex
tags:
- Financial
- Market Data
- Stocks
- Derivatives
- Exchange
- Real-Time
- Historical Data
- Order Book
- Reference Data
- IPO
website: https://www.hkex.com.hk/
---
