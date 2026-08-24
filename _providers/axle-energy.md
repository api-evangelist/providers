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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 32
  human_in_the_loop: 2
  name: Axle Energy Agentic Access
  operation_count: 55
  slug: axle-energy-agentic-access
  summary_line: 55 operations · 32 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: Authenticate yourself with the Axle API
  name: Axle Energy 1. Authentication API
  slug: axle-energy-1-authentication-api
- description: Find key info about your sites
  name: Axle Energy 2. Meters API
  slug: axle-energy-2-meters-api
- description: Register your sites with Axle; configure market participation
  name: Axle Energy 3. Sites API
  slug: axle-energy-3-sites-api
- description: Register your assets with Axle
  name: Axle Energy 4. Assets API
  slug: axle-energy-4-assets-api
- description: Send asset metrics to Axle, for analysis and optimisation purposes
  name: Axle Energy 5. Data API
  slug: axle-energy-5-data-api
- description: Determine how much your users have earned by participating with Axle; allow balance withdrawal
  name: Axle Energy 6. Rewards API
  slug: axle-energy-6-rewards-api
- description: Validate structured data against Axle's rules
  name: Axle Energy 7. Validation API
  slug: axle-energy-7-validation-api
- description: Get example data for testing
  name: Axle Energy 8. Examples API
  slug: axle-energy-8-examples-api
artifact_total: 22
asyncapis:
- description: ''
  name: Axle Energy Dispatch Webhooks
  slug: axle-energy-dispatch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Axle 1. Authentication API
  slug: open-axle-energy-1-authentication-api
- collection_type: open
  name: Axle 1. Authentication 2. Meters API
  slug: open-axle-energy-2-meters-api
- collection_type: open
  name: Axle 1. Authentication 3. Sites API
  slug: open-axle-energy-3-sites-api
- collection_type: open
  name: Axle 1. Authentication 4. Assets API
  slug: open-axle-energy-4-assets-api
- collection_type: open
  name: Axle 1. Authentication 5. Data API
  slug: open-axle-energy-5-data-api
- collection_type: open
  name: Axle 1. Authentication 6. Rewards API
  slug: open-axle-energy-6-rewards-api
- collection_type: open
  name: Axle 1. Authentication 7. Validation API
  slug: open-axle-energy-7-validation-api
- collection_type: open
  name: Axle 1. Authentication 8. Examples API
  slug: open-axle-energy-8-examples-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/axle-energy-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.axle.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axle.energy/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.axle.energy/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axle.energy/components/getting-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.axle.energy/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axle-energy
- group: operate
  title: ''
  type: Support
  url: mailto:support@axle.energy
- group: design
  title: ''
  type: Idempotency
  url: conventions/axle-energy-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/axle-energy-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/axle-energy-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/axle-energy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/axle-energy-packages.yml
- group: design
  title: ''
  type: Components
  url: components/axle-energy-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/axle-energy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/axle-energy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/axle-energy-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axle-energy-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/axle-energy-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/axle-energy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.axle.energy/
created: '2026-07-17'
description: Axle Energy operates a virtual power plant (VPP) platform that connects distributed energy assets — electric vehicles, EV chargers, home batteries, and heat pumps — to electricity flexibility markets through a single unified API. Partners (carmakers, charger and battery OEMs, HVAC suppliers, and utilities) register sites and assets, prequalify and enrol them in flex propositions, stream telemetry and plug/charge events, and let end users monetise shiftable demand. The API covers authentication, meter lookup (MPAN), sites, assets, telemetry/readings, rewards/payouts, validation, and half-hourly price curves, with markets live across Great Britain, France, Germany, the Netherlands, Denmark and Sweden. React/hosted UI components and a documented outbound dispatch webhook round out the developer surface.
image: https://cdn.prod.website-files.com/6706a319ca966248529c44be/6a4dc6c17d68be5261e80f8d_OG.png
layout: provider
mcp_servers:
- description: ''
  name: Axle Energy MCP Server
  slug: axle-energy-mcp-server
modified: '2026-07-18'
name: Axle Energy
nav: Providers
network: true
overview: 'Axle Energy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including 1. Authentication API, 2. Meters API, 3. Sites API, and 5 more. Tagged areas include Company, Energy, Flexibility, Virtual Power Plant, and Electric Vehicles.


  The Axle Energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Axle Energy''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 39.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 62.6
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axle-energy/refs/heads/main/screenshots/axle-energy-2026-07-25T202055.png
security:
- kind: authentication
  name: Axle Energy Authentication
  slug: axle-energy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Axle Energy Domain Security
  slug: axle-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: axle-energy
tags:
- Company
- Energy
- Flexibility
- Virtual Power Plant
- Electric Vehicles
- Smart Charging
- Batteries
- Demand Response
- Grid
- Sustainability
website: https://www.axle.energy/
---
