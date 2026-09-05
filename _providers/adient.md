---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adient-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adient-ei
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adient
- group: company
  title: ''
  type: Website
  url: https://www.adient.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/adient-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adient-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/adient-finops.yml
created: '2026-05-06'
description: Adient is a global automotive seating supplier headquartered in Plymouth, Michigan. Spun off from Johnson Controls in 2016, Adient designs and manufactures seating systems for global automakers across passenger and commercial vehicles.
finops:
- name: Adient Finops
  service_category: Industrial / Automotive
  slug: adient-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adient.png
layout: provider
modified: '2026-05-06'
name: Adient
nav: Providers
network: true
overview: Adient is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Seating, and OEM Supplier.
plans:
- name: Adient Plans Pricing
  plan_count: 1
  slug: adient-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Adient Rate Limits
  slug: adient-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 12.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adient/refs/heads/main/screenshots/adient-2026-06-20T164658.png
security:
- kind: domain-security
  name: Adient Domain Security
  slug: adient-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adient
tags:
- Automotive
- Tier 1 Supplier
- Seating
- OEM Supplier
website: https://www.adient.com/
---
