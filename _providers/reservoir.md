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
    auth_clarity: bearer
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
  score: 18.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: All-in-one NFT data and trading API enabling developers to get NFT data, create orders, and execute trades across 30+ EVM-compatible blockchains. Aggregates liquidity from major NFT marketplaces inclu
  name: Reservoir NFT API
  slug: reservoir-nft-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reservoir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reservoir.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://nft.reservoir.tools/reference/overview
- group: build
  title: ''
  type: GitHub
  url: https://github.com/reservoirprotocol
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uneven-labs
- group: company
  title: ''
  type: Blog
  url: https://reservoir.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://reservoir.tools/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reservoir.tools/
- group: other
  title: ''
  type: X
  url: https://x.com/reservoir0x
- group: commercial
  title: ''
  type: Plans
  url: plans/reservoir-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reservoir-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reservoir-finops.yml
created: '2026-06-12'
description: NFT marketplace infrastructure and data API for aggregating listings, bids, and sales across OpenSea, Blur, and other markets — powers buying, selling, and analytics across 30+ EVM chains. Reservoir provided a complete suite of APIs, SDKs, and UI kits abstracting the complexity of interacting with the NFT market. The service was sunset on October 15, 2025.
finops:
- name: Reservoir Finops
  service_category: ''
  slug: reservoir-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reservoir.png
jsonld:
- class_count: 11
  name: Reservoir Context
  property_count: 37
  slug: reservoir-context
layout: provider
modified: '2026-06-12'
name: Reservoir
nav: Providers
network: true
overview: 'Reservoir publishes 1 API on the [APIs.io](https://apis.io/) network: NFT API. Tagged areas include NFT, Blockchain, Marketplace, Ethereum, and EVM.


  The Reservoir catalog on APIs.io includes 1 JSON-LD context.


  Reservoir''s developer surface includes documentation, GitHub presence, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Reservoir Plans Pricing
  plan_count: 3
  slug: reservoir-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Reservoir Rate Limits
  slug: reservoir-rate-limits
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 41.3
    developer_ergonomics: 17.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reservoir/refs/heads/main/screenshots/reservoir-2026-06-20T193029.png
security:
- kind: domain-security
  name: Reservoir Domain Security
  slug: reservoir-domain-security
  summary_line: DMARC
slug: reservoir
tags:
- NFT
- Blockchain
- Marketplace
- Ethereum
- EVM
- Liquidity
- Order Book
- Web3
- DeFi
- Trading
- Data API
website: https://reservoir.dev/
---
