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
api_count: 5
apis:
- description: The primary developer interface for Alchemix is its on-chain smart contracts deployed on Ethereum Mainnet, Optimism, and Arbitrum. Core contracts include the Alchemist (vault deposits, borrowing, repa
  name: Alchemix Smart Contract API
  slug: alchemix-smart-contract-api
- description: 'Alchemix uses The Graph protocol to index on-chain events and expose yield data, harvest history, transmuter APR, and vault position data via GraphQL. The subgraph is queried by the official Alchemix '
  name: Alchemix Subgraph API
  slug: alchemix-subgraph-api
- description: DeFiLlama provides a free, public REST API for Alchemix protocol analytics including TVL history, fee revenue, chain breakdowns, and token data. The protocol slug for Alchemix is "alchemix". The API r
  name: Alchemix Protocol Analytics API (DeFiLlama)
  slug: alchemix-protocol-analytics-api-defillama
- description: CoinGecko provides real-time and historical price data for all Alchemix protocol tokens including ALCX (governance token), alUSD (synthetic USD stablecoin), and alETH (synthetic ETH). Prices are aggre
  name: Alchemix Token Price API (CoinGecko)
  slug: alchemix-token-price-api-coingecko
- description: Alchemix stores yield historic snapshots and transmuter APR data on IPFS via Pinata. The Alchemix frontend retrieves this data using the VITE_PINATA_KEY environment variable to access pinned JSON file
  name: Alchemix Yield Snapshot Storage API (Pinata/IPFS)
  slug: alchemix-yield-snapshot-storage-api-pinataipfs
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/alchemix-finance/v2-foundry/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/alchemix-finance/v2-foundry/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alchemix-domain-security.yml
description: Alchemix is a self-repaying DeFi protocol that allows users to take out interest-free, non-liquidating loans against yield-bearing collateral. Users deposit assets such as ETH, DAI, USDC, or USDT into yield-bearing vaults, and the generated yield automatically repays the loan over time. The protocol issues synthetic alAssets (alUSD, alETH) representing future yield, and provides a Transmuter mechanism to stabilize alAsset prices by gradually exchanging alAssets for underlying collateral. Alchemix operates on Ethereum Mainnet, Optimism, and Arbitrum, with V3 in active development targeting 90% LTV and Meta-Yield Tokens.
graphqls:
- description: Alchemix uses The Graph protocol to index on-chain events from its smart contracts and expose protocol data via GraphQL. The subgraph tracks Alchemist vault positions (deposits, withdrawals, harvests,
  name: Alchemix GraphQL API
  slug: alchemix-graphql
image: https://alchemix.fi/favicon.ico
layout: provider
modified: '2026-06-14'
name: Alchemix
nav: Providers
network: true
overview: Alchemix publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Self-Repaying Loans, Synthetic Assets, Yield, and Ethereum.
random_paper: 3
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alchemix/refs/heads/main/screenshots/alchemix-2026-06-20T171509.png
security:
- kind: domain-security
  name: Alchemix Domain Security
  slug: alchemix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alchemix
tags:
- DeFi
- Self-Repaying Loans
- Synthetic Assets
- Yield
- Ethereum
- Blockchain
- Lending
- alUSD
- alETH
- ALCX
website: https://alchemix.fi/
---
