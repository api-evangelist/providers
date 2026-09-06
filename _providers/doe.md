---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 53
  human_in_the_loop: 4
  name: Doe Agentic Access
  operation_count: 278
  slug: doe-agentic-access
  summary_line: 278 operations · 53 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: NREL/NLR Developer Network electricity APIs covering utility rates, electricity costs, generation, transmission, delivery, and monitoring. Includes OpenEI Utility Rates API providing access to utility
  name: NLR Electricity APIs
  slug: nlr-electricity-apis
- description: Solar resource data and analysis APIs from NREL/NLR Developer Network, including NSRDB (National Solar Radiation Database) data access. Sponsored by the U.S. Department of Energy.
  name: NLR Solar Resource APIs
  slug: nlr-solar-apis
- description: Wind resource data and analysis APIs from NREL/NLR Developer Network providing wind speed and direction data for energy planning. Sponsored by the U.S. Department of Energy.
  name: NLR Wind Resource APIs
  slug: nlr-wind-apis
- description: Alternative fuel station locator, alternative fuel vehicles database, EV infrastructure (EVI-Pro Lite), battery policies, transportation laws and incentives, and route energy optimization (RouteE) API
  name: NLR Transportation & Alternative Fuels APIs
  slug: nlr-transportation-apis
- description: APIs for energy efficiency and use of renewable technologies in residential and commercial buildings from NREL/NLR Developer Network. Sponsored by the U.S. Department of Energy.
  name: NLR Buildings Energy APIs
  slug: nlr-buildings-apis
- description: The DOE Data Explorer API allows querying the Department of Energy's repository of research datasets resulting from DOE research funding. Built on REST architecture providing predictable URLs and HTTP
  name: DOE Data Explorer API
  slug: doe-data-explorer-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Annual Energy Outlook Data
  name: Department of Energy AEO API
  slug: doe-aeo-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Coal Data
  name: Department of Energy COAL API
  slug: doe-coal-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Crude Oil Imports Data
  name: Department of Energy CRUD_IMPORTS API
  slug: doe-crud-imports-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Densified Biomass Data
  name: Department of Energy DBF API
  slug: doe-dbf-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Electricity Data
  name: Department of Energy ELEC API
  slug: doe-elec-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to CO2 Emissions Data
  name: Department of Energy EMISS API
  slug: doe-emiss-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to International Energy Outlook Data
  name: Department of Energy IEO API
  slug: doe-ieo-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to International Data
  name: Department of Energy INTL API
  slug: doe-intl-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Natural Gas Data
  name: Department of Energy NG API
  slug: doe-ng-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Nuclear Outages Data
  name: Department of Energy NUC_STATUS API
  slug: doe-nuc-status-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Available EIA API Datasets
  name: Department of Energy Root API
  slug: doe-root-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Daily Electricity Data
  name: Department of Energy RTO API
  slug: doe-rto-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to State Energy Data Systems (SEDS) Data
  name: Department of Energy SEDS API
  slug: doe-seds-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to State Electricity Profiles
  name: Department of Energy SEP API
  slug: doe-sep-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Short Term Energy Outlook Data
  name: Department of Energy STEO API
  slug: doe-steo-api
- baseURL: https://api.eia.gov/v2/
  baseurl_source: declared
  description: Access to Total Energy Data
  name: Department of Energy TOTAL API
  slug: doe-total-api
- description: 'The DOE PAGES (Public Access Gateway for Energy and Science) REST API provides programmatic access to publications resulting from DOE-funded research, hosted by the Office of Scientific and Technical '
  name: OSTI DOE PAGES API
  slug: osti-pages-api
- description: The OSTI ELINK API is the Office of Scientific and Technical Information's submission and retrieval interface for DOE research records. It supports submission of metadata and full text by DOE-funded r
  name: OSTI ELINK API
  slug: osti-elink-api
- description: The National Renewable Energy Laboratory (NREL, transitioning to NLR) Developer Network publishes a portfolio of REST APIs covering solar resource and PV simulation, alternative fuels and stations, el
  name: NREL/NLR Developer Network APIs
  slug: nrel-developer-api
- description: The Buildings Performance Database (BPD) is a DOE repository of anonymized empirical performance records for commercial and residential buildings. The BPD API allows partners to query aggregate distri
  name: Buildings Performance Database API
  slug: buildings-performance-database
- description: The DOE participates in Data.gov by publishing thousands of dataset records under the doe-gov organization. These datasets cover energy consumption, generation, environmental impact, R&D, and more, an
  name: Department of Energy Open Data Catalog
  slug: open-data-catalog
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Co2 Emissions API from Department of Energy — 1 operation(s) for co2 emissions.
  name: Department of Energy Co2 Emissions API
  slug: department-of-energy-co2-emissions-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The EIA Open Data API V2 API from Department of Energy — 1 operation(s) for eia open data api v2.
  name: Department of Energy EIA Open Data API V2 API
  slug: department-of-energy-eia-open-data-api-v2-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Electricity API from Department of Energy — 2 operation(s) for electricity.
  name: Department of Energy Electricity API
  slug: department-of-energy-electricity-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The International API from Department of Energy — 1 operation(s) for international.
  name: Department of Energy International API
  slug: department-of-energy-international-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Natural Gas API from Department of Energy — 1 operation(s) for natural gas.
  name: Department of Energy Natural Gas API
  slug: department-of-energy-natural-gas-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Nuclear Outages API from Department of Energy — 1 operation(s) for nuclear outages.
  name: Department of Energy Nuclear Outages API
  slug: department-of-energy-nuclear-outages-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Petroleum API from Department of Energy — 1 operation(s) for petroleum.
  name: Department of Energy Petroleum API
  slug: department-of-energy-petroleum-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Seriesid API from Department of Energy — 1 operation(s) for seriesid.
  name: Department of Energy Seriesid API
  slug: department-of-energy-seriesid-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: The Total Energy API from Department of Energy — 1 operation(s) for total energy.
  name: Department of Energy Total Energy API
  slug: department-of-energy-total-energy-api
artifact_total: 82
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EIA APIv2 AEO API
  slug: open-doe-aeo-api
- collection_type: open
  name: EIA APIv2 AEO COAL API
  slug: open-doe-coal-api
- collection_type: open
  name: EIA APIv2 AEO CRUD_IMPORTS API
  slug: open-doe-crud-imports-api
- collection_type: open
  name: EIA APIv2 AEO DBF API
  slug: open-doe-dbf-api
- collection_type: open
  name: EIA APIv2 AEO ELEC API
  slug: open-doe-elec-api
- collection_type: open
  name: EIA APIv2 AEO EMISS API
  slug: open-doe-emiss-api
- collection_type: open
  name: EIA APIv2 AEO IEO API
  slug: open-doe-ieo-api
- collection_type: open
  name: EIA APIv2 AEO INTL API
  slug: open-doe-intl-api
- collection_type: open
  name: EIA APIv2 AEO NG API
  slug: open-doe-ng-api
- collection_type: open
  name: EIA APIv2 AEO NUC_STATUS API
  slug: open-doe-nuc-status-api
- collection_type: open
  name: EIA APIv2 AEO Root API
  slug: open-doe-root-api
- collection_type: open
  name: EIA APIv2 AEO RTO API
  slug: open-doe-rto-api
- collection_type: open
  name: EIA APIv2 AEO SEDS API
  slug: open-doe-seds-api
- collection_type: open
  name: EIA APIv2 AEO SEP API
  slug: open-doe-sep-api
- collection_type: open
  name: EIA APIv2 AEO STEO API
  slug: open-doe-steo-api
- collection_type: open
  name: EIA APIv2 AEO TOTAL API
  slug: open-doe-total-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.energy.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/opendata/documentation.php
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/doecode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s--department-of-energy
- group: company
  title: ''
  type: Blog
  url: https://www.energy.gov/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.nlr.gov/docs/rate-limits/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.eia.gov/opendata/
- group: other
  title: ''
  type: X
  url: https://twitter.com/energy
- group: commercial
  title: ''
  type: Plans
  url: plans/doe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doe-finops.yml
created: '2026-06-13'
description: The U.S. Department of Energy provides REST APIs for energy consumption data, renewable energy statistics, fuel prices, electric vehicle infrastructure data, nuclear facility information, and scientific research publications. Primary API programs include the EIA Open Data API for energy time-series data, the NREL/NLR Developer Network for renewable energy and transportation data, and the OSTI APIs for DOE-funded research records.
examples:
- key_count: 5
  name: Eia Data Response Example
  slug: eia-data-response-example
- key_count: 4
  name: Eia Facet Response Example
  slug: eia-facet-response-example
- key_count: 4
  name: Eia Route Response Example
  slug: eia-route-response-example
finops:
- name: Doe Finops
  service_category: ''
  slug: doe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doe.png
json_schemas:
- name: DataParams
  property_count: 8
  slug: dataparams
- name: DataResponse
  property_count: 5
  slug: dataresponse
- name: DataResponseContainer
  property_count: 3
  slug: dataresponsecontainer
- name: Facet
  property_count: 3
  slug: facet
- name: FacetDetails
  property_count: 2
  slug: facetdetails
- name: FacetDetailsContainer
  property_count: 3
  slug: facetdetailscontainer
- name: FacetMetaData
  property_count: 2
  slug: facetmetadata
- name: FacetOptionList
  property_count: 2
  slug: facetoptionlist
- name: FacetOptionListContainer
  property_count: 3
  slug: facetoptionlistcontainer
- name: FinalRoute
  property_count: 10
  slug: finalroute
- name: FinalRouteResponse
  property_count: 2
  slug: finalrouteresponse
- name: FinalRouteResponseContainer
  property_count: 3
  slug: finalrouteresponsecontainer
- name: Frequency
  property_count: 4
  slug: frequency
- name: RouteRequest
  property_count: 2
  slug: routerequest
- name: RouteResponse
  property_count: 2
  slug: routeresponse
- name: RouteResponseContainer
  property_count: 3
  slug: routeresponsecontainer
- name: Routes
  property_count: 4
  slug: routes
- name: Sort
  property_count: 2
  slug: sort
jsonld:
- class_count: 19
  name: Doe Context
  property_count: 1
  slug: doe-context
layout: provider
modified: '2026-06-13'
name: Department of Energy
nav: Providers
network: true
overview: 'Department of Energy publishes 25 APIs on the [APIs.io](https://apis.io/) network, including AEO API, COAL API, CRUD_IMPORTS API, and 22 more. Tagged areas include Energy, Government, Renewable Energy, Electricity, and Natural Gas.


  The Department of Energy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of Energy''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Doe Plans Pricing
  plan_count: 5
  slug: doe-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Doe Rate Limits
  slug: doe-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Department of Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: doe-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 9.8
    contract_quality: 49.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doe/refs/heads/main/screenshots/doe-2026-06-20T180122.png
security:
- kind: authentication
  name: Doe Authentication
  slug: doe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Doe Domain Security
  slug: doe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: doe
tags:
- Energy
- Government
- Renewable Energy
- Electricity
- Natural Gas
- Petroleum
- Solar
- Wind
- Electric Vehicles
- Alternative Fuels
- Nuclear
- Scientific Research
website: https://www.energy.gov/
---
