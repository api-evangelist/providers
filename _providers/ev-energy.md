---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Auth API from ev.energy — 1 operation(s) for auth.
  name: ev.energy Auth API
  slug: ev-energy-auth-api
- description: The Boundary Meters API from ev.energy — 8 operation(s) for boundary meters.
  name: ev.energy Boundary Meters API
  slug: ev-energy-boundary-meters-api
- description: Endpoints for interacting with carbon intensity data.
  name: ev.energy Carbon API
  slug: ev-energy-carbon-api
- description: Endpoints related to records of charging. See [Understanding charging data](docs/understanding/charging_sessions.md) for how charging sessions (plug-in episodes), charging sub-sessions (per-mode segme
  name: ev.energy Charging Sessions API
  slug: ev-energy-charging-sessions-api
- description: The CT Clamps API from ev.energy — 4 operation(s) for ct clamps.
  name: ev.energy CT Clamps API
  slug: ev-energy-ct-clamps-api
- description: Endpoints for interacting with EVSEs.
  name: ev.energy EVS Es API
  slug: ev-energy-evses-api
- description: The Grid API from ev.energy — 3 operation(s) for grid.
  name: ev.energy Grid API
  slug: ev-energy-grid-api
- description: The HEM Systems API from ev.energy — 4 operation(s) for hem systems.
  name: ev.energy HEM Systems API
  slug: ev-energy-hem-systems-api
- description: Endpoints for interacting with home batteries.
  name: ev.energy Home Batteries API
  slug: ev-energy-home-batteries-api
- description: Endpoints for communicating notifications.
  name: ev.energy Notifications API
  slug: ev-energy-notifications-api
- description: Endpoints related to incentivised charging programs.
  name: ev.energy Programs API
  slug: ev-energy-programs-api
- description: Endpoints for interacting with rebates.
  name: ev.energy Rebates API
  slug: ev-energy-rebates-api
- description: The Reference Data API from ev.energy — 2 operation(s) for reference data.
  name: ev.energy Reference Data API
  slug: ev-energy-reference-data-api
- description: Geographic regions and region groups used for program eligibility and tariffs.
  name: ev.energy Regions API
  slug: ev-energy-regions-api
- description: The root endpoint which lists all the top-level collections.
  name: ev.energy Root API
  slug: ev-energy-root-api
- description: Endpoints for interacting with sites containing multiple EVSEs.
  name: ev.energy Sites API
  slug: ev-energy-sites-api
- description: Endpoints for interacting with solar arrays and inverters.
  name: ev.energy Solar API
  slug: ev-energy-solar-api
- description: Endpoints for interacting with solar forecasts and their logs.
  name: ev.energy Solar Forecasts API
  slug: ev-energy-solar-forecasts-api
- description: Endpoints for interacting with user subscriptions.
  name: ev.energy Subscriptions API
  slug: ev-energy-subscriptions-api
- description: Endpoints for interacting with customer support tickets.
  name: ev.energy Support Tickets API
  slug: ev-energy-support-tickets-api
- description: Endpoints related to energy suppliers and their tariffs.
  name: ev.energy Tariffs API
  slug: ev-energy-tariffs-api
- description: Endpoints for interacting with users.
  name: ev.energy Users API
  slug: ev-energy-users-api
- description: Endpoints for interacting with vehicles.
  name: ev.energy Vehicles API
  slug: ev-energy-vehicles-api
- description: Endpoints for virtual power plant - dispatch coordination and reporting.
  name: ev.energy VPP API
  slug: ev-energy-vpp-api
- description: Endpoints for configuring and managing webhooks.
  name: ev.energy Webhooks API
  slug: ev-energy-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Ev Energy Webhooks
  slug: ev-energy-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ev-energy-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ev-energy-api-v2-overlay.yaml
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
  name: ev.energy API Docs MCP Server
  slug: evenergy-api-docs-mcp-server
modified: '2026-08-12'
name: ev.energy
nav: Providers
network: true
overview: 'ev.energy publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Boundary Meters API, Carbon API, and 22 more. Tagged areas include Company, Energy, Electric Vehicles, EV Charging, and Smart Charging.


  The ev.energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ev.energy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 17 more developer resources.'
plans:
- name: Ev Energy Plans Pricing
  plan_count: 0
  slug: ev-energy-plans-pricing
random_paper: 11
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
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 65.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 57.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 71.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ev-energy/refs/heads/main/screenshots/ev-energy-2026-08-17T080920.png
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
