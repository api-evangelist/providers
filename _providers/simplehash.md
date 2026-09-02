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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Multi-chain REST API providing NFT metadata, ownership, transfers, floor prices, listings, bids, spam scores, and fungible token market prices across 80+ blockchains and testnets. Supports bulk lookup
  name: SimpleHash NFT & Token API
  slug: nft-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simplehash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplehash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simplehash.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simplehash.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/simplehash
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplehash/
- group: company
  title: ''
  type: Blog
  url: https://simplehash.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://simplehash.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://simplehash.betteruptime.com/
- group: other
  title: ''
  type: X
  url: https://x.com/SimpleHashInc
- group: commercial
  title: ''
  type: Plans
  url: plans/simplehash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simplehash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simplehash-finops.yml
created: '2026-06-12'
description: NFT data API aggregating metadata, ownership, transfers, floor prices, and token market data across 80+ blockchains. Provides REST API, webhooks, and Kafka streaming used by wallets, marketplaces, and analytics platforms including Coinbase, Phantom, Ledger, and Uniswap. Indexes 3B+ tokens and NFTs with 99.999% uptime SLA.
finops:
- name: Simplehash Finops
  service_category: ''
  slug: simplehash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplehash.png
jsonld:
- class_count: 29
  name: Simplehash Context
  property_count: 8
  slug: simplehash-context
layout: provider
modified: '2026-06-12'
name: SimpleHash
nav: Providers
network: true
overview: 'SimpleHash publishes 1 API on the [APIs.io](https://apis.io/) network: NFT & Token API. Tagged areas include NFT, Blockchain, Web3, Cryptocurrency, and Token.


  The SimpleHash catalog on APIs.io includes 1 JSON-LD context.


  SimpleHash''s developer surface includes documentation, GitHub presence, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Simplehash Plans Pricing
  plan_count: 2
  slug: simplehash-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Simplehash Rate Limits
  slug: simplehash-rate-limits
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simplehash/refs/heads/main/screenshots/simplehash-2026-06-20T193931.png
security:
- kind: domain-security
  name: Simplehash Domain Security
  slug: simplehash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Simplehash Vulnerability Disclosure
  slug: simplehash-vulnerability-disclosure
  summary_line: disclosure policy published
slug: simplehash
tags:
- NFT
- Blockchain
- Web3
- Cryptocurrency
- Token
- Metadata
- Multi-Chain
- Ethereum
- Solana
- Base
- Polygon
website: https://simplehash.com/
---
