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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Manifold Agentic Access
  operation_count: 2
  slug: manifold-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 7
apis:
- description: Open-source Solidity smart contract framework for deploying ERC721 and ERC1155 creator-owned NFT contracts. Provides minting, metadata modification, transfer, burn, and on-chain royalty configuration.
  name: Manifold Creator Core Smart Contracts
  slug: creator-core-contracts
- description: REST API backing Manifold's Client SDK, providing product instance data and purchase preparation information for minting dApps. Used to fetch Edition and BlindMint product details, validate eligibilit
  name: Manifold Studio Apps API
  slug: studio-apps-api
- description: On-chain smart contract registry that serves as a single source of truth for NFT royalties across all major marketplaces. Provides setRoyaltyLookupAddress() to override per-contract royalty destinatio
  name: Manifold Royalty Registry
  slug: royalty-registry
- description: Smart contract system powering Manifold Gallery listings and Marketplace Widgets. Supports Auction Listings (single NFT with bidding, configurable floor price, minimum bid increment, and extension int
  name: Manifold Marketplace Contracts
  slug: marketplace-contracts
- description: JavaScript widget library for embedding NFT minting and claim flows into any website or dApp. Served from claims.manifoldxyz.dev, current version 1.16.1. Configured via data-widget (claim type) and da
  name: Manifold Claim Widgets
  slug: claim-widgets
- description: Exchange a one-time authorization code for a long-lived access token allowing server-side access to private user data.
  name: Manifold Authorization Code Grant API
  slug: manifold-authorization-code-grant-api
- description: Validate a wallet signature session token to confirm a user's wallet address server-side.
  name: Manifold Signature Grant API
  slug: manifold-signature-grant-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Manifold OAuth2 Authentication Authorization Code Grant API
  slug: open-manifold-authorization-code-grant-api
- collection_type: open
  name: Manifold OAuth2 Authentication Authorization Code Grant Signature Grant API
  slug: open-manifold-signature-grant-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/manifold-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manifold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://manifold.xyz
- group: other
  title: ''
  type: Studio
  url: https://studio.manifold.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.manifold.xyz
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://docs.manifold.xyz/manifold-for-developers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/manifoldxyz
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.manifold.xyz/en/
- group: company
  title: ''
  type: Blog
  url: https://manifoldxyz.substack.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/manifoldxyz
- group: other
  title: ''
  type: ContractAddresses
  url: https://docs.manifold.xyz/contracts
- group: docs
  title: ''
  type: DocsIndex
  url: https://docs.manifold.xyz/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/manifold-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/manifold-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/manifold-finops.yml
created: '2026-06-13'
description: Manifold is an NFT creator tools platform that empowers artists and developers to deploy their own creator-owned smart contracts, mint NFTs, and build custom on-chain experiences without relying on platform-specific custody. Founded in 2021, Manifold provides a no-code studio (Manifold Studio) for ERC721 and ERC1155 contract deployment, open-source Creator Core smart contracts, a Royalty Registry adopted by all major NFT marketplaces, and a Client SDK for building custom minting dApps. The platform supports Ethereum Mainnet, Base, Optimism, Shape, Apechain, and Sepolia testnet. Manifold also exposes server-side authentication APIs (Signature Grant and Authorization Code Grant via oauth2.manifoldxyz.dev), a Studio Apps REST API (apps.api.manifoldxyz.dev) for product and minting data, open-source Solidity extension contracts for custom mint mechanics, and a Marketplace contract powering auction and fixed-price listings. Gas fees are the only cost for creators; Manifold charges
  no platform fees or royalties on sales.
finops:
- name: Manifold Finops
  service_category: Blockchain / Web3 Developer Tools
  slug: manifold-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manifold.png
json_schemas:
- name: Manifold OAuth2 Authentication API Schemas
  property_count: 0
  slug: manifold-oauth2-authentication
layout: provider
modified: '2026-06-13'
name: Manifold
nav: Providers
network: true
overview: 'Manifold publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authorization Code Grant API and Signature Grant API. Tagged areas include NFT, Creator Tools, Smart Contracts, Blockchain, and Web3.


  The Manifold catalog on APIs.io includes 1 Spectral governance ruleset.


  Manifold''s developer surface includes documentation, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Manifold Plans Pricing
  plan_count: 1
  slug: manifold-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Manifold Rate Limits
  slug: manifold-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Manifold API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: manifold-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.7
  delta: -7.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 56.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/manifold/refs/heads/main/screenshots/manifold-2026-06-20T184923.png
security:
- kind: domain-security
  name: Manifold Domain Security
  slug: manifold-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: manifold
tags:
- NFT
- Creator Tools
- Smart Contracts
- Blockchain
- Web3
- Ethereum
- ERC721
- ERC1155
- Royalties
- Marketplace
- Minting
- OpenSea
- Base
- Optimism
website: https://manifold.xyz
---
