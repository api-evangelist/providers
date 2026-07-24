---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 21
apis:
- description: Free API management gateway operated by the U.S. General Services Administration's Technology Transformation Services. Fronts the API keys, rate limiting, and analytics for over 450 APIs across roughl
  name: api.data.gov
  slug: apidatagov
- description: The U.S. federal open data catalog at catalog.data.gov, powered by the open-source CKAN platform. The CKAN Action API at https://catalog.data.gov/api/3/action/ exposes dataset metadata (package_search
  name: data.gov (CKAN catalog)
  slug: datagov-ckan-catalog
- description: The Regulations.gov v4 REST API exposes federal regulatory dockets, documents (Proposed Rules, Rules, Supporting & Related Material, Other), and public comments. Read endpoints follow api.data.gov rat
  name: Regulations.gov API
  slug: regulationsgov-api
- description: JSON REST API for the daily Federal Register published by the Office of the Federal Register and GPO. Exposes documents (Notice, Proposed Rule, Rule, Presidential Document), agencies, public-inspectio
  name: Federal Register API
  slug: federal-register-api
- description: 'U.S. Government Publishing Office (GPO) GovInfo developer hub. The Collections API at api.govinfo.gov delivers self-describing packages of authoritative federal content — Congressional bills, Federal '
  name: GovInfo API
  slug: govinfo-api
- description: System for Award Management (SAM.gov), the U.S. federal procurement and financial assistance system, exposes 11 production APIs catalogued at open.gsa.gov including Entity Management, Exclusions, Fede
  name: SAM.gov APIs
  slug: samgov-apis
- description: The USAspending API, maintained by the U.S. Department of the Treasury, provides public access to comprehensive U.S. government spending data including federal contracts, grants, loans, direct payment
  name: USAspending.gov API
  slug: usaspendinggov-api
- description: Bureau of the Fiscal Service API at api.fiscaldata.treasury.gov exposing Treasury's authoritative fiscal datasets — Debt to the Penny, Monthly Treasury Statement, Daily Treasury Statement, Exchange Ra
  name: Treasury Fiscal Data API
  slug: treasury-fiscal-data-api
- description: 'The api.congress.gov REST API, maintained by the Library of Congress, exposes structured legislative data — bills, amendments, summaries, members, committees, committee reports, congressional record, '
  name: Congress.gov API
  slug: congressgov-api
- description: Federal Election Commission's openFEC REST API at api.open.fec.gov exposes campaign finance data — candidates, committees (PACs, parties, campaigns), filings, contributions, disbursements, independent
  name: FEC openFEC API
  slug: fec-openfec-api
- description: 'National Weather Service REST + JSON-LD API at api.weather.gov delivering open weather forecasts, alerts, and observations. Endpoints include /points/{lat,lon}, /gridpoints/{office}/{x},{y}/forecast, '
  name: api.weather.gov (NOAA NWS)
  slug: apiweathergov-noaa-nws
- description: Aggregated NASA Open APIs hub at api.nasa.gov. Includes Astronomy Picture of the Day (APOD), Asteroids NeoWs, DONKI (Space Weather), Earth Imagery, EONET (Earth Observatory Natural Event Tracker), EPI
  name: api.nasa.gov
  slug: apinasagov
- description: U.S. Census Bureau Data API at api.census.gov serving approximately 1,784 datasets across major survey programs — Decennial Census, American Community Survey (ACS 1-year and 5-year), Population Estima
  name: Census Data API
  slug: census-data-api
- description: BEA Data API exposing GDP, national income, personal income, corporate profits, international trade and investment, regional accounts, and industry accounts. JSON and XML responses. API key obtained f
  name: Bureau of Economic Analysis (BEA) API
  slug: bureau-of-economic-analysis-bea-api
- description: OpenStates v3 REST API at v3.openstates.org, operated by Plural Policy, providing JSON access to U.S. state legislative information — bills, people (legislators and governors), jurisdictions, committe
  name: OpenStates API (Plural Policy)
  slug: openstates-api-plural-policy
- description: GovTrack.us civic-tech site tracking U.S. Congress — bills, votes, members, committees, congressional districts. Originally one of the first civic-tech APIs; today its bulk data downloads at govtrack.
  name: GovTrack
  slug: govtrack
- description: Open Civic Data is a community-maintained set of specifications and shared identifiers for civic information — Open Civic Data Division Identifiers (OCD-IDs) for political geographies, plus normalized
  name: Open Civic Data
  slug: open-civic-data
- description: Socrata Open Data API (SODA) is the read/write JSON API powering open data portals at federal, state, county, and city governments worldwide. Queries use SoQL (Socrata Query Language), responses are J
  name: Socrata Open Data API (Tyler Data and Insights)
  slug: socrata-open-data-api-tyler-data-and-insights
- description: 'Largest U.S. vendor of mission-critical software to state and local government. Product portfolio spans Courts & Justice (case management, e-filing, jury management, prosecution), Enterprise Resource '
  name: Tyler Technologies
  slug: tyler-technologies
- description: OpenGov sells a cloud ERP, budgeting, financial-reporting, permitting, licensing, and procurement suite to U.S. state and local governments. Originally a Sunlight Foundation spinout, OpenGov has conso
  name: OpenGov
  slug: opengov
- description: Kin Lane's 2026-05-05 roundup at apievangelist.com indexes 211 U.S. federal agencies and their public-facing APIs, RSS feeds, open-data surfaces, and referenced internal systems. Each agency has its o
  name: API Evangelist Federal Agencies Roundup
  slug: api-evangelist-federal-agencies-roundup
artifact_total: 34
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/public-sector-domain-security.yml
created: '2026-05-23'
description: Industry-vertical index for the public-sector / government API landscape across U.S. federal, state, and local levels. Catalogs the federal API gateway api.data.gov (operated by GSA's Technology Transformation Services under the Open Government Data Act of 2018, used by 25 agencies for over 450 APIs), the catalog.data.gov CKAN metadata catalog, headline federal programmatic surfaces (Regulations.gov, Federal Register, GovInfo, SAM.gov, USAspending.gov, Treasury Fiscal Data, Congress.gov, FEC openFEC, api.weather.gov, api.nasa.gov, Census Data API, Bureau of Economic Analysis), state and local infrastructure (Socrata / Tyler Data and Insights, Tyler Technologies courts/ERP/public-safety stack, OpenGov ERP/budgeting/permitting cloud), and the civic-tech layer (OpenStates / Plural Policy, GovTrack, Open Civic Data). Cross-references Kin Lane's 2026-05-05 roundup of 211 U.S. federal agencies and their APIs on apievangelist.com. The catalog focuses on the data-schema shape of a government
  dataset / agency / regulation record so that civic-tech and enterprise consumers can normalize across federal, state, and local publishers.
examples:
- key_count: 17
  name: Public Sector Agency Example
  slug: public-sector-agency-example
- key_count: 21
  name: Public Sector Dataset Example
  slug: public-sector-dataset-example
- key_count: 22
  name: Public Sector Regulation Example
  slug: public-sector-regulation-example
graphqls:
- description: ''
  name: Public Sector GraphQL API
  slug: public-sector-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/public-sector.png
json_schemas:
- name: PublicSectorAgency
  property_count: 16
  slug: public-sector-agency
- name: PublicSectorDataset
  property_count: 20
  slug: public-sector-dataset
- name: PublicSectorRegulation
  property_count: 20
  slug: public-sector-regulation
json_structures:
- name: Public Sector Agency Structure
  property_count: 0
  slug: public-sector-agency-structure
- name: Public Sector Dataset Structure
  property_count: 0
  slug: public-sector-dataset-structure
- name: Public Sector Regulation Structure
  property_count: 0
  slug: public-sector-regulation-structure
jsonld:
- class_count: 37
  name: Public Sector Context
  property_count: 31
  slug: public-sector-context
layout: provider
modified: '2026-05-23'
name: Public Sector
nav: Providers
network: true
overview: 'Public Sector publishes 21 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Public Sector, Government, Federal, State, and Local.


  The Public Sector catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 14
rules:
- name: Public Sector API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: public-sector-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.0
  delta: 0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 20.8
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 22.8
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/public-sector/refs/heads/main/screenshots/public-sector-2026-06-20T192241.png
security:
- kind: domain-security
  name: Public Sector Domain Security
  slug: public-sector-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: public-sector
tags:
- Public Sector
- Government
- Federal
- State
- Local
- Civic Tech
- Open Data
- Regulations
- Procurement
- Open Government
- Topic
---
