---
access_model:
  confidence: high
  label: Free · Anonymous, no signup (open grid data only)
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - documentation
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Atco Agentic Access
  operation_count: 5
  slug: atco-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- baseURL: https://services7.arcgis.com/cw2emabghNLkoYlB/arcgis/rest/services/AGO_HostingCapacity/FeatureServer
  baseurl_source: declared
  description: Read-only queries against the hosting capacity feature layer
  name: ATCO Query API
  slug: atco-query-api
- baseURL: https://services7.arcgis.com/cw2emabghNLkoYlB/arcgis/rest/services/AGO_HostingCapacity/FeatureServer
  baseurl_source: declared
  description: Feature service and feature layer metadata
  name: ATCO Service API
  slug: atco-service-api
arazzos:
- description: Go from ATCO Electric's whole Alberta distribution grid to a small, mapped shortlist of the feeder segments with the most DER hosting capacity, without ever pulling all 880,623 features.
  name: ATCO Electric DER siting shortlist
  slug: atco-der-siting-shortlist
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-atco-electric-hosting-capacity-featureserver
- collection_type: open
  name: API Collection
  slug: open-atco-electric-hosting-capacity-layer-0
- collection_type: open
  name: ATCO Electric Hosting Capacity Feature Service
  slug: open-atco-electric-hosting-capacity
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/atco-electric-hosting-capacity-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atco-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atco-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atco-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atco-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atco-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atco-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atco-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/atco-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.atco.com/
- group: company
  title: ''
  type: About
  url: https://www.atco.com/en-ca/about-us.html
- group: company
  title: ''
  type: Website
  url: https://electric.atco.com/en-ca.html
- group: company
  title: ''
  type: Website
  url: https://gas.atco.com/en-ca.html
- group: company
  title: ''
  type: Website
  url: https://www.atcoenergy.com/
- group: other
  title: ''
  type: SignIn
  url: https://store.atco.com/ccrz__CCSiteLogin
- group: start
  title: ''
  type: Login
  url: https://store.atco.com/ccrz__CCSiteLogin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atco.com/en-ca/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atco.com/en-ca/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://www.atco.com/en-ca/about-us/contact.html
- group: company
  title: ''
  type: News
  url: https://www.atco.com/en-ca/about-us/news.html
- group: company
  title: ''
  type: Investors
  url: https://www.atco.com/en-ca/investors.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atco-group
- group: other
  title: ''
  type: Regulator
  url: https://www.auc.ab.ca/
- group: other
  title: ''
  type: Regulator
  url: https://www.aeso.ca/
created: '2026-07-27'
description: 'ATCO Ltd. (TSX: ACO.X) is a Calgary, Alberta diversified global corporation and the controlling shareholder of Canadian Utilities Limited, through which it runs the regulated energy businesses that make it one of western Canada''s largest utility groups. It sits across several tiers of the value chain at once: ATCO Electric owns and operates electricity transmission and distribution across Alberta, ATCO Gas and ATCO Pipelines distribute and transmit natural gas in the province, ATCO EnPower builds storage, renewables and hydrogen assets, ATCO Australia operates gas distribution infrastructure in Western Australia, and ATCO Energy is a competitive retailer selling electricity, natural gas and home services to Alberta customers. Its API posture is the mirror image of the Ontario utilities: no consumer energy data mandate reaches it at all. Alberta has no Green Button regulation, ATCO is not on the Green Button Alliance member list, and it does not appear in the public Australian
  CDR energy data holder register — so there is no consumer data API, and a customer''s usage and billing data lives only behind the My Account login on a Salesforce commerce portal. What ATCO does publish, unmandated and without any signup at all, is real open grid data: ATCO Electric''s DER hosting capacity map is served from a public, anonymously queryable Esri ArcGIS REST feature service carrying 880,623 feeder segment features, linked directly from ATCO Electric''s own micro-generation and grid-connection pages. Open grid data, closed consumer data, no developer portal, and no OpenAPI anywhere on the estate.'
image: https://www.atco.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool set (derived — ATCO publishes no MCP server)
  slug: candidate-mcp-tool-set-derived-atco-publishes-no-mcp-server
modified: '2026-07-27'
name: ATCO
nav: Providers
network: true
overview: 'ATCO publishes 2 APIs on the [APIs.io](https://apis.io/) network: Query API and Service API. Tagged areas include Energy, Canada, Utilities, Electricity, and Gas.


  ATCO''s developer surface includes authentication, support, product news, and 24 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 28.4
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
    contract_quality: 16.0
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atco/refs/heads/main/screenshots/atco-2026-08-07T161823.png
security:
- kind: authentication
  name: Atco Authentication
  slug: atco-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atco Domain Security
  slug: atco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: atco
tags:
- Energy
- Canada
- Utilities
- Electricity
- Gas
- Grid
- Distribution
- Transmission
- DER
- Solar
- Renewables
- Open Data
- Geospatial
- Alberta
website: https://www.atco.com/
---
