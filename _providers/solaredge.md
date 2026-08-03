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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Account hierarchy.
  name: Solaredge Account API
  slug: solaredge-account-api
- description: Inverters, optimizers, gateways, meters and sensors.
  name: Solaredge Equipment API
  slug: solaredge-equipment-api
- description: Site-level list, details, energy, power and environmental data.
  name: Solaredge Sites API
  slug: solaredge-sites-api
- description: Battery / storage telemetry.
  name: Solaredge Storage API
  slug: solaredge-storage-api
- description: API version discovery.
  name: Solaredge Version API
  slug: solaredge-version-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solaredge-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.solaredge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.solaredge.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.solaredge.com/
- group: company
  title: ''
  type: Website
  url: https://www.solaredge.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SolarEdge
- group: operate
  title: ''
  type: Support
  url: https://www.solaredge.com/us/service/support
- group: start
  title: ''
  type: SignUp
  url: https://monitoring.solaredge.com/solaredge-web/p/login
- group: start
  title: ''
  type: Login
  url: https://monitoring.solaredge.com/solaredge-web/p/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solaredge.com/us/legal/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solaredge.com/us/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/solaredge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solaredge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/solaredge-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solaredge-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solaredge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/solaredge-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/solaredge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solaredge-llms.txt
created: '2026-07-17'
description: SolarEdge Technologies is a global provider of DC-optimized photovoltaic (PV) inverter systems — combining power optimizers, string inverters, batteries, EV chargers and a cloud monitoring platform for residential, commercial and utility solar installations. Its public developer surface is the SolarEdge Monitoring API, a read-only REST API over monitoringapi.solaredge.com that exposes site inventory, energy and power production, battery/storage telemetry, environmental benefits, equipment/inverter data, meters and sensors for the sites an account can access. Authentication is a single api_key query parameter issued in the SolarEdge monitoring platform; responses are JSON by default and errors use RFC 9457 problem+json (verified live).
image: https://monitoring.solaredge.com/solaredge-web/common/img/se-new-logo.png
layout: provider
mcp_servers:
- description: ''
  name: solaredge-mcp.yml
  slug: solaredge-mcpyml
modified: '2026-07-21'
name: Solaredge
nav: Providers
network: true
overview: 'Solaredge publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Equipment API, Sites API, and 2 more. Tagged areas include Company, Solar Energy, Photovoltaic, Energy Monitoring, and IoT.


  Solaredge''s developer surface includes documentation, API reference, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 3
  name: Solaredge Rate Limits
  slug: solaredge-rate-limits
score:
  band: developing
  composite: 46.2
  delta: 4.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 62.8
    developer_ergonomics: 41.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Solaredge Authentication
  slug: solaredge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Solaredge Domain Security
  slug: solaredge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: solaredge
tags:
- Company
- Solar Energy
- Photovoltaic
- Energy Monitoring
- IoT
- Renewable Energy
- Inverters
- Energy Storage
website: https://www.solaredge.com/
---
