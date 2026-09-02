---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: GraphQL subgraph for Fraxswap on Ethereum, exposing pairs, tokens, swaps, liquidity positions, TWAMM long-term orders, and protocol-level analytics via The Graph.
  name: Frax Finance GraphQL API
  slug: frax-finance-graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frax-finance-domain-security.yml
created: '2026-06-14'
description: Frax Finance is a fractional-algorithmic stablecoin protocol featuring FRAX (a stablecoin), FXS (Frax Shares governance token), and Fraxswap — a TWAMM-based AMM DEX. The protocol is deployed across multiple chains and exposes its on-chain data via The Graph subgraphs.
graphqls:
- description: Frax Finance is a fractional-algorithmic stablecoin protocol. Its primary products include FRAX (a partially collateralized stablecoin), FXS (Frax Shares, the governance and utility token), and Fraxsw
  name: Frax Finance GraphQL API
  slug: frax-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frax-finance.png
layout: provider
modified: '2026-06-14'
name: Frax Finance
nav: Providers
network: true
overview: Frax Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Stablecoins, AMM, TWAMM, and GraphQL.
random_paper: 5
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Frax Finance Domain Security
  slug: frax-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: frax-finance
tags:
- DeFi
- Stablecoins
- AMM
- TWAMM
- GraphQL
- Ethereum
---
