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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Moralis Agentic Access
  operation_count: 117
  slug: moralis-agentic-access
  summary_line: 117 operations · 10 acting
api_count: 29
apis:
- description: REST API for Solana on-chain data (accounts, NFTs, tokens, transactions).
  name: Moralis Solana API
  slug: solana-api
- description: REST API for managing real-time blockchain event streams delivered via webhooks.
  name: Moralis Streams API
  slug: streams
- description: REST API for Sign-In with Ethereum / Solana challenge generation and verification.
  name: Moralis Auth API
  slug: auth-api
- description: Bulk historical and ongoing blockchain dataset exports (Parquet/CSV via S3 / Snowflake share).
  name: Moralis Datashare
  slug: datashare
- description: The Balance API from Moralis — 2 operation(s) for balance.
  name: Moralis Balance API
  slug: moralis-balance-api
- description: The Block API from Moralis — 3 operation(s) for block.
  name: Moralis Block API
  slug: moralis-block-api
- description: The Categories API from Moralis — 1 operation(s) for categories.
  name: Moralis Categories API
  slug: moralis-categories-api
- description: The DeFi API from Moralis — 3 operation(s) for defi.
  name: Moralis DeFi API
  slug: moralis-defi-api
- description: The Discovery API from Moralis — 11 operation(s) for discovery.
  name: Moralis Discovery API
  slug: moralis-discovery-api
- description: The Entities API from Moralis — 4 operation(s) for entities.
  name: Moralis Entities API
  slug: moralis-entities-api
- description: The Get Balance API from Moralis — 1 operation(s) for get balance.
  name: Moralis Get Balance API
  slug: moralis-get-balance-api
- description: The Get Collections API from Moralis — 4 operation(s) for get collections.
  name: Moralis Get Collections API
  slug: moralis-get-collections-api
- description: The Get Floor Price API from Moralis — 3 operation(s) for get floor price.
  name: Moralis Get Floor Price API
  slug: moralis-get-floor-price-api
- description: The Get Market Data API from Moralis — 11 operation(s) for get market data.
  name: Moralis Get Market Data API
  slug: moralis-get-market-data-api
- description: The Get Metadata API from Moralis — 4 operation(s) for get metadata.
  name: Moralis Get Metadata API
  slug: moralis-get-metadata-api
- description: The Get Mutiple NFTs API from Moralis — 1 operation(s) for get mutiple nfts.
  name: Moralis Get Mutiple NFTs API
  slug: moralis-get-mutiple-nfts-api
- description: The Get NFTs API from Moralis — 2 operation(s) for get nfts.
  name: Moralis Get NFTs API
  slug: moralis-get-nfts-api
- description: The Get Owners API from Moralis — 3 operation(s) for get owners.
  name: Moralis Get Owners API
  slug: moralis-get-owners-api
- description: The Get Ownership API from Moralis — 1 operation(s) for get ownership.
  name: Moralis Get Ownership API
  slug: moralis-get-ownership-api
- description: The Get Transactions API from Moralis — 2 operation(s) for get transactions.
  name: Moralis Get Transactions API
  slug: moralis-get-transactions-api
- description: The Get Transfers API from Moralis — 3 operation(s) for get transfers.
  name: Moralis Get Transfers API
  slug: moralis-get-transfers-api
- description: The Get Unique Owners API from Moralis — 1 operation(s) for get unique owners.
  name: Moralis Get Unique Owners API
  slug: moralis-get-unique-owners-api
- description: The Market Data API from Moralis — 6 operation(s) for market data.
  name: Moralis Market Data API
  slug: moralis-market-data-api
- description: The NFT API from Moralis — 28 operation(s) for nft.
  name: Moralis NFT API
  slug: moralis-nft-api
- description: The Resolve Web3 Domain API from Moralis — 4 operation(s) for resolve web3 domain.
  name: Moralis Resolve Web3 Domain API
  slug: moralis-resolve-web3-domain-api
- description: The Token API from Moralis — 35 operation(s) for token.
  name: Moralis Token API
  slug: moralis-token-api
- description: The Transaction API from Moralis — 4 operation(s) for transaction.
  name: Moralis Transaction API
  slug: moralis-transaction-api
- description: The Utils API from Moralis — 4 operation(s) for utils.
  name: Moralis Utils API
  slug: moralis-utils-api
- description: The Wallets API from Moralis — 13 operation(s) for wallets.
  name: Moralis Wallets API
  slug: moralis-wallets-api
artifact_total: 37
collections:
- collection_type: open
  name: EVM API
  slug: open-moralis-evm-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moralis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moralis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moralis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moralis-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoralisWeb3
- group: company
  title: ''
  type: Blog
  url: https://moralis.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moralisweb3
- group: company
  title: ''
  type: Website
  url: https://moralis.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/moralis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moralis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moralis-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.moralis.com/llms.txt
created: '2026-05-08'
description: Moralis is a Web3 data platform offering REST-based Data APIs for EVM and Solana chains, real-time Streams (webhooks), Datashare exports, and an enterprise Data Indexer. Supports 30+ chains for wallets, analytics, automation, and data pipelines.
finops:
- name: Moralis Finops
  service_category: Web3
  slug: moralis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moralis.png
layout: provider
modified: '2026-05-08'
name: Moralis
nav: Providers
network: true
overview: 'Moralis publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Block API, Categories API, and 22 more. Tagged areas include Web3, Blockchain, Data API, Streams, and Indexing.


  Moralis'' developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Moralis Plans Pricing
  plan_count: 5
  slug: moralis-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 4
  name: Moralis Rate Limits
  slug: moralis-rate-limits
score:
  band: thin
  composite: 37.5
  delta: -2.9
  facets:
    commercial_clarity: 47.4
    contract_quality: 52.9
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moralis/refs/heads/main/screenshots/moralis-2026-06-20T185806.png
security:
- kind: authentication
  name: Moralis Authentication
  slug: moralis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moralis Domain Security
  slug: moralis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Moralis Trust Center
  slug: moralis-trust-center
  summary_line: SOC 2, ISO 27001
slug: moralis
tags:
- Web3
- Blockchain
- Data API
- Streams
- Indexing
website: https://moralis.com/
---
