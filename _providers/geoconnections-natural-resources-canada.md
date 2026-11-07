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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/geoconnections-natural-resources-canada/hosts/geoconnections-natural-resources-canada-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geoconnections-natural-resources-canada-hosts.yml
- group: other
  href: https://artifacts.apis.io/geoconnections-natural-resources-canada/vendors/geoconnections-natural-resources-canada-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geoconnections-natural-resources-canada-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://natural-resources.canada.ca/corporate/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canada.ca/en/transparency/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://natural-resources.canada.ca/corporate/plans-performance-reports
- group: company
  title: ''
  type: Newsroom
  url: https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=naturalresourcescanada&start=&end=
- group: auth
  href: https://artifacts.apis.io/geoconnections-natural-resources-canada/security/geoconnections-natural-resources-canada-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geoconnections-natural-resources-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://natural-resources.canada.ca/
coverage:
  checked: '2026-10-23'
  detail: The provider's API endpoints return JSON data but no OpenAPI or other machine-readable contract is published.
  evidence:
  - status: 200
    url: https://api.io.canada.ca/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: GeoConnections - Natural Resources Canada is a government entity focused on ensuring Canada’s abundant natural resources are developed sustainably, competitively and inclusively. It provides geospatial data and services to support environmental stewardship, resource management, and economic development across the country.
layout: provider
modified: '2026-10-23'
name: GeoConnections - Natural Resources Canada
nav: Providers
network: true
overview: 'GeoConnections - Natural Resources Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Natural Resources, Canada, Geospatial Data, and Sustainability.


  GeoConnections - Natural Resources Canada''s developer surface includes pricing and 7 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/geoconnections-natural-resources-canada/geoconnections-natural-resources-canada-2026-11-03T132605.png
security:
- kind: domain-security
  name: Geoconnections Natural Resources Canada Domain Security
  slug: geoconnections-natural-resources-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: geoconnections-natural-resources-canada
tags:
- Government
- Natural Resources
- Canada
- Geospatial Data
- Sustainability
website: https://natural-resources.canada.ca/
---
