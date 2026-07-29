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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Transpose Agentic Access
  operation_count: 21
  slug: transpose-agentic-access
  summary_line: 21 operations · 1 acting
api_count: 6
apis:
- description: Low-level blockchain primitives including accounts, blocks, transactions, logs, and traces across EVM chains.
  name: Transpose Block API API
  slug: transpose-block-api-api
- description: Ethereum Name Service records and transfer history.
  name: Transpose ENS API API
  slug: transpose-ens-api-api
- description: NFT collections, ownership, sales, and transfers for ERC-721 and ERC-1155 tokens.
  name: Transpose NFT API API
  slug: transpose-nft-api-api
- description: Custom SQL query interface against Transpose's entire indexed blockchain dataset.
  name: Transpose SQL Analytics API API
  slug: transpose-sql-analytics-api-api
- description: ERC-20, ERC-777, and native token balances, transfers, and DEX swaps.
  name: Transpose Token API API
  slug: transpose-token-api-api
- description: Real-time and historical OHLC price data for any token including LP tokens.
  name: Transpose Token Prices API API
  slug: transpose-token-prices-api-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transpose-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transpose-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transpose-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transpose-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://app.transpose.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.transpose.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.transpose.io/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.transpose.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.transpose.io/blogs
- group: auth
  title: ''
  type: Authentication
  url: https://docs.transpose.io/quickstart/
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
created: '2026-06-14'
description: Historical blockchain data REST API providing access to transaction history, token transfers, NFT metadata, smart contract events, DEX swaps, and price data across Ethereum and other EVM-compatible chains. Offers five enterprise-grade REST APIs plus a SQL Analytics API for querying indexed blockchain data across Ethereum, Polygon, Optimism, Base, Arbitrum, Avalanche, BSC, Bitcoin, and Tron.
examples:
- key_count: 5
  name: Nft Transfers Request
  slug: nft-transfers-request
- key_count: 4
  name: Nft Transfers Response
  slug: nft-transfers-response
- key_count: 5
  name: Sql Query Request
  slug: sql-query-request
- key_count: 4
  name: Sql Query Response
  slug: sql-query-response
- key_count: 5
  name: Token Price Response
  slug: token-price-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transpose.png
json_schemas:
- name: NFT Transfer
  property_count: 10
  slug: nft-transfer
- name: SQL Query Request
  property_count: 1
  slug: sql-query
- name: Token Transfer
  property_count: 8
  slug: token-transfer
- name: Transaction
  property_count: 12
  slug: transaction
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-14'
name: Transpose
nav: Providers
network: true
overview: 'Transpose publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Block API API, ENS API API, NFT API API, and 3 more. Tagged areas include Blockchain, NFT, Cryptocurrency, Web3, and Ethereum.


  The Transpose catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Transpose''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 19
rate_limits:
- limit_count: 5
  name: Rate Limits
  slug: rate-limits
rules:
- name: Transpose API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: transpose-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.6
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.8
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transpose/refs/heads/main/screenshots/transpose-2026-06-20T195630.png
security:
- kind: authentication
  name: Transpose Authentication
  slug: transpose-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transpose Domain Security
  slug: transpose-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Transpose Vulnerability Disclosure
  slug: transpose-vulnerability-disclosure
  summary_line: disclosure policy published
slug: transpose
tags:
- Blockchain
- NFT
- Cryptocurrency
- Web3
- Ethereum
- Token Transfers
- Smart Contracts
- Historical Data
- DeFi
- DEX
website: https://app.transpose.io
---
