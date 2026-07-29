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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Avail platform API providing programmatic access to rental property management capabilities including listings, applications, leases, payments, and maintenance requests. Avail does not publish an offi
  name: Avail API
  slug: avail-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.avail.com/education
- group: company
  title: ''
  type: Blog
  url: https://www.avail.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avail.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.avail.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/helloavail
- group: other
  title: ''
  type: X
  url: https://twitter.com/helloavail
- group: commercial
  title: ''
  type: Plans
  url: plans/avail-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/avail-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/avail-finops.yml
created: '2026-06-13'
description: Avail is a landlord-focused rental management platform offering tools for property listings, tenant applications, screening reports, lease agreements, rent payments, and maintenance requests. Designed for DIY independent landlords, Avail enables listing syndication across 19+ rental sites, state-specific digital lease signing, online rent collection, and maintenance request tracking through an all-in-one platform.
finops:
- name: Avail Finops
  service_category: ''
  slug: avail-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avail.png
layout: provider
modified: '2026-06-13'
name: Avail
nav: Providers
network: true
overview: 'Avail publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Rental Management, Landlord Software, Tenant Screening, and Lease Management.


  Avail''s developer surface includes documentation, engineering blog, pricing, support, and 7 more developer resources.'
plans:
- name: Avail Plans Pricing
  plan_count: 2
  slug: avail-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 3
  name: Avail Rate Limits
  slug: avail-rate-limits
score:
  band: emerging
  composite: 21.9
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Avail Domain Security
  slug: avail-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: avail
tags:
- Property Management
- Rental Management
- Landlord Software
- Tenant Screening
- Lease Management
- Rent Collection
- Maintenance Requests
- Real Estate
website: https://www.avail.com/
---
