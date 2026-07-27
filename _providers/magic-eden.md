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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
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
artifact_total: 29
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
created: '2026-05-24'
description: Magic Eden is a multi-chain NFT marketplace offering REST and instruction-generation APIs for Solana, EVM chains (Ethereum, Polygon, Base, ApeChain, Arbitrum, Berachain, BSC, SEI, Abstract), and Bitcoin Ordinals (inscriptions, rare sats, and runes). Developers can fetch collections, tokens, listings, bids, activity, holder stats, AMM pool data, launchpad data, and generate signed transactions or PSBTs for listing, buying, bidding, transferring, swapping, and minting across all supported chains.
finops:
- name: Magic Eden Finops
  service_category: Web3
  slug: magic-eden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magic-eden.png
layout: provider
modified: '2026-05-24'
name: Magic Eden
nav: Providers
network: true
overview: 'Magic Eden publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Assets API, Blocks API, and 16 more. Tagged areas include NFT, Web3, Blockchain, Marketplace, and Solana.


  Magic Eden''s developer surface includes authentication, developer portal, API reference, getting-started guide, changelog, and 14 more developer resources.'
plans:
- name: Magic Eden Plans Pricing
  plan_count: 2
  slug: magic-eden-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Magic Eden Rate Limits
  slug: magic-eden-rate-limits
score:
  band: thin
  composite: 44.9
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.7
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 41.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magic-eden/refs/heads/main/screenshots/magic-eden-2026-06-20T184841.png
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
website: https://magiceden.io
---
