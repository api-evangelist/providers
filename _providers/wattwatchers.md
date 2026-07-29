---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Wattwatchers Agentic Access
  operation_count: 14
  slug: wattwatchers-agentic-access
  summary_line: 14 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'The Wattwatchers REST API v3, code-named Mercury — 14 documented operations across 13 paths, covering device inventory and configuration (including switch control via PATCH), 30-second "short energy" '
  name: Wattwatchers REST API v3 (Mercury)
  slug: wattwatchers-rest-api-v3
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wattwatchers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wattwatchers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wattwatchers-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wattwatchers.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wattwatchers.com.au/
- group: docs
  title: ''
  type: InteractiveDocumentation
  url: https://docs.wattwatchers.com.au/api/v3/openapi/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.wattwatchers.com.au/api/v3/auth.html
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.wattwatchers.com.au/api/v3/rate-limits.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.wattwatchers.com.au/api/v3/release-notes.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wattwatchers
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/wattwatchers/rest-api-notebooks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wattwatchers-digital-energy
- group: operate
  title: ''
  type: Support
  url: https://service.wattwatchers.com.au/
- group: other
  title: ''
  type: Applications
  url: https://docs.wattwatchers.com.au/apps.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wattwatchers.com.au/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wattwatchers.com.au/api/v3/endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://service.wattwatchers.com.au/getting-started-with-wattwatchers
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.wattwatchers.com.au/api/roadmap.html
- group: build
  title: ''
  type: Packages
  url: packages/wattwatchers-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wattwatchers-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wattwatchers-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wattwatchers-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wattwatchers-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wattwatchers-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wattwatchers-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wattwatchers-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wattwatchers-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wattwatchers-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/wattwatchers-rest-api-v3-examples.json
- group: other
  title: ''
  type: Overlay
  url: overlays/wattwatchers-rest-api-v3-overlay.yaml
created: '2026-07-27'
description: 'Wattwatchers is an Australian digital energy company (founded 2007, headquartered in Sydney, NSW) that designs and manufactures the Auditor family of DIN-rail electricity monitoring and switching devices, and operates the cloud platform behind them. It sits behind the meter rather than at it — Auditors clamp onto individual circuits and report real-time, circuit-level energy data over 4G or WiFi to Wattwatchers'' hosted platform, which resells that data to solar installers, energy retailers, energy services companies, EV and DER programs, schools and research trials. Its API posture is genuinely open at the documentation layer and closed at the data layer — the full REST API v3 (Mercury) reference, a live Swagger UI and a downloadable OpenAPI 3.0 contract are all served anonymously from docs.wattwatchers.com.au, but no key is self-serve: Wattwatchers issues bearer tokens by hand and scopes each one to the specific devices you own or manage, so the API returns your fleet''s
  data and nothing else. Consumer usage data is therefore available through a documented API, while no open grid or market data is published at all. Wattwatchers is not a designated Consumer Data Right energy data holder and does not appear as an accredited data recipient — the CDR energy mandate applies to retailers and AEMO, not to behind-the-meter hardware vendors, so this platform carries no CDR obligation and implements no CDR or Green Button data standard. Wattwatchers entered voluntary administration in October 2025 and was acquired by EPX Limited (ASX:EPX, formerly EP&T Global); the Wattwatchers knowledge base now redirects to support.epx.tech, while the developer documentation, the API host and the OpenAPI contract all remain live and unchanged.'
examples:
- key_count: 7
  name: Wattwatchers Rest Api V3 Examples
  slug: wattwatchers-rest-api-v3-examples
image: https://docs.wattwatchers.com.au/assets/images/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: wattwatchers-mcp.yml
  slug: wattwatchers-mcpyml
modified: '2026-07-27'
name: Wattwatchers
nav: Providers
network: true
overview: 'Wattwatchers publishes 1 API on the [APIs.io](https://apis.io/) network: REST API v3 (Mercury). Tagged areas include Energy, Australia, Utilities, Electricity, and Smart Metering.


  Wattwatchers'' developer surface includes authentication, documentation, changelog, support, API reference, getting-started guide, code examples, and 24 more developer resources.'
random_paper: 33
rate_limits:
- limit_count: 2
  name: Wattwatchers Rate Limits
  slug: wattwatchers-rate-limits
score:
  band: thin
  composite: 33.3
  delta: -4.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wattwatchers Authentication
  slug: wattwatchers-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wattwatchers Domain Security
  slug: wattwatchers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wattwatchers
tags:
- Energy
- Australia
- Utilities
- Electricity
- Smart Metering
- Energy Data
- IoT
- Solar
- DER
- Demand Response
website: https://wattwatchers.com.au/
---
