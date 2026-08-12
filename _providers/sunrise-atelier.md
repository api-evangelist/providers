---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The Ip API from Sunrise Atelier — 2 operation(s) for ip.
  name: Sunrise Atelier Ip API
  slug: sunrise-atelier-ip-api
- description: The Timezone API from Sunrise Atelier — 2 operation(s) for timezone.
  name: Sunrise Atelier Timezone API
  slug: sunrise-atelier-timezone-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sunrise-atelier-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sunrise-atelier-world-time-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunrise-atelier-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sunrise-atelier-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://sunrise.am
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sunrise.am/developer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sunrise.am/info/terms-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sunrise.am/info/terms-privacy
- group: operate
  title: ''
  type: Support
  url: https://sunrise.am/info/contact
created: '2026-07-17'
description: Sunrise Atelier operates Sunrise.am, a free consumer service that provides accurate sunrise, sunset, twilight, golden-hour and daylight times for every city and country worldwide, plus a solar calendar, an online clock, and educational articles. For developers, Sunrise.am publishes a free public World Time API (documented at https://sunrise.am/developer and served from the time.now host) that returns the current time, timezone information, daylight-saving data, and IP-based time geolocation as clean JSON with no API key required and CORS enabled. Surfaced as a portfolio company of 500 Global and enriched in the API Evangelist network from its live developer surface.
image: https://sunrise.am/static/sunrise-am-og.png
layout: provider
mcp_servers:
- description: ''
  name: sunrise-atelier-mcp.yml
  slug: sunrise-atelier-mcpyml
modified: '2026-07-21'
name: Sunrise Atelier
nav: Providers
network: true
overview: 'Sunrise Atelier publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ip API and Timezone API. Tagged areas include Company, Time, Timezone, Astronomy, and Geolocation.


  Sunrise Atelier''s developer surface includes support and 9 more developer resources.'
random_paper: 56
score:
  band: thin
  composite: 31.1
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 59.7
    developer_ergonomics: 16.8
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Sunrise Atelier Authentication
  slug: sunrise-atelier-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sunrise Atelier Domain Security
  slug: sunrise-atelier-domain-security
  summary_line: TLSv1.3
slug: sunrise-atelier
tags:
- Company
- Time
- Timezone
- Astronomy
- Geolocation
- Sunrise
- Sunset
- Developer API
website: https://sunrise.am
---
