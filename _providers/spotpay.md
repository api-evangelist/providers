---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spotpay.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.spotpay.ai/download
created: '2026-07-17'
description: SpotPay is a global neobank that operates as a stablecoin-based global bank account, letting users hold, send, receive, and spend money anywhere in the world from a single identity-verified digital wallet without a traditional bank account. The service settles payments on blockchain rails using stablecoins and pairs the wallet with the SpotPay Calypso debit card plus Apple Pay and Google Pay support, and lets merchants accept QR-code payments with instant settlement. Founded by Zsika Phillip (CEO, ex-Google) and Thomas Cesare-Herriau (CTO, ex-Brex), SpotPay is a Y Combinator Winter 2026 company operating across 40+ countries and registered as a Money Services Business with FinCEN in the United States. As of this enrichment pass SpotPay is a consumer mobile-app product with no public API, developer portal, SDKs, or OpenAPI surface; api.spotpay.ai serves only the app's private backend.
image: https://www.spotpay.ai/favicon.ico
layout: provider
modified: '2026-07-21'
name: SpotPay
nav: Providers
network: true
overview: 'SpotPay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Neobank, Stablecoin, and Blockchain.


  SpotPay''s developer surface includes signup flow and 2 more developer resources.'
random_paper: 55
score:
  band: minimal
  composite: 7.6
  delta: -2.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Spotpay Domain Security
  slug: spotpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spotpay
tags:
- Company
- Payments
- Neobank
- Stablecoin
- Blockchain
- Fintech
- Digital Wallet
- Cross-Border Payments
- Y Combinator
website: https://www.spotpay.ai/
---
