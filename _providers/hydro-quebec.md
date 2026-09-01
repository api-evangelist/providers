---
agent_readiness:
  band: agent-native
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hydro Quebec Agentic Access
  operation_count: 32
  slug: hydro-quebec-agentic-access
  summary_line: 32 operations
api_count: 2
apis:
- description: The legacy Opendatasoft Search API v1 still served on the Hydro-Québec open data portal. Verified live and anonymous on 2026-07-27 — GET /api/datasets/1.0/search/ returned HTTP 200 with all 26 dataset
  name: Hydro-Québec Open Data Search API v1
  slug: hydro-quebec-open-data-search-api-v1
- description: API to enumerate datasets
  name: Hydro-Québec Catalog API
  slug: hydro-quebec-catalog-api
- description: API to work on records
  name: Hydro-Québec Dataset API
  slug: hydro-quebec-dataset-api
artifact_total: 12
collections:
- collection_type: open
  name: Explore API
  slug: open-hydro-quebec-open-data-explore-api-v2-0
- collection_type: open
  name: Explore API
  slug: open-hydro-quebec-open-data-explore-api-v2-1
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hydro-quebec-open-data-explore-api-v2-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hydro-quebec-open-data-explore-api-v2-0-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hydro-quebec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydro-quebec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hydro-quebec-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hydroquebec.com/
- group: start
  title: ''
  type: Portal
  url: https://donnees.hydroquebec.com/pages/accueil/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://donnees.hydroquebec.com/pages/accueil/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hydroquebec.com/documents-data/open-data/
- group: docs
  title: ''
  type: APIReference
  url: https://donnees.hydroquebec.com/api/v2/console
- group: start
  title: ''
  type: GettingStarted
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://www.hydroquebec.com/sefco2016/en/open-data-contact-us.html
- group: company
  title: ''
  type: Blog
  url: https://news.hydroquebec.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hydroquebec.com/terms-confidentiality.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hydroquebec.com/documents-data/act-respecting-access/protection-personal-information/
- group: other
  title: ''
  type: Licensing
  url: https://www.hydroquebec.com/documents-data/open-data/licence.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hydro-quebec
- group: build
  title: ''
  type: Packages
  url: packages/hydro-quebec-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hydro-quebec-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hydro-quebec-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hydro-quebec-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hydro-quebec-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydro-quebec-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hydro-quebec-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hydro-quebec-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydro-quebec-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huwise.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Introduction/v2.1-Changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hydro-quebec-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hydro-quebec-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hydro-quebec-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hydro-quebec-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hydro-quebec-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hydro-quebec-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/hydro-quebec-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hydro-quebec-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hydro-quebec-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://donnees.hydroquebec.com/.well-known/security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: Hydro-Québec is the government-owned Crown corporation that generates, transmits and distributes almost all of the electricity consumed in Québec, Canada — a vertically integrated, near-monopoly utility running one of the largest hydroelectric fleets in the world and serving roughly 4.6 million customer accounts across the province. It sits at every point of the value chain at once, as generator, transmission owner, distributor and retailer, plus a cross-border exporter into the New England and New York markets. Its API posture is a clean split. Market and grid data is genuinely open — a public Opendatasoft-powered portal at donnees.hydroquebec.com serves 26 datasets (electricity demand and generation, imports and exports, outages, GHG emission factors, hydrometric and weather data, winter peak demand events, vegetation control) through a documented, anonymously callable REST API with a machine-readable OpenAPI 3.0.3 description and a DCAT catalog export, licensed CC BY-NC 4.0.
  Consumer data is closed — there is no documented customer-facing API, no Green Button Download My Data or Connect My Data service, and no third-party consent flow; a customer's own usage is reachable only by logging into the Espace client web portal. Québec has no consumer energy data right. Ontario's Green Button regulation (O. Reg. 633/21 under the Electricity Act, 1998) is province-specific and does not bind Hydro-Québec, and Canada has no national equivalent to Australia's Consumer Data Right energy regime. Open market data, closed consumer data, no mandate.
image: https://hydroquebec.opendatasoft.com/assets/theme_image/hq-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Hydro-Québec MCP Server
  slug: hydro-québec-mcp-server
modified: '2026-07-27'
name: Hydro-Québec
nav: Providers
network: true
overview: 'Hydro-Québec publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Energy, Canada, Utilities, Electricity, and Grid.


  Hydro-Québec''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Hydro Quebec Rate Limits
  slug: hydro-quebec-rate-limits
scopes:
- name: Hydro Quebec Scopes
  scope_count: 1
  slug: hydro-quebec-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hydro-quebec/refs/heads/main/screenshots/hydro-quebec-2026-08-07T170514.png
security:
- kind: authentication
  name: Hydro Quebec Authentication
  slug: hydro-quebec-authentication
  summary_line: none/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Hydro Quebec Domain Security
  slug: hydro-quebec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hydro Quebec Vulnerability Disclosure
  slug: hydro-quebec-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hydro-quebec
tags:
- Energy
- Canada
- Utilities
- Electricity
- Grid
- Energy Markets
- Renewables
- Open Data
- Demand Response
- Carbon
website: https://www.hydroquebec.com/
---
