---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Space Weather API provides access to near real-time Australian Space Weather Forecasting Centre data from the Australian Bureau of Meteorology (A index, K index, Dst index, magnetic alerts and war
  name: Space Weather API
  slug: space-weather-api
- description: OGC Sensor Observation Service 2.0 (KISTERS KiWIS SOS2) behind the Bureau's Water Data Online, serving time series from water measurement stations across Australia (watercourse level and discharge, st
  name: Water Data Online SOS2
  slug: water-data-online-sos2
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/bureau-of-meteorology/plans/bureau-of-meteorology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bureau-of-meteorology-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-meteorology/conventions/bureau-of-meteorology-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bureau-of-meteorology-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-meteorology/authentication/bureau-of-meteorology-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bureau-of-meteorology-authentication.yml
- group: operate
  href: https://artifacts.apis.io/bureau-of-meteorology/lifecycle/bureau-of-meteorology-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bureau-of-meteorology-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-meteorology/lifecycle/bureau-of-meteorology-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-meteorology-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-meteorology/errors/bureau-of-meteorology-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-meteorology-error-codes.yml
- group: design
  href: https://artifacts.apis.io/bureau-of-meteorology/conformance/bureau-of-meteorology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bureau-of-meteorology-conformance.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-meteorology/hosts/bureau-of-meteorology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bureau-of-meteorology-hosts.yml
- group: other
  href: https://artifacts.apis.io/bureau-of-meteorology/vendors/bureau-of-meteorology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bureau-of-meteorology-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bureau-of-meteorology/security/bureau-of-meteorology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bureau-of-meteorology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bom.gov.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bom.gov.au/resources/data-services
- group: other
  title: ''
  type: DataCatalog
  url: https://reg.bom.gov.au/catalogue/data-feeds.shtml
- group: commercial
  title: ''
  type: Pricing
  url: https://reg.bom.gov.au/climate/data-services/charges.shtml
- group: start
  title: ''
  type: SignUp
  url: https://reg.bom.gov.au/reguser/reguser.shtml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bom.gov.au/sites/default/files/2026-10/bureau-of-meteorology-data-licence-agreement-october-2026.pdf
- group: other
  title: ''
  type: Copyright
  url: https://www.bom.gov.au/copyright
- group: other
  title: ''
  type: Disclaimer
  url: https://www.bom.gov.au/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bom.gov.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.bom.gov.au/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bom.gov.au/website-help
- group: company
  title: ''
  type: Blog
  url: https://www.bom.gov.au/news-and-media
- group: company
  title: ''
  type: About
  url: https://www.bom.gov.au/about-the-bureau
created: '2026-10-22'
description: The Bureau of Meteorology (BOM) is Australia's national weather, climate and water agency. It provides forecasts, severe weather warnings, observations, flood information, marine and high seas forecasts and climate information, and offers data products for weather, climate, atmosphere, oceans, water and space weather through free services and paid subscription services, including registered-user real-time data feeds (forecast grids, satellite, radar and a geospatial service), climate data services and water data.
image: https://www.bom.gov.au/themes/custom/bom_theme/images/icons/favicon-192.png
layout: provider
modified: '2026-10-22'
name: Bureau of Meteorology
nav: Providers
network: true
overview: 'Bureau of Meteorology is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Weather, Climate, and Meteorology.


  Bureau of Meteorology''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
plans:
- name: Bureau Of Meteorology Plans Pricing
  plan_count: 12
  slug: bureau-of-meteorology-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Bureau Of Meteorology Rate Limits
  slug: bureau-of-meteorology-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bureau-of-meteorology/bureau-of-meteorology-2026-11-03T122800.png
security:
- kind: authentication
  name: Bureau Of Meteorology Authentication
  slug: bureau-of-meteorology-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bureau Of Meteorology Domain Security
  slug: bureau-of-meteorology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-meteorology
tags:
- Company
- Government
- Weather
- Climate
- Meteorology
- Water
- Open Data
- Australia
website: https://www.bom.gov.au/
---
