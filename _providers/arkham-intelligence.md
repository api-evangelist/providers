---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 16.5
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: Web application for searching, browsing, and analysing labelled onchain entities - wallets, exchanges, funds, projects - across supported blockchains. Powers visualisations, alerts, and watchlists use
  name: Arkham Platform
  slug: platform
- description: Marketplace where users post and claim bounties for deanonymising specific addresses or unmasking activity. Bounties are funded in ARKM and resolved by community submissions reviewed by Arkham.
  name: Arkham Intel Exchange (Dreadnought)
  slug: intel-exchange
- description: REST and WebSocket API for programmatic access to Arkham's entity dataset - resolve addresses to entities, fetch entity profiles, balances, holdings, counterparties, and transfers, plus a real-time `/
  name: Arkham Entity Intelligence API
  slug: entity-api
- description: Arkham's centralized crypto exchange - spot and perpetual futures trading, deposits, withdrawals, and integrated onchain intelligence on counterparties. Web and mobile clients front the matching engin
  name: Arkham Exchange
  slug: exchange-web
- description: REST API for Arkham Exchange covering public market data (symbols, tickers, order book, trades, klines) and authenticated trading and account endpoints (orders, positions, balances, withdrawals).
  name: Arkham Exchange API
  slug: exchange-api
- description: WebSocket API for Arkham Exchange streaming market data and private account events - real-time ticker, depth, trades, and order updates. The exchange WebSocket is referenced in third-party material at
  name: Arkham Exchange WebSocket API
  slug: exchange-websocket
artifact_total: 12
asyncapis:
- description: Real-time streaming of blockchain transfers from Arkham Intelligence. Clients subscribe with filter payloads (from, to, chains, tokens, usdGte) and receive matching transfer events as they are observe
  name: Arkham Intelligence Transfers WebSocket API
  slug: arkham-intelligence-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arkham-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arkhamintelligence.com/
- group: company
  title: ''
  type: Website
  url: https://info.arkm.com/
- group: other
  title: ''
  type: Platform
  url: https://platform.arkhamintelligence.com/
- group: other
  title: ''
  type: Exchange
  url: https://www.arkm.com/
- group: other
  title: ''
  type: Intel
  url: https://intel.arkm.com/
- group: other
  title: ''
  type: X
  url: https://x.com/ArkhamIntel
- group: company
  title: ''
  type: Blog
  url: https://info.arkm.com/blog
created: '2026-05-23'
description: Arkham operates two related products. Arkham Intelligence (the Arkham Platform / Intel) is an onchain entity intelligence service that labels wallets and contracts with real-world identities and exposes them through a web app, intel exchange (Dreadnought / bounties), and an API for entity lookups, address profiles, balances, and transaction history. Arkham Exchange (arkm.com) is a centralized crypto exchange that publishes a REST and WebSocket trading API for spot and perpetual markets. Both share the ARKM token and operate under the same parent.
finops:
- name: Arkham Intelligence Finops
  service_category: API
  slug: arkham-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arkham-intelligence.png
layout: provider
modified: '2026-05-29'
name: Arkham Intelligence
nav: Providers
network: true
overview: 'Arkham Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network: Arkham Entity Intelligence API. Tagged areas include Onchain Intelligence, Entity Resolution, Crypto Exchange, Trading, and Market Data.


  The Arkham Intelligence catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Arkham Intelligence''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Arkham Intelligence Plans Pricing
  plan_count: 1
  slug: arkham-intelligence-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Arkham Intelligence Rate Limits
  slug: arkham-intelligence-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Arkham Intelligence API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: arkham-intelligence-asyncapi-spectral-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 41.5
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 21.1
  previous_composite: 28.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arkham-intelligence/refs/heads/main/screenshots/arkham-intelligence-2026-06-20T172448.png
security:
- kind: domain-security
  name: Arkham Intelligence Domain Security
  slug: arkham-intelligence-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: arkham-intelligence
tags:
- Onchain Intelligence
- Entity Resolution
- Crypto Exchange
- Trading
- Market Data
- Crypto
- Web3
website: https://www.arkhamintelligence.com/
---
