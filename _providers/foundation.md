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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: GraphQL API powered by The Graph protocol that indexes all Foundation NFT marketplace activity on Ethereum mainnet. Supports queries for NFTs, creators, collectors, auctions, bids, offers, buy-now lis
  name: Foundation Subgraph API
  slug: foundation-subgraph-api
- description: 'Ethereum smart contract interface for direct on-chain interaction with Foundation marketplace contracts. Supports minting NFTs, creating and bidding in auctions, placing and accepting offers, buy-now '
  name: Foundation Smart Contract API
  slug: foundation-smart-contract-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foundation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/f8n
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundation.app/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundation.app/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/foundation
- group: company
  title: ''
  type: Blog
  url: https://foundation.app/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foundationapp
created: '2026-06-13'
description: Foundation is a creator-focused NFT marketplace built on Ethereum that enables digital artists to mint, showcase, and auction unique digital artworks. The platform provides a GraphQL API via The Graph protocol for querying artwork, auctions, bids, collector profiles, offers, buy-now listings, and edition drop data. Foundation smart contracts remain live on Ethereum mainnet, and the subgraph continues to index on-chain activity for programmatic access.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Foundation was a creator-focused NFT marketplace built on Ethereum that enabled digital artists to mint, showcase, and auction unique digital artworks. The platform exposed a GraphQL API via The Graph
  name: Foundation GraphQL API
  slug: foundation-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foundation.png
layout: provider
modified: '2026-06-13'
name: Foundation
nav: Providers
network: true
overview: 'Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include NFT, Digital Art, Marketplace, Ethereum, and Web3.


  Foundation''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 52
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 30.9
  delta: 8.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 43.2
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/foundation/refs/heads/main/screenshots/foundation-2026-06-20T181453.png
security:
- kind: domain-security
  name: Foundation Domain Security
  slug: foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Foundation Vulnerability Disclosure
  slug: foundation-vulnerability-disclosure
  summary_line: disclosure policy published
slug: foundation
tags:
- NFT
- Digital Art
- Marketplace
- Ethereum
- Web3
- Blockchain
- Creators
- Auctions
- Collectors
---
