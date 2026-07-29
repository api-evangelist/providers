---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
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
  name: Worldtimeapi Agentic Access
  operation_count: 16
  slug: worldtimeapi-agentic-access
  summary_line: 16 operations
api_count: 6
apis:
- description: The Geo API from World Time API — 3 operation(s) for geo.
  name: World Time API Geo API
  slug: worldtimeapi-geo-api
- description: The Geo.txt API from World Time API — 1 operation(s) for geo.txt.
  name: World Time API Geo.txt API
  slug: worldtimeapi-geo-txt-api
- description: The Ip API from World Time API — 3 operation(s) for ip.
  name: World Time API Ip API
  slug: worldtimeapi-ip-api
- description: The Ip.txt API from World Time API — 1 operation(s) for ip.txt.
  name: World Time API Ip.txt API
  slug: worldtimeapi-ip-txt-api
- description: The Timezone API from World Time API — 7 operation(s) for timezone.
  name: World Time API Timezone API
  slug: worldtimeapi-timezone-api
- description: The Timezone.txt API from World Time API — 1 operation(s) for timezone.txt.
  name: World Time API Timezone.txt API
  slug: worldtimeapi-timezone-txt-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worldtimeapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldtimeapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://timeapi.world/
- group: docs
  title: ''
  type: Documentation
  url: https://timeapi.world/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sleeyax/world-time-api
- group: company
  title: ''
  type: Blog
  url: https://dev.to/sleeyax/i-built-a-better-world-time-api-14mh
- group: commercial
  title: ''
  type: Pricing
  url: https://timeapi.world/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/sleeyax
- group: commercial
  title: ''
  type: Plans
  url: plans/worldtimeapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/worldtimeapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/worldtimeapi-finops.yml
created: 2026-06-13
description: World Time API (timeapi.world) is a free REST API that provides current time, timezone information, UTC offset, DST status, and Unix epoch time for any timezone or IP address. Originally hosted at worldtimeapi.org (now sunset), the service continues as a source-available, drop-in compatible successor built on Cloudflare Workers with p99 latency under 40ms. It supports 537 IANA timezones, IP-to-timezone conversion, and IP geolocation. The API returns JSON or plain-text responses and requires no authentication on the free tier.
examples:
- key_count: 4
  name: Geo Lookup
  slug: geo-lookup
- key_count: 4
  name: Ip Lookup
  slug: ip-lookup
- key_count: 4
  name: Three Part Timezone Lookup
  slug: three-part-timezone-lookup
- key_count: 4
  name: Timezone Lookup
  slug: timezone-lookup
finops:
- name: Worldtimeapi Finops
  service_category: ''
  slug: worldtimeapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldtimeapi.png
json_schemas:
- name: DateTimeJsonResponse
  property_count: 15
  slug: datetime-response
- name: GeoJsonResponse
  property_count: 15
  slug: geo-response
jsonld:
- class_count: 0
  name: Worldtimeapi Context
  property_count: 31
  slug: worldtimeapi-context
layout: provider
modified: 2026-06-13
name: World Time API
nav: Providers
network: true
overview: 'World Time API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Geo API, Geo.txt API, Ip API, and 3 more. Tagged areas include Time, Timezone, World Time, UTC, and DST.


  The World Time API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  World Time API''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Worldtimeapi Plans Pricing
  plan_count: 5
  slug: worldtimeapi-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Worldtimeapi Rate Limits
  slug: worldtimeapi-rate-limits
rules:
- name: World Time API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: worldtimeapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worldtimeapi/refs/heads/main/screenshots/worldtimeapi-2026-06-20T201622.png
security:
- kind: domain-security
  name: Worldtimeapi Domain Security
  slug: worldtimeapi-domain-security
  summary_line: TLSv1.3
slug: worldtimeapi
tags:
- Time
- Timezone
- World Time
- UTC
- DST
- Daylight Saving Time
- IP Geolocation
- Unix Epoch
website: https://timeapi.world/
---
