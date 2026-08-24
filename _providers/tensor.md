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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Tensor Agentic Access
  operation_count: 47
  slug: tensor-agentic-access
  summary_line: 47 operations · 2 acting
api_count: 9
apis:
- description: Subscription-based realtime stream of Tensor marketplace events. Channels include `newTransaction` (every confirmed marketplace action), `ammOrderUpdate` / `ammOrderUpdateAll` (TSwap and TAmm pool sta
  name: Tensor WebSocket API
  slug: tensor-websocket-api
- description: The Bids API from Tensor — 8 operation(s) for bids.
  name: Tensor Bids API
  slug: tensor-bids-api
- description: The Collections API from Tensor — 5 operation(s) for collections.
  name: Tensor Collections API
  slug: tensor-collections-api
- description: The Escrow API from Tensor — 2 operation(s) for escrow.
  name: Tensor Escrow API
  slug: tensor-escrow-api
- description: The Listings API from Tensor — 6 operation(s) for listings.
  name: Tensor Listings API
  slug: tensor-listings-api
- description: The NFTs API from Tensor — 3 operation(s) for nfts.
  name: Tensor NFTs API
  slug: tensor-nfts-api
- description: The Pools API from Tensor — 7 operation(s) for pools.
  name: Tensor Pools API
  slug: tensor-pools-api
- description: The User API from Tensor — 10 operation(s) for user.
  name: Tensor User API
  slug: tensor-user-api
- description: The Utility API from Tensor — 6 operation(s) for utility.
  name: Tensor Utility API
  slug: tensor-utility-api
artifact_total: 56
asyncapis:
- description: Realtime subscription stream for the Tensor Solana NFT marketplace. Clients open a single WebSocket connection authenticated with `x-tensor-api-key`, then send JSON subscribe/unsubscribe control frame
  name: Tensor WebSocket API
  slug: tensor-websocket-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tensor API
  slug: open-tensor-api
- collection_type: open
  name: Tensor Bids API
  slug: open-tensor-bids-api
- collection_type: open
  name: Tensor Bids Collections API
  slug: open-tensor-collections-api
- collection_type: open
  name: Tensor Bids Escrow API
  slug: open-tensor-escrow-api
- collection_type: open
  name: Tensor Bids Listings API
  slug: open-tensor-listings-api
- collection_type: open
  name: Tensor Bids NFTs API
  slug: open-tensor-nfts-api
- collection_type: open
  name: Tensor Bids Pools API
  slug: open-tensor-pools-api
- collection_type: open
  name: Tensor Transaction (TX) API
  slug: open-tensor-tx-api
- collection_type: open
  name: Tensor Bids User API
  slug: open-tensor-user-api
- collection_type: open
  name: Tensor Bids Utility API
  slug: open-tensor-utility-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tensor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tensor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tensor-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://tensor.trade
- group: start
  title: ''
  type: Portal
  url: https://www.tensor.foundation
- group: start
  title: ''
  type: Portal
  url: https://dev.tensor.trade
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tensor.trade/docs
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tensor.trade/reference
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tensor.trade/changelog
- group: build
  title: ''
  type: CodeExamples
  url: https://dev.tensor.trade/recipes
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.tensor.trade/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tensor.trade/docs/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tensor.trade/docs/sdks-and-examples
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensor.trade/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensor.foundation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensor.foundation/tokenomics
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensor.foundation/governance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensor.foundation/audits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensor.foundation/grants
- group: operate
  title: ''
  type: Forums
  url: https://app.realms.today/dao/TNSR
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tensor-foundation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tensor-hq
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tensor-foundation/marketplace
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tensor-foundation/amm
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tensor-foundation/escrow
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tensor-foundation/whitelist
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tensor-foundation/fees
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-foundation/marketplace
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-foundation/amm
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-foundation/whitelist
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-foundation/escrow
- group: build
  title: ''
  type: SDKs
  url: https://crates.io/crates/tensor-marketplace
- group: build
  title: ''
  type: SDKs
  url: https://crates.io/crates/tensor-amm
- group: build
  title: ''
  type: SDKs
  url: https://crates.io/crates/tensor-whitelist
- group: build
  title: ''
  type: SDKs
  url: https://crates.io/crates/tensor-escrow
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-oss/tensorswap-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-oss/tcomp-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tensor-oss/ledger-solana-sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/tensor-foundation/SDK-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/tensor-hq/marketplace-nextjs-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/tensor-hq/salesbot-discord-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/tensor-hq/fpchecker-telegram-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensor-hq/toolbox
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensor-hq/toolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensor-hq/smart-rpc
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensor-hq/Unified-Wallet-Kit
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensor-hq/simple-nft-wash-trade-detection
- group: start
  title: ''
  type: Signup
  url: https://airtable.com/apppFpk6Ul9yiI6sw/pagCBazYyAewboZnT/form
- group: other
  title: ''
  type: SocialMedia
  url: https://twitter.com/tensor_hq
- group: other
  title: ''
  type: SocialMedia
  url: https://twitter.com/TNSR_DAO
- group: commercial
  title: ''
  type: Plans
  url: plans/tensor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tensor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tensor-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dev.tensor.trade/changelog
created: '2026-05-24T00:00:00.000Z'
description: Tensor is the Solana-native NFT marketplace and trading protocol founded by Tensor HQ and now stewarded by the Tensor Foundation. The platform exposes a public read REST API, a transaction-construction (TX) API that returns unsigned Solana transactions for list / buy / bid / pool flows, and a WebSocket subscription stream for realtime marketplace events. Five open-source Anchor programs — Marketplace, AMM v2, Whitelist, Escrow, and Fees — back the protocol and ship as `@tensor-foundation/*` JavaScript SDKs and `tensor-*` Rust crates. Tensor supports legacy NFTs, programmable NFTs (pNFT), and Bubblegum compressed NFTs (cNFT), and serves as the execution layer behind aggregators, wallets, sales bots, and AMM bonding-curve liquidity providers across the Solana ecosystem. Governance and ecosystem grants flow through the TNSR token and the Tensor DAO on Realms.
examples:
- key_count: 2
  name: Tensor Active Listings Example
  slug: tensor-active-listings-example
- key_count: 2
  name: Tensor Collection Find Example
  slug: tensor-collection-find-example
- key_count: 2
  name: Tensor Tx Buy Example
  slug: tensor-tx-buy-example
- key_count: 2
  name: Tensor Tx List Example
  slug: tensor-tx-list-example
features:
- Solana's leading NFT marketplace covering 30,000+ collections with deep liquidity
- Read API (REST) covering collections, listings, bids, pools, mints, user portfolios, transaction history, and royalty enforcement
- Transaction (TX) API that returns unsigned base64 Solana transactions for list / delist / buy / bid / pool ops — clients sign locally
- WebSocket subscriptions for `newTransaction`, `ammOrderUpdate`, `tcompBidUpdate`, with ping/unsubscribe control frames
- Supports legacy NFTs, programmable NFTs (pNFT), and Bubblegum compressed NFTs (cNFT)
- TensorSwap AMM v2 with bonding curves (linear, exponential) and shared escrow for capital-efficient market making
- Collection-wide bids, single-NFT bids, and trait-attribute bids
- Creator Portal — collection claim/verification, launchpad, and royalty configuration
- YOLO Buy aggregator and floor-purchase recipes
- On-chain programs are open-source (Apache-2.0) Anchor programs published as IDLs, npm packages, and Rust crates
- Five official programs — Marketplace, AMM v2, Whitelist, Escrow, Fees — each shipped as `@tensor-foundation/*` npm and `tensor-*` crates.io packages
- Authentication via `x-tensor-api-key` header issued through dev.tensor.trade after Airtable application
- smart-rpc transport, Unified Wallet Kit, Next.js / Discord / Telegram starter templates published on GitHub
- TNSR token (mint `TNSRxcUxoT9xBG3de7PiJyTDYu7kskLqcpddxnEJAS6`) — 1B supply, governance via Realms DAO at app.realms.today/dao/TNSR
- Tensor Foundation Grants program for ecosystem builders
- Multiple third-party audits of Anchor programs published at docs.tensor.foundation/audits
finops:
- name: Tensor Finops
  service_category: ''
  slug: tensor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tensor.png
json_schemas:
- name: Tensor Bid
  property_count: 11
  slug: tensor-bid
- name: Tensor Collection
  property_count: 18
  slug: tensor-collection
- name: Tensor Listing
  property_count: 10
  slug: tensor-listing
- name: Tensor Mint
  property_count: 10
  slug: tensor-mint
- name: Tensor AMM Pool
  property_count: 12
  slug: tensor-pool
jsonld:
- class_count: 47
  name: Tensor Context
  property_count: 3
  slug: tensor-context
layout: provider
modified: '2026-05-24'
name: Tensor
nav: Providers
network: true
overview: 'Tensor publishes 9 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, Bids API, Collections API, and 6 more. Tagged areas include NFT, Marketplace, Solana, Blockchain, and Web3.


  The Tensor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Tensor''s developer surface includes authentication, developer portal, documentation, code examples, getting-started guide, tooling, signup flow, and 47 more developer resources.'
plans:
- name: Tensor Plans Pricing
  plan_count: 2
  slug: tensor-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Tensor Rate Limits
  slug: tensor-rate-limits
rules:
- effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Tensor API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: tensor-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Tensor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tensor-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Tensor API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: tensor-rules
score:
  band: developing
  composite: 53.0
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 71.6
    developer_ergonomics: 61.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 36.8
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tensor/refs/heads/main/screenshots/tensor-2026-06-20T195119.png
security:
- kind: authentication
  name: Tensor Authentication
  slug: tensor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tensor Domain Security
  slug: tensor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tensor
tags:
- NFT
- Marketplace
- Solana
- Blockchain
- Web3
- Cryptocurrency
- Trading
- DAO
- DeFi
- AMM
website: https://tensor.trade
---
