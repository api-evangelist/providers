---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sushiswap Agentic Access
  operation_count: 11
  slug: sushiswap-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: Liquidity pool deposit operations
  name: SushiSwap Deposit API
  slug: sushiswap-deposit-api
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: All liquidity provider endpoints
  name: SushiSwap liquidity-providers API
  slug: sushiswap-liquidity-providers-api
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: Pool information and liquidity data endpoints
  name: SushiSwap Pool API
  slug: sushiswap-pool-api
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: All price endpoints
  name: SushiSwap price API
  slug: sushiswap-price-api
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: Quote generation and signing
  name: SushiSwap Quote API
  slug: sushiswap-quote-api
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: All swap endpoints
  name: SushiSwap swap API
  slug: sushiswap-swap-api
- baseURL: https://api.sushi.com/price/v1
  baseurl_source: declared
  description: All token endpoints
  name: SushiSwap token API
  slug: sushiswap-token-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blade Deposit API
  slug: open-sushiswap-deposit-api
- collection_type: open
  name: Blade Deposit liquidity-providers API
  slug: open-sushiswap-liquidity-providers-api
- collection_type: open
  name: Blade Deposit Pool API
  slug: open-sushiswap-pool-api
- collection_type: open
  name: Blade Deposit price API
  slug: open-sushiswap-price-api
- collection_type: open
  name: Blade Deposit Quote API
  slug: open-sushiswap-quote-api
- collection_type: open
  name: Blade Deposit swap API
  slug: open-sushiswap-swap-api
- collection_type: open
  name: Blade Deposit token API
  slug: open-sushiswap-token-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sushiswap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sushiswap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sushiswap-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://sushi.com/portal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sushi.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.sushi.com/blade-v2-openapi.json
- group: commercial
  title: ''
  type: Plans
  url: https://sushi.com/portal/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sushiswap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sushi.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sushi.com/terms
- group: company
  title: ''
  type: Blog
  url: https://www.sushi.com/blog
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/NVPXN4e
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sushiswap
- group: operate
  title: ''
  type: RateLimits
  url: /rate-limits/rate-limits.md
- group: commercial
  title: ''
  type: Plans
  url: /plans/plans.md
- group: commercial
  title: ''
  type: FinOps
  url: /finops/finops.md
created: '2026-06-13'
description: SushiSwap is a multi-chain decentralized exchange (DEX) protocol offering REST APIs for accessing liquidity pools, token prices, swap quotes, trading routes, and exchange analytics across 30+ blockchain networks. The Sushi API suite enables developers to integrate token pricing, generate swap quotes, and execute on-chain transactions programmatically via a unified base URL with per-chain routing.
graphqls:
- description: SushiSwap exposes its on-chain data through The Graph Protocol subgraphs. The primary subgraph covers the SushiSwap V2 AMM (Automated Market Maker), providing queryable access to factory statistics, t
  name: SushiSwap GraphQL API
  slug: sushiswap-graphql
image: https://sushi.com/favicon.ico
json_schemas:
- name: DepositRequest
  property_count: 9
  slug: depositrequest
- name: DepositResponse
  property_count: 11
  slug: depositresponse
- name: EIP2098Signature
  property_count: 3
  slug: eip2098signature
- name: ErrorResponse
  property_count: 4
  slug: errorresponse
- name: OffChainAsset
  property_count: 4
  slug: offchainasset
- name: OffChainPool
  property_count: 7
  slug: offchainpool
- name: OffChainPoolData
  property_count: 3
  slug: offchainpooldata
- name: OffChainPoolResponse
  property_count: 2
  slug: offchainpoolresponse
- name: OnChainAsset
  property_count: 6
  slug: onchainasset
- name: OnChainPool
  property_count: 6
  slug: onchainpool
- name: OnChainPoolData
  property_count: 2
  slug: onchainpooldata
- name: OnChainPoolResponse
  property_count: 2
  slug: onchainpoolresponse
- name: Pair
  property_count: 2
  slug: pair
- name: QuoteResponse
  property_count: 12
  slug: quoteresponse
- name: QuoteSignResponse
  property_count: 15
  slug: quotesignresponse
- name: SignRequest
  property_count: 7
  slug: signrequest
- name: SignResponse
  property_count: 10
  slug: signresponse
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 25
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-13'
name: SushiSwap
nav: Providers
network: true
overview: 'SushiSwap publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Deposit API, liquidity-providers API, Pool API, and 4 more. Tagged areas include DeFi, Decentralized Exchange, DEX, Cryptocurrency, and Web3.


  The SushiSwap catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  SushiSwap''s developer surface includes authentication, developer portal, documentation, engineering blog, and 12 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 5
  extends: []
  name: SushiSwap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sushiswap-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 66.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 61.4
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sushiswap/refs/heads/main/screenshots/sushiswap-2026-06-20T194745.png
security:
- kind: authentication
  name: Sushiswap Authentication
  slug: sushiswap-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sushiswap Domain Security
  slug: sushiswap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sushiswap
tags:
- DeFi
- Decentralized Exchange
- DEX
- Cryptocurrency
- Web3
- Blockchain
- Multi-Chain
- Liquidity
- Swap
- Token Pricing
website: https://sushi.com/portal
---
