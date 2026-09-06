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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
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
random_paper: 5
rate_limits:
- limit_count: 2
  name: Balancer Rate Limits
  slug: balancer-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Multi-Chain
- GraphQL
- Smart Order Router
- Open-Source
website: https://balancer.fi/
---
