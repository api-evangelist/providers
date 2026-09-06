---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Footprint Agentic Access
  operation_count: 16
  slug: footprint-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: Chain-level block and transaction data
  name: Footprint Analytics Chain API
  slug: footprint-chain-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: DeFi protocol metrics including TVL, DEX liquidity, and yield
  name: Footprint Analytics DeFi API
  slug: footprint-defi-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: Track user events via Growth Analytics SDK
  name: Footprint Analytics Events API
  slug: footprint-events-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: Blockchain gaming economics and player analytics
  name: Footprint Analytics GameFi API
  slug: footprint-gamefi-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: NFT collection and token market data
  name: Footprint Analytics NFT API
  slug: footprint-nft-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: Execute SQL queries against blockchain datasets
  name: Footprint Analytics Query API
  slug: footprint-query-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: Token price, supply, and holder analytics
  name: Footprint Analytics Token API
  slug: footprint-token-api
- baseURL: https://api.footprint.network
  baseurl_source: declared
  description: Wallet profile, portfolio, and eligibility checks
  name: Footprint Analytics Wallet API
  slug: footprint-wallet-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Footprint Analytics Data Chain API
  slug: open-footprint-chain-api
- collection_type: open
  name: Footprint Analytics Data Chain DeFi API
  slug: open-footprint-defi-api
- collection_type: open
  name: Footprint Analytics Data Chain Events API
  slug: open-footprint-events-api
- collection_type: open
  name: Footprint Analytics Data Chain GameFi API
  slug: open-footprint-gamefi-api
- collection_type: open
  name: Footprint Analytics Data Chain NFT API
  slug: open-footprint-nft-api
- collection_type: open
  name: Footprint Analytics Data Chain Query API
  slug: open-footprint-query-api
- collection_type: open
  name: Footprint Analytics Data Chain Token API
  slug: open-footprint-token-api
- collection_type: open
  name: Footprint Analytics Data Chain Wallet API
  slug: open-footprint-wallet-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/footprint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/footprint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/footprint-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.footprint.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.footprint.network/docs/get-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/footprintanalytics
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@footprintofficial
- group: commercial
  title: ''
  type: Pricing
  url: https://www.footprint.network/data-api
- group: operate
  title: ''
  type: Status
  url: https://www.footprint.network/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.footprint.network/docs/get-started
created: '2026-06-14'
description: Footprint Analytics is a blockchain data analytics platform providing unified REST and SQL APIs for querying DeFi protocol metrics, NFT market data, token analytics, GameFi economics, and on-chain activity across 30+ chains including Ethereum, Bitcoin, Solana, BNB Chain, Polygon, Arbitrum, Optimism, and Sui. The platform indexes 30,000+ protocols, 100M+ tokens, 2M+ NFT collections, and 3,000+ blockchain games, offering both no-code dashboards and programmatic API access for developers building Web3 data applications.
examples:
- key_count: 4
  name: Query Defi Tvl
  slug: query-defi-tvl
- key_count: 4
  name: Query Nft Floor Price
  slug: query-nft-floor-price
- key_count: 4
  name: Track Event
  slug: track-event
- key_count: 4
  name: Wallet Nft Eligibility
  slug: wallet-nft-eligibility
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/footprint.png
json_schemas:
- name: Footprint Analytics Query Request
  property_count: 2
  slug: query
- name: Footprint Growth Analytics Track Event Request
  property_count: 6
  slug: track-event
- name: Footprint Analytics Wallet Profile
  property_count: 10
  slug: wallet-profile
jsonld:
- class_count: 16
  name: Footprint Context
  property_count: 9
  slug: footprint
layout: provider
modified: '2026-06-14'
name: Footprint Analytics
nav: Providers
network: true
overview: 'Footprint Analytics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Chain API, DeFi API, Events API, and 5 more. Tagged areas include Blockchain, DeFi, NFT, GameFi, and Token Analytics.


  The Footprint Analytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Footprint Analytics'' developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, status page, changelog, and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 10
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Footprint Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: footprint-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.7
    developer_ergonomics: 13.1
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/footprint/refs/heads/main/screenshots/footprint-2026-06-20T181412.png
security:
- kind: authentication
  name: Footprint Authentication
  slug: footprint-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Footprint Domain Security
  slug: footprint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: footprint
tags:
- Blockchain
- DeFi
- NFT
- GameFi
- Token Analytics
- On-Chain Data
- Web3
- Crypto
website: https://www.footprint.network/
---
