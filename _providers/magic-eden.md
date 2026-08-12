---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Magic Eden Agentic Access
  operation_count: 86
  slug: magic-eden-agentic-access
  summary_line: 86 operations · 25 acting
api_count: 19
apis:
- description: The Activity API from Magic Eden — 1 operation(s) for activity.
  name: Magic Eden Activity API
  slug: magic-eden-activity-api
- description: The Assets API from Magic Eden — 2 operation(s) for assets.
  name: Magic Eden Assets API
  slug: magic-eden-assets-api
- description: The Blocks API from Magic Eden — 1 operation(s) for blocks.
  name: Magic Eden Blocks API
  slug: magic-eden-blocks-api
- description: The Collections API from Magic Eden — 13 operation(s) for collections.
  name: Magic Eden Collections API
  slug: magic-eden-collections-api
- description: Get instructions for the blockchain
  name: Magic Eden instructions API
  slug: magic-eden-instructions-api
- description: The Ixs API from Magic Eden — 9 operation(s) for ixs.
  name: Magic Eden Ixs API
  slug: magic-eden-ixs-api
- description: Get launchpad information
  name: Magic Eden launchpad API
  slug: magic-eden-launchpad-api
- description: The magic-ticket API from Magic Eden — 1 operation(s) for magic-ticket.
  name: Magic Eden magic-ticket API
  slug: magic-eden-magic-ticket-api
- description: Get information about Magic Eden's marketplace!
  name: Magic Eden marketplace API
  slug: magic-eden-marketplace-api
- description: Get AMM information
  name: Magic Eden mmm API
  slug: magic-eden-mmm-api
- description: The Orders API from Magic Eden — 2 operation(s) for orders.
  name: Magic Eden Orders API
  slug: magic-eden-orders-api
- description: The Rare Sats API from Magic Eden — 4 operation(s) for rare sats.
  name: Magic Eden Rare Sats API
  slug: magic-eden-rare-sats-api
- description: The Runes Info API from Magic Eden — 7 operation(s) for runes info.
  name: Magic Eden Runes Info API
  slug: magic-eden-runes-info-api
- description: The Runes Listing API from Magic Eden — 4 operation(s) for runes listing.
  name: Magic Eden Runes Listing API
  slug: magic-eden-runes-listing-api
- description: The Runes Market Sell API from Magic Eden — 2 operation(s) for runes market sell.
  name: Magic Eden Runes Market Sell API
  slug: magic-eden-runes-market-sell-api
- description: The Runes Swap API from Magic Eden — 3 operation(s) for runes swap.
  name: Magic Eden Runes Swap API
  slug: magic-eden-runes-swap-api
- description: The Runes Sweeping API from Magic Eden — 2 operation(s) for runes sweeping.
  name: Magic Eden Runes Sweeping API
  slug: magic-eden-runes-sweeping-api
- description: The Tokens API from Magic Eden — 5 operation(s) for tokens.
  name: Magic Eden Tokens API
  slug: magic-eden-tokens-api
- description: Get information of a wallet
  name: Magic Eden wallets API
  slug: magic-eden-wallets-api
artifact_total: 55
collections:
- collection_type: open
  name: Magic Eden EVM API
  slug: open-magic-eden-evm
- collection_type: open
  name: Magic Eden Bitcoin Ordinals API
  slug: open-magic-eden-ordinals
- collection_type: open
  name: Magic Eden Solana API
  slug: open-magic-eden-solana
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/magiceden/magiceden-sdk/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magic-eden-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/magic-eden-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magic-eden-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magic-eden-authentication.yml
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
  type: APIReference
  url: https://docs.magiceden.io/reference/getting-started-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.magiceden.io/reference/getting-started-1
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.magiceden.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magiceden
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magicoss
- group: build
  title: ''
  type: SDKs
  url: https://github.com/magiceden/magiceden-sdk
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.magiceden.io/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://magiceden.io/terms-of-service.pdf
- group: auth
  title: ''
  type: BugBounty
  url: https://hackerone.com/magic-eden
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/magiceden
- group: commercial
  title: ''
  type: Plans
  url: plans/magic-eden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magic-eden-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/magic-eden-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.magiceden.io
- group: auth
  title: Magic Eden API Key Application Form
  type: APIKeyForm
  url: https://airtable.com/appe8frCT8yj415Us/pagqgEFcpBlbm2DAF/form
- group: learn
  title: Step-by-step integration tutorials for common tasks
  type: Recipes
  url: https://docs.magiceden.io/recipes
- group: build
  title: Magic Eden TypeScript SDK
  type: GitHubRepository
  url: https://github.com/magiceden/magiceden-sdk
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MagicEden
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/magic-eden-context.jsonld
- group: design
  title: ''
  type: JSONLDProvider
  url: json-ld/magic-eden-provider.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/magic-eden-collection.json
created: '2026-05-24'
description: Magic Eden is a multi-chain NFT marketplace offering REST and instruction-generation APIs for Solana, EVM chains (Ethereum, Polygon, Base, ApeChain, Arbitrum, Berachain, BSC, SEI, Abstract), and Bitcoin Ordinals (inscriptions, rare sats, and runes). Developers can fetch collections, tokens, listings, bids, activity, holder stats, AMM pool data, launchpad data, and generate signed transactions or PSBTs for listing, buying, bidding, transferring, swapping, and minting across all supported chains.
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
- name: Magic Eden Finops
  service_category: Web3
  slug: magic-eden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magic-eden.png
json_schemas:
- name: MagicEdenActivity
  property_count: 12
  slug: magic-eden-activity
- name: MagicEdenAMMPool
  property_count: 17
  slug: magic-eden-amm-pool
- name: MagicEdenCollection
  property_count: 19
  slug: magic-eden-collection
- name: MagicEdenNFTToken
  property_count: 18
  slug: magic-eden-nft-token
- name: MagicEdenWallet
  property_count: 7
  slug: magic-eden-wallet
jsonld:
- class_count: 61
  name: Magic Eden Context
  property_count: 0
  slug: magic-eden-context
- class_count: 0
  name: Magic Eden Provider Context
  property_count: 0
  slug: magic-eden-provider
layout: provider
modified: '2026-08-08'
name: Magic Eden
nav: Providers
network: true
overview: 'Magic Eden publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Assets API, Blocks API, and 16 more. Tagged areas include NFT, Web3, Blockchain, Marketplace, and Solana.


  The Magic Eden catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Magic Eden''s developer surface includes authentication, developer portal, API reference, getting-started guide, changelog, documentation, and 22 more developer resources.'
plans:
- name: Magic Eden Plans Pricing
  plan_count: 2
  slug: magic-eden-plans-pricing
- name: Magic Eden Plans
  plan_count: 2
  slug: magic-eden-plans
random_paper: 42
rate_limits:
- limit_count: 4
  name: Magic Eden Rate Limits
  slug: magic-eden-rate-limits
rules:
- name: Magic Eden API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: magic-eden-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.2
  delta: 1.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.1
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magic-eden/refs/heads/main/screenshots/magic-eden-2026-06-20T184844.png
security:
- kind: authentication
  name: Magic Eden Authentication
  slug: magic-eden-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Magic Eden Domain Security
  slug: magic-eden-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Magic Eden Vulnerability Disclosure
  slug: magic-eden-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: magic-eden
tags:
- NFT
- Web3
- Blockchain
- Marketplace
- Solana
- Ethereum
- Bitcoin
- Ordinals
- Runes
- Multi-chain
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
