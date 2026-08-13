---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Endeavour Energy Agentic Access
  operation_count: 32
  slug: endeavour-energy-agentic-access
  summary_line: 32 operations
api_count: 1
apis:
- description: Anonymous, key-free REST API over Endeavour Energy's public network open data catalogue, served on the Opendatasoft Explore API v2.1. Exposes eight datasets covering distribution network assets (440,7
  name: Endeavour Energy Open Data Explore API
  slug: endeavour-energy-open-data-explore-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/endeavour-energy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/endeavour-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/endeavour-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/endeavour-energy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.endeavourenergy.com.au/
- group: start
  title: ''
  type: Portal
  url: https://data.endeavourenergy.com.au/pages/home/
- group: docs
  title: ''
  type: Documentation
  url: https://www.endeavourenergy.com.au/our-network/resilience-and-emergency-planning/nsw-emergency-backstop-mechanism
- group: docs
  title: ''
  type: Documentation
  url: https://www.endeavourenergy.com.au/for-your-home/solar-and-battery-options/flexible-exports
- group: docs
  title: ''
  type: Documentation
  url: https://www.endeavourenergy.com.au/our-network/network-demand-and-capacity/network-capacity-map
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.endeavourenergy.com.au/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/endeavour-energy-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.endeavourenergy.com.au/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/endeavour-energy-well-known.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/endeavour-energy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.endeavourenergy.com.au/pages/home/
- group: docs
  title: ''
  type: Documentation
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html
- group: docs
  title: ''
  type: APIReference
  url: https://data.endeavourenergy.com.au/api-console/explore/v2.1/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://www.endeavourenergy.com.au/about-us/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.endeavourenergy.com.au/about-us/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.endeavourenergy.com.au/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://data.endeavourenergy.com.au/login/
- group: build
  title: ''
  type: Packages
  url: packages/endeavour-energy-packages.yml
- group: design
  title: ''
  type: Components
  url: components/endeavour-energy-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/endeavour-energy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/endeavour-energy-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/endeavour-energy-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/endeavour-energy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/endeavour-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/endeavour-energy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Versioning/Deprecation-warnings
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/endeavour-energy-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/endeavour-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/endeavour-energy-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/endeavour-energy-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/endeavour-energy-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/endeavour-energy-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/endeavour-energy-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: 'Endeavour Energy is the regulated electricity distribution network service provider (DNSP) for Greater Western Sydney, the Blue Mountains, the Illawarra, the Southern Highlands, the South Coast and Central West of New South Wales, Australia, delivering power to around 2.8 million people over the poles-and-wires network it owns and operates. It sits between transmission and retail in the value chain - it moves electricity and hosts the meters, but it does not sell energy to consumers, so it holds no retail billing relationship. Its API posture is a sharp split. On the market and network side it is genuinely open: a live Opendatasoft portal at data.endeavourenergy.com.au serves eight network datasets (poles, conductors, distribution districts, other network assets, distribution substation available capacity, and live planned/unplanned/single-premise outages) through a documented, anonymous, no-key REST Explore API with a downloadable OpenAPI 3.0.3 contract, most of it under the
  Open Database Licence. On the consumer side it is closed and, more importantly, unobligated: Australia''s Consumer Data Right was extended to energy, but the designation put the data-holder obligation on electricity retailers as primary holders and AEMO as the secondary holder and gateway, not on distributors. Endeavour Energy appears nowhere in the 84 brands of the CDR energy data holder register, publishes no CDR base URI, and makes no reference to the Consumer Data Right anywhere on its corporate site. It does operate a CSIP-AUS (Common Smart Inverter Profile - Australia) utility server for NSW flexible exports and the emergency backstop mechanism, but that machine interface is device-facing and entirely undocumented publicly. The open data portal itself is not linked from the corporate website.'
image: https://www.endeavourenergy.com.au/images/ee-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: endeavour-energy-mcp.yml
  slug: endeavour-energy-mcpyml
modified: '2026-07-27'
name: Endeavour Energy
nav: Providers
network: true
overview: 'Endeavour Energy publishes 1 API on the [APIs.io](https://apis.io/) network: Open Data Explore API. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Endeavour Energy''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
random_paper: 104
rate_limits:
- limit_count: 2
  name: Endeavour Energy Rate Limits
  slug: endeavour-energy-rate-limits
scopes:
- name: Endeavour Energy Scopes
  scope_count: 1
  slug: endeavour-energy-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 56.7
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 59.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/endeavour-energy/refs/heads/main/screenshots/endeavour-energy-2026-08-07T164855.png
security:
- kind: authentication
  name: Endeavour Energy Authentication
  slug: endeavour-energy-authentication
  summary_line: none/apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Endeavour Energy Domain Security
  slug: endeavour-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Endeavour Energy Vulnerability Disclosure
  slug: endeavour-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: endeavour-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Open Data
- Energy Networks
- Distribution
- Outages
- Consumer Data Right
- Smart Metering
- DER
- Solar
- Renewables
website: https://www.endeavourenergy.com.au/
---
