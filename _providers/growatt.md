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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Token-authenticated REST API for the Growatt ShineServer monitoring platform. Exposes plant lists and details, plant energy overview and history, device lists, and per-device energy, detail, history a
  name: Growatt Open API V1
  slug: growatt-open-api-v1
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://growatt.com/
- group: start
  title: ''
  type: Portal
  url: https://openapi.growatt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.showdoc.com.cn/262556420217021/0
- group: docs
  title: ''
  type: APIReference
  url: https://www.showdoc.com.cn/262556420217021/0
- group: build
  title: ''
  type: Packages
  url: packages/growatt-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/growatt-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/growatt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/growatt-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/growatt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/growatt-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/growatt-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/growatt-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growatt-domain-security.yml
created: '2026-07-17'
description: Growatt New Energy is a global manufacturer of solar PV inverters, energy storage systems, and smart energy management products for residential, commercial, and utility-scale installations. Growatt operates the ShineServer / ShinePhone cloud monitoring platform and publishes a token-authenticated Open API (V1) that lets third-party systems read plant and device telemetry, retrieve historical energy data, and read or write inverter parameters for MIN (TLX) string inverters and SPH (MIX) hybrid inverters across regional endpoints. Originally surfaced as a portfolio company of IDG Capital; enriched from Growatt's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/growatt.png
layout: provider
mcp_servers:
- description: ''
  name: growatt-mcp.yml
  slug: growatt-mcpyml
modified: '2026-07-19'
name: Growatt
nav: Providers
network: true
overview: 'Growatt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Technology, Solar, Energy, and Photovoltaic.


  Growatt''s developer surface includes developer portal, documentation, API reference, authentication, and 9 more developer resources.'
random_paper: 47
score:
  band: emerging
  composite: 17.5
  delta: -0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/growatt/refs/heads/main/screenshots/growatt-2026-07-25T220401.png
security:
- kind: authentication
  name: Growatt Authentication
  slug: growatt-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Growatt Domain Security
  slug: growatt-domain-security
  summary_line: TLSv1.2 · DMARC
slug: growatt
tags:
- Company
- Consumer Technology
- Solar
- Energy
- Photovoltaic
- Inverters
- Energy Storage
- IoT
- Monitoring
website: https://growatt.com/
---
