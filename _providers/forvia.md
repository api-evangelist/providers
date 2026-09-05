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
  url: security/forvia-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forvia
- group: company
  title: ''
  type: Website
  url: https://www.forvia.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/forvia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forvia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forvia-finops.yml
created: '2026-05-06'
description: Forvia is a French global Tier 1 automotive supplier formed in 2022 by the combination of Faurecia and Hella. Forvia designs and manufactures cockpits, seating, interiors, lighting, electronics, hydrogen storage, and clean mobility systems for global automakers.
finops:
- name: Forvia Finops
  service_category: Industrial / Automotive
  slug: forvia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forvia.png
layout: provider
modified: '2026-05-06'
name: Forvia
nav: Providers
network: true
overview: Forvia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Seating, Interiors, and Lighting.
plans:
- name: Forvia Plans Pricing
  plan_count: 1
  slug: forvia-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Forvia Rate Limits
  slug: forvia-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forvia/refs/heads/main/screenshots/forvia-2026-06-20T181449.png
security:
- kind: domain-security
  name: Forvia Domain Security
  slug: forvia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: forvia
tags:
- Automotive
- Tier 1 Supplier
- Seating
- Interiors
- Lighting
- Electronics
website: https://www.forvia.com/
---
