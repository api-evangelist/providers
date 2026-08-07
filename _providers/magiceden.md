---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Magiceden Agentic Access
  operation_count: 57
  slug: magiceden-agentic-access
  summary_line: 57 operations · 10 acting
api_count: 11
apis:
- description: Token and NFT data endpoints for the Magic Eden Solana marketplace. Provides token metadata retrieval by mint address, token activity history, token listings, received offers on a token, and general t
  name: Magic Eden Solana Tokens API
  slug: magiceden-solana-tokens-api
- description: Wallet-oriented endpoints for the Magic Eden Solana marketplace. Covers wallet information, wallet activity history, ownership activity, escrow balance, offers made and received by a wallet, tokens ow
  name: Magic Eden Solana Wallets API
  slug: magiceden-solana-wallets-api
- description: Trading instruction endpoints for the Magic Eden Solana marketplace. Generates unsigned transaction instructions for buy now, bid/offer, list/sell, cancel buy, cancel sell, change buy price, change se
  name: Magic Eden Solana Trading Instructions API
  slug: magiceden-solana-trading-api
- description: Automated Market Maker (AMM/MMM) pool endpoints for the Magic Eden Solana marketplace. Supports creating, closing, updating, and depositing/withdrawing SOL from liquidity pools. Provides endpoints for
  name: Magic Eden Solana AMM Pool API
  slug: magiceden-solana-amm-api
- description: Bitcoin Ordinals and inscription endpoints for the Magic Eden marketplace. Covers block activity, collection statistics, collection search and retrieval, and inscription-level marketplace data. Also s
  name: Magic Eden Bitcoin Ordinals API
  slug: magiceden-ordinals-api
- description: Runes protocol trading endpoints for the Magic Eden Bitcoin marketplace. Provides rune activity, collection stats, market information, rune orders, UTXOs by wallet, and wallet activities and balances.
  name: Magic Eden Runes API
  slug: magiceden-runes-api
- description: Endpoints related to Bitcoin blockchain
  name: Magic Eden Bitcoin API
  slug: magiceden-bitcoin-api
- description: Endpoints related to Ethereum, Polygon and Base blockchain
  name: Magic Eden EVM API
  slug: magiceden-evm-api
- description: The General API from Magic Eden — 1 operation(s) for general.
  name: Magic Eden General API
  slug: magiceden-general-api
- description: Check Diamond Rewards Eligibility
  name: Magic Eden Rewards API
  slug: magiceden-rewards-api
- description: Endpoints related to Solana blockchain
  name: Magic Eden Solana API
  slug: magiceden-solana-api
artifact_total: 43
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magiceden-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/magiceden-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magiceden-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magiceden-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://magiceden.io
- group: start
  title: ''
  type: Portal
  url: https://docs.magiceden.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.magiceden.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.magiceden.io/reference/solana-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.magiceden.io/reference/solana-api-keys
- group: auth
  title: API key obtained via application form; public endpoints have no-key free tier at 120 QPM
  type: Authentication
  url: https://docs.magiceden.io/reference/solana-api-keys
- group: auth
  title: Magic Eden API Key Application Form
  type: APIKeyForm
  url: https://airtable.com/appe8frCT8yj415Us/pagqgEFcpBlbm2DAF/form
- group: build
  title: Magic Eden TypeScript SDK (multi-chain)
  type: SDKs
  url: https://github.com/magiceden/magiceden-sdk
- group: learn
  title: Step-by-step integration tutorials for common tasks
  type: Recipes
  url: https://docs.magiceden.io/recipes
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.magiceden.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magiceden
- group: build
  title: Magic Eden TypeScript SDK
  type: GitHubRepository
  url: https://github.com/magiceden/magiceden-sdk
- group: auth
  title: HackerOne Bug Bounty Program
  type: BugBounty
  url: https://hackerone.com/magiceden
- group: commercial
  title: ''
  type: TermsOfService
  url: https://magiceden.us/legal-policies/api-terms
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MagicEden
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/magiceden
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magiceden-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/magiceden-plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/magiceden-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/magiceden-openapi.yaml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/magiceden-context.jsonld
- group: design
  title: ''
  type: JSONLDProvider
  url: json-ld/magiceden-provider.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magiceden-collection.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magiceden-nft-token.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magiceden-activity.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magiceden-wallet.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magiceden-amm-pool.json
created: '2026-06-13'
description: Magic Eden is a multi-chain NFT marketplace and trading platform supporting Solana, Bitcoin (Ordinals and Runes), Ethereum, and Polygon. It provides REST APIs for accessing NFT listings, collection statistics, wallet activities, offers, and token metadata across supported chains, as well as trading instruction endpoints to generate and submit buy, sell, bid, and cancel orders directly on the Magic Eden marketplace. The Solana API also exposes Automated Market Maker (AMM/MMM) pool endpoints for liquidity provision. The Bitcoin Ordinals API covers inscriptions, rare sats, and the Runes protocol. Magic Eden has announced deprecation of its Bitcoin and EVM APIs; the Solana API remains the primary supported surface as of mid-2026.
examples:
- key_count: 1
  name: Amm Pool Response
  slug: amm-pool-response
- key_count: 10
  name: Buy Instruction Request
  slug: buy-instruction-request
- key_count: 19
  name: Collection Stats Response
  slug: collection-stats-response
- key_count: 17
  name: Nft Token Response
  slug: nft-token-response
- key_count: 1
  name: Wallet Activity Response
  slug: wallet-activity-response
features:
- description: Single API surface spanning Solana, Bitcoin (Ordinals and Runes), Ethereum, and Polygon NFT markets
  name: Multi-Chain Coverage
- description: Both read-only market data endpoints and write-side transaction instruction generation in one API
  name: Data and Trading in One
- description: Full lifecycle management of automated market maker liquidity pools on Solana NFT collections
  name: AMM Pool Management
- description: Comprehensive wallet endpoints covering holdings, offers, escrow, and activity feeds
  name: Wallet-Level Activity
- description: Native support for the Bitcoin Runes protocol including order creation, swaps, quotes, and sweeping
  name: Runes Protocol Support
- description: Free public tier available without API key; higher QPS tiers accessible via application form
  name: API Key Application
finops:
- name: Magiceden Finops
  service_category: NFT Marketplace API
  slug: magiceden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magiceden.png
json_schemas:
- name: MagicEdenActivity
  property_count: 12
  slug: magiceden-activity
- name: MagicEdenAMMPool
  property_count: 17
  slug: magiceden-amm-pool
- name: MagicEdenCollection
  property_count: 19
  slug: magiceden-collection
- name: MagicEdenNFTToken
  property_count: 18
  slug: magiceden-nft-token
- name: MagicEdenWallet
  property_count: 7
  slug: magiceden-wallet
jsonld:
- class_count: 61
  name: Magiceden Context
  property_count: 0
  slug: magiceden-context
- class_count: 0
  name: Magiceden Provider Context
  property_count: 0
  slug: magiceden-provider
layout: provider
modified: '2026-06-13'
name: Magic Eden
nav: Providers
network: true
overview: 'Magic Eden publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bitcoin API, EVM API, General API, and 2 more. Tagged areas include NFT, NFT Marketplace, Multi-Chain, Solana, and Bitcoin.


  The Magic Eden catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Magic Eden''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, changelog, and 25 more developer resources.'
plans:
- name: Magiceden Plans
  plan_count: 2
  slug: magiceden-plans
random_paper: 21
rate_limits:
- limit_count: 4
  name: Magiceden Rate Limits
  slug: magiceden-rate-limits
rules:
- name: Magic Eden API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: magiceden-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.0
    developer_ergonomics: 52.2
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magiceden/refs/heads/main/screenshots/magiceden-2026-06-20T184844.png
security:
- kind: authentication
  name: Magiceden Authentication
  slug: magiceden-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Magiceden Domain Security
  slug: magiceden-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Magiceden Vulnerability Disclosure
  slug: magiceden-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: magiceden
tags:
- NFT
- NFT Marketplace
- Multi-Chain
- Solana
- Bitcoin
- Ordinals
- Runes
- Ethereum
- Polygon
- Web3
- Blockchain
- DeFi
- Trading
use_cases:
- description: Retrieve tokens owned by a wallet and activity history to build a multi-chain NFT portfolio dashboard
  name: NFT Portfolio Tracker
- description: Pull collection statistics, holder distributions, and leaderboard data for market intelligence tools
  name: Collection Analytics
- description: Use trading instruction endpoints to automate buy, sell, and bid operations on the Solana marketplace
  name: Programmatic Trading Bot
- description: Create and manage MMM liquidity pools on Solana NFT collections for algorithmic market-making strategies
  name: AMM Market Making
- description: Surface Bitcoin inscription and Runes marketplace data, listings, and wallet balances in explorer UIs
  name: Ordinals/Runes Explorer
- description: Aggregate Magic Eden listings alongside other venues using the batch listings and search endpoints
  name: Marketplace Aggregator
website: https://magiceden.io
---
