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
- description: The Hitachi Construction Machinery Telematics API provides operational data about construction equipment including location, fuel consumption, operating hours, and diagnostic information, compliant wi
  name: Hitachi Construction Machinery Telematics API
  slug: telematics-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hitachi-construction-machinery/refs/heads/main/plans/hitachi-construction-machinery-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hitachi-construction-machinery-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hitachi-construction-machinery/refs/heads/main/rate-limits/hitachi-construction-machinery-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hitachi-construction-machinery-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hitachi-construction-machinery/refs/heads/main/finops/hitachi-construction-machinery-finops.yml
  title: ''
  type: FinOps
  url: finops/hitachi-construction-machinery-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hitachicm.com/global/en/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hitachi-construction-machinery/refs/heads/main/security/hitachi-construction-machinery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hitachi-construction-machinery-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hitachi-construction-machinery
- group: company
  title: ''
  type: Website
  url: https://www.hitachicm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hitachicm.com/global/en/solutions/telematics-api/
created: '2025-02-12'
description: Hitachi Construction Machinery provides operational data about machines and equipment on construction sites through the Telematics API, which complies with the ISO 15143-3 (AEMP 2.0) standard. The API enables higher efficiency, productivity, and safety while reducing life cycle costs.
finops:
- has_sources: false
  method: generated
  name: Hitachi Construction Machinery Finops
  primary_unit: ''
  service_category: API
  slug: hitachi-construction-machinery-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hitachi-construction-machinery.png
layout: provider
modified: '2026-10-06'
name: Hitachi Construction Machinery
nav: Providers
network: true
overview: 'Hitachi Construction Machinery is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Equipment, IoT, ISO 15143-3, and Telematics.


  Hitachi Construction Machinery''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Hitachi Construction Machinery Plans Pricing
  plan_count: 3
  slug: hitachi-construction-machinery-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Hitachi Construction Machinery Rate Limits
  slug: hitachi-construction-machinery-rate-limits
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 10.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/hitachi-construction-machinery/refs/heads/main/screenshots/hitachi-construction-machinery-2026-10-11T190532.png
security:
- kind: domain-security
  name: Hitachi Construction Machinery Domain Security
  slug: hitachi-construction-machinery-domain-security
  summary_line: TLSv1.3
slug: hitachi-construction-machinery
tags:
- Construction
- Equipment
- IoT
- ISO 15143-3
- Telematics
website: https://www.hitachicm.com/
---
