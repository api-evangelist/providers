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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Eight Sleep Agentic Access
  operation_count: 13
  slug: eight-sleep-agentic-access
  summary_line: 13 operations · 5 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Alarm and routine reads and control (unofficial).
  name: Eight Sleep Alarms API
  slug: eight-sleep-alarms-api
- description: OAuth2 password-grant token issuance (unofficial).
  name: Eight Sleep Authentication API
  slug: eight-sleep-authentication-api
- description: Adjustable Base position control (unofficial).
  name: Eight Sleep Base API
  slug: eight-sleep-base-api
- description: Pod device state and side assignment reads (unofficial).
  name: Eight Sleep Device API
  slug: eight-sleep-device-api
- description: Heating level and away-mode control (unofficial).
  name: Eight Sleep Temperature API
  slug: eight-sleep-temperature-api
- description: Per-night sleep and biometric trend reads (unofficial).
  name: Eight Sleep Trends API
  slug: eight-sleep-trends-api
- description: Current and individual user profile reads (unofficial).
  name: Eight Sleep User API
  slug: eight-sleep-user-api
artifact_total: 14
collections:
- collection_type: open
  name: Eight Sleep Unofficial Community API
  slug: open-eight-sleep
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eight-sleep-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eight-sleep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eight-sleep-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eight-sleep
- group: company
  title: ''
  type: Website
  url: https://www.eightsleep.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/lukas-clarke/eight_sleep
- group: commercial
  title: ''
  type: Plans
  url: plans/eight-sleep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eight-sleep-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eight-sleep-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://eightsleep.com/blog/
created: '2026-06-20'
description: Eight Sleep builds the Pod, a temperature-regulating smart mattress cover with Autopilot AI sleep optimization, sleep and biometric tracking, thermal alarms, and an adjustable Base. Eight Sleep does NOT publish an official public developer API. This catalog documents the UNOFFICIAL, community-reverse-engineered client API (auth-api.8slp.net, client-api.8slp.net, app-api.8slp.net) that powers the Eight Sleep mobile app and is used by open-source projects such as pyEight and the Home Assistant Eight Sleep integration. Endpoints can change without notice and are not supported by Eight Sleep.
finops:
- name: Eight Sleep Finops
  service_category: Internet of Things
  slug: eight-sleep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eight-sleep.png
layout: provider
modified: '2026-06-20'
name: Eight Sleep
nav: Providers
network: true
overview: 'Eight Sleep publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Authentication API, Base API, and 4 more. Tagged areas include Sleep, IoT, Smart Home, Wearables, and Health.


  Eight Sleep''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Eight Sleep Plans Pricing
  plan_count: 3
  slug: eight-sleep-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 3
  name: Eight Sleep Rate Limits
  slug: eight-sleep-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eight-sleep/refs/heads/main/screenshots/eight-sleep-2026-06-20T180520.png
security:
- kind: authentication
  name: Eight Sleep Authentication
  slug: eight-sleep-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eight Sleep Domain Security
  slug: eight-sleep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eight-sleep
tags:
- Sleep
- IoT
- Smart Home
- Wearables
- Health
- Unofficial
website: https://www.eightsleep.com
---
