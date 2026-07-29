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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Core Aave V3 protocol contracts — Pool, L2 Pool, Wrapped Token Gateway, PoolAddressesProvider, Pool Configurator, Interest Rate Strategy, Access Control Manager, Oracles, aTokens, variable / stable de
  name: Aave V3 Pool (Smart Contracts)
  slug: v3-pool
- description: Next-generation Aave V4 protocol implementation with unified liquidity layer, hub-and-spoke architecture, and improved risk management. Source available in the aave-v4 repository.
  name: Aave V4 Protocol (Smart Contracts)
  slug: v4-protocol
- description: Official TypeScript SDK for Aave V3 that wraps protocol interactions — supply, borrow, repay, withdraw, swap collateral, repay-with-collateral, and read operations — across supported networks.
  name: Aave V3 SDK
  slug: sdk-v3
- description: Official TypeScript SDK for the Aave V4 protocol, exposing typed operations for supplying, borrowing, and reading V4 hub state.
  name: Aave V4 SDK
  slug: sdk-v4
- description: Higher-level toolkit (React + TypeScript + GraphQL) for embedding Aave market data and protocol actions into apps. Built on top of the Aave SDK and protocol subgraphs.
  name: Aave Kit
  slug: kit
- description: The Graph subgraphs that index Aave V2 and V3 reserves, users, liquidations, flash loans, rewards, and historical balances. Queried via GraphQL across each deployed network.
  name: Aave Protocol Subgraphs
  slug: protocol-subgraphs
- description: TypeScript helper library exposing math, formatting, and contract-call helpers for building UIs and analytics on top of Aave V2 and V3 markets.
  name: aave-utilities
  slug: utilities
- description: Open-source web interface (app.aave.com) for interacting with the Aave protocol — a reference implementation that integrates the SDK, Kit, and subgraphs.
  name: Aave Interface
  slug: interface
artifact_total: 14
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aave-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aave.com
- group: docs
  title: ''
  type: Documentation
  url: https://aave.com/docs
- group: other
  title: ''
  type: Build
  url: https://aave.com/build
- group: other
  title: ''
  type: App
  url: https://app.aave.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/aave
- group: other
  title: ''
  type: Governance
  url: https://governance.aave.com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/aave
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/aave
- group: company
  title: ''
  type: Blog
  url: https://aave.com/blog
created: '2026-05-23'
description: 'Aave is a decentralized, non-custodial liquidity protocol where users supply assets to earn yield and borrow against collateral. The protocol runs on Ethereum and many L2s (Arbitrum, Optimism, Base, Polygon, Avalanche, zkSync, Scroll, Metis) and exposes developer surfaces beyond on-chain contracts: official Aave V3 / V4 TypeScript SDKs, Aave Kit (React + TypeScript + GraphQL), and protocol subgraphs hosted on The Graph for indexed market, reserve, user, and historical data.'
finops:
- name: Aave Finops
  service_category: API
  slug: aave-finops
graphqls:
- description: Higher-level toolkit (React + TypeScript + GraphQL) for embedding Aave market data and protocol actions into apps. Built on top of the Aave SDK and protocol subgraphs.
  name: Aave GraphQL API
  slug: aave-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aave.png
layout: provider
modified: '2026-05-23'
name: Aave
nav: Providers
network: true
overview: 'Aave publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Lending, Borrowing, Liquidity, and Protocol.


  Aave''s developer surface includes documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Aave Plans Pricing
  plan_count: 1
  slug: aave-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Aave Rate Limits
  slug: aave-rate-limits
score:
  band: emerging
  composite: 20.4
  delta: -2.6
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aave/refs/heads/main/screenshots/aave-2026-06-20T163031.png
security:
- kind: domain-security
  name: Aave Domain Security
  slug: aave-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Aave Trust Center
  slug: aave-trust-center
  summary_line: SOC 2
slug: aave
tags:
- DeFi
- Lending
- Borrowing
- Liquidity
- Protocol
- Subgraph
- GraphQL
website: https://aave.com
---
