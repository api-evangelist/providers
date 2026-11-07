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
api_count: 1
apis:
- description: Public API providing weather observations, forecasts, maps and climate information. Documentation is limited to a minimal landing page without machine‑readable specifications.
  name: Met Eireann API
  slug: met-eireann-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/met-eireann/hosts/met-eireann-hosts.yml
  title: ''
  type: Hosts
  url: hosts/met-eireann-hosts.yml
- group: other
  href: https://artifacts.apis.io/met-eireann/vendors/met-eireann-vendors.yml
  title: ''
  type: Vendors
  url: vendors/met-eireann-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.met.ie/about-us/media
- group: auth
  href: https://artifacts.apis.io/met-eireann/security/met-eireann-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/met-eireann-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.met.ie/
- group: docs
  title: ''
  type: Documentation
  url: https://prodapi.met.ie/
- group: docs
  title: ''
  type: APIReference
  url: https://prodapi.met.ie/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.met.ie/about-us/privacy
- group: other
  title: ''
  type: DataCatalogue
  url: https://datacatalogue.gov.ie/dataset/met-eireann-weather-forecast-api
coverage:
  checked: '2026-10-28'
  detail: Documentation at https://prodapi.met.ie/ is a minimal HTML page without machine‑readable specifications, and attempts to fetch common spec URLs return 404.
  evidence:
  - status: 404
    url: https://prodapi.met.ie/openapi.json
  - status: 404
    url: https://prodapi.met.ie/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Met Éireann is the Irish National Meteorological Service, providing weather forecasts, warnings and climate data for Ireland. It offers public APIs for weather observations, forecasts, maps and climate information, supporting developers, researchers and businesses with reliable meteorological data.
image: https://www.met.ie/images/OG-icon.jpg
layout: provider
modified: '2026-10-28'
name: Met Eireann
nav: Providers
network: true
overview: 'Met Eireann is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Meteorology, Ireland, and Public Data.


  Met Eireann''s developer surface includes documentation, API reference, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/met-eireann/met-eireann-2026-11-03T135519.png
security:
- kind: domain-security
  name: Met Eireann Domain Security
  slug: met-eireann-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: met-eireann
tags:
- Company
- Weather
- Meteorology
- Ireland
- Public Data
website: https://www.met.ie/
---
