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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-08-24'
api_count: 10
apis:
- description: Endpoints that return control data from building management systems (BMS)
  name: Verdigris Technologies Control API
  slug: verdigris-technologies-control-api
- description: Endpoints that return current data
  name: Verdigris Technologies Current API
  slug: verdigris-technologies-current-api
- description: Endpoints that return energy data
  name: Verdigris Technologies Energy API
  slug: verdigris-technologies-energy-api
- description: The Events API from Verdigris Technologies — 3 operation(s) for events.
  name: Verdigris Technologies Events API
  slug: verdigris-technologies-events-api
- description: The Forecast API from Verdigris Technologies — 1 operation(s) for forecast.
  name: Verdigris Technologies Forecast API
  slug: verdigris-technologies-forecast-api
- description: Endpoints that return power data
  name: Verdigris Technologies Power API
  slug: verdigris-technologies-power-api
- description: Endpoints that return power factor data
  name: Verdigris Technologies Power Factor API
  slug: verdigris-technologies-power-factor-api
- description: Endpoints that return total harmonic distortion data
  name: Verdigris Technologies Total Harmonic Distortion API
  slug: verdigris-technologies-total-harmonic-distortion-api
- description: Endpoints that return voltage data
  name: Verdigris Technologies Voltage API
  slug: verdigris-technologies-voltage-api
- description: Endpoints that return weather data
  name: Verdigris Technologies Weather API
  slug: verdigris-technologies-weather-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Data Control API
  slug: open-verdigris-technologies-control-api
- collection_type: open
  name: Data Control Current API
  slug: open-verdigris-technologies-current-api
- collection_type: open
  name: Data Control Energy API
  slug: open-verdigris-technologies-energy-api
- collection_type: open
  name: Data Control Events API
  slug: open-verdigris-technologies-events-api
- collection_type: open
  name: Data Control Forecast API
  slug: open-verdigris-technologies-forecast-api
- collection_type: open
  name: Data Control Power API
  slug: open-verdigris-technologies-power-api
- collection_type: open
  name: Data Control Power Factor API
  slug: open-verdigris-technologies-power-factor-api
- collection_type: open
  name: Data Control Total Harmonic Distortion API
  slug: open-verdigris-technologies-total-harmonic-distortion-api
- collection_type: open
  name: Data Control Voltage API
  slug: open-verdigris-technologies-voltage-api
- collection_type: open
  name: Data Control Weather API
  slug: open-verdigris-technologies-weather-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/verdigris-technologies-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verdigris-technologies-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/verdigris-technologies-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.verdigris.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verdigris.co/docs/vedigris-api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.verdigris.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.verdigris.co/reference/getting-started-with-your-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/verdigris-technologies-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.verdigris.co
- group: company
  title: ''
  type: Blog
  url: https://verdigris.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VerdigrisTech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verdigris.co/terms
- group: start
  title: ''
  type: Login
  url: https://admin.verdigris.co
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verdigris-technologies-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verdigris-technologies-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verdigris-technologies-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/verdigris-technologies-data-v4-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/verdigris-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.verdigris.co/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verdigris-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verdigris-technologies-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verdigris-technologies-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verdigris-technologies-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Verdigris Technologies builds AI-powered building energy intelligence, pairing proprietary current-sensor hardware clamped onto a building''s electrical panels with cloud software that monitors every circuit in real time. The Verdigris API exposes that telemetry through OAuth2-secured REST endpoints (the Data API v4): energy, power, voltage, current, power factor, total harmonic distortion, weather, energy forecasts, building controls, and high-resolution Pro Capture waveforms, all queryable at building, panel, circuit, and breaker granularity with batch variants for pulling many entities in a single request. Developers use it to power enterprise data lakes, internal power-monitoring dashboards, and sustainability and energy-optimization applications for smart buildings.'
image: https://verdigris.co/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Verdigris Technologies MCP Server
  slug: verdigris-technologies-mcp-server
modified: '2026-07-21'
name: Verdigris Technologies
nav: Providers
network: true
overview: 'Verdigris Technologies publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Control API, Current API, Energy API, and 7 more. Tagged areas include Company, Energy, Energy Management, Building Automation, and Smart Buildings.


  Verdigris Technologies'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, and 18 more developer resources.'
random_paper: 15
scopes:
- name: Verdigris Technologies Scopes
  scope_count: 0
  slug: verdigris-technologies-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.9
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 16.7
    contract_quality: 58.0
    developer_ergonomics: 39.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verdigris-technologies/refs/heads/main/screenshots/verdigris-technologies-2026-08-17T082727.png
security:
- kind: authentication
  name: Verdigris Technologies Authentication
  slug: verdigris-technologies-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Verdigris Technologies Domain Security
  slug: verdigris-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Verdigris Technologies Trust Center
  slug: verdigris-technologies-trust-center
  summary_line: SOC 2
slug: verdigris-technologies
tags:
- Company
- Energy
- Energy Management
- Building Automation
- Smart Buildings
- IoT
- Sustainability
- Power Monitoring
- Time Series
- Analytics
- Electricity
website: https://docs.verdigris.co
---
