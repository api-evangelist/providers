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
  href: https://artifacts.apis.io/mgm/hosts/mgm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mgm-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mgm/security/mgm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mgm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mgm.gov.tr/
coverage:
  checked: '2026-10-28'
  detail: The provider's site returns a 302 redirect to a 404 page for typical OpenAPI URLs and no documentation host is identified.
  evidence:
  - status: 302
    url: https://www.mgm.gov.tr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Meteoroloji Genel Müdürlüğü (MGM) is Turkey’s national meteorological service, providing weather forecasts, climate data, and atmospheric observations for the public, aviation, maritime, agriculture, and emergency management sectors. The agency offers real‑time weather maps, forecasts, warnings, and historical climate datasets through its web portal and APIs, supporting developers and researchers in building weather‑aware applications.
image: https://www.mgm.gov.tr/App_Themes/mgm/img/mgmlogo-final.svg
layout: provider
modified: '2026-10-28'
name: Meteoroloji Genel Mudurlugu
nav: Providers
network: true
overview: Meteoroloji Genel Mudurlugu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Forecast, and Turkey.
random_paper: 9
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.4
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/mgm/mgm-2026-11-03T135555.png
security:
- kind: domain-security
  name: Mgm Domain Security
  slug: mgm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mgm
tags:
- Company
- Weather
- Climate
- Forecast
- Turkey
website: https://mgm.gov.tr/
---
