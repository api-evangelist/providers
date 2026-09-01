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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: PadMapper provides a web-based rental listing search service covering apartments, houses, condos, and rooms for rent across major US and Canadian cities. The platform is powered by Zumper and aggregat
  name: PadMapper Rental Listings
  slug: padmapper-rental-listings
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/padmapper-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/padmapper/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/padmapper/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/padmapper/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.padmapper.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.padmapper.com/privacy
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:hello@padmapper.com
- group: other
  title: ''
  type: X
  url: https://x.com/padmapper
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/padmapper/
created: '2026-06-13'
description: PadMapper is a location-based apartment and rental search platform that plots rental listings on an interactive map, enabling renters to search, filter, and discover rental properties across the US and Canada. Powered by Zumper, the platform aggregates over one million active listings with real-time filtering by price, bedrooms, bathrooms, amenities, and neighborhood. PadMapper does not offer a formal public API; programmatic access to listing data is not officially supported and is prohibited by its Terms of Service.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/padmapper.png
layout: provider
modified: '2026-06-13'
name: PadMapper
nav: Providers
network: true
overview: PadMapper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Rental Listings, Apartment Search, Map-Based Search, and Housing.
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/padmapper/refs/heads/main/screenshots/padmapper-2026-06-20T191318.png
security:
- kind: domain-security
  name: Padmapper Domain Security
  slug: padmapper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: padmapper
tags:
- Real-Estate
- Rental Listings
- Apartment Search
- Map-Based Search
- Housing
- Property Discovery
- Rental Market Data
---
