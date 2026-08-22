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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aviationstack Agentic Access
  operation_count: 11
  slug: aviationstack-agentic-access
  summary_line: 11 operations
api_count: 11
apis:
- description: The Aircraft Types API from Aviationstack — 1 operation(s) for aircraft types.
  name: Aviationstack Aircraft Types API
  slug: aviationstack-aircraft-types-api
- description: The Airlines API from Aviationstack — 1 operation(s) for airlines.
  name: Aviationstack Airlines API
  slug: aviationstack-airlines-api
- description: The Airplanes API from Aviationstack — 1 operation(s) for airplanes.
  name: Aviationstack Airplanes API
  slug: aviationstack-airplanes-api
- description: The Airports API from Aviationstack — 1 operation(s) for airports.
  name: Aviationstack Airports API
  slug: aviationstack-airports-api
- description: The Cities API from Aviationstack — 1 operation(s) for cities.
  name: Aviationstack Cities API
  slug: aviationstack-cities-api
- description: The Countries API from Aviationstack — 1 operation(s) for countries.
  name: Aviationstack Countries API
  slug: aviationstack-countries-api
- description: The Flights API from Aviationstack — 1 operation(s) for flights.
  name: Aviationstack Flights API
  slug: aviationstack-flights-api
- description: The FlightsFuture API from Aviationstack — 1 operation(s) for flightsfuture.
  name: Aviationstack FlightsFuture API
  slug: aviationstack-flightsfuture-api
- description: The Routes API from Aviationstack — 1 operation(s) for routes.
  name: Aviationstack Routes API
  slug: aviationstack-routes-api
- description: The Taxes API from Aviationstack — 1 operation(s) for taxes.
  name: Aviationstack Taxes API
  slug: aviationstack-taxes-api
- description: The Timetable API from Aviationstack — 1 operation(s) for timetable.
  name: Aviationstack Timetable API
  slug: aviationstack-timetable-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AviationStack Aircraft Types API
  slug: open-aviationstack-aircraft-types-api
- collection_type: open
  name: AviationStack Aircraft Types Airlines API
  slug: open-aviationstack-airlines-api
- collection_type: open
  name: AviationStack Aircraft Types Airplanes API
  slug: open-aviationstack-airplanes-api
- collection_type: open
  name: AviationStack Aircraft Types Airports API
  slug: open-aviationstack-airports-api
- collection_type: open
  name: AviationStack Aircraft Types Cities API
  slug: open-aviationstack-cities-api
- collection_type: open
  name: AviationStack Aircraft Types Countries API
  slug: open-aviationstack-countries-api
- collection_type: open
  name: AviationStack Aircraft Types Flights API
  slug: open-aviationstack-flights-api
- collection_type: open
  name: AviationStack Aircraft Types FlightsFuture API
  slug: open-aviationstack-flightsfuture-api
- collection_type: open
  name: AviationStack Aircraft Types Routes API
  slug: open-aviationstack-routes-api
- collection_type: open
  name: AviationStack Aircraft Types Taxes API
  slug: open-aviationstack-taxes-api
- collection_type: open
  name: AviationStack Aircraft Types Timetable API
  slug: open-aviationstack-timetable-api
- collection_type: open
  name: AviationStack API
  slug: open-aviationstack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aviationstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviationstack-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aviationstack.com/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aviationstack/
created: '2025-02-24'
description: Aviationstack is a comprehensive aviation data platform that provides real-time, accurate, and reliable information about flights, airlines, airports, and aircraft. This powerful tool offers a wide range of data including flight schedules, arrival and departure times, route information, aircraft details, and more.
finops:
- name: Aviationstack Finops
  service_category: API
  slug: aviationstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aviationstack.png
layout: provider
modified: '2026-05-19'
name: Aviationstack
nav: Providers
network: true
overview: 'Aviationstack publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Aircraft Types API, Airlines API, Airplanes API, and 8 more. Tagged areas include Airlines, Airports, Aviation, Flights, and Real-Time.


  Aviationstack''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: Aviationstack Plans Pricing
  plan_count: 3
  slug: aviationstack-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Aviationstack Rate Limits
  slug: aviationstack-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: -4.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.3
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviationstack/refs/heads/main/screenshots/aviationstack-2026-06-20T172726.png
security:
- kind: domain-security
  name: Aviationstack Domain Security
  slug: aviationstack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aviationstack
tags:
- Airlines
- Airports
- Aviation
- Flights
- Real-Time
website: https://aviationstack.com/documentation
---
