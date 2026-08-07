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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sense Agentic Access
  operation_count: 15
  slug: sense-agentic-access
  summary_line: 15 operations · 3 acting
api_count: 6
apis:
- description: The Sense Realtime API delivers live electricity usage data via a WebSocket connection, streaming second-by-second power consumption readings for the whole home and identified devices. The feed includ
  name: Sense Realtime API
  slug: sense-realtime-api
- description: Authenticate and manage sessions
  name: Sense Authentication API
  slug: sense-authentication-api
- description: Device-level energy data and device information
  name: Sense Devices API
  slug: sense-devices-api
- description: Historical energy usage and solar production data
  name: Sense History API
  slug: sense-history-api
- description: Monitor overview, status, and device detection
  name: Sense Monitors API
  slug: sense-monitors-api
- description: User-level timeline and usage data
  name: Sense Users API
  slug: sense-users-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sense-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sense-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sense.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.sense.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/scottbonline/sense
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/senseenergy
- group: company
  title: ''
  type: Blog
  url: https://blog.sense.com
- group: commercial
  title: ''
  type: Pricing
  url: https://sense.com/homes/buy-monitor/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sense.com
- group: other
  title: ''
  type: X
  url: https://x.com/sense
- group: commercial
  title: ''
  type: Plans
  url: plans/sense-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sense-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sense-finops.yml
created: '2026-06-13'
description: Sense is a ClimateTech company founded in 2013 that provides home energy intelligence through a high-resolution electrical monitoring device installed in residential electrical panels. The Sense platform captures real-time electricity usage data and uses machine learning to disaggregate power consumption into individual device-level signatures, enabling homeowners to understand exactly which appliances are using electricity and when. The API provides access to real-time power consumption and solar production data via a WebSocket realtime feed, and historical trend data via a REST interface covering daily, weekly, monthly, and annual usage breakdowns. Sense also supports device detection data, grid exchange metrics, and push notifications through integrations including Amazon Alexa. The company pivoted in 2025 to embed its machine learning technology directly into next-generation smart meters deployed by utility partners, expanding its reach to tens of millions of homes without
  requiring standalone hardware purchases.
examples:
- key_count: 2
  name: Sense Authenticate Request
  slug: sense-authenticate-request
- key_count: 4
  name: Sense Authenticate Response
  slug: sense-authenticate-response
- key_count: 6
  name: Sense Realtime Payload
  slug: sense-realtime-payload
- key_count: 1
  name: Sense Solar History Response
  slug: sense-solar-history-response
- key_count: 3
  name: Sense Usage History Response
  slug: sense-usage-history-response
finops:
- name: Sense Finops
  service_category: ''
  slug: sense-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sense.png
json_schemas:
- name: Sense Device
  property_count: 7
  slug: sense-device
- name: Sense Realtime Payload
  property_count: 6
  slug: sense-realtime-payload
- name: Sense Usage History
  property_count: 3
  slug: sense-usage-history
jsonld:
- class_count: 8
  name: Sense Context
  property_count: 39
  slug: sense-context
layout: provider
modified: '2026-06-13'
name: Sense
nav: Providers
network: true
overview: 'Sense publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Devices API, History API, and 2 more. Tagged areas include Energy, Home Energy Monitoring, IoT, Smart Home, and Electricity.


  The Sense catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sense''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Sense Plans Pricing
  plan_count: 3
  slug: sense-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Sense Rate Limits
  slug: sense-rate-limits
rules:
- name: Sense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sense-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 74.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sense/refs/heads/main/screenshots/sense-2026-06-20T193703.png
security:
- kind: authentication
  name: Sense Authentication
  slug: sense-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sense Domain Security
  slug: sense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sense
tags:
- Energy
- Home Energy Monitoring
- IoT
- Smart Home
- Electricity
- Solar
- Device Detection
- Real-Time Data
- ClimateTech
website: https://sense.com
---
