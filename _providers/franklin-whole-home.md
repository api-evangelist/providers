---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Franklin Whole Home Agentic Access
  operation_count: 38
  slug: franklin-whole-home-agentic-access
  summary_line: 38 operations · 19 acting
api_count: 1
apis:
- description: The FranklinWH partner API - a unified developer access platform for authorised partners to connect to FranklinWH systems. Thirty-eight operations across a standard namespace (/api-common/) covering s
  name: FranklinWH API
  slug: franklinwh-api
artifact_total: 7
common:
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
  name: franklin-whole-home-mcp.yml
  slug: franklin-whole-home-mcpyml
modified: '2026-08-16'
name: Franklin Whole Home
nav: Providers
network: true
overview: 'Franklin Whole Home publishes 1 API on the [APIs.io](https://apis.io/) network: FranklinWH API. Tagged areas include Company, Energy, Energy Storage, Home Energy Management, and Solar.


  Franklin Whole Home''s developer surface includes API reference, engineering blog, support, documentation, signup flow, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Franklin Whole Home Plans Pricing
  plan_count: 0
  slug: franklin-whole-home-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 0
  name: Franklin Whole Home Rate Limits
  slug: franklin-whole-home-rate-limits
score:
  band: thin
  composite: 29.8
  delta: -12.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 14.7
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
