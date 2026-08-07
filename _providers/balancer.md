---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: Public GraphQL API used by the Balancer UI and integrators. Provides pools, tokens, swaps, gauges, voting, and analytics across all supported chains.
  name: Balancer GraphQL API
  slug: graphql-api
- description: Per-chain GraphQL subgraphs published on The Graph for raw indexed Balancer events.
  name: Balancer Subgraph
  slug: subgraph
- description: Client-side TypeScript / Solidity SDK for the Balancer Smart Order Router; constructs swap routes against current pool state.
  name: Balancer SOR SDK
  slug: sor-sdk
- description: Vault and Router smart contracts where swaps and liquidity actions are executed on-chain. v2 and v3 versions deployed across Ethereum, Arbitrum, Optimism, Polygon, Avalanche, Gnosis, etc.
  name: Balancer Smart Contracts
  slug: smart-contracts
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/balancer-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/balancer-labs
- group: start
  title: ''
  type: Portal
  url: https://balancer.fi/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.balancer.fi/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/balancer
- group: operate
  title: ''
  type: Forums
  url: https://forum.balancer.fi/
- group: commercial
  title: ''
  type: Plans
  url: plans/balancer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/balancer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/balancer-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.balancer.fi/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/balancer-protocol
created: '2026-05-08'
description: Balancer is a DeFi AMM and programmable liquidity platform supporting weighted, stable, and custom pools (v2 and v3). Balancer publishes a public GraphQL API at api-v3.balancer.fi for pool, swap, and analytics data, plus per-chain subgraph endpoints. Smart-contract entry points (Vault and Router) are the primary write surface; SDKs wrap the SOR (Smart Order Router) for client-side route construction.
finops:
- name: Balancer Finops
  service_category: DeFi Protocol
  slug: balancer-finops
graphqls:
- description: Public GraphQL API used by the Balancer UI and integrators. Provides pools, tokens, swaps, gauges, voting, and analytics across all supported chains.
  name: Balancer GraphQL API
  slug: balancer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/balancer.png
layout: provider
modified: '2026-05-08'
name: Balancer
nav: Providers
network: true
overview: 'Balancer publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Web3, DeFi, DEX, AMM, and Liquidity.


  Balancer''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Balancer Plans Pricing
  plan_count: 2
  slug: balancer-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 2
  name: Balancer Rate Limits
  slug: balancer-rate-limits
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/balancer/refs/heads/main/screenshots/balancer-2026-06-20T172932.png
security:
- kind: domain-security
  name: Balancer Domain Security
  slug: balancer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: balancer
tags:
- Web3
- DeFi
- DEX
- AMM
- Liquidity
- Multi-chain
- GraphQL
- Smart Order Router
- Open Source
website: https://balancer.fi/
---
