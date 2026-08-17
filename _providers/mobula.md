---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mobula Agentic Access
  operation_count: 11
  slug: mobula-agentic-access
  summary_line: 11 operations
api_count: 4
apis:
- description: Real-time and historical market data for tokens and assets.
  name: Mobula Market API
  slug: mobula-market-api
- description: Asset and token metadata.
  name: Mobula Metadata API
  slug: mobula-metadata-api
- description: Universal search and filterable market queries.
  name: Mobula Search API
  slug: mobula-search-api
- description: Multichain wallet portfolio, history, and transactions.
  name: Mobula Wallet API
  slug: mobula-wallet-api
artifact_total: 18
asyncapis:
- description: AsyncAPI 2.6 description of Mobula's real-time WebSocket feed at `wss://api.mobula.io`. Unlike the SSE-only providers, Mobula publishes a genuine bidirectional WebSocket surface. A client opens a WebS
  name: Mobula Realtime Feed (WebSocket)
  slug: mobula-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mobula Market API
  slug: open-mobula-market-api
- collection_type: open
  name: Mobula Market Metadata API
  slug: open-mobula-metadata-api
- collection_type: open
  name: Mobula Market Search API
  slug: open-mobula-search-api
- collection_type: open
  name: Mobula Market Wallet API
  slug: open-mobula-wallet-api
- collection_type: open
  name: Mobula API
  slug: open-mobula
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mobula-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobula-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mobula-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mobula-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mobula
- group: company
  title: ''
  type: Website
  url: https://mobula.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mobula.io
- group: commercial
  title: ''
  type: Plans
  url: plans/mobula-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mobula-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mobula-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.mobula.io/feed
created: '2026-07-01'
description: Mobula is an onchain-native crypto and web3 market data provider. Its REST and WebSocket APIs serve real-time and historical token prices, asset and token metadata, trading pairs and OHLCV candles, and multichain wallet portfolio, net-worth history, and transaction data across EVM, Solana, TON, and other chains, all keyed off a single free API key.
finops:
- name: Mobula Finops
  service_category: Analytics and Data
  slug: mobula-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mobula.png
layout: provider
modified: '2026-07-01'
name: Mobula
nav: Providers
network: true
overview: 'Mobula publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Market API, Metadata API, Search API, and 1 more. Tagged areas include Crypto, Web3, Market Data, Blockchain, and Wallet.


  The Mobula catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mobula''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Mobula Plans Pricing
  plan_count: 4
  slug: mobula-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 6
  name: Mobula Rate Limits
  slug: mobula-rate-limits
rules:
- name: Mobula API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: mobula-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mobula/refs/heads/main/screenshots/mobula-2026-08-07T183915.png
security:
- kind: authentication
  name: Mobula Authentication
  slug: mobula-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mobula Domain Security
  slug: mobula-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mobula
tags:
- Crypto
- Web3
- Market Data
- Blockchain
- Wallet
- Real Time
website: https://mobula.io/
---
