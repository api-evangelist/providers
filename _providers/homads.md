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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Homads marketplace surface for searching and browsing mid-term (30+ day) furnished rental listings by location, dates, and neighborhood. As of the catalog date this is a consumer-facing web produc
  name: Homads Rental Market Data
  slug: rental-market-data
- description: The neighborhood-matching and side-by-side rental comparison experience Homads provides to help guests compare furnished mid-term rentals across neighborhoods during a relocation. This is delivered th
  name: Homads Rent Comparison
  slug: rent-comparison
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Homads API
  slug: open-homads
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homads-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/homads
- group: company
  title: ''
  type: Website
  url: https://homads.com/
- group: docs
  title: ''
  type: Documentation
  url: https://homads.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/homads-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/homads-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/homads-finops.yml
created: '2026-06-21'
description: Homads is an Austin-based mid-term rental marketplace connecting hosts and guests for furnished stays of 30 days or longer. The platform pairs rental listings with neighborhood-matching technology to help relocating professionals, travelers, and people in transition find a place to live. Homads is primarily a consumer and host web application; it does not publish a public developer API. Its rental inventory is exposed to property managers through channel-manager partners (for example Hostfully) via private connectivity, not a documented public API.
finops:
- name: Homads Finops
  service_category: Real Estate and Rental Marketplace
  slug: homads-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homads.png
layout: provider
modified: '2026-06-21'
name: Homads
nav: Providers
network: true
overview: 'Homads publishes 2 APIs on the [APIs.io](https://apis.io/) network: Rental Market Data and Rent Comparison. Tagged areas include Rental, Mid-Term Rental, Real Estate, Marketplace, and Neighborhood Data.


  Homads'' developer surface includes documentation and 6 more developer resources.'
plans:
- name: Homads Plans Pricing
  plan_count: 2
  slug: homads-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 1
  name: Homads Rate Limits
  slug: homads-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: -0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 28.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homads/refs/heads/main/screenshots/homads-2026-07-25T221327.png
security:
- kind: domain-security
  name: Homads Domain Security
  slug: homads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: homads
tags:
- Rental
- Mid-Term Rental
- Real Estate
- Marketplace
- Neighborhood Data
website: https://homads.com/
---
