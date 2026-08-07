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
- description: The live, anonymous REST API behind the SP Energy Networks Open Data Portal — ScottishPower's regulated distribution and transmission arm publishing its network data under Ofgem's Data Best Practice "
  name: SP Energy Networks Open Data Explore API
  slug: spen-open-data-explore-api
- description: 'The legacy Opendatasoft Search API v1.0 still served alongside Explore v2.1 on the SP Energy Networks Open Data Portal. Verified anonymously on 2026-07-27: GET /api/datasets/1.0/search/?rows=1 returne'
  name: SP Energy Networks Open Data Search API (v1.0)
  slug: spen-open-data-search-api-v1
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scottishpower-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://spenergynetworks.opendatasoft.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scottishpower-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scottishpower-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scottishpower-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/scottishpower-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/scottishpower-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/scottishpower-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scottishpower-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scottishpower-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scottishpower-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.opendatasoft.com/apis/ods-explore-v2/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/scottishpower-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scottishpower-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scottishpower-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/scottishpower-packages.yml
- group: design
  title: ''
  type: Components
  url: components/scottishpower-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scottishpower-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/scottishpower-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scottishpower-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://spenergynetworks.opendatasoft.com/
- group: docs
  title: ''
  type: APIReference
  url: https://spenergynetworks.opendatasoft.com/api/explore/v2.1/console
- group: start
  title: ''
  type: GettingStarted
  url: https://spenergynetworks.opendatasoft.com/explore/
- group: start
  title: ''
  type: SignUp
  url: https://spenergynetworks.opendatasoft.com/signup/
- group: start
  title: ''
  type: Login
  url: https://spenergynetworks.opendatasoft.com/login/
- group: company
  title: ''
  type: Website
  url: https://www.scottishpower.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.spenergynetworks.co.uk/
- group: start
  title: ''
  type: PortalHome
  url: https://spenergynetworks.opendatasoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.spenergynetworks.co.uk/pages/energy_data_hub.aspx
- group: other
  title: ''
  type: Licensing
  url: https://spenergynetworks.opendatasoft.com/p/sp-energy-networks-open-data-licence/
- group: other
  title: ''
  type: Licensing
  url: https://spenergynetworks.opendatasoft.com/p/sp-energy-networks-shared-data-licence/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spenergynetworks.opendatasoft.com/terms/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spenergynetworks.opendatasoft.com/terms/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://spenergynetworks.opendatasoft.com/pages/support-help-main/
- group: operate
  title: ''
  type: Forum
  url: https://community.scottishpower.co.uk/
- group: operate
  title: ''
  type: FAQ
  url: https://spenergynetworks.opendatasoft.com/p/faq/
created: '2026-07-27'
description: 'ScottishPower (Scottish Power Limited, Glasgow) is one of the "Big Six" British energy companies and has been wholly owned by Spain''s Iberdrola since 2007. It is unusual in the post-liberalisation UK market for still spanning three regulated roles at once: ScottishPower Energy Retail supplies electricity and gas to millions of British homes and businesses; SP Energy Networks is the licensed distribution network operator for central and southern Scotland (SP Distribution), Merseyside, Cheshire and North Wales (SP Manweb), plus the transmission owner for southern Scotland (SP Transmission); and ScottishPower Renewables develops and operates onshore and offshore wind. That structure produces the sharpest possible version of this sector''s split, and the split is the finding. On the consumer side there is nothing — Britain has no Consumer Data Right, no Green Button mandate and no consumer energy data-portability obligation of any kind, and ScottishPower publishes no developer
  portal, no self-serve API programme and no documented way for a third party to obtain an individual customer''s usage or billing data. developer.scottishpower.co.uk, developers.scottishpower.co.uk, data.scottishpower.co.uk and docs.scottishpower.co.uk do not resolve at all, api.scottishpower.co.uk exists in DNS but returns HTTP 403, and www.scottishpower.co.uk returns HTTP 403 to every anonymous client on every path including /robots.txt. The only public account of ScottishPower''s API programme is a WSO2 customer story describing an API Manager deployment used to expose services to commercial partners — an internal, partner-gated estate, not a developer programme. On the network side the picture inverts completely. Ofgem''s Data Best Practice Guidance, made a licence condition under the RIIO-ED2 price control (Special Licence Condition 9.5), obliges electricity network licensees to treat their data as "presumed open", and SP Energy Networks has actually built that: the SP Energy Networks
  Open Data Portal at spenergynetworks.opendatasoft.com serves 150 datasets — embedded capacity register, network flow, historic substation demand, LV monitoring, smart-meter penetration, generation heat maps, flexibility and connections data — through a live, fully anonymous Opendatasoft Explore API v2.1 with a real OpenAPI 3.0.3 contract, CORS wide open, a 5,000 request/day anonymous quota, a DCAT-AP catalogue export, and an SP Energy Networks Open Data Licence based on Creative Commons Attribution 4.0. Britain mandated the infrastructure and the network data, not the data right — ScottishPower is the proof. Its smart-meter obligation runs through the Smart DCC and the Smart Energy Code, which is an infrastructure monopoly for licensed parties rather than a consumer data right, and no public register entry or endpoint for that obligation could be verified from outside.'
examples:
- key_count: 2
  name: Scottishpower Catalog Facets Example
  slug: scottishpower-catalog-facets-example
- key_count: 2
  name: Scottishpower List Datasets Example
  slug: scottishpower-list-datasets-example
- key_count: 2
  name: Scottishpower Query Records Example
  slug: scottishpower-query-records-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the OpenAPI (no provider-operated server)
  slug: candidate-mcp-tool-surface-derived-from-the-openapi-no-provider-operated-server
modified: '2026-07-27'
name: ScottishPower
nav: Providers
network: true
overview: 'ScottishPower publishes 1 API on the [APIs.io](https://apis.io/) network: SP Energy Networks Open Data Explore API. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  ScottishPower''s developer surface includes authentication, changelog, code examples, API reference, getting-started guide, signup flow, documentation, and 31 more developer resources.'
random_paper: 82
rate_limits:
- limit_count: 2
  name: Scottishpower Rate Limits
  slug: scottishpower-rate-limits
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 15.7
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 40.9
  provenance:
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
    score: 52.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Scottishpower Authentication
  slug: scottishpower-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Scottishpower Domain Security
  slug: scottishpower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scottishpower Vulnerability Disclosure
  slug: scottishpower-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: scottishpower
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Energy Retailer
- Smart Metering
- Grid
- Open Data
- Distribution Network Operator
- Renewables
- Energy Markets
website: https://www.scottishpower.co.uk/
---
