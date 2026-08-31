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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Aviyair API provides global flight data including real-time flight tracking and status, historical flight data, airline schedules, IATA and ICAO codes, routes, and delay information.
  name: Aviyair
  slug: aviyair
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviyair-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aviyair.com/aviation-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aviyair
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aviyair/
created: '2025-02-24'
description: Aviyair provides global coverage of flight and airport information including real-time and historical flight tracking, flight schedules with airline arrival and departure times, IATA and ICAO codes, airline routes, and flight delays information.
finops:
- name: Aviyair Finops
  service_category: API
  slug: aviyair-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aviyair.png
layout: provider
modified: '2026-04-19'
name: Aviyair
nav: Providers
network: true
overview: 'Aviyair publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Airlines, Airports, Aviation, Flight Tracking, and IATA.


  Aviyair''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: Aviyair Plans Pricing
  plan_count: 3
  slug: aviyair-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Aviyair Rate Limits
  slug: aviyair-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviyair/refs/heads/main/screenshots/aviyair-2026-06-20T172731.png
security:
- kind: domain-security
  name: Aviyair Domain Security
  slug: aviyair-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aviyair
tags:
- Airlines
- Airports
- Aviation
- Flight Tracking
- IATA
website: https://aviyair.com/aviation-api/
---
