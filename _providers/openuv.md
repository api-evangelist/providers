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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openuv Agentic Access
  operation_count: 5
  slug: openuv-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: API status and per-key usage statistics
  name: OpenUV Account API
  slug: openuv-account-api
- description: Sun protection window recommendations
  name: OpenUV Protection API
  slug: openuv-protection-api
- description: Current and forecasted UV index data
  name: OpenUV UV Index API
  slug: openuv-uv-index-api
artifact_total: 58
collections:
- collection_type: postman
  name: OpenUV Account API
  slug: postman-openuv-account-api
- collection_type: postman
  name: OpenUV Account Protection API
  slug: postman-openuv-protection-api
- collection_type: postman
  name: OpenUV Account UV Index API
  slug: postman-openuv-uv-index-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenUV Account API
  slug: open-openuv-account-api
- collection_type: open
  name: OpenUV Account Protection API
  slug: open-openuv-protection-api
- collection_type: open
  name: OpenUV Account UV Index API
  slug: open-openuv-uv-index-api
- collection_type: open
  name: OpenUV API
  slug: open-openuv
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openuv/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openuv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openuv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openuv-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.openuv.io
- group: start
  title: ''
  type: Portal
  url: https://www.openuv.io
- group: start
  title: ''
  type: Console
  url: https://www.openuv.io/console
- group: start
  title: ''
  type: Signup
  url: https://www.openuv.io/auth/signup
- group: start
  title: ''
  type: Login
  url: https://www.openuv.io/auth/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openuv.io/console
- group: commercial
  title: ''
  type: Plans
  url: plans/openuv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openuv-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@openuv.io
- group: operate
  title: ''
  type: Contact
  url: mailto:support@openuv.io
- group: company
  title: ''
  type: Blog
  url: https://www.openuv.io/blog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aershov24/openuv-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bachya/pyopenuv
- group: build
  title: ''
  type: Tools
  url: https://github.com/ag2-mcp-servers/openuv---global-real-time-uv-index-forecast-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenUV
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/openuv-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openuv-vocabulary.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/openuv-structure.json
- group: commercial
  title: ''
  type: FinOps
  url: finops/openuv-finops.yml
created: '2026-05-28'
description: OpenUV provides a global real-time UV index API. The service combines meteorological inputs (ozone, cloud cover, area reflection) with NASA satellite sources to return current UV index, daily maximum UV, ozone level, safe sun-exposure times per Fitzpatrick skin type, and a recommended sun protection window for any geographic coordinate.
examples:
- key_count: 1
  name: Openuv Api Statistics Example
  slug: openuv-api-statistics-example
- key_count: 1
  name: Openuv Api Status Example
  slug: openuv-api-status-example
- key_count: 1
  name: Openuv Protection Window Example
  slug: openuv-protection-window-example
- key_count: 1
  name: Openuv Uv Forecast Example
  slug: openuv-uv-forecast-example
- key_count: 1
  name: Openuv Uv Index Example
  slug: openuv-uv-index-example
features:
- description: Current UV index for any latitude/longitude with ozone-adjusted and cloud-adjusted calculations.
  name: Real-Time UV Index
- description: Time-series UV index forecast (hourly) including sun position at each forecast step.
  name: UV Forecast
- description: Recommended start/end times each day when UV index crosses configurable protection thresholds (default 3.5).
  name: Sun Protection Window
- description: Minutes of safe unprotected sun exposure for all six Fitzpatrick skin types (st1-st6).
  name: Safe Exposure Times
- description: Live total column ozone in Dobson units used in the UV calculation.
  name: Ozone Data
- description: Optional altitude parameter for elevation-corrected UV readings.
  name: Altitude Adjustment
- description: Solar azimuth and altitude returned with each UV reading and at each forecast step.
  name: Sun Position
- description: Per-key request and cost statistics for today, yesterday, this month and last month.
  name: API Usage Statistics
- description: Lightweight /status endpoint for uptime checks before making metered requests.
  name: Health Check
finops:
- name: Openuv Finops
  service_category: Data & Analytics
  slug: openuv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openuv.png
integrations:
- description: Official OpenUV integration providing UV index, max UV, ozone, protection window and safe-exposure sensors.
  name: Home Assistant
- description: openHAB binding for OpenUV exposing UV channels in smart-home rule engines.
  name: openHAB
- description: Homey app integration for triggering UV-based flows.
  name: Homey
- description: Community ioBroker adapters (ioBroker.openuv, ioBroker.uv-protect) for the ioBroker IoT platform.
  name: ioBroker
- description: OpenUV is also published on the RapidAPI marketplace.
  name: RapidAPI
- description: OpenUV is listed on the Sulu API platform.
  name: Sulu
json_schemas:
- name: OpenUV API Statistics
  property_count: 1
  slug: openuv-api-statistics
- name: OpenUV Protection Window
  property_count: 1
  slug: openuv-protection-window
- name: OpenUV UV Forecast
  property_count: 1
  slug: openuv-uv-forecast
- name: OpenUV UV Index
  property_count: 1
  slug: openuv-uv-index
json_structures:
- name: Openuv Protection Window Structure
  property_count: 4
  slug: openuv-protection-window-structure
- name: Openuv Structure
  property_count: 0
  slug: openuv-structure
- name: Openuv Uv Forecast Structure
  property_count: 0
  slug: openuv-uv-forecast-structure
- name: Openuv Uv Index Structure
  property_count: 8
  slug: openuv-uv-index-structure
jsonld:
- class_count: 8
  name: Openuv Context
  property_count: 39
  slug: openuv-context
layout: provider
modified: '2026-05-29'
name: OpenUV
nav: Providers
network: true
overview: 'OpenUV publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Protection API, and UV Index API. Tagged areas include Weather, UV Index, Sun, Solar, and Geolocation.


  The OpenUV catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  OpenUV''s developer surface includes authentication, developer portal, developer console, signup flow, pricing, support, engineering blog, and 17 more developer resources.'
plans:
- name: Openuv Plans Pricing
  plan_count: 5
  slug: openuv-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Openuv Rate Limits
  slug: openuv-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenUV API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: openuv-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: OpenUV API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 6
  slug: openuv-rules
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 28.8
    contract_quality: 74.1
    developer_ergonomics: 26.2
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openuv/refs/heads/main/screenshots/openuv-2026-06-20T191048.png
security:
- kind: authentication
  name: Openuv Authentication
  slug: openuv-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openuv Domain Security
  slug: openuv-domain-security
  summary_line: TLSv1.3
slug: openuv
solutions:
- description: Drop-in UV layer for mobile and web weather products.
  name: Consumer Weather
- description: Automation triggers for sun-aware homes and devices.
  name: Smart Home
- description: Skin-type-aware sun safety nudges for wellness apps.
  name: Health and Wellness
tags:
- Weather
- UV Index
- Sun
- Solar
- Geolocation
- Forecast
- Public APIs
use_cases:
- description: Add live UV index, daily UV max and skin-type-specific exposure recommendations to consumer weather apps.
  name: Weather Apps
- description: Trigger blinds, awnings or wearable reminders when UV crosses a threshold (e.g. via Home Assistant or openHAB).
  name: Smart Home Automation
- description: Surface safe-exposure minutes and protection windows in hiking, running, cycling and sailing apps.
  name: Outdoor Activity Planning
- description: Notify users when to apply or reapply sunscreen based on the protection window endpoint.
  name: Sunscreen Reminders
- description: Combine UV, ozone and sun position with solar generation or crop UV-stress models.
  name: Solar and Agriculture
- description: Aggregate UV exposure data across populations and geographies for skin-cancer research.
  name: Public Health Research
- description: Show destination-specific UV risk to travelers before and during trips.
  name: Travel Advisories
website: https://www.openuv.io
---
