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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: 'REST and WebSocket API for advanced crypto trading on Nexo Pro. Supports spot trading, futures, TWAP orders, account balances, order placement, order cancellation, trade history, and futures position '
  name: Nexo Pro Trading API
  slug: nexo-pro-trading-api
- description: 'REST API enabling merchants to accept cryptocurrency payments. Supports listing available assets, creating deposit addresses per transaction reference, and receiving webhook notifications (PG_DEPOSIT '
  name: Nexo Payment Gateway API
  slug: nexo-payment-gateway-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nexo.com
- group: docs
  title: ''
  type: Documentation
  url: https://pro.nexo.com/apiDocPro.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nexofinance
- group: company
  title: ''
  type: LinkedIn
  url: https://ky.linkedin.com/company/nexofinance
- group: company
  title: ''
  type: Blog
  url: https://nexo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nexo.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nexo.com
- group: other
  title: ''
  type: X
  url: https://x.com/Nexo
- group: commercial
  title: ''
  type: Plans
  url: plans/nexo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nexo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nexo-finops.yml
created: '2026-06-13'
description: Nexo is a crypto-backed lending and earning platform offering a REST API for managing crypto credit lines, earning interest on digital assets, swapping assets, and portfolio management. The Nexo Pro API provides programmatic access to advanced trading (spot, futures, TWAP), account balances, order management, and trade history via REST and WebSocket interfaces. A separate Payment Gateway API enables merchants to accept crypto payments with webhook-based deposit notifications.
finops:
- name: Nexo Finops
  service_category: ''
  slug: nexo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nexo.png
jsonld:
- class_count: 19
  name: Nexo Context
  property_count: 0
  slug: nexo-context
layout: provider
modified: '2026-06-13'
name: Nexo
nav: Providers
network: true
overview: 'Nexo publishes 1 API on the [APIs.io](https://apis.io/) network: Pro Trading API. Tagged areas include Crypto, Lending, Earning, Trading, and Payments.


  The Nexo catalog on APIs.io includes 1 JSON-LD context.


  Nexo''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Nexo Plans Pricing
  plan_count: 4
  slug: nexo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Nexo Rate Limits
  slug: nexo-rate-limits
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 68.0
    catalog_earned_first_party: 0.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexo/refs/heads/main/screenshots/nexo-2026-06-20T190254.png
security:
- kind: domain-security
  name: Nexo Domain Security
  slug: nexo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nexo Vulnerability Disclosure
  slug: nexo-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: nexo
tags:
- Crypto
- Lending
- Earning
- Trading
- Payments
- Digital Assets
- DeFi
website: https://nexo.com
---
