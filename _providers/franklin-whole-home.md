---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Franklin Whole Home Agentic Access
  operation_count: 38
  slug: franklin-whole-home-agentic-access
  summary_line: 38 operations · 19 acting
api_count: 1
apis:
- description: Token issuance for the FranklinWH partner API.
  name: Franklin Whole Home Authentication API
  slug: franklin-whole-home-authentication-api
- description: Power, energy, telemetry, inventory and historical load data.
  name: Franklin Whole Home Device Data API
  slug: franklin-whole-home-device-data-api
- description: Device inventory, device information and device parameters.
  name: Franklin Whole Home Devices API
  slug: franklin-whole-home-devices-api
- description: Grid-event scheduling and query.
  name: Franklin Whole Home Grid Events API
  slug: franklin-whole-home-grid-events-api
- description: Device grouping and bulk settings applied by group.
  name: Franklin Whole Home Groups API
  slug: franklin-whole-home-groups-api
- description: Audit log of setting changes.
  name: Franklin Whole Home Modification Records API
  slug: franklin-whole-home-modification-records-api
- description: Site records — query, list, modify and delete.
  name: Franklin Whole Home Sites API
  slug: franklin-whole-home-sites-api
- description: Sunrun-specific operations on the /api-sunrun namespace.
  name: Franklin Whole Home Sunrun API
  slug: franklin-whole-home-sunrun-api
- description: Sunrun site asset inventory.
  name: Franklin Whole Home Sunrun Sites API
  slug: franklin-whole-home-sunrun-sites-api
- description: Sunrun energy-management and aPower switch control.
  name: Franklin Whole Home Sunrun System Setup API
  slug: franklin-whole-home-sunrun-system-setup-api
- description: Time-of-use profiles, aPower switch control and smart-circuit settings.
  name: Franklin Whole Home System Settings API
  slug: franklin-whole-home-system-settings-api
- description: Historical device warnings and backup (outage) events.
  name: Franklin Whole Home Warnings and Events API
  slug: franklin-whole-home-warnings-and-events-api
artifact_total: 18
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/franklin-whole-home-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.franklinwh.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.franklinwh.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.franklinwh.com/
- group: company
  title: ''
  type: Blog
  url: https://www.franklinwh.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.franklinwh.com/support/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.franklinwh.com/support/articles/faq/
- group: docs
  title: ''
  type: Documentation
  url: https://www.franklinwh.com/support/documents/
- group: start
  title: ''
  type: SignUp
  url: https://www.franklinwh.com/apply?role=installer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.franklinwh.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.franklinwh.com/policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/franklin-whole-home-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/franklin-whole-home-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/franklin-whole-home-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/franklin-whole-home-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/franklin-whole-home-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/franklin-whole-home-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/franklin-whole-home-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/franklin-whole-home-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/franklin-whole-home-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/franklin-whole-home-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/franklin-whole-home-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/franklin-whole-home-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/franklin-whole-home-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/franklin-whole-home-agentic-access.yml
created: '2026-08-16'
description: 'Franklin Whole Home (FranklinWH Energy Storage Inc.) builds whole-home energy management and storage hardware for residential solar: the aPower lithium iron phosphate AC battery, the aGate energy management and controller unit, and the FranklinWH mobile app, together forming an ecosystem that coordinates solar, battery, grid, generator and EV power sources for backup, self-consumption, time-of-use arbitrage and off-grid operation. Founded in 2019 and headquartered in the San Francisco Bay Area, the company designs and manufactures nearly all of its own components and sells through a certified installer and distributor channel. FranklinWH publishes a partner API - a unified developer access platform for authorised third-party owners, financiers, installers and service providers to read device and site data, monitor system performance, receive operational alerts and perform approved remote device control.'
image: https://www.franklinwh.com/icoLogo1.png
layout: provider
mcp_servers:
- description: ''
  name: Franklin Whole Home MCP Server
  slug: franklin-whole-home-mcp-server
modified: '2026-08-16'
name: Franklin Whole Home
nav: Providers
network: true
overview: 'Franklin Whole Home publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Device Data API, Devices API, and 9 more. Tagged areas include Company, Energy, Energy Storage, Home Energy Management, and Solar.


  Franklin Whole Home''s developer surface includes API reference, engineering blog, support, documentation, signup flow, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Franklin Whole Home Plans Pricing
  plan_count: 0
  slug: franklin-whole-home-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Franklin Whole Home Rate Limits
  slug: franklin-whole-home-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/franklin-whole-home/refs/heads/main/screenshots/franklin-whole-home-2026-08-17T080936.png
security:
- kind: authentication
  name: Franklin Whole Home Authentication
  slug: franklin-whole-home-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Franklin Whole Home Domain Security
  slug: franklin-whole-home-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: franklin-whole-home
tags:
- Company
- Energy
- Energy Storage
- Home Energy Management
- Solar
- Batteries
- Internet of Things
- Smart Home
- Electric Vehicles
- Cleantech
- Device Telemetry
website: https://www.franklinwh.com/
---
