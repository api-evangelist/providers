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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Internal REST API powering the Hemlane property management platform, providing access to rental listings, tenant applications, lease tracking, rent payments, maintenance requests, and owner financial '
  name: Hemlane API
  slug: hemlane-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hemlane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hemlane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.hemlane.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.hemlane.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hemlane.com/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hemlane
- group: other
  title: ''
  type: X
  url: https://twitter.com/hemlane
- group: commercial
  title: ''
  type: Plans
  url: plans/hemlane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hemlane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hemlane-finops.yml
created: '2026-06-13'
description: Hemlane is a technology platform for managing long-term rental properties, combining AI tools with human support to assist with tenant placement, rent collection, lease management, maintenance coordination, and eviction support. The platform operates across all 50 US states and has processed over $1.8B in payments.
finops:
- name: Hemlane Finops
  service_category: ''
  slug: hemlane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hemlane.png
layout: provider
modified: '2026-06-13'
name: Hemlane
nav: Providers
network: true
overview: 'Hemlane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real-Estate, Rentals, Tenant Screening, and Lease Management.


  Hemlane''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Hemlane Plans Pricing
  plan_count: 4
  slug: hemlane-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Hemlane Rate Limits
  slug: hemlane-rate-limits
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hemlane/refs/heads/main/screenshots/hemlane-2026-06-20T182638.png
security:
- kind: domain-security
  name: Hemlane Domain Security
  slug: hemlane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hemlane
tags:
- Property Management
- Real-Estate
- Rentals
- Tenant Screening
- Lease Management
- Rent Collection
- Maintenance
- Landlord
website: https://www.hemlane.com/
---
