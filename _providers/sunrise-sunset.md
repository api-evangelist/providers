---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sunrise Sunset Agentic Access
  operation_count: 1
  slug: sunrise-sunset-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The Json API from Sunrise Sunset — 1 operation(s) for json.
  name: Sunrise Sunset Json API
  slug: sunrise-sunset-json-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sunrise-sunset-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunrise-sunset-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sunrise-sunset.org/
- group: docs
  title: ''
  type: Documentation
  url: https://sunrise-sunset.org/api
- group: operate
  title: ''
  type: StatusPage
  url: https://apistatus.sunrise-sunset.org/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sunrise-sunset/refs/heads/main/plans/sunrise-sunset-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sunrise-sunset/refs/heads/main/rate-limits/sunrise-sunset-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sunrise-sunset/refs/heads/main/finops/sunrise-sunset-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sunrise-sunset.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sunrise-sunset.org/privacy
- group: operate
  title: ''
  type: Contact
  url: https://sunrise-sunset.org/contact
created: '2026-06-13'
description: Free REST API providing sunrise, sunset, solar noon, day length, and civil, nautical, and astronomical twilight times for any geographic location and date. No API key or account required; attribution to sunrise-sunset.org is required. A single GET request to https://api.sunrise-sunset.org/json with a latitude, longitude, and optional date returns all solar time data for that location.
examples:
- key_count: 4
  name: Get Solar Times Formatted
  slug: get-solar-times-formatted
- key_count: 4
  name: Get Solar Times Iso8601
  slug: get-solar-times-iso8601
finops:
- name: Sunrise Sunset Finops
  service_category: ''
  slug: sunrise-sunset-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sunrise-sunset.png
json_schemas:
- name: SolarTimesResponse
  property_count: 3
  slug: solar-times-response
jsonld:
- class_count: 2
  name: Sunrise Sunset Context
  property_count: 16
  slug: sunrise-sunset-context
layout: provider
modified: '2026-06-13'
name: Sunrise Sunset
nav: Providers
network: true
overview: 'Sunrise Sunset publishes 1 API on the [APIs.io](https://apis.io/) network: Json API. Tagged areas include Sunrise, Sunset, Solar, Astronomy, and Twilight.


  The Sunrise Sunset catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sunrise Sunset''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Sunrise Sunset Plans Pricing
  plan_count: 1
  slug: sunrise-sunset-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 0
  name: Sunrise Sunset Rate Limits
  slug: sunrise-sunset-rate-limits
rules:
- name: Sunrise Sunset API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sunrise-sunset-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  delta: -3.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 15.8
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunrise-sunset/refs/heads/main/screenshots/sunrise-sunset-2026-06-20T194659.png
security:
- kind: domain-security
  name: Sunrise Sunset Domain Security
  slug: sunrise-sunset-domain-security
  summary_line: TLSv1.3
slug: sunrise-sunset
tags:
- Sunrise
- Sunset
- Solar
- Astronomy
- Twilight
- Weather
- Geolocation
- Free
website: https://sunrise-sunset.org/
---
