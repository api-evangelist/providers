---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The official ev.energy v2 REST API. 210 operations across 180 paths covering users, vehicles, EVSEs, charging sessions, schedules, tariffs, regions, solar, solar forecasts, home batteries, boundary me
  name: ev.energy v2 API
  slug: ev-energy-api-v2
artifact_total: 9
asyncapis:
- description: ''
  name: Ev Energy Webhooks
  slug: ev-energy-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ev.energy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ev.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ev.energy/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ev.energy/ev.energy-api-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ev.energy/docs/intro
- group: operate
  title: ''
  type: Support
  url: https://support.ev.energy/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.ev.energy/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ev-energy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ev.energy/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ev.energy/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/ev-energy-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ev-energy-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ev-energy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ev-energy-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ev-energy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ev-energy-security.txt
- group: auth
  title: ''
  type: Security
  url: security/ev-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ev-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ev-energy-domain-security.yml
created: '2026-08-12'
description: ev.energy is a London- and Palo-Alto-based smart electric-vehicle charging platform. Its cloud software connects EV drivers, vehicles, EVSEs (chargers), home batteries, solar inverters and utility programs so charging can be shifted to cheaper, greener periods and aggregated as grid flexibility. The company operates a consumer driver app across the UK, EU, US and Canada, a white-label platform for utilities and e-mobility businesses, an EV Flex virtual power plant product, and the Smart Charge API — a public OpenAPI 3.1 REST contract at api.ev.energy covering vehicles, EVSEs, charging sessions, schedules, tariffs, solar, home batteries, VPP dispatch, rebates and utility program enrollment.
image: https://cdn.prod.website-files.com/6278ea1f9c10c9550411fdd7/627a9ce3111e36661da5018c_ev-logo-256px.png
layout: provider
mcp_servers:
- description: ''
  name: ev-energy-mcp.yml
  slug: ev-energy-mcpyml
modified: '2026-08-12'
name: ev.energy
nav: Providers
network: true
overview: 'ev.energy publishes 1 API on the [APIs.io](https://apis.io/) network: v2 API. Tagged areas include Company, Energy, Electric Vehicles, EV Charging, and Smart Charging.


  The ev.energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ev.energy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
plans:
- name: Ev Energy Plans Pricing
  plan_count: 0
  slug: ev-energy-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Ev Energy Rate Limits
  slug: ev-energy-rate-limits
scopes:
- name: Ev Energy Scopes
  scope_count: 35
  slug: ev-energy-scopes
  summary_line: 35 scopes
score:
  band: developing
  composite: 46.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 63.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Ev Energy Authentication
  slug: ev-energy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ev Energy Domain Security
  slug: ev-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ev Energy Vulnerability Disclosure
  slug: ev-energy-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ev-energy
tags:
- Company
- Energy
- Electric Vehicles
- EV Charging
- Smart Charging
- Utilities
- Sustainability
- Virtual Power Plant
- Demand Response
- Solar
- Home Energy
- Internet of Things
website: https://www.ev.energy/
---
