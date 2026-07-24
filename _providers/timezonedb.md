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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
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
artifact_total: 16
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
- name: TimezoneDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: timezonedb-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 77.9
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 54.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
