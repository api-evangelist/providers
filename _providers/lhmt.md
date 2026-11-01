---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-10-31'
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
overview: 'LHMT (Lithuania) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Meteorology, API, and Lithuania.


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
    artifact_dirs: 13
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- API
- Lithuania
- Government
website: https://meteo.lt/
---
