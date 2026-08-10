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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Superrare Agentic Access
  operation_count: 17
  slug: superrare-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 10
apis:
- description: SDK and CLI for programmatic management of rare.xyz creator profiles, storefronts, products, posts, social interactions, messages, analytics, and events. Uses OAuth device flow authentication with sco
  name: SuperRare Profile & Creator API
  slug: superrare-profile-creator-api
- description: 'Command-line interface and SDK for deploying ERC-721 NFT collections, minting tokens, managing reserve-price auctions, and querying tokens and collections on Ethereum Mainnet, Sepolia, Base, and Base '
  name: SuperRare Rare Protocol CLI
  slug: superrare-rare-protocol-cli
- description: Unified marketplace and auction house smart contract on Ethereum that enables reserve-price auctions, sale price listings, offer placement, and bid management for curated digital art NFTs. Supports no
  name: SuperRare Smart Contracts - The Bazaar
  slug: superrare-smart-contracts-the-bazaar
- description: SuperRare ERC-721 NFT asset contracts including shared minting contracts (SuperRareV1, SuperRareV2), creator-owned Sovereign minting contracts (Series), and curator-managed Space contracts. The Approv
  name: SuperRare Smart Contracts - Assets (ERC-721)
  slug: superrare-smart-contracts-assets-erc-721
- description: List, retrieve, and import NFT collections
  name: SuperRare Collections API
  slug: superrare-collections-api
- description: Upload and process NFT media assets to IPFS
  name: SuperRare Media API
  slug: superrare-media-api
- description: Generate and manage Merkle roots and proofs for batch operations
  name: SuperRare Merkle Roots API
  slug: superrare-merkle-roots-api
- description: Search, retrieve, and manage NFT tokens and metadata
  name: SuperRare NFTs API
  slug: superrare-nfts-api
- description: Retrieve token price data
  name: SuperRare Tokens API
  slug: superrare-tokens-api
- description: Retrieve user profile information
  name: SuperRare Users API
  slug: superrare-users-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superrare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superrare-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.superrare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superrare.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.superrare.com/
- group: operate
  title: ''
  type: Forums
  url: https://forum.rare.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superrare
- group: company
  title: ''
  type: Website
  url: https://superrare.com/
- group: company
  title: ''
  type: Blog
  url: https://superrare.com/magazine
- group: other
  title: ''
  type: Marketplace
  url: https://superrare.com/explore
- group: other
  title: ''
  type: Governance
  url: https://docs.superrare.com/
- group: other
  title: ''
  type: WhitePaper
  url: https://docs.superrare.com/whitepapers/master
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campaigns.superrare.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@rareprotocol/rare-cli
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@rareprotocol/rare-profile
created: '2026-06-13'
description: SuperRare is a premier digital art marketplace and auction house built on Ethereum for discovering, collecting, and trading unique single-edition digital artworks as NFTs. The platform provides REST APIs, a profile/creator SDK, smart contract interfaces, and a CLI for accessing artwork metadata, artist profiles, auction data, edition information, and sales history.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superrare.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: SuperRare
nav: Providers
network: true
overview: 'SuperRare publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Media API, Merkle Roots API, and 3 more. Tagged areas include NFT, Digital Art, Marketplace, Ethereum, and Blockchain.


  The SuperRare catalog on APIs.io includes 1 JSON-LD context.


  SuperRare''s developer surface includes developer portal, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 57
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.2
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superrare/refs/heads/main/screenshots/superrare-2026-06-20T194728.png
security:
- kind: domain-security
  name: Superrare Domain Security
  slug: superrare-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: superrare
tags:
- NFT
- Digital Art
- Marketplace
- Ethereum
- Blockchain
- Auctions
- Collectibles
website: https://superrare.com/
---
