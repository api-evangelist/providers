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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Raw punch records across a date range
  name: Workwell Technologies Punch Reports API
  slug: workwell-technologies-punch-reports-api
- description: Per-user, per-pay-period timecards
  name: Workwell Technologies Timecards API
  slug: workwell-technologies-timecards-api
- description: User records for the uAttend account
  name: Workwell Technologies Users API
  slug: workwell-technologies-users-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/workwell-technologies-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/workwell-technologies-uattend-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://workwelltech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uattend.zendesk.com/hc/en-us/articles/48783008798875-uAttend-API
- group: docs
  title: ''
  type: APIReference
  url: https://uattend.zendesk.com/hc/en-us/articles/48783008798875-uAttend-API
- group: operate
  title: ''
  type: Support
  url: https://uattend.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://uattend.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uattend.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://v2.trackmytime.com/login/login.aspx
created: '2026-07-17'
description: Workwell Technologies, Inc. is a Carlsbad, California workforce management company backed by Battery Ventures, best known for its uAttend cloud-connected time and attendance platform and uPunch punch clocks. uAttend pairs biometric time clocks (fingerprint, facial recognition, RFID, voice control) with cloud software for time tracking, scheduling, overtime alerts, and optional payroll processing for small businesses. The WorkWell Technologies API exposes employee, timecard, and punch data from uAttend accounts over HTTPS with API-key authentication, supporting payroll and HRIS integrations.
image: https://uattend.com/wp-content/uploads/2019/07/uAttendLogo-01.svg
layout: provider
mcp_servers:
- description: ''
  name: workwell-technologies-mcp.yml
  slug: workwell-technologies-mcpyml
modified: '2026-07-21'
name: Workwell Technologies
nav: Providers
network: true
overview: 'Workwell Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Punch Reports API, Timecards API, and Users API. Tagged areas include Company, Workforce Management, Time Tracking, Attendance, and Payroll.


  Workwell Technologies'' developer surface includes documentation, API reference, support, engineering blog, and 5 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 35.8
  delta: -0.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 64.2
    developer_ergonomics: 23.9
    discoverability: 92.6
    governance: 8.3
    operational_transparency: 0.0
  previous_composite: 36.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
slug: workwell-technologies
tags:
- Company
- Workforce Management
- Time Tracking
- Attendance
- Payroll
- Human Resources
- Time Clocks
- Biometrics
- Scheduling
website: https://workwelltech.com/
---
