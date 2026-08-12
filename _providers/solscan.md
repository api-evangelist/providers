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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-11'
api_count: 7
apis:
- description: Free, lower-rate-limit public API exposing basic account, transaction, and token endpoints used by the Solscan UI.
  name: Solscan Public API
  slug: public-api
- description: Commercial Pro API with full account, transaction, token, NFT, DeFi, and analytics endpoints. Higher rate limits, decoded events, and historical depth. Authentication via token header.
  name: Solscan Pro API
  slug: pro-api
- description: Solana account data
  name: Solscan Account API
  slug: solscan-account-api
- description: Block lookups
  name: Solscan Block API
  slug: solscan-block-api
- description: NFT collection data
  name: Solscan NFT API
  slug: solscan-nft-api
- description: SPL token data
  name: Solscan Token API
  slug: solscan-token-api
- description: Transaction lookups
  name: Solscan Transaction API
  slug: solscan-transaction-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solscan-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solscanofficial
- group: start
  title: ''
  type: Portal
  url: https://solscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solscan.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://solscan.io/apis
- group: commercial
  title: ''
  type: Plans
  url: plans/solscan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solscan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/solscan-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.solscan.io/llms.txt
created: '2026-05-08'
description: Solscan is a leading Solana block explorer with a Public API (free, basic) and a Pro API (paid, with full account, transaction, token, NFT, and DeFi endpoints). The Pro API serves decoded on-chain data and is the primary commercial product. Authentication uses a token (Bearer or query parameter) and is required for all Pro endpoints.
finops:
- name: Solscan Finops
  service_category: Crypto Explorer
  slug: solscan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solscan.png
layout: provider
modified: '2026-05-08'
name: Solscan
nav: Providers
network: true
overview: 'Solscan publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Block API, NFT API, and 2 more. Tagged areas include Web3, Solana, Explorer, On-Chain, and Tokens.


  Solscan''s developer surface includes developer portal, documentation, pricing, and 6 more developer resources.'
plans:
- name: Solscan Plans Pricing
  plan_count: 5
  slug: solscan-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Solscan Rate Limits
  slug: solscan-rate-limits
score:
  band: thin
  composite: 32.4
  delta: -6.6
  facets:
    commercial_clarity: 26.3
    contract_quality: 55.2
    developer_ergonomics: 17.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 39.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/solscan/refs/heads/main/screenshots/solscan-2026-06-20T194154.png
security:
- kind: domain-security
  name: Solscan Domain Security
  slug: solscan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: solscan
tags:
- Web3
- Solana
- Explorer
- On-Chain
- Tokens
- NFTs
website: https://solscan.io/
---
