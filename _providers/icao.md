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
api_count: 7
apis:
- description: The ICAO API Data Service provides programmatic access to authoritative civil aviation data published by ICAO, with continuously updated endpoints across six data areas. An API key is required and res
  name: ICAO API Data Service
  slug: icao-api-data-service
- description: Endpoints providing reference and statistical data on ICAO Member States, including state-level aviation activity, agreements, and contracting state metadata.
  name: ICAO States API
  slug: icao-states-api
- description: Endpoints exposing ICAO airport reference data including DOC7910 location indicators, airport metadata, and related aerodrome information.
  name: ICAO Airports API
  slug: icao-airports-api
- description: Endpoints providing operator reference data including DOC8585 three-letter operator designators, telephony, and operator details for airlines and aircraft operators.
  name: ICAO Operators API
  slug: icao-operators-api
- description: Endpoints providing airspace, navigation, and route data including flight information regions and airspace structures relevant to international air navigation.
  name: ICAO Airspace API
  slug: icao-airspace-api
- description: Endpoints providing access to aviation safety occurrence data, including accident and incident records reported through ICAO's safety information systems.
  name: ICAO Occurrences API
  slug: icao-occurrences-api
- description: Endpoints providing aircraft reference data including DOC8643 aircraft type designators, manufacturer information, and aircraft performance categories.
  name: ICAO Aircraft API
  slug: icao-aircraft-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icao-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/icao
- group: company
  title: ''
  type: Website
  url: https://www.icao.int/
- group: start
  title: ''
  type: Portal
  url: https://applications.icao.int/dataservices/default.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
- group: build
  title: ''
  type: Samples
  url: https://applications.icao.int/dataservices/api-data-samples
- group: commercial
  title: ''
  type: Pricing
  url: https://store.icao.int/en/aviation-api-data-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.icao.int/sites/default/files/Aviation-API-Data-Service/Documents/User-Terms-and-Condtions-for-ICAO-API-Data-Service-APIs-LEB_FINAL_13.04.21.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.icao.int/contact/
created: '2026-03-16'
description: The International Civil Aviation Organization (ICAO) is a specialized agency of the United Nations that codifies the principles and techniques of international air navigation and fosters the planning and development of international air transport. ICAO's API Data Service provides 50+ continuously updated APIs covering states, airports, operators, airspace, occurrences, and aircraft, including official reference datasets such as DOC7910 location indicators, DOC8585 operator three-letter codes, and DOC8643 aircraft type designators.
finops:
- name: Icao Finops
  service_category: API
  slug: icao-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icao.png
layout: provider
modified: '2026-04-28'
name: ICAO
nav: Providers
network: true
overview: 'ICAO publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Airlines, Airports, Airspace, Aviation, and Reference Data.


  ICAO''s developer surface includes developer portal, documentation, pricing, support, and 5 more developer resources.'
plans:
- name: Icao Plans Pricing
  plan_count: 3
  slug: icao-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Icao Rate Limits
  slug: icao-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 1.4
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/icao/refs/heads/main/screenshots/icao-2026-06-20T183144.png
security:
- kind: domain-security
  name: Icao Domain Security
  slug: icao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: icao
tags:
- Airlines
- Airports
- Airspace
- Aviation
- Reference Data
- Standards
- United Nations
website: https://www.icao.int/
---
