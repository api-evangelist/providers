---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dopex Agentic Access
  operation_count: 20
  slug: dopex-agentic-access
  summary_line: 20 operations
api_count: 10
apis:
- description: REST API for liquidity providers participating in Dopex CLAMM vaults. Exposes endpoints to prepare deposit transaction calldata, query current LP positions for a given wallet address, retrieve deposit
  name: Dopex LP Management API
  slug: lp-management-api
- description: REST API for querying xSYK (escrowed SYK) staking and vesting positions for a given account address. Returns details of vested and staked xSYK allocations including total allocation amounts and pendin
  name: Dopex xSYK Staking Positions API
  slug: xsyk-staking-api
- description: The deposit API from Dopex — 3 operation(s) for deposit.
  name: Dopex deposit API
  slug: dopex-deposit-api
- description: The exercise API from Dopex — 2 operation(s) for exercise.
  name: Dopex exercise API
  slug: dopex-exercise-api
- description: The option-markets API from Dopex — 2 operation(s) for option-markets.
  name: Dopex option-markets API
  slug: dopex-option-markets-api
- description: The purchase API from Dopex — 3 operation(s) for purchase.
  name: Dopex purchase API
  slug: dopex-purchase-api
- description: The stats API from Dopex — 7 operation(s) for stats.
  name: Dopex stats API
  slug: dopex-stats-api
- description: The strikes-chain API from Dopex — 1 operation(s) for strikes-chain.
  name: Dopex strikes-chain API
  slug: dopex-strikes-chain-api
- description: The withdraw API from Dopex — 1 operation(s) for withdraw.
  name: Dopex withdraw API
  slug: dopex-withdraw-api
- description: The xSYK API from Dopex — 1 operation(s) for xsyk.
  name: Dopex xSYK API
  slug: dopex-xsyk-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dopex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dopex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stryke.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stryke.xyz
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.dopex.io
- group: docs
  title: ''
  type: LegacyDocs
  url: https://docs.dopex.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stryke-xyz
- group: build
  title: Legacy SDK (dopex-io/elvarg)
  type: GitHub
  url: https://github.com/dopex-io/elvarg
- group: company
  title: ''
  type: Blog
  url: https://teamdopex.medium.com
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/stryke
- group: other
  title: ''
  type: X
  url: https://twitter.com/stryke_xyz
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: other
  title: ''
  type: Audits
  url: https://docs.stryke.xyz/security-audits
- group: auth
  title: ''
  type: BugBounty
  url: https://docs.stryke.xyz/bug-bounty
created: '2026-06-14'
description: Dopex (Decentralized Options Exchange) is a DeFi protocol built on Arbitrum that enables users to trade and write options through Single Staking Option Vaults (SSOV). The protocol uses a dual-token model — DPX (governance and fee accrual) and rDPX (rebate token) — and prices options on-chain using the Black-Scholes formula with implied volatility sourced via Chainlink adapters. SSOVs allow liquidity providers to lock collateral for monthly epochs and sell call or put options at defined strike prices, earning premiums plus base DeFi yield. Dopex has since evolved into Stryke (stryke.xyz), which extends the model with Concentrated Liquidity AMM Options (CLAMM) and cross-chain support via LayerZero and Chainlink CCIP. The REST API (api.stryke.xyz) exposes endpoints for option market data, strike chains, LP position management, trade history, and xSYK staking positions, supporting integrators building on-chain options products and analytics on Arbitrum and other EVM chains.
examples:
- key_count: 3
  name: Purchase Quote Response
  slug: purchase-quote-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dopex.png
json_schemas:
- name: OptionMarketsResponseDtoV2
  property_count: 18
  slug: OptionMarketsResponseDtoV2
- name: PurchasePositionMetaDto
  property_count: 4
  slug: PurchasePositionMetaDto
- name: PurchasePositionMetaHandlerDto
  property_count: 4
  slug: PurchasePositionMetaHandlerDto
- name: PurchasePositionsResponseDto
  property_count: 6
  slug: PurchasePositionsResponseDto
- name: QuoteResponseDto
  property_count: 3
  slug: QuoteResponseDto
- name: TokenDto
  property_count: 3
  slug: TokenDto
- name: UserXSykDataResponseDto
  property_count: 3
  slug: UserXSykDataResponseDto
- name: VestPositionsResponseDto
  property_count: 7
  slug: VestPositionsResponseDto
layout: provider
modified: '2026-06-14'
name: Dopex
nav: Providers
network: true
overview: 'Dopex publishes 8 APIs on the [APIs.io](https://apis.io/) network, including deposit API, exercise API, option-markets API, and 5 more. Tagged areas include DeFi, Decentralized Options, SSOV, Options Exchange, and Arbitrum.


  The Dopex catalog on APIs.io includes 1 Spectral governance ruleset.


  Dopex''s developer surface includes documentation, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Dopex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dopex-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.0
  delta: -3.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 42.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dopex/refs/heads/main/screenshots/dopex-2026-06-20T180154.png
security:
- kind: domain-security
  name: Dopex Domain Security
  slug: dopex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dopex
tags:
- DeFi
- Decentralized Options
- SSOV
- Options Exchange
- Arbitrum
- DPX
- rDPX
- Staking
- Implied Volatility
- Black-Scholes
- Options Pricing
- CLAMM
- Cryptocurrency
- Web3
- EVM
website: https://www.stryke.xyz
---
