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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sound Transit Agentic Access
  operation_count: 20
  slug: sound-transit-agentic-access
  summary_line: 20 operations
api_count: 7
apis:
- description: Transit agency information and coverage
  name: Sound Transit Agencies API
  slug: sound-transit-agencies-api
- description: Real-time and scheduled arrival/departure information
  name: Sound Transit Arrivals And Departures API
  slug: sound-transit-arrivals-and-departures-api
- description: Route definitions and schedules
  name: Sound Transit Routes API
  slug: sound-transit-routes-api
- description: Stop locations and schedules
  name: Sound Transit Stops API
  slug: sound-transit-stops-api
- description: System utilities and configuration
  name: Sound Transit System API
  slug: sound-transit-system-api
- description: Trip details and active vehicle positions
  name: Sound Transit Trips API
  slug: sound-transit-trips-api
- description: Active vehicle locations and assignments
  name: Sound Transit Vehicles API
  slug: sound-transit-vehicles-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sound Transit OneBusAway Agencies API
  slug: open-sound-transit-agencies-api
- collection_type: open
  name: Sound Transit OneBusAway Agencies Arrivals And Departures API
  slug: open-sound-transit-arrivals-and-departures-api
- collection_type: open
  name: Sound Transit OneBusAway API
  slug: open-sound-transit-onebusaway
- collection_type: open
  name: Sound Transit OneBusAway Agencies Routes API
  slug: open-sound-transit-routes-api
- collection_type: open
  name: Sound Transit OneBusAway Agencies Stops API
  slug: open-sound-transit-stops-api
- collection_type: open
  name: Sound Transit OneBusAway Agencies System API
  slug: open-sound-transit-system-api
- collection_type: open
  name: Sound Transit OneBusAway Agencies Trips API
  slug: open-sound-transit-trips-api
- collection_type: open
  name: Sound Transit OneBusAway Agencies Vehicles API
  slug: open-sound-transit-vehicles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sound-transit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sound-transit-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SoundTransit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sound-transit
- group: start
  title: ''
  type: Portal
  url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd
- group: company
  title: ''
  type: Website
  url: https://www.soundtransit.org/
- group: other
  title: ''
  type: GTFS Static Feeds
  url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd/otd-downloads
- group: other
  title: ''
  type: GTFS-RT Service Alerts (Protocol Buffers)
  url: https://s3.amazonaws.com/st-service-alerts-prod/alerts.pb
- group: other
  title: ''
  type: GTFS-RT Service Alerts (JSON)
  url: https://s3.amazonaws.com/st-service-alerts-prod/alerts_pb.json
- group: other
  title: ''
  type: Transitland Feed
  url: https://www.transit.land/feeds/f-c23-soundtransit
- group: other
  title: ''
  type: OneBusAway
  url: https://onebusaway.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd/transit-data-terms-use
- group: auth
  title: ''
  type: API Key Request
  url: mailto:oba_api_key@soundtransit.org
- group: operate
  title: ''
  type: Support
  url: mailto:open_transit_data@soundtransit.org
- group: commercial
  title: ''
  type: Trip Planner
  url: https://tripplanner.kingcounty.gov/
- group: other
  title: ''
  type: Real-Time Coverage
  url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd
created: '2026-03-16'
description: Sound Transit is a regional transit authority serving the Seattle-Puget Sound area of Washington State, operating light rail, commuter rail, and express bus services. The Sound Transit Open Transit Data (OTD) program provides GTFS static and real-time data feeds, OneBusAway API access, and GTFS-RT service alerts for transit application developers and researchers.
examples:
- key_count: 2
  name: Sound Transit Get Arrivals Example
  slug: sound-transit-get-arrivals-example
finops:
- name: Sound Transit Finops
  service_category: API
  slug: sound-transit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sound-transit.png
json_schemas:
- name: Sound Transit Arrival And Departure
  property_count: 14
  slug: sound-transit-arrival
- name: Sound Transit Stop
  property_count: 9
  slug: sound-transit-stop
json_structures:
- name: Sound Transit Arrivals Structure
  property_count: 0
  slug: sound-transit-arrivals-structure
jsonld:
- class_count: 7
  name: Sound Transit Context
  property_count: 15
  slug: sound-transit-context
layout: provider
modified: '2026-05-19'
name: Sound Transit
nav: Providers
network: true
overview: 'Sound Transit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agencies API, Arrivals And Departures API, Routes API, and 4 more. Tagged areas include Transit, Transportation, GTFS, Real-Time, and Public Transit.


  The Sound Transit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sound Transit''s developer surface includes developer portal, support, and 14 more developer resources.'
plans:
- name: Sound Transit Plans Pricing
  plan_count: 3
  slug: sound-transit-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Sound Transit Rate Limits
  slug: sound-transit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sound Transit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sound-transit-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Sound Transit API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 7
  slug: sound-transit-rules
score:
  band: thin
  composite: 37.6
  delta: 3.4
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 13.6
    contract_quality: 57.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sound-transit/refs/heads/main/screenshots/sound-transit-2026-06-20T194217.png
security:
- kind: domain-security
  name: Sound Transit Domain Security
  slug: sound-transit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sound-transit
tags:
- Transit
- Transportation
- GTFS
- Real-Time
- Public Transit
- Government
- Seattle
website: https://www.soundtransit.org/
---
