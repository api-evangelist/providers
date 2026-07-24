---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: Cross-border payouts to bank accounts, cards and wallets in 220+ countries with real-time delivery in 100+.
  name: Nium Payout API
  slug: nium-payout-api
- description: Accept payments via bank transfers, cards and wallets across 35+ countries.
  name: Nium Payin API
  slug: nium-payin-api
- description: Multi-currency virtual wallets for storing and managing funds.
  name: Nium Wallet API
  slug: nium-wallet-api
- description: Issue and manage virtual and physical cards.
  name: Nium Cards API
  slug: nium-cards-api
- description: Real-time foreign exchange quotes and conversions.
  name: Nium FX API
  slug: nium-fx-api
- description: KYC/KYB onboarding flows for individuals and corporates.
  name: Nium Onboarding API
  slug: nium-onboarding-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nium-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nium.com/blog
created: '2026-05-08'
description: Nium is a global payments infrastructure platform for cross-border payouts, collections, FX, and card issuing. Serves financial institutions, fintechs, and corporates with a single API.
finops:
- name: Nium Finops
  service_category: Fintech
  slug: nium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nium.png
layout: provider
modified: '2026-05-08'
name: Nium
nav: Providers
network: true
overview: 'Nium publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Cross-Border, Payments, FX, and Issuing.


  Nium''s developer surface includes engineering blog and 1 more developer resources.'
plans:
- name: Nium Plans Pricing
  plan_count: 1
  slug: nium-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 1
  name: Nium Rate Limits
  slug: nium-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: -0.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nium/refs/heads/main/screenshots/nium-2026-06-20T190335.png
security:
- kind: domain-security
  name: Nium Domain Security
  slug: nium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nium
tags:
- Fintech
- Cross-Border
- Payments
- FX
- Issuing
---
