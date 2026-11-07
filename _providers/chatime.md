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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/chatime/well-known/chatime-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatime-well-known.yml
- group: other
  href: https://artifacts.apis.io/chatime/hosts/chatime-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatime-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatime/vendors/chatime-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatime-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chatime.com.tw/tossing-8/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chatime.com.tw/zh/privacy-policy-2/
- group: auth
  href: https://artifacts.apis.io/chatime/security/chatime-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chatime.com.tw/en/
- group: company
  title: ''
  type: Blog
  url: https://www.chatime.com.tw/en/category/news-en/
- group: other
  title: ''
  type: Social
  url: https://www.facebook.com/chatimeglobal
coverage:
  checked: '2026-10-08'
  detail: The provider's documentation is only static HTML pages without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.chatime.com.tw/en/
  - status: 301
    url: https://api.com.tw/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chatime is a global bubble tea franchise founded in 2005, operating in over 30 countries with thousands of stores. It offers a wide variety of handcrafted tea drinks, seasonal flavors, and a franchise model for entrepreneurs. The company focuses on quality ingredients, innovative beverage concepts, and expanding its presence worldwide through franchising and corporate-owned locations.
layout: provider
modified: '2026-10-08'
name: Chatime
nav: Providers
network: true
overview: 'Chatime is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bubble Tea, Franchise, Food and Beverage, and Global.


  Chatime''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  previous_composite: 9.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chatime/chatime-2026-11-03T123914.png
security:
- kind: domain-security
  name: Chatime Domain Security
  slug: chatime-domain-security
  summary_line: TLSv1.3
slug: chatime
tags:
- Company
- Bubble Tea
- Franchise
- Food and Beverage
- Global
website: https://www.chatime.com.tw/en/
---
