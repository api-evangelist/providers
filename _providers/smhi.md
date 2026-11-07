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
- description: Public data APIs provided by the Swedish Meteorological and Hydrological Institute.
  name: SMHI Data API
  slug: smhi-data-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/smhi/hosts/smhi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smhi-hosts.yml
- group: build
  href: https://artifacts.apis.io/smhi/packages/smhi-packages.yml
  title: ''
  type: SDKs
  url: packages/smhi-packages.yml
- group: build
  href: https://artifacts.apis.io/smhi/packages/smhi-packages.yml
  title: ''
  type: Packages
  url: packages/smhi-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.smhi.se/kontakta-smhi/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smhi
- group: auth
  href: https://artifacts.apis.io/smhi/security/smhi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smhi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smhi.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.smhi.se/data
- group: docs
  title: ''
  type: APIReference
  url: https://opendata.smhi.se/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.smhi.se/om-smhi
- group: operate
  title: ''
  type: Support
  url: https://www.smhi.se/kontakta-smhi
- group: company
  title: ''
  type: Blog
  url: https://www.smhi.se/blogg
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.smhi.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: SMHI (Swedish Meteorological and Hydrological Institute) is Sweden’s national authority for weather, water and climate information. It provides public services, research, and professional solutions, offering open data, forecasts, climate scenarios, and expert advice to support societal planning, safety, and sustainability. The institute gathers extensive observational data and develops models to inform the public, businesses, and policymakers about weather events, climate change, and water resources.
layout: provider
modified: '2026-10-15'
name: SMHI
nav: Providers
network: true
overview: 'SMHI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Climate, Data, Research, and Sweden.


  SMHI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 54.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/smhi/smhi-2026-11-03T143347.png
security:
- kind: domain-security
  name: Smhi Domain Security
  slug: smhi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: smhi
tags:
- Weather
- Climate
- Data
- Research
- Sweden
website: https://www.smhi.se/
---
