---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Western Power Agentic Access
  operation_count: 9
  slug: western-power-agentic-access
  summary_line: 9 operations
api_count: 3
apis:
- description: Western Power's network asset and capacity spatial data — distribution and transmission overhead powerlines, underground cables, poles, pillars, pits, transformers, enclosures, substations, streetligh
  name: Western Power Public Secure Services (SLIP)
  slug: western-power-public-secure-services-slip
- baseURL: https://www.westernpower.com.au/api/corp/outage
  baseurl_source: declared
  description: The Content API from Western Power — 2 operation(s) for content.
  name: Western Power Content API
  slug: western-power-content-api
- baseURL: https://www.westernpower.com.au/api/corp/outage
  baseurl_source: declared
  description: The Metadata API from Western Power — 2 operation(s) for metadata.
  name: Western Power Metadata API
  slug: western-power-metadata-api
- baseURL: https://www.westernpower.com.au/api/corp/outage
  baseurl_source: declared
  description: Live planned and unplanned outage data for the South West Interconnected System.
  name: Western Power Outages API
  slug: western-power-outages-api
- baseURL: https://www.westernpower.com.au/api/corp/outage
  baseurl_source: declared
  description: The Query API from Western Power — 1 operation(s) for query.
  name: Western Power Query API
  slug: western-power-query-api
- baseURL: https://www.westernpower.com.au/api/corp/outage
  baseurl_source: declared
  description: The Search API from Western Power — 1 operation(s) for search.
  name: Western Power Search API
  slug: western-power-search-api
artifact_total: 16
collections:
- collection_type: open
  name: Western Power Outage Areas Feature Service (ArcGIS REST)
  slug: open-western-power-arcgis-outage
- collection_type: open
  name: Western Power Corporate Web API
  slug: open-western-power-corporate-web
- collection_type: open
  name: Western Power Outage Web API
  slug: open-western-power-outage
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/western-power-outage-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/western-power-check-outages.md
- group: other
  title: ''
  type: Overlay
  url: overlays/western-power-corporate-web-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/western-power-arcgis-outage-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/western-power-query-outage-geography.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/western-power-mcp.yml
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
overview: 'Western Power publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Content API, Metadata API, Outages API, and 2 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Western Power''s developer surface includes authentication, support, engineering blog, documentation, developer portal, and 27 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 15.0
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 54.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/western-power/refs/heads/main/screenshots/western-power-2026-09-02T170733.png
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
