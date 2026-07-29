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
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Western Power Agentic Access
  operation_count: 9
  slug: western-power-agentic-access
  summary_line: 9 operations
api_count: 4
apis:
- description: The undocumented first-party JSON API behind the public Western Power outage tracker. The outage page declares its own endpoints in markup — all-outages-endpoint="/api/corp/outage/all-outages" and sin
  name: Western Power Outage Web API
  slug: western-power-outage-web-api
- description: The anonymous read endpoints behind westernpower.com.au itself — site search, the news article feed and the careers vacancy feed. These are internal endpoints of the Optimizely/EPiServer corporate sit
  name: Western Power Corporate Web API
  slug: western-power-corporate-web-api
- description: Live outage data for the South West Interconnected System, served as an Esri ArcGIS Online hosted feature service (layer 0, "Outage_Areas") that backs the public Western Power outage tracker at wester
  name: Western Power Outage Areas Feature Service
  slug: western-power-outage-areas-feature-service
- description: Western Power's network asset and capacity spatial data — distribution and transmission overhead powerlines, underground cables, poles, pillars, pits, transformers, enclosures, substations, streetligh
  name: Western Power Public Secure Services (SLIP)
  slug: western-power-public-secure-services-slip
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/western-power-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-power-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/western-power-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/western-power-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/western-power-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/western-power-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/western-power-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/western-power-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/western-power-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/western-power-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/western-power-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Western-Power
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westernpower.com.au/terms--conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westernpower.com.au/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.westernpower.com.au/about/contact-us/
- group: company
  title: ''
  type: Website
  url: https://www.westernpower.com.au/
- group: company
  title: ''
  type: About
  url: https://www.westernpower.com.au/about/
- group: company
  title: ''
  type: Blog
  url: https://www.westernpower.com.au/news/
- group: other
  title: ''
  type: OpenData
  url: https://catalogue.data.wa.gov.au/group/about/western-power-group
- group: commercial
  title: ''
  type: License
  url: https://catalogue.data.wa.gov.au/dataset/wp-licence-terms-and-conditions
- group: docs
  title: ''
  type: Documentation
  url: https://www.westernpower.com.au/resources-education/industry-resources/retailers-and-generators/
- group: other
  title: ''
  type: Registration
  url: https://www.westernpower.com.au/issues-enquiries/requests-preferences/registration-for-access-to-energy-data/
- group: other
  title: ''
  type: Consent
  url: https://www.westernpower.com.au/issues-enquiries/requests-preferences/verifiable-consent-for-access-to-energy-data/
- group: start
  title: ''
  type: Portal
  url: https://services.westernpower.com.au/online/nbu/do/restricted/Home
- group: start
  title: ''
  type: Portal
  url: https://www.mywpprojects.westernpower.com.au/
created: '2026-07-27'
description: Western Power is the Western Australian state-owned statutory corporation that owns and operates the electricity transmission and distribution network — the poles, wires, substations and streetlights — across the South West Interconnected System (SWIS), from Kalbarri in the north to Albany in the south and east to Kalgoorlie, across more than 103,000 km of powerlines, 825,788 poles and towers, 276,000 streetlights and 154 transmission substations. It is a regulated network distributor (DNO/DSO), not a retailer and not a generator; Synergy is the SWIS retailer for residential and small-business customers and AEMO operates the WA Wholesale Electricity Market. Its API posture is honestly minimal — there is no developer portal, no published API program, no developer documentation and no published OpenAPI anywhere on westernpower.com.au (developer./api./docs./data. subdomains all fail to resolve; /developers, /docs and /openapi.json all return 404). It is nonetheless not API-less.
  Three anonymous machine-readable surfaces were verified on 2026-07-27 — an undocumented first-party JSON API at westernpower.com.au/api/corp/outage/* that backs the public outage tracker and returns every current and upcoming outage, one outage with hazard flags and update history, and a per-suburb rollup; an Esri ArcGIS Online feature service serving the same outages as polygons with SQL, spatial and statistical query; and the corporate site's own search, news and vacancy endpoints. All are internal endpoints of Western Power's web applications — robots.txt disallows /api/ — with no reference, no terms of use, no versioning, no SLA and no support channel. Consumer energy data is real but not programmatic — a third party must register a business with Western Power and collect verifiable customer consent, after which up to two years of interval and accumulated metering data is delivered by email or a web portal, never an API. Australia's Consumer Data Right, the mandate that forced identical
  banking APIs and was then transplanted into energy, does not reach this organisation at all — CDR energy covers National Electricity Market retailers, and Western Australia sits outside the NEM while distributors were never designated data holders in any state. Its 36 network asset and capacity datasets are published through the WA Government DataWA/SLIP portals as "open data subject to registering for access" under Western Power's own data licence — WFS, WMS and ArcGIS REST endpoints that return HTTP 401 to an anonymous caller.
examples:
- key_count: 25
  name: Western Power Outage Details Sample
  slug: western-power-outage-details-sample
- key_count: 14
  name: Western Power Outage Status Sample
  slug: western-power-outage-status-sample
- key_count: 7
  name: Western Power Search Sample
  slug: western-power-search-sample
- key_count: 5
  name: Western Power Vacancies Sample
  slug: western-power-vacancies-sample
image: https://www.westernpower.com.au/faviconImages/apple-touch-icon.png
layout: provider
modified: '2026-07-27'
name: Western Power
nav: Providers
network: true
overview: 'Western Power publishes 3 APIs on the [APIs.io](https://apis.io/) network: Outage Web API, Corporate Web API, and Outage Areas Feature Service. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Western Power''s developer surface includes authentication, support, engineering blog, documentation, developer portal, and 21 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.8
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 54.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Western Power Authentication
  slug: western-power-authentication
  summary_line: none/esri-token/session-cookie · 5 schemes
- kind: domain-security
  name: Western Power Domain Security
  slug: western-power-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western-power
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Network Distribution
- Smart Metering
- Open Data
- GIS
- Outages
website: https://www.westernpower.com.au/
---
