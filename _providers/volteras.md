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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Volteras Agentic Access
  operation_count: 50
  slug: volteras-agentic-access
  summary_line: 50 operations · 24 acting · 1 human-in-the-loop
api_count: 19
apis:
- description: The Accounts API from Volteras — 4 operation(s) for accounts.
  name: Volteras Accounts API
  slug: volteras-accounts-api
- description: The Authentication API from Volteras — 2 operation(s) for authentication.
  name: Volteras Authentication API
  slug: volteras-authentication-api
- description: The Rate Limit API from Volteras — 1 operation(s) for rate limit.
  name: Volteras Rate Limit API
  slug: volteras-rate-limit-api
- description: The Tags API from Volteras — 2 operation(s) for tags.
  name: Volteras Tags API
  slug: volteras-tags-api
- description: The Vehicle Alerts API from Volteras — 1 operation(s) for vehicle alerts.
  name: Volteras Vehicle Alerts API
  slug: volteras-vehicle-alerts-api
- description: The Vehicle Charging History API from Volteras — 2 operation(s) for vehicle charging history.
  name: Volteras Vehicle Charging History API
  slug: volteras-vehicle-charging-history-api
- description: The Vehicle Charging Schedule API from Volteras — 2 operation(s) for vehicle charging schedule.
  name: Volteras Vehicle Charging Schedule API
  slug: volteras-vehicle-charging-schedule-api
- description: The Vehicle Command Executions API from Volteras — 15 operation(s) for vehicle command executions.
  name: Volteras Vehicle Command Executions API
  slug: volteras-vehicle-command-executions-api
- description: The Vehicle Connection API from Volteras — 4 operation(s) for vehicle connection.
  name: Volteras Vehicle Connection API
  slug: volteras-vehicle-connection-api
- description: The Vehicle Eligibility API from Volteras — 2 operation(s) for vehicle eligibility.
  name: Volteras Vehicle Eligibility API
  slug: volteras-vehicle-eligibility-api
- description: The Vehicle Journeys API from Volteras — 1 operation(s) for vehicle journeys.
  name: Volteras Vehicle Journeys API
  slug: volteras-vehicle-journeys-api
- description: The Vehicle Listening API from Volteras — 2 operation(s) for vehicle listening.
  name: Volteras Vehicle Listening API
  slug: volteras-vehicle-listening-api
- description: The Vehicle Manufacturer Alerts API from Volteras — 1 operation(s) for vehicle manufacturer alerts.
  name: Volteras Vehicle Manufacturer Alerts API
  slug: volteras-vehicle-manufacturer-alerts-api
- description: The Vehicle Range API from Volteras — 1 operation(s) for vehicle range.
  name: Volteras Vehicle Range API
  slug: volteras-vehicle-range-api
- description: The Vehicle Services API from Volteras — 1 operation(s) for vehicle services.
  name: Volteras Vehicle Services API
  slug: volteras-vehicle-services-api
- description: The Vehicle State of Health API from Volteras — 1 operation(s) for vehicle state of health.
  name: Volteras Vehicle State of Health API
  slug: volteras-vehicle-state-of-health-api
- description: The Vehicle Telemetry API from Volteras — 1 operation(s) for vehicle telemetry.
  name: Volteras Vehicle Telemetry API
  slug: volteras-vehicle-telemetry-api
- description: The Vehicle Tires API from Volteras — 1 operation(s) for vehicle tires.
  name: Volteras Vehicle Tires API
  slug: volteras-vehicle-tires-api
- description: The Vehicles API from Volteras — 5 operation(s) for vehicles.
  name: Volteras Vehicles API
  slug: volteras-vehicles-api
artifact_total: 26
asyncapis:
- description: ''
  name: Volteras Webhooks
  slug: volteras-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://volteras.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.volteras.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.volteras.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.volteras.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.volteras.com/overview/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://portal.volteras.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://www.volteras.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.volteras.com/blog/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volteras
- group: operate
  title: ''
  type: StatusPage
  url: https://status.volteras.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.volteras.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.volteras.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.volteras.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/volteras-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/volteras-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/volteras-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volteras-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/volteras-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/volteras-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/volteras-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/volteras-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/volteras-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/volteras-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/volteras-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/volteras-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/volteras-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/volteras-connect-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/volteras-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Volteras is the intelligence layer for OEM-grade connected vehicle data, providing a single Connect API that streams real-time telemetry, charging sessions, journeys, battery state of health, alerts, and asynchronous remote commands (charging, climate, locks) from 35+ global automakers across 340+ vehicle models, sourced directly from manufacturers rather than scrapers or hardware. Vehicles onboard via consent flow or bulk VIN upload, with a full-fidelity sandbox, Svix-powered webhooks, and OAuth 2.0 client-credentials security, serving fleet telematics, insurance, leasing, ride-hailing, and EV charging use cases across North America, Europe, and Australia. Backed by Union Square Ventures, Edenred, WEX, and Long Journey Ventures.
image: https://avatars.githubusercontent.com/u/89023482
layout: provider
mcp_servers:
- description: ''
  name: volteras-mcp.yml
  slug: volteras-mcpyml
modified: '2026-07-21'
name: Volteras
nav: Providers
network: true
overview: 'Volteras publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Rate Limit API, and 16 more. Tagged areas include Company, Electric Vehicles, Connected Vehicles, Automotive, and Vehicle Telemetry.


  The Volteras catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Volteras'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 89
rate_limits:
- limit_count: 0
  name: Volteras Rate Limits
  slug: volteras-rate-limits
scopes:
- name: Volteras Scopes
  scope_count: 12
  slug: volteras-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 65.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Volteras Authentication
  slug: volteras-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Volteras Domain Security
  slug: volteras-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: volteras
tags:
- Company
- Electric Vehicles
- Connected Vehicles
- Automotive
- Vehicle Telemetry
- EV Charging
- Energy
- Mobility
- Fleet Management
website: https://volteras.com
---
