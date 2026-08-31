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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blur-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blur-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blur.io
- group: other
  title: ''
  type: Foundation
  url: https://blur.foundation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blur.foundation
- group: other
  title: ''
  type: Governance
  url: https://gov.blur.foundation
- group: auth
  title: ''
  type: Tokenomics
  url: https://docs.blur.foundation/tokenomics
- group: other
  title: ''
  type: Contracts
  url: https://docs.blur.foundation/contracts
- group: other
  title: ''
  type: Metrics
  url: https://docs.blur.foundation/metrics
- group: other
  title: ''
  type: HolderAirdrop
  url: https://hold.blur.foundation
- group: other
  title: ''
  type: BrandAssets
  url: https://blur.gitbook.io/blur-foundation/UB7gUEpwmYsMGrZHwZFm/brand-assets
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drive.google.com/file/d/1MruZnfSInUcz71z6UYoHaDA2rOiWYSgI/view
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/blur_io
- group: company
  title: ''
  type: TwitterFoundation
  url: https://twitter.com/blurfoundation
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/blurdao
- group: build
  title: ''
  type: GitHub
  url: https://github.com/blur-io
- group: start
  title: ''
  type: OperatorFilterRegistry
  url: https://github.com/blur-io/operator-filter-registry
created: '2026-05-24'
description: Blur is a New York-based NFT marketplace and aggregator built for professional traders on Ethereum, founded by the pseudonymous "Pacman" (Tieshun Roquerre) in October 2022 and backed by Paradigm and Standard Crypto. The flagship product, blur.io, offers zero marketplace fees, multi-marketplace sweeping, bulk listing/bidding, real-time mempool reveal sniping, and a portfolio-grade analytics surface that aggregates liquidity from OpenSea, X2Y2, LooksRare, and other Seaport-compatible venues. Blur also operates Blend, a peer-to-peer perpetual NFT lending protocol designed by Paradigm researchers that powers ETH-against-NFT borrowing and Buy-Now-Pay-Later flows without oracles or fixed expiries — Blend has captured the dominant share of NFT lending volume on Ethereum. The BLUR token, distributed via multi-season airdrop campaigns, governs the Blur DAO through the Blur Foundation. The same team launched Blast, an Ethereum L2 with native yield, which now hosts its own NFT activity.
  Blur does not publish an official public developer API or SDK; on-chain integration happens via the deployed marketplace and Blend smart contracts (Seaport-compatible), and marketplace data is reached through third-party indexers such as Bitquery, SimpleHash, and Alchemy rather than a Blur-operated REST or GraphQL endpoint.
graphqls:
- description: ''
  name: Blur GraphQL API
  slug: blur-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blur.png
layout: provider
modified: '2026-05-24'
name: Blur
nav: Providers
network: true
overview: 'Blur is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include NFT, NFT Marketplace, NFT Aggregator, NFT Lending, and Ethereum.


  Blur''s developer surface includes documentation, GitHub presence, and 15 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blur/refs/heads/main/screenshots/blur-2026-06-20T173536.png
security:
- kind: domain-security
  name: Blur Domain Security
  slug: blur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blur Vulnerability Disclosure
  slug: blur-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blur
tags:
- NFT
- NFT Marketplace
- NFT Aggregator
- NFT Lending
- Ethereum
- Web3
- Blockchain
- DeFi
- Smart Contracts
- Seaport
- Blend
- BLUR Token
- DAO
- Governance
- Blast L2
- Pro Trading
website: https://blur.io
---
