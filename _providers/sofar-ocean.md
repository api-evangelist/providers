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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sofar Ocean Agentic Access
  operation_count: 8
  slug: sofar-ocean-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: Spotter device discovery
  name: Sofar Ocean Devices API
  slug: sofar-ocean-devices-api
- description: Data collected by Smart Mooring subsurface sensors
  name: Sofar Ocean Smart Mooring API
  slug: sofar-ocean-smart-mooring-api
- description: Data collected by onboard Spotter sensors
  name: Sofar Ocean Spotter Data API
  slug: sofar-ocean-spotter-data-api
- description: Sofar Operational WaveWatch III wave spectra forecast
  name: Sofar Ocean Wave Spectra API
  slug: sofar-ocean-wave-spectra-api
artifact_total: 9
asyncapis:
- description: ''
  name: Sofar Ocean Data Forwarding Webhooks
  slug: sofar-ocean-data-forwarding-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sofar-ocean-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sofarocean.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sofarocean.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sofarocean.com/spotter-and-smart-mooring
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sofarocean.com/spotter-and-smart-mooring/test-the-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/sofar-ocean-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sofar-ocean-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sofar-ocean-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sofar-ocean-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sofar-ocean-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sofar-ocean-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sofar-ocean-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sofar-ocean-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sofar-ocean-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sofar-ocean-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sofar-ocean-spotter-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sofar-ocean-data-forwarding-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sofar-ocean-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sofar-ocean-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://sofarocean.statuspage.io
- group: operate
  title: ''
  type: Support
  url: https://www.sofarocean.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.sofarocean.com/posts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SofarOcean
- group: start
  title: ''
  type: Login
  url: https://spotter.sofarocean.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sofarocean.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sofarocean.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.sofarocean.com
created: '2026-07-17'
description: Sofar Ocean operates one of the world's largest privately owned networks of real-time ocean weather sensors. Its Spotter buoys and Smart Mooring subsurface sensors stream wave, wind, sea-surface temperature, barometric pressure, and acoustic data via cellular and satellite telemetry, and the Wayfinder platform turns that data into maritime voyage optimization. The Sofar API (Spotter & Smart Mooring plus the Operational Wave Spectra forecast) gives developers token-authenticated access to device telemetry, historical and geospatial data queries, subsurface sensor readings, NetCDF wave-spectra forecasts, and outbound data-forwarding webhooks.
image: https://cdn.prod.website-files.com/64d14310c4accecbf82f0e9f/67eb3186e1334d183e9d2b0e_meta%20image%20sofar%20site-min.jpg
layout: provider
mcp_servers:
- description: ''
  name: sofar-ocean-mcp.yml
  slug: sofar-ocean-mcpyml
modified: '2026-07-21'
name: Sofar Ocean
nav: Providers
network: true
overview: 'Sofar Ocean publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Smart Mooring API, Spotter Data API, and 1 more. Tagged areas include Company, Climate, Ocean Data, Weather, and Maritime.


  The Sofar Ocean catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sofar Ocean''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 21 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 70.8
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 54.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Sofar Ocean Authentication
  slug: sofar-ocean-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sofar Ocean Domain Security
  slug: sofar-ocean-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sofar-ocean
tags:
- Company
- Climate
- Ocean Data
- Weather
- Maritime
- Sensors
- IoT
- Environmental Data
- Wave Data
- Buoys
website: https://www.sofarocean.com
---
