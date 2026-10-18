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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: MODIFI's partnership API supports trade finance transaction requests, financing status evaluation, and transaction management.
  name: MODIFI
  slug: modifi
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/modifi/refs/heads/main/plans/modifi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/modifi-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/modifi/refs/heads/main/rate-limits/modifi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/modifi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/modifi/refs/heads/main/finops/modifi-finops.yml
  title: ''
  type: FinOps
  url: finops/modifi-finops.yml
- group: company
  title: ''
  type: Website
  url: https://modifi.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/modifi/refs/heads/main/security/modifi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modifi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modifi-moderndigitalfinance
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.modifi.com/llms.txt
created: '2025-02-08'
description: Welcome to the MODIFI partnership API developer hub. You'll find comprehensive guides and documentation to help you start working with the partnership API as quickly as possible, as well as support if you get stuck.
finops:
- has_sources: false
  method: generated
  name: Modifi Finops
  primary_unit: ''
  service_category: API
  slug: modifi-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modifi.png
layout: provider
modified: '2026-09-16'
name: MODIFI
nav: Providers
network: true
overview: MODIFI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Trade Finance, Financing, Partnerships, and Transaction.
plans:
- name: Modifi Plans Pricing
  plan_count: 3
  slug: modifi-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Modifi Rate Limits
  slug: modifi-rate-limits
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.4
    operational_transparency: 7.9
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/modifi/refs/heads/main/screenshots/modifi-2026-06-20T185655.png
security:
- kind: domain-security
  name: Modifi Domain Security
  slug: modifi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: modifi
tags:
- Trade Finance
- Financing
- Partnerships
- Transaction
website: https://modifi.com
---
