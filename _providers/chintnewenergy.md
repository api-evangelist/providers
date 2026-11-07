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
  href: https://artifacts.apis.io/chintnewenergy/hosts/chintnewenergy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chintnewenergy-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://energy.chint.com/en/news/index.html
- group: auth
  href: https://artifacts.apis.io/chintnewenergy/security/chintnewenergy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chintnewenergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://energy.chint.com/en/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://energy.chint.com/en/
  - status: 403
    url: https://equityzen.com/company/chintnewenergy
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Chintnewenergy, officially Zhejiang Chint New Energy Development Co., Ltd., is a clean‑energy enterprise under the CHINT Group. It focuses on photovoltaic generation systems, building‑integrated photovoltaics, and related smart‑energy solutions. Established in Hangzhou in 2009, the company develops, constructs, operates, and invests in solar farms, energy storage, micro‑grids, and energy‑transaction platforms, serving customers in over 140 countries.
layout: provider
modified: '2026-10-08'
name: Chintnewenergy
nav: Providers
network: true
overview: Chintnewenergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Solar, Cleantech, and China.
random_paper: 2
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chintnewenergy/chintnewenergy-2026-11-03T124046.png
security:
- kind: domain-security
  name: Chintnewenergy Domain Security
  slug: chintnewenergy-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: chintnewenergy
tags:
- Company
- Energy
- Solar
- Cleantech
- China
- Renewables
website: https://energy.chint.com/en/
---
