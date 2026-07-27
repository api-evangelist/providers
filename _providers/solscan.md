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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Free, lower-rate-limit public API exposing basic account, transaction, and token endpoints used by the Solscan UI.
  name: Solscan Public API
  slug: public-api
- description: Commercial Pro API with full account, transaction, token, NFT, DeFi, and analytics endpoints. Higher rate limits, decoded events, and historical depth. Authentication via token header.
  name: Solscan Pro API
  slug: pro-api
artifact_total: 6
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
overview: 'Solscan publishes 1 API on the [APIs.io](https://apis.io/) network: Pro API. Tagged areas include Web3, Solana, Explorer, On-Chain, and Tokens.


  Solscan''s developer surface includes developer portal, documentation, pricing, and 6 more developer resources.'
plans:
- name: Solscan Plans Pricing
  plan_count: 5
  slug: solscan-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Solscan Rate Limits
  slug: solscan-rate-limits
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 37.7
    developer_ergonomics: 17.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
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
