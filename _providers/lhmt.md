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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'LHMT (Lithuania) API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: LHMT (Lithuania) API
  slug: lhmt-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/lhmt/rules/lhmt-rules.yml
  title: ''
  type: Spectral
  url: rules/lhmt-rules.yml
- group: design
  href: https://artifacts.apis.io/lhmt/json-ld/lhmt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lhmt-context.jsonld
- group: design
  href: https://artifacts.apis.io/lhmt/vocabulary/lhmt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lhmt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lhmt/data-model/lhmt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lhmt-data-model.yml
- group: design
  href: https://artifacts.apis.io/lhmt/conformance/lhmt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lhmt-conformance.yml
- group: other
  href: https://artifacts.apis.io/lhmt/hosts/lhmt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lhmt-hosts.yml
- group: auth
  href: https://artifacts.apis.io/lhmt/security/lhmt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lhmt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meteo.lt/
coverage:
  checked: '2026-10-28'
  detail: All attempts to fetch OpenAPI specifications from the API host returned 404, indicating no machine‑readable contract is published.
  evidence:
  - status: 404
    url: https://api.meteo.lt/openapi.json
  - status: 404
    url: https://api.meteo.lt/openapi.yaml
  - status: 404
    url: https://api.meteo.lt/swagger.json
  - status: 404
    url: https://api.meteo.lt/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: LHMT (Lithuania) operates the national meteorological service, providing weather forecasts, climate data, and a public API (api.meteo.lt) that offers access to current observations, forecasts, and historical weather information for Lithuania. The service supports developers with JSON endpoints and documentation, enabling integration of meteorological data into applications and research.
image: https://www.meteo.lt/app/themes/slyva/images/social-default.png
json_schemas:
- name: GetHydroStationsStationcodeObservationsObservationtypeRespon
  property_count: 8
  slug: lhmt-get-hydro-stations-stationcode-observations-observationtype-respon
- name: GetHydroStationsStationcodeObservationsResponse
  property_count: 8
  slug: lhmt-get-hydro-stations-stationcode-observations-response
- name: GetPlacesPlacecodeForecastsForecasttypeResponse
  property_count: 21
  slug: lhmt-get-places-placecode-forecasts-forecasttype-response
- name: GetPlacesPlacecodeForecastsResponse
  property_count: 10
  slug: lhmt-get-places-placecode-forecasts-response
- name: GetStationsStationcodeObservationsDateResponse
  property_count: 17
  slug: lhmt-get-stations-stationcode-observations-date-response
- name: GetStationsStationcodeObservationsResponse
  property_count: 7
  slug: lhmt-get-stations-stationcode-observations-response
jsonld:
- class_count: 12
  name: Lhmt Context
  property_count: 34
  slug: lhmt-context
layout: provider
modified: '2026-10-28'
name: LHMT (Lithuania)
nav: Providers
network: true
overview: 'LHMT (Lithuania) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Meteorology, Lithuania, and Government.


  The LHMT (Lithuania) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: LHMT (Lithuania) API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: lhmt-rules
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - lithuania
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/lhmt/lhmt-2026-11-03T134839.png
security:
- kind: domain-security
  name: Lhmt Domain Security
  slug: lhmt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lhmt
tags:
- Company
- Weather
- Meteorology
- Lithuania
- Government
website: https://meteo.lt/
---
