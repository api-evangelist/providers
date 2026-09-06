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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
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
random_paper: 0
rate_limits:
- limit_count: 1
  name: Nium Rate Limits
  slug: nium-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
