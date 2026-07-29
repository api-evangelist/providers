---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Noaa Co Ops Agentic Access
  operation_count: 14
  slug: noaa-co-ops-agentic-access
  summary_line: 14 operations
api_count: 13
apis:
- description: The Benchmarks API from NOAA CO-OPS — 1 operation(s) for benchmarks.
  name: NOAA CO-OPS Benchmarks API
  slug: noaa-co-ops-benchmarks-api
- description: The Datagetter API from NOAA CO-OPS — 1 operation(s) for datagetter.
  name: NOAA CO-OPS Datagetter API
  slug: noaa-co-ops-datagetter-api
- description: The Extremewaterlevels API from NOAA CO-OPS — 1 operation(s) for extremewaterlevels.
  name: NOAA CO-OPS Extremewaterlevels API
  slug: noaa-co-ops-extremewaterlevels-api
- description: The Htf Annual API from NOAA CO-OPS — 1 operation(s) for htf annual.
  name: NOAA CO-OPS Htf Annual API
  slug: noaa-co-ops-htf-annual-api
- description: The Htf Monthly API from NOAA CO-OPS — 1 operation(s) for htf monthly.
  name: NOAA CO-OPS Htf Monthly API
  slug: noaa-co-ops-htf-monthly-api
- description: The Htf Projection Decadal API from NOAA CO-OPS — 1 operation(s) for htf projection decadal.
  name: NOAA CO-OPS Htf Projection Decadal API
  slug: noaa-co-ops-htf-projection-decadal-api
- description: The Peakwaterlevels API from NOAA CO-OPS — 1 operation(s) for peakwaterlevels.
  name: NOAA CO-OPS Peakwaterlevels API
  slug: noaa-co-ops-peakwaterlevels-api
- description: The Ports.json API from NOAA CO-OPS — 1 operation(s) for ports.json.
  name: NOAA CO-OPS Ports.json API
  slug: noaa-co-ops-ports-json-api
- description: The Sealvltrends API from NOAA CO-OPS — 1 operation(s) for sealvltrends.
  name: NOAA CO-OPS Sealvltrends API
  slug: noaa-co-ops-sealvltrends-api
- description: The Slr Projections API from NOAA CO-OPS — 1 operation(s) for slr projections.
  name: NOAA CO-OPS Slr Projections API
  slug: noaa-co-ops-slr-projections-api
- description: NOAA CO-OPS station metadata, sensors, datums, and configuration
  name: NOAA CO-OPS Stations API
  slug: noaa-co-ops-stations-api
- description: The Stations.json API from NOAA CO-OPS — 1 operation(s) for stations.json.
  name: NOAA CO-OPS Stations.json API
  slug: noaa-co-ops-stations-json-api
- description: The Toptenwaterlevels API from NOAA CO-OPS — 1 operation(s) for toptenwaterlevels.
  name: NOAA CO-OPS Toptenwaterlevels API
  slug: noaa-co-ops-toptenwaterlevels-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/noaa-co-ops-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noaa-co-ops-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://tidesandcurrents.noaa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://tidesandcurrents.noaa.gov/web_services_info.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noaa.gov/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noaa.gov/disclaimer
- group: operate
  title: ''
  type: Contact
  url: https://tidesandcurrents.noaa.gov/contact.html
- group: operate
  title: ''
  type: StatusPage
  url: https://tidesandcurrents.noaa.gov/
- group: commercial
  title: ''
  type: Plans
  url: /plans/free.md
- group: operate
  title: ''
  type: RateLimits
  url: /rate-limits/rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: /finops/finops.md
- group: docs
  title: ''
  type: JSONSchema
  url: /json-schema/data-point.json
- group: docs
  title: ''
  type: JSONSchema
  url: /json-schema/station.json
- group: build
  title: ''
  type: Examples
  url: /examples/water-level-request.json
- group: build
  title: ''
  type: Examples
  url: /examples/water-level-response.json
- group: build
  title: ''
  type: Examples
  url: /examples/tide-predictions-request.json
- group: build
  title: ''
  type: Examples
  url: /examples/station-metadata-response.json
- group: build
  title: ''
  type: Examples
  url: /examples/sea-level-trend-response.json
- group: design
  title: ''
  type: Vocabulary
  url: /vocabulary/vocabulary.json
- group: design
  title: ''
  type: JSONLDContext
  url: /json-ld/context.json
- group: design
  title: ''
  type: JSONLD
  url: /json-ld/station.json
created: '2026-06-13'
description: NOAA Center for Operational Oceanographic Products and Services (CO-OPS) provides REST APIs for tides and currents predictions, observed water levels, meteorological data (wind, barometric pressure, air and water temperature), and oceanographic products. The APIs serve real-time and historical data from NOAA observation stations across the United States coastline and Great Lakes.
examples:
- key_count: 3
  name: Sea Level Trend Response
  slug: sea-level-trend-response
- key_count: 3
  name: Station Metadata Response
  slug: station-metadata-response
- key_count: 4
  name: Tide Predictions Request
  slug: tide-predictions-request
- key_count: 4
  name: Water Level Request
  slug: water-level-request
- key_count: 3
  name: Water Level Response
  slug: water-level-response
image: https://tidesandcurrents.noaa.gov/images/noaa-logo.png
json_schemas:
- name: CO-OPS Data Point
  property_count: 9
  slug: data-point
- name: CO-OPS Station
  property_count: 14
  slug: station
layout: provider
modified: '2026-06-13'
name: NOAA CO-OPS
nav: Providers
network: true
overview: 'NOAA CO-OPS publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Benchmarks API, Datagetter API, Extremewaterlevels API, and 10 more. Tagged areas include NOAA, Tides, Currents, Oceanographic, and Water Level.


  The NOAA CO-OPS catalog on APIs.io includes 1 Spectral governance ruleset.


  NOAA CO-OPS''s developer surface includes developer portal, documentation, code examples, and 18 more developer resources.'
random_paper: 0
rules:
- name: NOAA CO-OPS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: noaa-co-ops-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.5
  delta: -4.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 17.4
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 15.8
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noaa-co-ops/refs/heads/main/screenshots/noaa-co-ops-2026-06-20T190339.png
security:
- kind: domain-security
  name: Noaa Co Ops Domain Security
  slug: noaa-co-ops-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: noaa-co-ops
tags:
- NOAA
- Tides
- Currents
- Oceanographic
- Water Level
- Weather
- Predictions
- Government
website: https://tidesandcurrents.noaa.gov/
---
