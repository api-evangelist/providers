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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trialpay-domain-security.yml
created: '2026-07-17'
description: TrialPay was an alternative-payments and offer-based advertising company founded in 2006 and based in Mountain View, California, backed by Battery Ventures among others. Its platform let merchants and game developers offer users a product for "free" in exchange for completing an advertiser-sponsored action (a purchase, trial, or signup), with the advertiser paying the merchant — monetizing users who would not otherwise pay. TrialPay shipped web, Android, and iOS SDKs plus offer-wall and monetization APIs (e.g. GetBuyCoinsInfo / GetBuyDirectInfo) widely used in social and mobile games. Visa acquired TrialPay in April 2015 and folded the technology into the Visa Commerce Network; TrialPay no longer operates as a standalone company and its public developer surface (help.trialpay.com, trialpay.com) is offline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trialpay.png
layout: provider
modified: '2026-07-21'
name: TrialPay
nav: Providers
network: true
overview: TrialPay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Advertising, Monetization, and Offerwall.
random_paper: 9
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Trialpay Domain Security
  slug: trialpay-domain-security
  summary_line: no transport/DNS hardening detected
slug: trialpay
tags:
- Company
- Payments
- Advertising
- Monetization
- Offerwall
- Gaming
- Mobile
- Acquired
---
