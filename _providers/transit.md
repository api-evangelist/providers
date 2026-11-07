---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Transit Agentic Access
  operation_count: 7
  slug: transit-agentic-access
  summary_line: 7 operations
api_count: 8
apis:
- description: Deep-link URL scheme for launching the Transit mobile app from partner apps and websites. Supports directions and nearby-routes hand-offs without requiring an API key.
  name: Transit URL Scheme
  slug: url-scheme
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Service alerts and disruptions
  name: Transit Alerts API
  slug: transit-alerts-api
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Real-time and scheduled transit departure information
  name: Transit Departures API
  slug: transit-departures-api
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Shared bikes, scooters, and carshares
  name: Transit Mobility API
  slug: transit-mobility-api
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Transit network and agency data
  name: Transit Networks API
  slug: transit-networks-api
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Route information and schedules
  name: Transit Routes API
  slug: transit-routes-api
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Stop and station information
  name: Transit Stops API
  slug: transit-stops-api
- baseURL: https://api-doc.transitapp.com
  baseurl_source: declared
  description: Multimodal trip planning and results
  name: Transit Trips API
  slug: transit-trips-api
- baseURL: transit://
  baseurl_source: declared
  description: Available transit networks and coverage near a location.
  name: Transit Locations API
  slug: transit-locations-api
- baseURL: transit://
  baseurl_source: declared
  description: Public transit routes near a location with real-time departures.
  name: Transit Nearby Routes API
  slug: transit-nearby-routes-api
- baseURL: transit://
  baseurl_source: declared
  description: Public transit stops near a location.
  name: Transit Nearby Stops API
  slug: transit-nearby-stops-api
- baseURL: transit://
  baseurl_source: declared
  description: Itineraries, stops, and geometry for a specific route.
  name: Transit Route Details API
  slug: transit-route-details-api
- baseURL: transit://
  baseurl_source: declared
  description: Service alerts and disruptions for routes, stops, and networks.
  name: Transit Service Alerts API
  slug: transit-service-alerts-api
- baseURL: transit://
  baseurl_source: declared
  description: Multimodal origin-to-destination trip planning.
  name: Transit Trip Planning API
  slug: transit-trip-planning-api
artifact_total: 37
collections:
- collection_type: open
  name: Transit Alerts API
  slug: open-transit-alerts-api
- collection_type: open
  name: Transit Alerts Departures API
  slug: open-transit-departures-api
- collection_type: open
  name: Transit Alerts Mobility API
  slug: open-transit-mobility-api
- collection_type: open
  name: Transit Alerts Networks API
  slug: open-transit-networks-api
- collection_type: open
  name: Transit Alerts Routes API
  slug: open-transit-routes-api
- collection_type: open
  name: Transit Alerts Stops API
  slug: open-transit-stops-api
- collection_type: open
  name: Transit Alerts Trips API
  slug: open-transit-trips-api
- collection_type: open
  name: Transit API
  slug: open-transit
- collection_type: open
  name: Transit API
  slug: open-transitapp
common:
- group: other
  href: https://artifacts.apis.io/transit/capabilities/transit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/transit-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/transit/overview
- group: commercial
  href: https://artifacts.apis.io/transit/plans/transit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/transit/rate-limits/transit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/transit/finops/transit-finops.yml
  title: ''
  type: FinOps
  url: finops/transit-finops.yml
- group: agent
  href: https://artifacts.apis.io/transit/agentic-access/transit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/transit/security/transit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/transit/authentication/transit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://transitapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://transitapp.com/apis
- group: docs
  title: ''
  type: APIDocumentation
  url: https://api-doc.transitapp.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TransitApp
- group: company
  title: ''
  type: Blog
  url: https://blog.transitapp.com/
- group: company
  title: ''
  type: BlogFeed
  url: https://blog.transitapp.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://help.transitapp.com/
- group: company
  title: ''
  type: Careers
  url: https://transitapp.com/careers
- group: company
  title: ''
  type: Press
  url: https://transitapp.com/press
- group: commercial
  title: ''
  type: Pricing
  url: https://transitapp.com/apis
- group: start
  title: ''
  type: Signup
  url: https://docs.google.com/forms/d/e/1FAIpQLScZbUsb1G1gRzIkEQo4FuuAbfzQbldTvu6-62j_pSRWPtKZiA/viewform
- group: operate
  title: ''
  type: ContactSales
  url: mailto:partners+website@transit.app
- group: operate
  title: ''
  type: ContactGeneral
  url: mailto:info@transit.app
created: '2025-05-02'
description: Transit ("The world's most accurate transit app") provides real-time public transit data, multimodal trip planning, and shared mobility across 1,000+ cities including New York, Paris, London, and Montreal, partnering with 180+ transit agencies. The platform aggregates trains, buses, bikes, scooters, and carshares with crowdsourced GO real-time signals, ships a freemium partner API (5 calls/minute, 1,500 calls/month), and monetizes consumers via the Transit Royale subscription ($2/month billed annually).
examples:
- key_count: 2
  name: Transit Get Stop Departures Example
  slug: transit-get-stop-departures-example
- key_count: 2
  name: Transit Plan Trip Example
  slug: transit-plan-trip-example
finops:
- has_sources: true
  method: derived
  name: Transit Finops
  primary_unit: ''
  service_category: ''
  slug: transit-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transit.png
json_schemas:
- name: Transit Departure
  property_count: 7
  slug: transit-departure
- name: Transit Stop
  property_count: 6
  slug: transit-stop
json_structures:
- name: Transit Stop Structure
  property_count: 0
  slug: transit-stop-structure
jsonld:
- class_count: 32
  name: Transit Context
  property_count: 0
  slug: transit-context
layout: provider
modified: '2026-05-23'
name: Transit
nav: Providers
network: true
overview: 'Transit publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Departures API, Mobility API, and 11 more. Tagged areas include Transit, Public Transit, Real-Time, Trip Planning, and Multi-Modal.


  The Transit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Transit''s developer surface includes authentication, documentation, GitHub presence, engineering blog, support, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Transit Plans Pricing
  plan_count: 1
  slug: transit-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Transit Rate Limits
  slug: transit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Transit — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: transit-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Transit API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 5
  slug: transit-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 77.0
    catalog_earned_first_party: 8.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 44.7
    contract_governance: 27.3
    contract_quality: 65.0
    developer_ergonomics: 35.7
    discoverability: 72.3
    operational_transparency: 13.2
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/transit/transit-2026-06-20T195544.png
security:
- kind: authentication
  name: Transit Authentication
  slug: transit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transit Domain Security
  slug: transit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transit
tags:
- Transit
- Public Transit
- Real-Time
- Trip Planning
- Multi-Modal
- GTFS
- GOFS
- Mobility
- Shared Mobility
website: https://transitapp.com/
---
