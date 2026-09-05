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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
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
overview: 'SpotPay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Neobank, Stablecoins, and Blockchain.


  SpotPay''s developer surface includes signup flow and 2 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spotpay/refs/heads/main/screenshots/spotpay-2026-09-02T160600.png
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
- Stablecoins
- Blockchain
- Fintech
- Digital Wallet
- Cross-Border Payments
- Y Combinator
website: https://www.spotpay.ai/
---
