---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: SkyWest Airlines flight data including flight status, schedules, and routes is accessible through third-party aviation APIs such as AirLabs. SkyWest operates under IATA code OO / ICAO code SKW and ser
  name: SkyWest Flight Data
  slug: flight-data
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skywest-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skywestairlines
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skywest-airlines
- group: company
  title: ''
  type: Website
  url: https://www.skywest.com
- group: company
  title: ''
  type: About
  url: https://www.skywest.com/about-skywest-airlines/
- group: other
  title: ''
  type: FactSheet
  url: https://www.skywest.com/about-skywest-airlines/facts
- group: other
  title: ''
  type: History
  url: https://www.skywest.com/about-skywest-airlines/skywest-history
- group: company
  title: ''
  type: Careers
  url: https://www.skywest.com/careers/
- group: operate
  title: ''
  type: FlightStatus
  url: https://www.skywest.com/fly-skywest-airlines/flight-status/
- group: other
  title: ''
  type: ThirdPartyAPI
  url: https://airlabs.co/skywest-airlines-developer-api
- group: other
  title: ''
  type: FlightTracking
  url: https://www.flightradar24.com/data/airlines/oo-skw
- group: company
  title: ''
  type: Press
  url: https://www.skywest.com/about-skywest-airlines/press-room/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/skywest-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/skywest-vocabulary.yml
created: '2026-05-02'
description: SkyWest Airlines is the largest regional airline in North America, headquartered in St. George, Utah. Operating under partnership agreements with United Airlines, Delta Air Lines, American Airlines, and Alaska Airlines, SkyWest serves over 256 destinations across the United States, Canada, and Mexico with a fleet of 500+ Bombardier regional jets (CRJ200, CRJ550, CRJ900). Founded in 1972, SkyWest carries over 46 million passengers annually operating as United Express, Delta Connection, American Eagle, and Alaska SkyWest. The company does not offer a public developer API; flight data is accessible through third-party aviation data providers.
finops:
- name: Skywest Finops
  service_category: API
  slug: skywest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skywest.png
jsonld:
- class_count: 0
  name: Skywest Context
  property_count: 6
  slug: skywest-context
layout: provider
modified: '2026-05-02'
name: SkyWest Airlines
nav: Providers
network: true
overview: 'SkyWest Airlines publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Airlines, Aviation, Regional Airline, Transportation, and Fortune 1000.


  The SkyWest Airlines catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Skywest Plans Pricing
  plan_count: 3
  slug: skywest-plans-pricing
press:
- date: '2026-05-25'
  title: 2024 ANNUAL REPORT - SkyWest Incorporated
  url: https://inc.skywest.com/assets/Uploads/AnnualReports/2024-Annual-Report-and-Proxy-Statement.pdf
- date: '2026-05-25'
  title: Barkley Regional Airport prepares for SkyWest launch ...
  url: https://www.wpsdlocal6.com/news/barkley-regional-airport-prepares-for-skywest-launch-mobile-id-upgrades/article_522bc4f6-b4a8-4719-b708-3792d2d9d3d1.html
- date: '2026-05-25'
  title: 2025 ANNUAL REPORT - SkyWest Incorporated
  url: https://inc.skywest.com/assets/Uploads/AnnualReports/2025Annual-Report-and-Proxy-Statement.pdf
- date: '2026-05-25'
  title: Could AI Have Prevented SkyWest Airliner's Near Collision ...
  url: https://www.scientificamerican.com/article/could-ai-have-prevented-skywest-airliners-near-collision-with-a-b52-bomber/
- date: '2026-05-25'
  title: SkyWest set to deploy CAE's next-generation Flight ...
  url: https://www.prnewswire.com/news-releases/skywest-set-to-deploy-caes-next-generation-flight-operations-solutions-301836499.html
random_paper: 46
rate_limits:
- limit_count: 5
  name: Skywest Rate Limits
  slug: skywest-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 9.4
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 13.2
    operational_transparency: 36.8
  previous_composite: 24.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skywest/refs/heads/main/screenshots/skywest-2026-06-20T194019.png
security:
- kind: domain-security
  name: Skywest Domain Security
  slug: skywest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skywest
tags:
- Airlines
- Aviation
- Regional Airline
- Transportation
- Fortune 1000
website: https://www.skywest.com
---
