---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Wattwatchers Agentic Access
  operation_count: 14
  slug: wattwatchers-agentic-access
  summary_line: 14 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api-v3.wattwatchers.com.au
  baseurl_source: declared
  description: Operations related to devices
  name: Wattwatchers Devices API
  slug: wattwatchers-devices-api
- baseURL: https://api-v3.wattwatchers.com.au
  baseurl_source: declared
  description: Operations related to Long Energy (LE)
  name: Wattwatchers Long Energy API
  slug: wattwatchers-long-energy-api
- baseURL: https://api-v3.wattwatchers.com.au
  baseurl_source: declared
  description: Operations related to Modbus
  name: Wattwatchers Modbus API
  slug: wattwatchers-modbus-api
- baseURL: https://api-v3.wattwatchers.com.au
  baseurl_source: declared
  description: Operations related to Short Energy (SE)
  name: Wattwatchers Short Energy API
  slug: wattwatchers-short-energy-api
artifact_total: 11
collections:
- collection_type: open
  name: Wattwatchers API
  slug: open-wattwatchers-rest-api-v3
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
- description: 'Candidate MCP tool surface for the Wattwatchers REST API v3 (Mercury). All 14 operations map cleanly to tools. Note the safety profile: 13 of 14 are safe reads, and exactly one — update_device — is a '
  name: Wattwatchers MCP Server
  slug: wattwatchers-mcp-server
modified: '2026-07-27'
name: Wattwatchers
nav: Providers
network: true
overview: 'Wattwatchers publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Long Energy API, Modbus API, and 1 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Smart Metering.


  Wattwatchers'' developer surface includes authentication, documentation, changelog, support, API reference, getting-started guide, code examples, and 24 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Wattwatchers Rate Limits
  slug: wattwatchers-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 60.2
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wattwatchers/refs/heads/main/screenshots/wattwatchers-2026-09-02T170454.png
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
