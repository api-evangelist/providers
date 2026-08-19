---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Looksrare Agentic Access
  operation_count: 10
  slug: looksrare-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 8
apis:
- description: Retrieve token and order activity events from the LooksRare marketplace including LIST, SALE, OFFER, CANCEL_LIST, and CANCEL_OFFER event types. GET /v2/events supports filtering by collection address,
  name: LooksRare Events API
  slug: events-api
- description: 'Retrieve NFT token metadata including token details, collection information, and token attributes for any token indexed by LooksRare. GET /v1/tokens accepts a collection contract address and token ID '
  name: LooksRare Tokens API
  slug: tokens-api
- description: Retrieve collection-level data for NFT collections indexed on LooksRare. Endpoints return Collection objects including logoURI, bannerURI, and collection statistics. The /v2/collections/seaport endpoi
  name: LooksRare Collections API
  slug: collections-api
- description: Retrieve NFT collection-level metadata, statistics, and integration eligibility.
  name: LooksRare Collections API
  slug: looksrare-collections-api
- description: Retrieve token and order activity events from the LooksRare marketplace, including listings, sales, offers, and cancellations.
  name: LooksRare Events API
  slug: looksrare-events-api
- description: Read and write NFT maker orders in the LooksRare V2 off-chain order book. Supports both standard (specific token) and collection-wide strategies for asks (listings) and bids (offers).
  name: LooksRare Orders API
  slug: looksrare-orders-api
- description: Endpoints specific to the LooksRare Seaport integration, enabling Seaport-compatible orders and events while earning LooksRare rewards.
  name: LooksRare Seaport API
  slug: looksrare-seaport-api
- description: Retrieve NFT token metadata including collection information and on-chain attribute traits.
  name: LooksRare Tokens API
  slug: looksrare-tokens-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LooksRare Public Collections API
  slug: open-looksrare-collections-api
- collection_type: open
  name: LooksRare Public Collections Events API
  slug: open-looksrare-events-api
- collection_type: open
  name: LooksRare Public Collections Orders API
  slug: open-looksrare-orders-api
- collection_type: open
  name: LooksRare Public Collections Seaport API
  slug: open-looksrare-seaport-api
- collection_type: open
  name: LooksRare Public Collections Tokens API
  slug: open-looksrare-tokens-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/looksrare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/looksrare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/looksrare-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://looksrare.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.looksrare.org/developers/welcome
- group: start
  title: ''
  type: Portal
  url: https://looksrare.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://looksrare.dev/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LooksRare
- group: build
  title: LooksRare SDK v2 (TypeScript)
  type: SDKs
  url: https://github.com/LooksRare/sdk-v2
- group: build
  title: '@looksrare/sdk-v2 (npm)'
  type: SDKs
  url: https://www.npmjs.com/package/@looksrare/sdk-v2
- group: operate
  title: Developer Discord
  type: Discord
  url: https://discord.gg/LooksRareDevelopers
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LooksRare
- group: company
  title: ''
  type: Blog
  url: https://docs.looksrare.org/blog
- group: docs
  title: LooksRare V2 Protocol Overview
  type: ProtocolDocs
  url: https://docs.looksrare.org/developers/protocol/looksrare-v2-protocol-overview
- group: commercial
  title: ''
  type: Plans
  url: plans/looksrare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/looksrare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/looksrare-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/looksrare.jsonld
created: '2026-06-13'
description: LooksRare is a community-first NFT marketplace built on Ethereum that rewards traders, collectors, and creators with LOOKS token incentives. The platform operates an off-chain order book with on-chain settlement via the LooksRare V2 protocol (and Seaport integration), supporting standard and collection-wide orders for ERC-721 and ERC-1155 tokens. The public REST API exposes read and write access to orders, events (listings, sales, offers, cancellations), token metadata, and collection data across Ethereum Mainnet and the Sepolia testnet. API access is free with attribution; a mainnet API key is required for write operations such as order creation.
finops:
- name: Looksrare Finops
  service_category: API
  slug: looksrare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/looksrare.png
jsonld:
- class_count: 62
  name: Looksrare Context
  property_count: 5
  slug: looksrare
layout: provider
modified: '2026-06-13'
name: LooksRare
nav: Providers
network: true
overview: 'LooksRare publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Events API, Orders API, and 2 more. Tagged areas include NFT, Marketplace, Ethereum, Web3, and Orders.


  The LooksRare catalog on APIs.io includes 1 JSON-LD context.


  LooksRare''s developer surface includes authentication, documentation, developer portal, changelog, engineering blog, and 13 more developer resources.'
plans:
- name: Looksrare Plans Pricing
  plan_count: 2
  slug: looksrare-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 4
  name: Looksrare Rate Limits
  slug: looksrare-rate-limits
score:
  band: developing
  composite: 43.9
  delta: -1.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 64.9
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/looksrare/refs/heads/main/screenshots/looksrare-2026-06-20T184713.png
security:
- kind: authentication
  name: Looksrare Authentication
  slug: looksrare-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Looksrare Domain Security
  slug: looksrare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: looksrare
tags:
- NFT
- Marketplace
- Ethereum
- Web3
- Orders
- Collections
- Tokens
- Events
- ERC-721
- ERC-1155
- Seaport
- Community
website: https://looksrare.org
---
