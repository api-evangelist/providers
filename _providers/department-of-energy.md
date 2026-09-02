---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Department Of Energy Agentic Access
  operation_count: 14
  slug: department-of-energy-agentic-access
  summary_line: 14 operations
api_count: 18
apis:
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
- description: The Aeo API from Department of Energy — 1 operation(s) for aeo.
  name: Department of Energy Aeo API
  slug: department-of-energy-aeo-api
- description: The Co2 Emissions API from Department of Energy — 1 operation(s) for co2 emissions.
  name: Department of Energy Co2 Emissions API
  slug: department-of-energy-co2-emissions-api
- description: The Coal API from Department of Energy — 1 operation(s) for coal.
  name: Department of Energy Coal API
  slug: department-of-energy-coal-api
- description: The EIA Open Data API V2 API from Department of Energy — 1 operation(s) for eia open data api v2.
  name: Department of Energy EIA Open Data API V2 API
  slug: department-of-energy-eia-open-data-api-v2-api
- description: The Electricity API from Department of Energy — 2 operation(s) for electricity.
  name: Department of Energy Electricity API
  slug: department-of-energy-electricity-api
- description: The International API from Department of Energy — 1 operation(s) for international.
  name: Department of Energy International API
  slug: department-of-energy-international-api
- description: The Natural Gas API from Department of Energy — 1 operation(s) for natural gas.
  name: Department of Energy Natural Gas API
  slug: department-of-energy-natural-gas-api
- description: The Nuclear Outages API from Department of Energy — 1 operation(s) for nuclear outages.
  name: Department of Energy Nuclear Outages API
  slug: department-of-energy-nuclear-outages-api
- description: The Petroleum API from Department of Energy — 1 operation(s) for petroleum.
  name: Department of Energy Petroleum API
  slug: department-of-energy-petroleum-api
- description: The Seds API from Department of Energy — 1 operation(s) for seds.
  name: Department of Energy Seds API
  slug: department-of-energy-seds-api
- description: The Seriesid API from Department of Energy — 1 operation(s) for seriesid.
  name: Department of Energy Seriesid API
  slug: department-of-energy-seriesid-api
- description: The Steo API from Department of Energy — 1 operation(s) for steo.
  name: Department of Energy Steo API
  slug: department-of-energy-steo-api
- description: The Total Energy API from Department of Energy — 1 operation(s) for total energy.
  name: Department of Energy Total Energy API
  slug: department-of-energy-total-energy-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EIA Open Data API V2 Aeo API
  slug: open-department-of-energy-aeo-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Co2 Emissions API
  slug: open-department-of-energy-co2-emissions-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Coal API
  slug: open-department-of-energy-coal-api
- collection_type: open
  name: Aeo EIA Open Data API V2 API
  slug: open-department-of-energy-eia-open-data-api-v2-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Electricity API
  slug: open-department-of-energy-electricity-api
- collection_type: open
  name: EIA Open Data API V2 Aeo International API
  slug: open-department-of-energy-international-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Natural Gas API
  slug: open-department-of-energy-natural-gas-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Nuclear Outages API
  slug: open-department-of-energy-nuclear-outages-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Petroleum API
  slug: open-department-of-energy-petroleum-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Seds API
  slug: open-department-of-energy-seds-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Seriesid API
  slug: open-department-of-energy-seriesid-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Steo API
  slug: open-department-of-energy-steo-api
- collection_type: open
  name: EIA Open Data API V2 Aeo Total Energy API
  slug: open-department-of-energy-total-energy-api
- collection_type: open
  name: EIA Open Data API V2
  slug: open-department-of-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-energy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energy
- group: company
  title: ''
  type: Website
  url: https://www.energy.gov
- group: other
  title: ''
  type: Open Energy Data
  url: https://www.energy.gov/data/open-energy-data
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.data.gov/
- group: other
  title: ''
  type: EIA
  url: https://www.eia.gov
- group: other
  title: ''
  type: OSTI
  url: https://www.osti.gov
- group: other
  title: ''
  type: NREL Developer
  url: https://developer.nlr.gov/
- group: other
  title: ''
  type: Open Energy Data Initiative
  url: https://data.openei.org/
- group: other
  title: ''
  type: Energy Data eXchange
  url: https://edx.netl.doe.gov/
- group: other
  title: ''
  type: Data.gov DOE Catalog
  url: https://catalog.data.gov/organization/doe-gov
- group: company
  title: ''
  type: News
  url: https://www.energy.gov/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.energy.gov/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doe-doe
- group: design
  title: ''
  type: JSONLD
  url: json-ld/department-of-energy-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-energy-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.energy.gov/rss.xml
created: '2024-12-03'
description: The U.S. Department of Energy (DOE) provides extensive open data and APIs across its national laboratories and program offices. Notable APIs are published by the Energy Information Administration (EIA) for energy statistics, the Office of Scientific and Technical Information (OSTI) for research and publications, the National Renewable Energy Laboratory (NREL, rebranding as NLR) developer network for renewables and alternative fuels, and the Buildings Performance Database (BPD).
finops:
- name: Department Of Energy Finops
  service_category: API
  slug: department-of-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-energy.png
jsonld:
- class_count: 0
  name: Department Of Energy Context
  property_count: 6
  slug: department-of-energy-context
layout: provider
modified: '2026-05-19'
name: Department of Energy
nav: Providers
network: true
overview: 'Department of Energy publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Aeo API, Co2 Emissions API, Coal API, and 10 more. Tagged areas include Buildings, Electricity, Energy, Federal-Government, and Open Data.


  The Department of Energy catalog on APIs.io includes 1 JSON-LD context.


  Department of Energy''s developer surface includes authentication, product news, engineering blog, and 16 more developer resources.'
plans:
- name: Department Of Energy Plans Pricing
  plan_count: 3
  slug: department-of-energy-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Department Of Energy Rate Limits
  slug: department-of-energy-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 15.2
    contract_quality: 53.1
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 10.5
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-energy/refs/heads/main/screenshots/department-of-energy-2026-06-20T175917.png
security:
- kind: authentication
  name: Department Of Energy Authentication
  slug: department-of-energy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Department Of Energy Domain Security
  slug: department-of-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-energy
tags:
- Buildings
- Electricity
- Energy
- Federal-Government
- Open Data
- Renewables
- Research
- Solar
- Statistics
website: https://www.energy.gov
---
