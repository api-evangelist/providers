---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 3
apis:
- description: The Rome2Rio Search API returns multi-modal door-to-door travel routes between any origin and destination worldwide. Given origin and destination as place names or coordinates, it returns a ranked lis
  name: Rome2Rio Search API
  slug: search
- description: 'The Rome2Rio Autocomplete API provides place-name suggestions as a user types, returning a ranked list of matching locations (cities, airports, train stations, addresses) that can be passed as origin '
  name: Rome2Rio Autocomplete API
  slug: autocomplete
- description: The Rome2Rio Geocode API resolves a place-name or address string to a canonical Rome2Rio place record with geographic coordinates, place type, and country, enabling precise origin and destination inpu
  name: Rome2Rio Geocode API
  slug: geocode
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rome2rio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rome2rio.com/
- group: company
  title: ''
  type: About
  url: https://www.rome2rio.com/about/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rome2rio.com/documentation/1-4/search/
- group: company
  title: ''
  type: Blog
  url: https://www.rome2rio.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.rome2rio.com/en/support/tickets/new
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.rome2rio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rome2rio.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rome2rio.com/about/terms/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rome2rio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rome2rio
- group: other
  title: ''
  type: Advertise
  url: https://www.rome2rio.com/advertise/
- group: other
  title: ''
  type: GetListed
  url: https://www.rome2rio.com/get-listed/
created: '2026-06-13'
description: Rome2Rio is a multi-modal travel planning platform founded in Melbourne, Australia in 2011, and part of the Omio Group since 2019. It covers 240+ countries, 10 million+ locations, and 20,000+ transport operators, enabling door-to-door route discovery across flights, trains, buses, ferries, and driving. Developers can access route search, geocoding, and autocomplete capabilities through the Rome2Rio REST API, which returns JSON responses covering routes, segments, duration, and operator information for any two points worldwide.
finops:
- name: Rome2Rio Finops
  service_category: API
  slug: rome2rio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rome2rio.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Rome2Rio
nav: Providers
network: true
overview: 'Rome2Rio publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Multi-Modal, Transportation, Routes, and Transit.


  The Rome2Rio catalog on APIs.io includes 1 JSON-LD context.


  Rome2Rio''s developer surface includes documentation, engineering blog, support, GitHub presence, and 9 more developer resources.'
plans:
- name: Rome2Rio Plans Pricing
  plan_count: 2
  slug: rome2rio-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Rome2Rio Rate Limits
  slug: rome2rio-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Rome2Rio Domain Security
  slug: rome2rio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rome2rio
tags:
- Travel
- Multi-Modal
- Transportation
- Routes
- Transit
- Flights
- Trains
- Bus
- Ferries
- Navigation
website: https://www.rome2rio.com/
---
