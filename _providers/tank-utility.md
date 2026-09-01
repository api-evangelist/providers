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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Exchange account credentials for a short-lived API token.
  name: Tank Utility Authentication API
  slug: tank-utility-authentication-api
- description: List and read propane tank monitor devices.
  name: Tank Utility Devices API
  slug: tank-utility-devices-api
arazzos:
- description: Authenticate to the Tank Utility API, list the propane monitors on the account, and read the latest reading (fuel level %, temperature) for the first device.
  name: Tank Utility — read propane tank level
  slug: tank-utility-read-tank-level
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tank Utility Propane Monitor Authentication API
  slug: open-tank-utility-authentication-api
- collection_type: open
  name: Tank Utility Propane Monitor Authentication Devices API
  slug: open-tank-utility-devices-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tank-utility-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tank-utility-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tank-utility-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tank-utility-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tank-utility-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tank-utility-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tank-utility-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tank-utility-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/tank-utility-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tank-utility-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tank-utility-devices-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tank-utility-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tank-utility-read-tank-level.yml
- group: operate
  title: ''
  type: Support
  url: https://support.tankutility.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://tankutility.com/blog/
- group: start
  title: ''
  type: Login
  url: https://portal.tankutility.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tankutility.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anova.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://tankutility.com
created: '2026-07-17'
description: Tank Utility makes LTE-connected propane tank monitors, mobile apps, and a read-only API that surface their data. Its sensors report tank fuel level, temperature, and battery state so homeowners get low-fuel alerts and fuel marketers can route deliveries by real consumption instead of guesswork — Tank Utility says this drops the same gallons in up to 40% fewer deliveries. The Tank Utility API lets an account exchange credentials (HTTP Basic) for a short-lived token, list the monitors on the account, and read each device's latest reading. Tank Utility is owned by Anova.
image: https://tankutility.com/wp-content/uploads/2025/06/logo_merge.png
layout: provider
mcp_servers:
- description: ''
  name: Tank Utility MCP Server
  slug: tank-utility-mcp-server
modified: '2026-07-21'
name: Tank Utility
nav: Providers
network: true
overview: 'Tank Utility publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Devices API. Tagged areas include Propane, Tank Monitoring, IoT, Fuel Delivery, and Telemetry.


  Tank Utility''s developer surface includes authentication, CLI, support, engineering blog, and 16 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 14.2
    developer_ergonomics: 28.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tank Utility Authentication
  slug: tank-utility-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tank Utility Domain Security
  slug: tank-utility-domain-security
  summary_line: TLSv1.3
slug: tank-utility
tags:
- Propane
- Tank Monitoring
- IoT
- Fuel Delivery
- Telemetry
- Energy
- Sensors
- Company
website: https://tankutility.com
---
