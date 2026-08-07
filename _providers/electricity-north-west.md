---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    well_known_catalog: true
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The current Opendatasoft Explore REST API v2.1 scoped to the SP Electricity North West open data domain. Read-only (GET only, JSON), 16 documented paths covering catalogue search over the 146 publishe
  name: SP Electricity North West Open Data Explore API v2.1
  slug: explore-api-v2-1
- description: The previous-generation Opendatasoft Explore REST API v2.0, still served on the SP Electricity North West domain alongside v2.1. Same 16-path read-only shape — catalogue, dataset metadata, records, fa
  name: SP Electricity North West Open Data Explore API v2.0
  slug: explore-api-v2-0
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.enwl.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://electricitynorthwest.opendatasoft.com/api
- group: start
  title: ''
  type: Portal
  url: https://electricitynorthwest.opendatasoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://electricitynorthwest.opendatasoft.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://help.huwise.com/apis/ods-explore-v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.huwise.com/apis/ods-explore-v2/#section/Getting-Started
- group: start
  title: ''
  type: Sandbox
  url: sandbox/electricity-north-west-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://electricitynorthwest.opendatasoft.com/api-console/explore/v2.1/
- group: start
  title: ''
  type: SignUp
  url: https://electricitynorthwest.opendatasoft.com/pages/registration_log_in/
- group: other
  title: ''
  type: Registration
  url: https://electricitynorthwest.opendatasoft.com/pages/registration_log_in/
- group: operate
  title: ''
  type: Support
  url: mailto:dataportal@enwl.co.uk
- group: company
  title: ''
  type: Blog
  url: https://news.enwl.co.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electricity-north-west
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spenw-open-data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enwl.co.uk/about-us/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enwl.co.uk/misc/privacy-policy/
- group: other
  title: ''
  type: Data
  url: https://electricitynorthwest.opendatasoft.com/explore
- group: other
  title: ''
  type: Data
  url: https://electricitynorthwest.opendatasoft.com/api/explore/v2.1/catalog/exports/dcat
- group: auth
  title: ''
  type: Authentication
  url: authentication/electricity-north-west-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/electricity-north-west-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/electricity-north-west-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/electricity-north-west-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/electricity-north-west-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/electricity-north-west-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/electricity-north-west-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huwise.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://help.huwise.com/apis/ods-explore-v2/#section/Versioning/Deprecation-warnings
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/electricity-north-west-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/electricity-north-west-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/electricity-north-west-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/electricity-north-west-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/electricity-north-west-packages.yml
- group: design
  title: ''
  type: Components
  url: components/electricity-north-west-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/electricity-north-west-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/electricity-north-west-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/electricity-north-west-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/electricity-north-west-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/electricity-north-west-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electricity-north-west-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/electricity-north-west-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.huwise.com/en/security/
- group: other
  title: ''
  type: Regulator
  url: https://www.ofgem.gov.uk/sites/default/files/2024-10/Track_Changes_Data_Best_Practice_Guidance_v301728394292260.pdf
created: '2026-07-27'
description: 'Electricity North West — rebranded SP Electricity North West in August 2025 after Iberdrola acquired it and folded it in alongside SP Energy Networks — is the regulated electricity distribution network operator for the North West of England, running roughly 13,000 km of overhead line and more than 44,000 km of underground cable from Cumbria to Manchester. It is a poles-and-wires business in the regulated middle of the United Kingdom value chain: it owns the meter point and the network, it earns a regulated revenue under Ofgem''s RIIO-ED2 price control, and it never bills the household — the supplier does. Its API posture is a clean split and worth stating plainly. On the MARKET-DATA side it is genuinely API-native for a network operator: it runs an Opendatasoft-hosted open data portal at electricitynorthwest.opendatasoft.com carrying 146 datasets — embedded capacity register, DFES scenarios, LV headroom and peak demand, network capacity heatmaps, GSP connection queue, GIS conductor
  and substation layers — served through the documented Opendatasoft Explore REST API v2.1 (and legacy v2.0) with a real OpenAPI 3.0.3 contract, a DCAT-AP catalogue export, and an in-portal API console. 96 of those datasets are CC BY 4.0 and 8 are Open Government Licence v3.0, but 41 sit under a bespoke "SP ENW Shared Licence" rather than an open one. On the CONSUMER-DATA side there is nothing: the United Kingdom has no consumer energy data-portability right equivalent to Australia''s Consumer Data Right, Great Britain''s smart-meter mandate produced infrastructure (the licensed Smart DCC) rather than a data right, Green Button has no UK footprint, and Electricity North West publishes no customer usage or billing API of any kind. The obligation that actually binds it is Ofgem''s Data Best Practice Guidance under the RIIO-ED2 digitalisation licence condition — an open-data duty, not a consumer data right — and the portal is a real, verifiable implementation of it. Note that the corporate
  site www.enwl.co.uk sits behind a Cloudflare managed challenge and returns HTTP 403 to every non-browser client, so no part of the main website is machine-readable.'
examples:
- key_count: 2
  name: Electricity North West Catalog Facets License Example
  slug: electricity-north-west-catalog-facets-license-example
- key_count: 2
  name: Electricity North West Forbidden Records Example
  slug: electricity-north-west-forbidden-records-example
- key_count: 10
  name: Electricity North West Get Dataset Example
  slug: electricity-north-west-get-dataset-example
- key_count: 2
  name: Electricity North West List Datasets Example
  slug: electricity-north-west-list-datasets-example
- key_count: 1
  name: Electricity North West List Export Formats Example
  slug: electricity-north-west-list-export-formats-example
- key_count: 2
  name: Electricity North West Odsql Error Example
  slug: electricity-north-west-odsql-error-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: electricity-north-west-mcp.yml
  slug: electricity-north-west-mcpyml
modified: '2026-07-27'
name: Electricity North West
nav: Providers
network: true
overview: 'Electricity North West publishes 2 APIs on the [APIs.io](https://apis.io/) network: SP Electricity North West Open Data Explore API v2.1 and SP Electricity North West Open Data Explore API v2.0. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Grid.


  Electricity North West''s developer surface includes developer portal, documentation, API reference, getting-started guide, sandbox, developer console, signup flow, and 37 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 3
  name: Electricity North West Rate Limits
  slug: electricity-north-west-rate-limits
scopes:
- name: Electricity North West Scopes
  scope_count: 1
  slug: electricity-north-west-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 58.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.9
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 86.8
  previous_composite: 58.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Electricity North West Authentication
  slug: electricity-north-west-authentication
  summary_line: apiKey/oauth2/cookie · 4 schemes
- kind: domain-security
  name: Electricity North West Domain Security
  slug: electricity-north-west-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Electricity North West Vulnerability Disclosure
  slug: electricity-north-west-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: electricity-north-west
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- DER
- Renewables
- Energy Markets
- Smart Metering
website: https://www.enwl.co.uk/
---
