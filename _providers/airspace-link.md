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
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API delivering airspace data and services for UAS applications — B4UFLY airspace briefings, LAANC SDSP operations and authorizations, ASL and ephemeral operations, surface/risk/routing, elevation
  name: AirHub API
  slug: airhub-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://airspacelink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.airspacelink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.airspacelink.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.airspacelink.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.airspacelink.com/doc-521691
- group: operate
  title: ''
  type: Support
  url: https://support.airspacelink.com/
- group: company
  title: ''
  type: Blog
  url: https://airspacelink.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airspacelink.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airspace-link-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://airspacelink.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.airspacelink.com/
- group: start
  title: ''
  type: Login
  url: https://portal.airspacelink.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airspacelink.com/terms-conditions-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airspacelink.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airspace-link-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/airspace-link-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airspace-link-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airspace-link-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airspace-link-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/airspace-link-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airspace-link-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airspace-link-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/airspace-link-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airspace-link-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airspace-link-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airspace-link-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Airspace Link provides digital infrastructure for safer skies, operating the AirHub platform for drone and unmanned aircraft system (UAS) operations. Its AirHub API is a REST service that delivers airspace awareness, FAA data, LAANC authorizations, B4UFLY briefings, operational hazard and risk assessment, routing, elevation, position telemetry, and vector tiles to power UAS applications. Airspace Link also offers a Drone Operations Management System (DOMS), FAA-approved Unmanned Traffic Management (UTM) services, and airspace security capabilities for state and local governments, federal and defense agencies, and commercial drone programs. The API authenticates with OAuth 2.0 client-credentials plus an API key and runs in separate sandbox and live environments.
image: https://airspacelink.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: airspace-link-mcp.yml
  slug: airspace-link-mcpyml
modified: '2026-07-18'
name: Airspace Link
nav: Providers
network: true
overview: 'Airspace Link publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, UAS, Airspace, and Aviation.


  Airspace Link''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 39
scopes:
- name: Airspace Link Scopes
  scope_count: 15
  slug: airspace-link-scopes
  summary_line: 15 scopes
score:
  band: thin
  composite: 33.3
  delta: -1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 34.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airspace-link/refs/heads/main/screenshots/airspace-link-2026-07-25T195436.png
security:
- kind: authentication
  name: Airspace Link Authentication
  slug: airspace-link-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Airspace Link Domain Security
  slug: airspace-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airspace-link
tags:
- Company
- Drones
- UAS
- Airspace
- Aviation
- LAANC
- UTM
- Geospatial
- Public Safety
- Logistics
website: https://airspacelink.com/
---
