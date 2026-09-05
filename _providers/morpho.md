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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 7
apis:
- description: GraphQL queries for Morpho Blue lending markets — retrieve market parameters (loan asset, collateral asset, LLTV, oracle, IRM), real-time state metrics (supply, borrow, collateral assets and USD value
  name: Morpho Markets API
  slug: markets-api
- description: GraphQL queries for Morpho Vaults (MetaMorpho V1 and V2) — discover vault addresses, symbols, and assets; retrieve total deposits, liquidity, share price, and APY metrics; track depositor positions an
  name: Morpho Vaults API
  slug: vaults-api
- description: GraphQL queries for individual user positions across Morpho Markets and Vaults — query marketPositions for collateral, borrow assets, supply shares, and USD values by user address; retrieve account ov
  name: Morpho Positions API
  slug: positions-api
- description: GraphQL queries for liquidation events on Morpho Markets — filter marketTransactions by type Liquidation to retrieve seized collateral amounts, repaid loan amounts, bad debt figures, liquidator addres
  name: Morpho Liquidations API
  slug: liquidations-api
- description: GraphQL queries for Morpho rewards and incentive campaigns — retrieve supply and borrow reward APRs per asset, campaign details, and user-level reward accruals across markets and vaults. Enables calcu
  name: Morpho Rewards API
  slug: rewards-api
- description: GraphQL queries for the Morpho Public Allocator — retrieve allocator addresses and configurations, query total reallocatable liquidity and market available liquidity (combining direct and reallocatabl
  name: Morpho Public Allocator API
  slug: public-allocator-api
- description: GraphQL time-series queries for historical market and vault state — query historicalState on markets or vaults with configurable startTimestamp, endTimestamp, and interval (YEAR, QUARTER, MONTH, WEEK,
  name: Morpho Historical Data API
  slug: historical-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morpho-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.morpho.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.morpho.org/
- group: docs
  title: ''
  type: GraphQL Playground
  url: https://api.morpho.org/graphql
- group: build
  title: ''
  type: GitHub
  url: https://github.com/morpho-org
- group: build
  title: ''
  type: SDKs
  url: https://docs.morpho.org/tools/offchain/sdks/get-started/
- group: company
  title: ''
  type: Blog
  url: https://morpho.org/blog/
- group: operate
  title: ''
  type: Status
  url: https://status.morpho.org/
- group: operate
  title: ''
  type: Support
  url: https://help.morpho.org/
- group: other
  title: ''
  type: Subgraphs
  url: https://docs.morpho.org/tools/offchain/subgraphs/
- group: other
  title: ''
  type: X
  url: https://x.com/MorphoLabs
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/morpho
created: '2026-06-14'
description: Morpho is an open DeFi credit network enabling permissionless lending and borrowing of digital assets. The Morpho API provides a GraphQL-based interface to access comprehensive onchain and offchain data from the Morpho ecosystem in real time, covering Morpho Markets, Morpho Vaults, user positions, collateral, liquidations, rewards, and historical analytics across Ethereum, Base, Arbitrum, and other supported chains. The API is publicly accessible without authentication and includes a companion TypeScript SDK suite for application integration.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: The Morpho GraphQL API is the primary offchain data interface for the Morpho DeFi credit protocol. It exposes comprehensive real-time and historical data covering Morpho Blue lending markets, MetaMorp
  name: Morpho GraphQL API
  slug: morpho-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morpho.png
layout: provider
modified: '2026-06-14'
name: Morpho
nav: Providers
network: true
overview: 'Morpho publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Lending, Borrowing, Collateral, and Liquidations.


  Morpho''s developer surface includes documentation, GitHub presence, engineering blog, status page, support, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 10
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morpho/refs/heads/main/screenshots/morpho-2026-06-20T185812.png
security:
- kind: domain-security
  name: Morpho Domain Security
  slug: morpho-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: morpho
tags:
- DeFi
- Lending
- Borrowing
- Collateral
- Liquidations
- Rewards
- Markets
- Vault
- Web3
website: https://developers.morpho.org/
---
