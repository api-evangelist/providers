---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vesper Agentic Access
  operation_count: 6
  slug: vesper-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: Smart contract interface reference for Vesper pools, strategies, PoolAccountant, PoolRewards, and related on-chain components enabling direct DeFi integration via Web3.
  name: Vesper Contracts API Reference
  slug: vesper-contracts-api-reference
- description: GraphQL subgraph for querying Vesper Finance on-chain events, pool history, strategy performance, and token metrics via The Graph protocol.
  name: Vesper Subgraph API
  slug: vesper-subgraph-api
- description: Vesper Grow Pool data and metadata
  name: Vesper Finance Pools API
  slug: vesper-pools-api
- description: APY, APR, and lending rate data
  name: Vesper Finance Rates API
  slug: vesper-rates-api
- description: Total value locked metrics
  name: Vesper Finance TVL API
  slug: vesper-tvl-api
- description: VSP token statistics and staking data
  name: Vesper Finance VSP API
  slug: vesper-vsp-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vesper-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vesper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vesper.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vesper.finance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vesperfi
- group: build
  title: ''
  type: JavaScriptLibrary
  url: https://github.com/vesperfi/lib-js
- group: company
  title: ''
  type: Blog
  url: https://medium.com/vesperfinance
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/vesperfinance
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/VesperFi
- group: design
  title: ''
  type: PoolMetadata
  url: https://github.com/vesperfi/metadata
created: '2026-06-14'
description: Vesper Finance is a DeFi yield aggregator that enables users to deposit assets into managed pools where yield strategies automatically optimize returns across decentralized finance protocols. The platform provides REST APIs for querying pool performance metrics, APY data, strategy information, VSP token statistics, and historical value-locked data across Ethereum, Polygon, Avalanche, and Optimism.
examples:
- key_count: 1
  name: Getloanrates Response
  slug: getLoanRates-response
- key_count: 7
  name: Getvspstats Response
  slug: getVspStats-response
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: The Vesper Finance subgraph is deployed on The Graph protocol and provides a GraphQL API for querying on-chain pool data, revenue metrics, and token statistics for Vesper pools on Ethereum Mainnet.
  name: Vesper Finance GraphQL Subgraph
  slug: vesper-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vesper.png
json_schemas:
- name: DataPoint
  property_count: 6
  slug: DataPoint
- name: LoanRatesResponse
  property_count: 1
  slug: LoanRatesResponse
- name: Pool
  property_count: 13
  slug: Pool
- name: PoolDashboard
  property_count: 8
  slug: PoolDashboard
- name: ValueLocked
  property_count: 3
  slug: ValueLocked
- name: VspStats
  property_count: 7
  slug: VspStats
jsonld:
- class_count: 19
  name: context Context
  property_count: 31
  slug: context
layout: provider
modified: '2026-06-14'
name: Vesper Finance
nav: Providers
network: true
overview: 'Vesper Finance publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Pools API, Rates API, TVL API, and 1 more. Tagged areas include DeFi, Yield Aggregator, Liquidity Pools, APY, and Staking.


  The Vesper Finance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vesper Finance''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 49
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Vesper Finance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vesper-jsonschema-spectral-rules
score:
  band: thin
  composite: 43.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.9
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 43.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vesper/refs/heads/main/screenshots/vesper-2026-06-20T201000.png
security:
- kind: domain-security
  name: Vesper Domain Security
  slug: vesper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vesper
tags:
- DeFi
- Yield Aggregator
- Liquidity Pools
- APY
- Staking
- VSP Token
- Ethereum
- Polygon
- Avalanche
- Optimism
website: https://vesper.finance/
---
