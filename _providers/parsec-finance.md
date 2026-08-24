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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Pro GraphQL API for on-chain DeFi and NFT market data — DEX trades, candles, lending markets, liquidity pools and positions, NFT collections and trades, token holders, transfers, transactions, contrac
  name: Parsec Finance API
  slug: parsec-finance-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://parsec.fi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.parsec.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parsec.finance/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parsec.finance/
- group: commercial
  title: ''
  type: Pricing
  url: https://parsec.fi/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parsec-finance
- group: build
  title: ''
  type: Packages
  url: packages/parsec-finance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parsec-finance-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parsec-finance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parsec-finance-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parsec-finance-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parsec-finance-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parsec-finance-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parsec-finance-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parsec-finance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsec-finance-domain-security.yml
created: '2026-07-17'
description: 'Parsec Finance is an institutional-grade on-chain analytics platform for DeFi and NFT markets. Its modular "Command Center" lets traders and analysts drag and drop dozens of real-time components — live trade firehoses, liquidity-depth charts, wallet trackers, lending dashboards and NFT floor monitors — across many EVM chains. Beyond the app, Parsec exposes a Pro GraphQL API at api.parsec.finance for programmatic access to on-chain market data: DEX trades, OHLCV candles, lending markets, liquidity pools (including concentrated-liquidity positions), NFT collections and trades, token holders and balance changes, transfers, transactions, contract logs, trending contracts, trade metrics and address label resolution. A first-party Python SDK (parsecfi) wraps the API. Parsec is used by firms such as Polychain and Galaxy Digital.'
image: https://parsec.fi/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Parsec Finance MCP Server
  slug: parsec-finance-mcp-server
modified: '2026-07-20'
name: Parsec Finance
nav: Providers
network: true
overview: 'Parsec Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, DeFi, NFT, and Blockchain.


  Parsec Finance''s developer surface includes documentation, API reference, pricing, authentication, and 13 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 21.0
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 21.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Parsec Finance Authentication
  slug: parsec-finance-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parsec Finance Domain Security
  slug: parsec-finance-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: parsec-finance
tags:
- Company
- Analytics
- DeFi
- NFT
- Blockchain
- Cryptocurrency
- On-Chain Data
- Web3
- GraphQL
- Trading
website: https://parsec.fi
---
