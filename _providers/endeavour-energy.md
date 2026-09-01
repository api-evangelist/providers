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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Endeavour Energy Agentic Access
  operation_count: 32
  slug: endeavour-energy-agentic-access
  summary_line: 32 operations
api_count: 2
apis:
- description: API to enumerate datasets
  name: Endeavour Energy Catalog API
  slug: endeavour-energy-catalog-api
- description: API to work on records
  name: Endeavour Energy Dataset API
  slug: endeavour-energy-dataset-api
artifact_total: 11
collections:
- collection_type: open
  name: Explore API
  slug: open-endeavour-energy-open-data-explore-api-v2-0
- collection_type: open
  name: Explore API
  slug: open-endeavour-energy-open-data-explore-api-v2-1
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/endeavour-energy-open-data-explore-api-v2-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/endeavour-energy-open-data-explore-api-v2-0-overlay.yaml
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
- description: 'Endeavour Energy publishes no MCP server. This is a CANDIDATE manifest: one tool per real operationId, each inheriting its input contract from the backing operation in the harvested OpenAPI. It is a d'
  name: Endeavour Energy MCP Server
  slug: endeavour-energy-mcp-server
modified: '2026-07-27'
name: Endeavour Energy
nav: Providers
network: true
overview: 'Endeavour Energy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Endeavour Energy''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, engineering blog, and 34 more developer resources.'
random_paper: 5
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
  composite: 51.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 53.8
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 51.8
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
