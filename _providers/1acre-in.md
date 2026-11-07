---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/1acre-in/hosts/1acre-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1acre-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/1acre-in/vendors/1acre-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1acre-in-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1acre.in/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1acre.in/privacy-policy
- group: auth
  href: https://artifacts.apis.io/1acre-in/security/1acre-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1acre-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1acre.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.1acre.in/
- group: company
  title: ''
  type: Blog
  url: https://1acre.in/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.1acre.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.1acre.in/
- group: operate
  title: ''
  type: Support
  url: https://wa.me/918341109311?text=Hello%201acre.in
coverage:
  checked: '2026-10-31'
  detail: The provider offers a developer portal but no public API documentation or machine‑readable contract.
  evidence:
  - status: 200
    url: https://developers.1acre.in/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: 1acre offers a digital marketplace that aggregates verified land parcels across India, enabling buyers, sellers, and developers to discover, evaluate, and transact on premium real‑estate assets. The platform provides extensive data layers, mapping tools, and a subscription‑based developer dashboard that supports joint‑development projects and outright purchases, with pricing plans for individuals and enterprises.
image: https://1acre.in/static/images/icons/logo.png
layout: provider
modified: '2026-10-31'
name: 1acre
nav: Providers
network: true
overview: '1acre is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, LandMarketplace, DataLayers, India, and Developer Tools.


  1acre''s developer surface includes engineering blog, documentation, pricing, support, and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 16.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 1Acre In Domain Security
  slug: 1acre-in-domain-security
  summary_line: TLSv1.3
slug: 1acre-in
tags:
- Real Estate
- LandMarketplace
- DataLayers
- India
- Developer Tools
website: https://1acre.in/
---
