---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Transitapp Agentic Access
  operation_count: 7
  slug: transitapp-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: Available transit networks and coverage near a location.
  name: Transit Locations API
  slug: transitapp-locations-api
- description: Public transit routes near a location with real-time departures.
  name: Transit Nearby Routes API
  slug: transitapp-nearby-routes-api
- description: Public transit stops near a location.
  name: Transit Nearby Stops API
  slug: transitapp-nearby-stops-api
- description: Itineraries, stops, and geometry for a specific route.
  name: Transit Route Details API
  slug: transitapp-route-details-api
- description: Service alerts and disruptions for routes, stops, and networks.
  name: Transit Service Alerts API
  slug: transitapp-service-alerts-api
- description: Upcoming departures for a specific stop.
  name: Transit Stop Departures API
  slug: transitapp-stop-departures-api
- description: Multimodal origin-to-destination trip planning.
  name: Transit Trip Planning API
  slug: transitapp-trip-planning-api
artifact_total: 14
collections:
- collection_type: open
  name: Transit API
  slug: open-transitapp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transitapp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transitapp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transitapp-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TransitApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transit-app
- group: company
  title: ''
  type: Website
  url: https://transitapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.transitapp.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/transitapp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transitapp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/transitapp-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.transitapp.com/feed/
created: '2026-07-03'
description: Transit (the Transit App) is a real-time public transit trip planning and departures platform covering 1,100+ cities in 37 countries. The Transit REST API delivers real-time departures, nearby routes and stops, route details, multimodal trip planning, and service alerts, plus shared-mobility availability for bikes, scooters, and carshare. The API is publicly documented at api-doc.transitapp.com but access is key-gated - developers request a key that grants a free tier (5 requests/minute, 1,500 requests/month), and higher volumes are arranged with the partnerships team. Requests are authenticated with an apiKey header against https://external.transitapp.com/v3.
finops:
- name: Transitapp Finops
  service_category: Mobility and Transit Data
  slug: transitapp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transitapp.png
layout: provider
modified: '2026-07-03'
name: Transit
nav: Providers
network: true
overview: 'Transit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Locations API, Nearby Routes API, Nearby Stops API, and 4 more. Tagged areas include Transit, Public Transportation, Real-Time, Mobility, and Trip Planning.


  Transit''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Transitapp Plans Pricing
  plan_count: 2
  slug: transitapp-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 3
  name: Transitapp Rate Limits
  slug: transitapp-rate-limits
score:
  band: thin
  composite: 37.4
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Transitapp Authentication
  slug: transitapp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transitapp Domain Security
  slug: transitapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transitapp
tags:
- Transit
- Public Transportation
- Real-Time
- Mobility
- Trip Planning
- Departures
- GTFS
- MaaS
website: https://transitapp.com
---
