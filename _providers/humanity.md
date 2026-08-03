---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Humanity HVII Public API is a REST API for workforce management — employees, positions, locations, shifts, shift swaps and trades, timeclocks, leaves, messages, training, tasks (master/shift/emplo
  name: Humanity HVII Public API
  slug: humanity-hvii-public-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.humanity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.humanity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.humanity.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://platform.humanity.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.humanity.com/docs/getting-started-with-authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/humanity-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humanity-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/humanity-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/humanity-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/humanity-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/humanity-conformance.yml
- group: operate
  title: ''
  type: Support
  url: https://community.tcpsoftware.com/s/
- group: company
  title: ''
  type: Blog
  url: https://tcpsoftware.com/resource-library/?type=post
- group: commercial
  title: ''
  type: Pricing
  url: https://tcpsoftware.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.humanity.com/app/
- group: start
  title: ''
  type: Login
  url: https://www.humanity.com/app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tcpsoftware.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tcpsoftware.com/privacy-policy/
created: '2026-07-17'
description: Humanity (Humanity Schedule) is an employee scheduling and workforce management platform owned by TCP Software (TimeClock Plus, LLC). It automates shift planning, closes coverage gaps, forecasts demand, and manages labor compliance across employees, positions, and locations, with time tracking, leave management, training, tasks, and payroll integration. Humanity exposes a public REST API (v1.0 and v2.0) documented on its ReadMe-hosted developer platform, using OAuth2 for authentication, so integrators can synchronize employees, shifts, timeclocks, leaves, reports, skills, and tasks with external HR, payroll, and workforce systems.
image: https://tcpsoftware.com/products/humanity/
layout: provider
mcp_servers:
- description: ''
  name: humanity-mcp.yml
  slug: humanity-mcpyml
modified: '2026-07-19'
name: Humanity
nav: Providers
network: true
overview: 'Humanity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Employee Scheduling, Shift Planning, and Time Tracking.


  Humanity''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 24
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 30.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humanity/refs/heads/main/screenshots/humanity-2026-07-25T221658.png
security:
- kind: authentication
  name: Humanity Authentication
  slug: humanity-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Humanity Domain Security
  slug: humanity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: humanity
tags:
- Company
- Workforce Management
- Employee Scheduling
- Shift Planning
- Time Tracking
- Human Resources
- Leave Management
- Payroll
- Workforce
website: https://www.humanity.com
---
