---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Timezonedb Agentic Access
  operation_count: 3
  slug: timezonedb-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Operations for converting time between timezones
  name: TimezoneDB Conversion API
  slug: timezonedb-conversion-api
- description: Operations for listing and retrieving timezone information
  name: TimezoneDB Timezones API
  slug: timezonedb-timezones-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TimezoneDB Conversion API
  slug: open-timezonedb-conversion-api
- collection_type: open
  name: TimezoneDB Conversion Timezones API
  slug: open-timezonedb-timezones-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/timezonedb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timezonedb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/timezonedb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://timezonedb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://timezonedb.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://timezonedb.com/premium
- group: start
  title: ''
  type: Register
  url: https://timezonedb.com/register
- group: other
  title: ''
  type: X
  url: https://twitter.com/timezonedb
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/timezonedb/refs/heads/main/plans/timezonedb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/timezonedb/refs/heads/main/rate-limits/timezonedb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/timezonedb/refs/heads/main/finops/timezonedb-finops.yml
created: '2026-06-13'
description: TimezoneDB is a REST API providing timezone information for cities and coordinates worldwide. It supports looking up local time, GMT offset, and daylight saving time (DST) status by timezone name, geographic coordinates (latitude/longitude), city name, or IP address. The service also supports converting times between timezones and listing all 400+ supported timezones across 240+ countries. Responses are available in JSON or XML formats.
examples:
- key_count: 3
  name: Convert Time Zone
  slug: convert-time-zone
- key_count: 4
  name: Get Time Zone
  slug: get-time-zone
- key_count: 3
  name: List Time Zone
  slug: list-time-zone
finops:
- name: Timezonedb Finops
  service_category: ''
  slug: timezonedb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/timezonedb.png
json_schemas:
- name: ConvertTimeZoneResponse
  property_count: 9
  slug: convert-time-zone-response
- name: GetTimeZoneResponse
  property_count: 17
  slug: get-time-zone-response
- name: ListTimeZoneResponse
  property_count: 3
  slug: list-time-zone-response
jsonld:
- class_count: 4
  name: Timezonedb Context
  property_count: 25
  slug: timezonedb-context
layout: provider
modified: '2026-06-13'
name: TimezoneDB
nav: Providers
network: true
overview: 'TimezoneDB publishes 2 APIs on the [APIs.io](https://apis.io/) network: Conversion API and Timezones API. Tagged areas include Timezone, Time, Geographic Coordinates, DST, and UTC Offset.


  The TimezoneDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TimezoneDB''s developer surface includes authentication, documentation, pricing, and 8 more developer resources.'
plans:
- name: Timezonedb Plans Pricing
  plan_count: 3
  slug: timezonedb-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Timezonedb Rate Limits
  slug: timezonedb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TimezoneDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: timezonedb-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  delta: -6.7
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 70.6
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/timezonedb/refs/heads/main/screenshots/timezonedb-2026-06-20T195402.png
security:
- kind: authentication
  name: Timezonedb Authentication
  slug: timezonedb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Timezonedb Domain Security
  slug: timezonedb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: timezonedb
tags:
- Timezone
- Time
- Geographic Coordinates
- DST
- UTC Offset
- Time Conversion
- Location
website: https://timezonedb.com/
---
