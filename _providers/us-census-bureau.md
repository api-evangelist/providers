---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Us Census Bureau Agentic Access
  operation_count: 47
  slug: us-census-bureau-agentic-access
  summary_line: 47 operations · 2 acting
api_count: 19
apis:
- description: The 2010 API from US Census Bureau — 1 operation(s) for 2010.
  name: US Census Bureau 2010 API
  slug: us-census-bureau-2010-api
- description: The 2020 API from US Census Bureau — 1 operation(s) for 2020.
  name: US Census Bureau 2020 API
  slug: us-census-bureau-2020-api
- description: American Community Survey datasets (1-Year, Supplemental, 5-Year)
  name: US Census Bureau ACS API
  slug: us-census-bureau-acs-api
- description: ACS Public Use Microdata Sample (person and household)
  name: US Census Bureau ACS PUMS API
  slug: us-census-bureau-acs-pums-api
- description: Bulk geocoding (up to 10,000 records)
  name: US Census Bureau Batch API
  slug: us-census-bureau-batch-api
- description: Service directory
  name: US Census Bureau Catalog API
  slug: us-census-bureau-catalog-api
- description: Current Population Survey basic monthly and supplements
  name: US Census Bureau CPS API
  slug: us-census-bureau-cps-api
- description: Current vintage TIGERweb services
  name: US Census Bureau Current API
  slug: us-census-bureau-current-api
- description: Decennial Census of Population and Housing
  name: US Census Bureau Decennial API
  slug: us-census-bureau-decennial-api
- description: Dataset discovery via the DCAT-compliant catalog
  name: US Census Bureau Discovery API
  slug: us-census-bureau-discovery-api
- description: Economic Census, ABS, CBP, NES
  name: US Census Bureau Economic API
  slug: us-census-bureau-economic-api
- description: Address to coordinates plus Census geographies
  name: US Census Bureau Geographies API
  slug: us-census-bureau-geographies-api
- description: Address to coordinates
  name: US Census Bureau Locations API
  slug: us-census-bureau-locations-api
- description: Per-dataset variables, groups, geographies, and examples
  name: US Census Bureau Metadata API
  slug: us-census-bureau-metadata-api
- description: Population Estimates Program
  name: US Census Bureau PEP API
  slug: us-census-bureau-pep-api
- description: The Popclock API from US Census Bureau — 2 operation(s) for popclock.
  name: US Census Bureau Popclock API
  slug: us-census-bureau-popclock-api
- description: Household Pulse Survey near-real-time experimental data
  name: US Census Bureau Pulse API
  slug: us-census-bureau-pulse-api
- description: Survey of Income and Program Participation panels
  name: US Census Bureau SIPP API
  slug: us-census-bureau-sipp-api
- description: The Timeseries API from US Census Bureau — 7 operation(s) for timeseries.
  name: US Census Bureau Timeseries API
  slug: us-census-bureau-timeseries-api
artifact_total: 64
collections:
- collection_type: open
  name: Business Dynamics Statistics API
  slug: open-census-bds-api
- collection_type: open
  name: Census Data API
  slug: open-census-data-api
- collection_type: open
  name: Census Geocoding Services API
  slug: open-census-geocoder-api
- collection_type: open
  name: International Trade API
  slug: open-census-international-trade-api
- collection_type: open
  name: Census Microdata API
  slug: open-census-microdata-api
- collection_type: open
  name: Population Clock API
  slug: open-census-population-clock-api
- collection_type: open
  name: TIGERweb REST Services
  slug: open-census-tigerweb-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-census-bureau-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-census-bureau-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-census-bureau-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.census.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.census.gov/data/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.census.gov/data/developers/about.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.census.gov/data/developers/guidance/api-user-guide.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.census.gov/data/developers/guidance/microdata-api-user-guide.html
- group: other
  title: ''
  type: APICatalog
  url: https://api.census.gov/data.json
- group: docs
  title: ''
  type: Documentation
  url: https://www.census.gov/data/developers/updates/new-discovery-tool.html
- group: start
  title: ''
  type: Signup
  url: https://api.census.gov/data/key_signup.html
- group: start
  title: ''
  type: Signup
  url: https://www.census.gov/data/developers/api-key.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.census.gov/data/developers/about/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.census.gov/about/policies/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.census.gov/newsroom/blogs/director.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.census.gov/data/developers/updates.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uscensusbureau
- group: build
  title: ''
  type: SDKs
  url: https://github.com/uscensusbureau/citysdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/uscensusbureau/us-census-bureau-data-api-mcp
- group: build
  title: ''
  type: Tools
  url: https://api.census.gov/data.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
- group: docs
  title: ''
  type: Documentation
  url: https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_apps.html
- group: docs
  title: ''
  type: Documentation
  url: https://geocoding.geo.census.gov/geocoder/
- group: docs
  title: ''
  type: Documentation
  url: https://data.census.gov
- group: operate
  title: ''
  type: Forums
  url: https://www.data.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://catalog.data.gov/organization/census-gov
- group: operate
  title: ''
  type: Support
  url: https://ask.census.gov
- group: operate
  title: ''
  type: ContactForm
  url: https://ask.census.gov/prweb/PRServletCustom/app/ECORRAsk/YACFBFye-rFIz_FoGtyvDRUGg1Uzu5Mn*/!STANDARD
- group: other
  title: ''
  type: Email
  url: mailto:cnmp.developers.list@census.gov
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/publicdomain/zero/1.0/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/us-census-bureau-rate-limits.yml
created: '2026-05-25'
description: The U.S. Census Bureau is the federal statistical agency responsible for producing data about the American people and economy. Established in 1902 and part of the U.S. Department of Commerce, the Bureau conducts the constitutionally mandated Decennial Census every ten years and dozens of ongoing surveys including the American Community Survey, Economic Census, Population Estimates, Current Population Survey, and Survey of Income and Program Participation. The Census Bureau exposes its statistics through the Census Data API (over 1,700 datasets), the Microdata API for PUMS tabulation, the TIGERweb geospatial REST services, and the Geocoding Services API — all free, requiring only a free API key for the data endpoints and released into the public domain under CC0.
examples:
- key_count: 4
  name: Census Acs5 Get Example
  slug: census-acs5-get-example
- key_count: 4
  name: Census Discovery List Example
  slug: census-discovery-list-example
- key_count: 4
  name: Census Geocoder Onelineaddress Example
  slug: census-geocoder-onelineaddress-example
- key_count: 4
  name: Census Pums Tabulate Example
  slug: census-pums-tabulate-example
features:
- Over 1,700 datasets exposed via a single REST API base (api.census.gov/data)
- American Community Survey (ACS) 1-Year, 1-Year Supplemental, 3-Year, and 5-Year detailed and subject tables
- Decennial Census of Population and Housing (2000, 2010, 2020) Public Law 94-171 and DHC tables
- Economic Census 2002-2022 with establishment, sales, payroll, employment by industry and geography
- Population Estimates Program (PEP) — annual intercensal estimates by age, sex, race, Hispanic origin
- Annual Business Survey (ABS) — women, minority, veteran owned business statistics
- County Business Patterns (CBP) and ZIP Code Business Patterns (ZBP) — annual since 1986
- Nonemployer Statistics (NES) — businesses with no paid employees
- Business Dynamics Statistics (BDS) — establishment births, deaths, job creation, destruction
- Household Pulse Survey — near-real-time experimental data on social and economic effects
- Quarterly Workforce Indicators (QWI) and Job-to-Job Flows from LEHD
- International Trade — monthly imports and exports, HS commodity codes, port-level
- Current Population Survey (CPS) basic monthly and supplements (microdata)
- Survey of Income and Program Participation (SIPP) longitudinal panels
- Small Area Income and Poverty Estimates (SAIPE)
- Small Area Health Insurance Estimates (SAHIE)
- Population Clock JSON feed for real-time U.S. and world population estimates
- Public Use Microdata Sample (PUMS) tabulation API for ACS, CPS, and SIPP
- TIGERweb ArcGIS REST services — states, counties, tracts, blocks, ZCTAs, congressional districts
- Geocoding Services API — address to coordinates and Census geographies (free, no key)
- DCAT-compliant discovery catalog at api.census.gov/data.json
- CitySDK JavaScript library and official Census Data API MCP server for AI assistants
- All data released under Creative Commons Zero (CC0) public domain dedication
- Free API key with no published rate limit; one key per email; required for all data queries
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-census-bureau.png
json_schemas:
- name: CensusDataRow
  property_count: 0
  slug: census-data-row
- name: CensusDatasetMetadata
  property_count: 19
  slug: census-dataset-metadata
json_structures:
- name: Census Data Row Structure
  property_count: 0
  slug: census-data-row-structure
jsonld:
- class_count: 7
  name: Us Census Bureau Context
  property_count: 4
  slug: us-census-bureau-context
layout: provider
modified: '2026-05-25'
name: US Census Bureau
nav: Providers
network: true
overview: 'US Census Bureau publishes 19 APIs on the [APIs.io](https://apis.io/) network, including 2010 API, 2020 API, ACS API, and 16 more. Tagged areas include Government, Federal, Demographics, Statistics, and Economics.


  The US Census Bureau catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Census Bureau''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, changelog, tooling, and 24 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 5
  name: Us Census Bureau Rate Limits
  slug: us-census-bureau-rate-limits
rules:
- name: US Census Bureau API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: census-data-api-rules
- name: US Census Bureau API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-census-bureau-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  delta: -2.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.3
    developer_ergonomics: 41.3
    discoverability: 61.1
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-census-bureau/refs/heads/main/screenshots/us-census-bureau-2026-06-20T200557.png
security:
- kind: authentication
  name: Us Census Bureau Authentication
  slug: us-census-bureau-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Us Census Bureau Domain Security
  slug: us-census-bureau-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-census-bureau
tags:
- Government
- Federal
- Demographics
- Statistics
- Economics
- Geospatial
- Open Data
- Public Sector
website: https://www.census.gov
---
