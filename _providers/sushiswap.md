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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sushiswap Agentic Access
  operation_count: 11
  slug: sushiswap-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 7
apis:
- description: Liquidity pool deposit operations
  name: SushiSwap Deposit API
  slug: sushiswap-deposit-api
- description: All liquidity provider endpoints
  name: SushiSwap liquidity-providers API
  slug: sushiswap-liquidity-providers-api
- description: Pool information and liquidity data endpoints
  name: SushiSwap Pool API
  slug: sushiswap-pool-api
- description: All price endpoints
  name: SushiSwap price API
  slug: sushiswap-price-api
- description: Quote generation and signing
  name: SushiSwap Quote API
  slug: sushiswap-quote-api
- description: All swap endpoints
  name: SushiSwap swap API
  slug: sushiswap-swap-api
- description: All token endpoints
  name: SushiSwap token API
  slug: sushiswap-token-api
artifact_total: 31
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
random_paper: 51
rules:
- name: SushiSwap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sushiswap-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.3
  delta: -2.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 68.6
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
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
