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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/jp-morgan-chase/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wepay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wepay.com
created: '2026-07-17'
description: WePay is a payments platform, founded in 2008 and backed by 500 Global and Y Combinator, that provided integrated payments (payment processing, merchant onboarding, and payouts) embedded inside software platforms and online marketplaces. WePay was acquired by JPMorgan Chase in 2017 and its capabilities were folded into Chase Integrated Payments (WePay Clear and WePay Link). As of this enrichment pass the standalone WePay developer platform has been decommissioned. developer.wepay.com serves a deleted storage bucket, api.wepay.com is unreachable, www.wepay.com redirects to a dead landing page, and all wepay.com TLS certificates have expired, so no live public API surface remains.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wepay.png
layout: provider
modified: '2026-07-21'
name: WePay
nav: Providers
network: true
overview: WePay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payment Processing, Platform Payments, Marketplaces, and Fintech.
random_paper: 4
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
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Wepay Domain Security
  slug: wepay-domain-security
  summary_line: DMARC
slug: wepay
tags:
- Payments
- Payment Processing
- Platform Payments
- Marketplaces
- Fintech
- Merchant Onboarding
- Payouts
- Company
website: https://wepay.com
---
