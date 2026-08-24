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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Local Bus service. Includes GTFS-Fares V2 fare data.
  name: MDOT MTA Local Bus GTFS
  slug: mta-local-bus-gtfs
- description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Light Rail service. Includes GTFS-Fares V2 fare data.
  name: MDOT MTA Light Rail GTFS
  slug: mta-light-rail-gtfs
- description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Metro Subway service. Includes GTFS-Fares V2 fare data.
  name: MDOT MTA Metro Subway GTFS
  slug: mta-metro-subway-gtfs
- description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA MARC commuter rail service.
  name: MDOT MTA MARC Train GTFS
  slug: mta-marc-train-gtfs
- description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Commuter Bus service.
  name: MDOT MTA Commuter Bus GTFS
  slug: mta-commuter-bus-gtfs
- description: System-wide GTFS-RT service alerts feed for all MDOT MTA modes.
  name: MDOT MTA Service Alerts
  slug: mta-service-alerts
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maryland-transit-administration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maryland-transit-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mtamaryland
- group: start
  title: ''
  type: Portal
  url: https://www.mta.maryland.gov/developer-resources
- group: company
  title: ''
  type: Website
  url: https://www.mta.maryland.gov/
- group: docs
  title: ''
  type: GTFS Specification
  url: https://gtfs.org/
- group: docs
  title: ''
  type: Swiftly Documentation
  url: https://swiftly-inc.stoplight.io/docs/realtime-standalone/
- group: company
  title: ''
  type: Blog
  url: https://www.mta.maryland.gov/articles
created: '2025-05-02'
description: The Maryland Transit Administration (MDOT MTA) supports open transit data initiatives and makes resources available to developers and applications. It primarily uses the General Transit Feed Specification (GTFS) and GTFS-RT to convey schedule, geographic, fare, vehicle position, and trip update data for Local Bus, Light Rail, Metro Subway, MARC Train, and Commuter Bus services in a standardized format.
finops:
- name: Maryland Transit Administration Finops
  service_category: API
  slug: maryland-transit-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maryland-transit-administration.png
layout: provider
modified: '2026-04-28'
name: Maryland Transit Administration
nav: Providers
network: true
overview: 'Maryland Transit Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Government, GTFS, GTFS-RT, Public Transportation, and Transit.


  Maryland Transit Administration''s developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Maryland Transit Administration Plans Pricing
  plan_count: 3
  slug: maryland-transit-administration-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Maryland Transit Administration Rate Limits
  slug: maryland-transit-administration-rate-limits
score:
  band: emerging
  composite: 14.1
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maryland-transit-administration/refs/heads/main/screenshots/maryland-transit-administration-2026-06-20T185010.png
security:
- kind: domain-security
  name: Maryland Transit Administration Domain Security
  slug: maryland-transit-administration-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Maryland Transit Administration Vulnerability Disclosure
  slug: maryland-transit-administration-vulnerability-disclosure
  summary_line: disclosure policy published
slug: maryland-transit-administration
tags:
- Government
- GTFS
- GTFS-RT
- Public Transportation
- Transit
- Bus
- Rail
- Subway
website: https://www.mta.maryland.gov/
---
