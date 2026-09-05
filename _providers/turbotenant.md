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
- description: TurboTenant provides a partner API for integrations covering rental property management workflows including listings, tenant applications, screening, lease management, rent collection, and maintenance
  name: TurboTenant API
  slug: turbotenant-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turbotenant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.turbotenant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.turbotenant.com/features/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/turbotenant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turbotenant
- group: company
  title: ''
  type: Blog
  url: https://www.turbotenant.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.turbotenant.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.turbotenant.com/
- group: other
  title: ''
  type: X
  url: https://x.com/turbotenant
- group: commercial
  title: ''
  type: Plans
  url: plans/turbotenant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turbotenant-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turbotenant-finops.yml
created: '2026-06-13'
description: TurboTenant is a rental property management platform designed for independent landlords and property managers. It provides tools for advertising rental listings across 28+ syndication sites, managing tenant applications, conducting background and credit screening, creating lease agreements, collecting rent online, handling maintenance requests, and in-app messaging. The platform integrates with partner services via API for renters insurance, accounting, and other property management workflows.
finops:
- name: Turbotenant Finops
  service_category: ''
  slug: turbotenant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turbotenant.png
layout: provider
modified: '2026-06-13'
name: TurboTenant
nav: Providers
network: true
overview: 'TurboTenant publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Rental Listings, Tenant Screening, Rent Collection, and Lease Agreements.


  TurboTenant''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Turbotenant Plans Pricing
  plan_count: 3
  slug: turbotenant-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Turbotenant Rate Limits
  slug: turbotenant-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
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
    operational_transparency: 42.1
  previous_composite: 24.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turbotenant/refs/heads/main/screenshots/turbotenant-2026-06-20T195834.png
security:
- kind: domain-security
  name: Turbotenant Domain Security
  slug: turbotenant-domain-security
  summary_line: TLSv1.3 · DMARC
slug: turbotenant
tags:
- Property Management
- Rental Listings
- Tenant Screening
- Rent Collection
- Lease Agreements
- Maintenance Requests
- Real-Estate
website: https://www.turbotenant.com/
---
