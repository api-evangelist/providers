---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: REST API for processing payments, authorizations, cancellations, and refunds through the Toss Payments platform. Supports card, virtual account, mobile phone, bank transfer, and digital wallet payment
  name: Toss Payments API
  slug: toss-payments-api
- description: Legacy REST API for Toss Pay payment transactions, merchant approval flows, refunds, and payment status checks. Operates on the pay.toss.im domain with API key authentication.
  name: Toss Pay API
  slug: toss-pay-api
- description: Event-driven webhook system for receiving real-time notifications on payment status changes, virtual account deposits, cancellations, BrandPay method updates, and marketplace payout results.
  name: Toss Payments Webhooks
  slug: toss-payments-webhooks
- description: API for marketplace and platform operators to disburse funds to registered sellers. Supports seller registration, payout requests, and event-driven payout status updates via webhooks.
  name: Toss Payments Payouts API
  slug: toss-payments-payouts-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toss.im
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tosspayments.com/en
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tosspayments
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/toss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/viva-republica
- group: company
  title: ''
  type: Blog
  url: https://toss.tech
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.tosspayments.com/en/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tosspayments.com
- group: other
  title: ''
  type: X
  url: https://x.com/toss_im
- group: commercial
  title: ''
  type: Plans
  url: plans/toss-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/toss-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/toss-finops.yml
created: 2026-06-13
description: Toss is a Korean financial super-app operated by Viva Republica that provides REST APIs for payments, banking, credit scoring, identity verification, and financial services across the Toss ecosystem. The Toss Payments platform supports card payments, virtual accounts, mobile phone billing, bank transfers, and digital wallets including TossPay, KakaoPay, NaverPay, and SamsungPay, serving over 30 million registered users across South Korea.
finops:
- name: Toss Finops
  service_category: ''
  slug: toss-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toss.png
layout: provider
modified: 2026-06-13
name: Toss
nav: Providers
network: true
overview: 'Toss publishes 1 API on the [APIs.io](https://apis.io/) network: Payments API. Tagged areas include Payments, Fintech, Banking, Korea, and Digital Wallet.


  Toss'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Toss Plans Pricing
  plan_count: 3
  slug: toss-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Toss Rate Limits
  slug: toss-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 25.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toss/refs/heads/main/screenshots/toss-2026-06-20T195501.png
security:
- kind: domain-security
  name: Toss Domain Security
  slug: toss-domain-security
  summary_line: TLSv1.2 · DMARC
slug: toss
tags:
- Payments
- Fintech
- Banking
- Korea
- Digital Wallet
- Credit Scoring
- Identity Verification
- Financial-Services
- Super App
website: https://toss.im
---
