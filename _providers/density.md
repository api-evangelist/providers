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
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Density v3 Public API for real-time occupancy and presence, historical space metrics (occupancy, utilization, time used, sessions), spaces / doorways / sensors / labels management, sensor and space he
  name: Density Public API v3
  slug: density-public-api-v3
artifact_total: 5
asyncapis:
- description: ''
  name: Density Websockets Events
  slug: density-websockets-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/density-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.density.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.density.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.density.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.density.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.density.io/quick_start/
- group: operate
  title: ''
  type: Support
  url: https://support.density.io/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://atlas.density.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.density.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.density.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.density.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DensityCo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.density.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/density-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/density-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/density-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/density-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/density-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/density-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/density-packages.yml
- group: design
  title: ''
  type: Components
  url: components/density-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/density-websockets-events.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/density-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/density-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/density-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/density-llms.txt
created: '2026-07-17'
description: Density builds radar-based occupancy sensors and a workplace analytics platform that measures how people use physical space without cameras or personally identifiable information. Its v3 Public API (api.density.io) exposes real-time occupancy and presence, historical metrics (occupancy, utilization, time used, sessions, raw sessions), spaces / doorways / sensors / labels resources, sensor and space health, wayfinding display tokens, and WebSocket streams for live floor presence and space occupancy. Authentication is OAuth 2.0 client-credentials (Auth0-backed) or static Bearer API tokens. Originally surfaced as a portfolio company of kleiner-perkins and enriched from Density's public developer surface.
image: https://cdn.prod.website-files.com/5f49c40736fbe713860f9203/681a28ab6cdef3f72543b7bd_density-favicon_256x256.png
layout: provider
mcp_servers:
- description: ''
  name: density-mcp.yml
  slug: density-mcpyml
modified: '2026-07-18'
name: Density
nav: Providers
network: true
overview: 'Density publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Occupancy Sensors, Workplace Analytics, and Real Time.


  The Density catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Density''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, authentication, and 19 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 45.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/density/refs/heads/main/screenshots/density-2026-07-25T211718.png
security:
- kind: authentication
  name: Density Authentication
  slug: density-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Density Domain Security
  slug: density-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: density
tags:
- Company
- Enterprise
- Occupancy Sensors
- Workplace Analytics
- Real Time
- Occupancy
- Sensors
- IoT
- Space Utilization
- Proptech
website: https://www.density.io
---
