---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Paraswap Agentic Access
  operation_count: 4
  slug: paraswap-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: The Velora Delta API is an intent-based protocol that enables gas-less token swaps where multiple agents compete to execute trades on behalf of users. Users sign a Delta Order (EIP-712 off-chain signa
  name: ParaSwap Delta API
  slug: paraswap-delta-api
- description: 'The AugustusRFQ API enables market makers to integrate with ParaSwap''s on-chain limit order and Request-for-Quote system, supporting fungible token (ERC-20) and NFT trading. Market makers implement a '
  name: ParaSwap AugustusRFQ API
  slug: paraswap-augustusrfq-api
- baseURL: https://api.paraswap.io
  baseurl_source: declared
  description: 'Retrieves the curated list of tokens supported across all ParaSwap-integrated networks. Returns token metadata including symbol, contract address, decimals, and icon image URL. Supports all 12 active '
  name: ParaSwap Tokens API
  slug: paraswap-tokens-api
- description: ParaSwap exposes TheGraph subgraphs for historical swap data and limit order/RFQ activity across multiple networks. Augustus v5 subgraphs cover standard DEX swaps on Ethereum, Arbitrum, Avalanche, Bas
  name: ParaSwap Subgraphs (GraphQL)
  slug: paraswap-subgraphs
- baseURL: https://api.paraswap.io
  baseurl_source: declared
  description: Get swap path and pricing.
  name: ParaSwap prices API
  slug: paraswap-prices-api
- baseURL: https://api.paraswap.io
  baseurl_source: declared
  description: Return tokens list from Paraswap
  name: ParaSwap tokens API
  slug: paraswap-tokens-api
- baseURL: https://api.paraswap.io
  baseurl_source: declared
  description: Build parameters for a transaction
  name: ParaSwap transactions API
  slug: paraswap-transactions-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ParaSwap Market API v5 prices API
  slug: open-paraswap-prices-api
- collection_type: open
  name: ParaSwap Market API v5 prices tokens API
  slug: open-paraswap-tokens-api
- collection_type: open
  name: ParaSwap Market API v5 prices transactions API
  slug: open-paraswap-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paraswap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paraswap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.velora.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.velora.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.velora.xyz/api/velora-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VeloraDEX
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VeloraDEX/sdk
- group: build
  title: ''
  type: npm Package
  url: https://www.npmjs.com/package/@paraswap/sdk
- group: auth
  title: ''
  type: Security Audits
  url: https://developers.velora.xyz/security
- group: other
  title: ''
  type: Subgraphs
  url: https://developers.velora.xyz/subgraphs
- group: company
  title: ''
  type: Blog
  url: https://velora.xyz/blog
- group: other
  title: ''
  type: App
  url: https://app.velora.xyz/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/paraswap/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/paraswap/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/paraswap/refs/heads/main/finops/finops.yml
created: '2026-06-14'
description: ParaSwap (now Velora) is a DEX aggregator that enables dApps and traders to get the best swap rates by aggregating liquidity across 170+ DEXes and liquidity pools on 12 EVM-compatible chains. The platform offers two core APIs — the Market API for optimal route discovery and transaction building, and the Delta API for intent-based, gas-less swaps with MEV protection — plus an AugustusRFQ API for market makers to provide on-chain limit orders and peer-to-peer trading.
examples:
- key_count: 3
  name: Build Transaction
  slug: build-transaction
- key_count: 3
  name: Get Prices Eth Usdc
  slug: get-prices-eth-usdc
- key_count: 3
  name: Get Tokens
  slug: get-tokens
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: ParaSwap (now Velora) exposes historical on-chain data through The Graph protocol subgraphs. The Augustus v5 subgraph tracks all token swaps executed through the ParaSwap Augustus smart contract acros
  name: ParaSwap GraphQL API
  slug: paraswap-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paraswap.png
json_schemas:
- name: ParaSwap PriceRoute
  property_count: 22
  slug: price-route
- name: ParaSwap Token
  property_count: 9
  slug: token
layout: provider
modified: '2026-06-14'
name: ParaSwap
nav: Providers
network: true
overview: 'ParaSwap publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Tokens API, prices API, tokens API, and 1 more. Tagged areas include DeFi, DEX Aggregator, Token Swaps, Blockchain, and EVM.


  The ParaSwap catalog on APIs.io includes 1 Spectral governance ruleset.


  ParaSwap''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ParaSwap API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: paraswap-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.3
    catalog_earned_first_party: 0.0
    catalog_gap: 59.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 52.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paraswap/refs/heads/main/screenshots/paraswap-2026-06-20T191402.png
security:
- kind: domain-security
  name: Paraswap Domain Security
  slug: paraswap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: paraswap
tags:
- DeFi
- DEX Aggregator
- Token Swaps
- Blockchain
- EVM
- Cryptocurrency
- Liquidity
- Smart Contracts
website: https://www.velora.xyz/
---
