---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/geosphere-austria/hosts/geosphere-austria-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geosphere-austria-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://geosphere.at/de/aktuelles/news
- group: other
  title: ''
  type: Leadership
  url: https://geosphere.at/de/ueber-uns/management
- group: auth
  href: https://artifacts.apis.io/geosphere-austria/security/geosphere-austria-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geosphere-austria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geosphere.at/
coverage:
  checked: '2026-10-28'
  detail: The website provides weather data but no developer program or API documentation is publicly available.
  evidence:
  - status: 200
    url: https://geosphere.at/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: GeoSphere Austria provides weather forecasts and climate data for Austria, offering detailed regional forecasts, historical weather data, and climate insights. The site presents current conditions, hourly and daily predictions, and aggregates data from national meteorological services, serving both public users and developers interested in Austrian weather information.
image: https://geosphere.at/static/media/Logo.9bc86c1a.svg
layout: provider
modified: '2026-10-28'
name: GeoSphere Austria
nav: Providers
network: true
overview: GeoSphere Austria is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Forecast, Austria, Climate, and Data.
random_paper: 16
scopes:
- name: Geosphere Austria Scopes
  scope_count: 0
  slug: geosphere-austria-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.3
  provenance:
    conformance: unknown
    mcp: derived
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
screenshot: https://apis.io/screenshots/geosphere-austria/geosphere-austria-2026-11-03T132644.png
security:
- kind: authentication
  name: Geosphere Austria Authentication
  slug: geosphere-austria-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Geosphere Austria Domain Security
  slug: geosphere-austria-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geosphere-austria
tags:
- Weather
- Forecast
- Austria
- Climate
- Data
- Company
website: https://geosphere.at/
---
