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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API serving balloon observations, soundings, WeatherMesh point and gridded forecasts, constellation/flight metadata, tropical cyclones, and population-weighted degree-day insights. Bearer API-key
  name: WindBorne Data API
  slug: windborne-data-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://windbornesystems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.windbornesystems.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.windbornesystems.com/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://windbornesystems.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windborne
- group: start
  title: ''
  type: SignUp
  url: https://app.windbornesystems.com/api_tokens
- group: operate
  title: ''
  type: Support
  url: https://windbornesystems.com/faq
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windbornesystems-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/windbornesystems-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/windbornesystems-llms.txt
created: '2026-07-17'
description: WindBorne Systems operates a global constellation of long-duration Global Sounding Balloons and pairs that proprietary in-situ atmospheric data with WeatherMesh, its AI-based numerical weather forecast model. The WindBorne Data API serves real-time balloon observations, soundings, super-observations, constellation and flight-path metadata, point and gridded WeatherMesh forecasts, tropical-cyclone tracks, and population-weighted heating/cooling degree-day insights. Access is via a Bearer API key over REST, an official Python library and CLI, and a hosted Model Context Protocol server for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windbornesystems.png
layout: provider
mcp_servers:
- description: ''
  name: windbornesystems-mcp.yml
  slug: windbornesystems-mcpyml
modified: '2026-07-21'
name: WindBorne Systems
nav: Providers
network: true
overview: 'WindBorne Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Weather Data, Forecasting, and Atmospheric Data.


  WindBorne Systems'' developer surface includes documentation, getting-started guide, engineering blog, signup flow, support, and 5 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 18.3
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Windbornesystems Authentication
  slug: windbornesystems-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Windbornesystems Domain Security
  slug: windbornesystems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: windbornesystems
tags:
- Company
- Weather
- Weather Data
- Forecasting
- Atmospheric Data
- Geospatial
- Climate
- Machine Learning
- MCP
website: https://windbornesystems.com/
---
