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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mbta Agentic Access
  operation_count: 22
  slug: mbta-agentic-access
  summary_line: 22 operations
api_count: 12
apis:
- description: Service disruption communications
  name: MBTA Alerts API
  slug: mbta-alerts-api
- description: Stop amenities such as elevators and bike racks
  name: MBTA Facilities API
  slug: mbta-facilities-api
- description: Transit lines grouped by mode
  name: MBTA Lines API
  slug: mbta-lines-api
- description: Real-time arrival and departure forecasts
  name: MBTA Predictions API
  slug: mbta-predictions-api
- description: Possible travel patterns within a route
  name: MBTA RoutePatterns API
  slug: mbta-routepatterns-api
- description: Route information per line
  name: MBTA Routes API
  slug: mbta-routes-api
- description: Scheduled stop times
  name: MBTA Schedules API
  slug: mbta-schedules-api
- description: Operational dates and frequencies
  name: MBTA Services API
  slug: mbta-services-api
- description: Trip route polylines for mapping
  name: MBTA Shapes API
  slug: mbta-shapes-api
- description: Boarding and disembarking locations
  name: MBTA Stops API
  slug: mbta-stops-api
- description: Vehicle journey definitions
  name: MBTA Trips API
  slug: mbta-trips-api
- description: Vehicle movement and position data
  name: MBTA Vehicles API
  slug: mbta-vehicles-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MBTA V3 Alerts API
  slug: open-mbta-alerts-api
- collection_type: open
  name: MBTA V3 Alerts Facilities API
  slug: open-mbta-facilities-api
- collection_type: open
  name: MBTA V3 Alerts Lines API
  slug: open-mbta-lines-api
- collection_type: open
  name: MBTA V3 API
  slug: open-mbta-mbta-v3-api
- collection_type: open
  name: MBTA V3 Alerts Predictions API
  slug: open-mbta-predictions-api
- collection_type: open
  name: MBTA V3 Alerts RoutePatterns API
  slug: open-mbta-routepatterns-api
- collection_type: open
  name: MBTA V3 Alerts Routes API
  slug: open-mbta-routes-api
- collection_type: open
  name: MBTA V3 Alerts Schedules API
  slug: open-mbta-schedules-api
- collection_type: open
  name: MBTA V3 Alerts Services API
  slug: open-mbta-services-api
- collection_type: open
  name: MBTA V3 Alerts Shapes API
  slug: open-mbta-shapes-api
- collection_type: open
  name: MBTA V3 Alerts Stops API
  slug: open-mbta-stops-api
- collection_type: open
  name: MBTA V3 Alerts Trips API
  slug: open-mbta-trips-api
- collection_type: open
  name: MBTA V3 Alerts Vehicles API
  slug: open-mbta-vehicles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mbta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mbta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mbta-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mbta
- group: start
  title: ''
  type: Portal
  url: https://www.mbta.com/developers
- group: start
  title: ''
  type: Signup
  url: https://api-v3.mbta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mbta
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mass.gov/files/documents/2017/10/27/massdot-developers-license-agreement.pdf
- group: company
  title: ''
  type: Blog
  url: https://www.mbta.com/news/rss.xml
created: '2025-02-24'
description: The Massachusetts Bay Transportation Authority (MBTA) V3 API provides fast, easy access to MBTA schedules, alerts, and real-time information using the JSON:API format. Free API keys are available via the developer portal.
finops:
- name: Mbta Finops
  service_category: API
  slug: mbta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mbta.png
layout: provider
modified: '2026-05-19'
name: MBTA
nav: Providers
network: true
overview: 'MBTA publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Facilities API, Lines API, and 9 more. Tagged areas include Boston, Massachusetts, Public Transportation, Real-Time, and Transit.


  MBTA''s developer surface includes authentication, developer portal, signup flow, engineering blog, and 5 more developer resources.'
plans:
- name: Mbta Plans Pricing
  plan_count: 3
  slug: mbta-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Mbta Rate Limits
  slug: mbta-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mbta/refs/heads/main/screenshots/mbta-2026-06-20T185053.png
security:
- kind: authentication
  name: Mbta Authentication
  slug: mbta-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mbta Domain Security
  slug: mbta-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mbta
tags:
- Boston
- Massachusetts
- Public Transportation
- Real-Time
- Transit
website: https://www.mbta.com/developers
---
