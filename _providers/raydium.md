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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Raydium Agentic Access
  operation_count: 23
  slug: raydium-agentic-access
  summary_line: 23 operations
api_count: 6
apis:
- description: REST API for Raydium pool list, CLMM pools, farm rewards, token metadata, swap quote, and price endpoints. Used by raydium.io UI and third-party integrators. JSON output. Free, unauthenticated, fair-u
  name: Raydium REST API v3
  slug: rest-api
- description: Raydium's swap, AMM, CLMM, farm, and launchpad programs deployed on Solana.
  name: Raydium Solana Programs
  slug: smart-contracts
- description: The Farms API from Raydium — 3 operation(s) for farms.
  name: Raydium Farms API
  slug: raydium-farms-api
- description: The Main API from Raydium — 11 operation(s) for main.
  name: Raydium Main API
  slug: raydium-main-api
- description: The Mint API from Raydium — 3 operation(s) for mint.
  name: Raydium Mint API
  slug: raydium-mint-api
- description: The Pools API from Raydium — 6 operation(s) for pools.
  name: Raydium Pools API
  slug: raydium-pools-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Raydium REST API v3 Farms API
  slug: open-raydium-farms-api
- collection_type: open
  name: Raydium REST API v3 Farms Main API
  slug: open-raydium-main-api
- collection_type: open
  name: Raydium REST API v3 Farms Mint API
  slug: open-raydium-mint-api
- collection_type: open
  name: Raydium REST API v3 Farms Pools API
  slug: open-raydium-pools-api
- collection_type: open
  name: Raydium REST API v3
  slug: open-raydium
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/raydium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raydium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/raydium
- group: start
  title: ''
  type: Portal
  url: https://raydium.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.raydium.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/raydium-io
- group: commercial
  title: ''
  type: Plans
  url: plans/raydium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/raydium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/raydium-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.raydium.io/llms.txt
created: '2026-05-08'
description: Raydium is a leading Solana AMM and liquidity provider supporting standard AMM, concentrated liquidity (CLMM), and a launchpad. The Raydium API at api-v3.raydium.io exposes pool, farm, token, swap quote, and price endpoints used by the Raydium UI and integrators. Smart-contract entry points are the primary write path.
finops:
- name: Raydium Finops
  service_category: DeFi Protocol
  slug: raydium-finops
graphqls:
- description: Raydium's own REST API (api-v3.raydium.io) does not expose a GraphQL endpoint. GraphQL access to Raydium on-chain program state is provided by **Shyft** (shyft.to), a Solana indexing platform that par
  name: Raydium GraphQL
  slug: raydium-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raydium.png
layout: provider
modified: '2026-05-08'
name: Raydium
nav: Providers
network: true
overview: 'Raydium publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Farms API, Main API, Mint API, and 1 more. Tagged areas include Web3, Solana, DEX, AMM, and Liquidity.


  Raydium''s developer surface includes developer portal, documentation, GitHub presence, and 7 more developer resources.'
plans:
- name: Raydium Plans Pricing
  plan_count: 2
  slug: raydium-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Raydium Rate Limits
  slug: raydium-rate-limits
score:
  band: thin
  composite: 28.3
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 49.4
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raydium/refs/heads/main/screenshots/raydium-2026-06-20T192619.png
security:
- kind: domain-security
  name: Raydium Domain Security
  slug: raydium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raydium
tags:
- Web3
- Solana
- DEX
- AMM
- Liquidity
- CLMM
- Launchpad
- Open-Source
website: https://raydium.io/
---
