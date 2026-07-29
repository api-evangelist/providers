---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Daily-updated CSV dataset containing information on 85,000+ airports worldwide, including ICAO/IATA codes, coordinates, elevation, type, scheduled service status, and links to official and Wikipedia p
  name: OurAirports Airports Dataset
  slug: ourairports-airports-dataset
- description: Daily-updated CSV dataset describing runway surfaces, dimensions, lighting, and endpoint coordinates for airports in the OurAirports database. Includes both low-end and high-end runway designators wit
  name: OurAirports Runways Dataset
  slug: ourairports-runways-dataset
- description: Daily-updated CSV dataset of radio navigation aids (VOR, NDB, DME, TACAN, VORTAC, and combinations) associated with airports worldwide. Includes frequency, position, power level, usage type, and DME p
  name: OurAirports Navaids Dataset
  slug: ourairports-navaids-dataset
- description: Daily-updated CSV dataset of radio communication frequencies for airports, including tower (TWR), ground (GND), ATIS, UNICOM, and remote communications outlet (RCO) frequencies in megahertz.
  name: OurAirports Airport Frequencies Dataset
  slug: ourairports-airport-frequencies-dataset
- description: Reference CSV dataset of sovereign states and country-like entities used to cross-reference the iso_country field in other OurAirports datasets. Includes ISO 3166-1 alpha-2 codes, continent assignment
  name: OurAirports Countries Dataset
  slug: ourairports-countries-dataset
- description: Reference CSV dataset of high-level administrative subdivisions (states, provinces, territories) used to cross-reference the iso_region field in the airports dataset. Includes ISO 3166-2 codes and loc
  name: OurAirports Regions Dataset
  slug: ourairports-regions-dataset
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ourairports-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ourairports.com/about.html
- group: commercial
  title: ''
  type: License
  url: https://unlicense.org/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/davidmegginson/ourairports-data
- group: build
  title: ''
  type: GitHubPagesData
  url: https://davidmegginson.github.io/ourairports-data/
- group: other
  title: ''
  type: DataDictionary
  url: https://ourairports.com/help/data-dictionary.html
- group: operate
  title: ''
  type: Community
  url: https://ourairports.com
created: '2026-06-13'
description: OurAirports is an open airport data platform maintained by a global community of aviation enthusiasts. It provides a comprehensive, community-maintained database of 85,000+ airports, runways, radio navigation aids (navaids), and communication frequencies worldwide. All data is released to the public domain and is available as daily-updated CSV datasets hosted on GitHub Pages. The platform covers airports of every type — from large commercial hubs to small private airstrips, heliports, seaplane bases, and balloon ports — across every country and territory on Earth.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://ourairports.com/favicon.ico
jsonld:
- class_count: 0
  name: Dataset Context
  property_count: 0
  slug: dataset
layout: provider
modified: '2026-06-13'
name: OurAirports
nav: Providers
network: true
overview: 'OurAirports publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Airports, Open Data, CSV, and Geospatial.


  The OurAirports catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 11
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 20.3
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 4.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ourairports/refs/heads/main/screenshots/ourairports-2026-06-20T191224.png
security:
- kind: domain-security
  name: Ourairports Domain Security
  slug: ourairports-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ourairports
tags:
- Aviation
- Airports
- Open Data
- CSV
- Geospatial
- Transportation
- Runways
- Navaids
- Public Domain
website: https://ourairports.com
---
