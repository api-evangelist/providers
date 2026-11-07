---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/japan-meteorological-agency/hosts/japan-meteorological-agency-hosts.yml
  title: ''
  type: Hosts
  url: hosts/japan-meteorological-agency-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://jma.go.jp/
coverage:
  checked: '2026-10-28'
  detail: Public JSON endpoints exist (e.g., forecast data) but no OpenAPI/AsyncAPI/GraphQL spec is provided.
  evidence:
  - status: 200
    url: https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The Japan Meteorological Agency (JMA) is the national authority responsible for weather observation, forecasting, and issuing warnings in Japan. It provides public meteorological information, earthquake and tsunami alerts, climate data, and supports disaster prevention. The agency operates a network of observation stations, radar, satellites, and offers data services to the public, media, and researchers.
image: https://www.jma.go.jp/jma/jma_top/image/logo.gif
layout: provider
modified: '2026-10-28'
name: JMA
nav: Providers
network: true
overview: JMA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Meteorology, Japan, and Government.
random_paper: 1
rate_limits:
- limit_count: 0
  name: Japan Meteorological Agency Rate Limits
  slug: japan-meteorological-agency-rate-limits
scopes:
- name: Japan Meteorological Agency Scopes
  scope_count: 0
  slug: japan-meteorological-agency-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 17
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
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Japan Meteorological Agency Authentication
  slug: japan-meteorological-agency-authentication
  summary_line: 0 schemes
slug: japan-meteorological-agency
tags:
- Company
- Weather
- Meteorology
- Japan
- Government
website: https://jma.go.jp/
---
