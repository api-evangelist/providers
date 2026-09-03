---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Marinetraffic Agentic Access
  operation_count: 5
  slug: marinetraffic-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: MarineTraffic Real-time Events API delivers live updates on port calls, bunkering operations, ship-to-ship transfers, and other maritime events as they occur.
  name: MarineTraffic Real-time Events API
  slug: marinetraffic-real-time-events-api
- description: MarineTraffic Predictive Events API delivers predicted destinations, estimated time of arrivals (ETAs), and voyage forecasts using AI and AIS data analysis.
  name: MarineTraffic Predictive Events API
  slug: marinetraffic-predictive-events-api
- description: MarineTraffic Past Events API provides access to historical vessel movements and events, enabling retrospective analysis of shipping patterns, port call history, and voyage records.
  name: MarineTraffic Past Events API
  slug: marinetraffic-past-events-api
- description: MarineTraffic Ship Database API provides detailed information on vessel characteristics, ownership, photos, vessel type, flag state, dimensions, and technical specifications for ships worldwide.
  name: MarineTraffic Ship Database API
  slug: marinetraffic-ship-database-api
- description: MarineTraffic provides AIS (Automatic Identification System) vessel tracking APIs delivering real-time vessel positions, speeds, headings, destinations, and ETAs. The REST API returns XML-formatted AI
  name: MarineTraffic AIS Vessel Tracking API
  slug: marinetraffic-api
- baseURL: https://services.marinetraffic.com/api
  baseurl_source: declared
  description: Port calls, arrivals, and departures
  name: MarineTraffic Port Operations API
  slug: marinetraffic-port-operations-api
- baseURL: https://services.marinetraffic.com/api
  baseurl_source: declared
  description: Real-time and historical vessel positions
  name: MarineTraffic Vessel Tracking API
  slug: marinetraffic-vessel-tracking-api
- baseURL: https://services.marinetraffic.com/api
  baseurl_source: declared
  description: Vessel static data and characteristics
  name: MarineTraffic Vessels API
  slug: marinetraffic-vessels-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MarineTraffic AIS Vessel Tracking API
  slug: open-marinetraffic-ais
- collection_type: open
  name: MarineTraffic AIS Vessel Tracking Port Operations API
  slug: open-marinetraffic-port-operations-api
- collection_type: open
  name: MarineTraffic AIS Port Operations Vessel Tracking API
  slug: open-marinetraffic-vessel-tracking-api
- collection_type: open
  name: MarineTraffic AIS Vessel Tracking Port Operations Vessels API
  slug: open-marinetraffic-vessels-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marinetraffic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marinetraffic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marinetraffic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marinetraffic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marinetraffic
- group: start
  title: ''
  type: Portal
  url: https://www.kpler.com/product/maritime/data-services
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kpler.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kpler.com/company/terms-of-use
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/openapi/marinetraffic-ais-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/json-schema/marinetraffic-vessel-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/json-ld/marinetraffic-context.jsonld
created: '2026-03-18'
description: MarineTraffic, a Kpler company, is a global provider of vessel tracking and maritime intelligence data. The platform offers AIS-based real-time vessel positions, port calls, predictive ETAs, historical voyage data, and ship registry information used for fleet monitoring, port operations, and supply chain visibility.
finops:
- name: Marinetraffic Finops
  service_category: Maritime Data API
  slug: marinetraffic-finops
json_schemas:
- name: ErrorResponse
  property_count: 1
  slug: marinetraffic-errorresponse
- name: ExpectedArrival
  property_count: 9
  slug: marinetraffic-expectedarrival
- name: ExpectedArrivalsResponse
  property_count: 1
  slug: marinetraffic-expectedarrivalsresponse
- name: PortCall
  property_count: 11
  slug: marinetraffic-portcall
- name: PortCallsResponse
  property_count: 1
  slug: marinetraffic-portcallsresponse
- name: MarineTraffic Vessel
  property_count: 28
  slug: marinetraffic-vessel
- name: VesselPositionsResponse
  property_count: 1
  slug: marinetraffic-vesselpositionsresponse
- name: VesselResponse
  property_count: 1
  slug: marinetraffic-vesselresponse
- name: VesselTrackPoint
  property_count: 8
  slug: marinetraffic-vesseltrackpoint
- name: VesselTrackResponse
  property_count: 1
  slug: marinetraffic-vesseltrackresponse
json_structures:
- name: Marinetraffic Structure
  property_count: 0
  slug: marinetraffic-structure
jsonld:
- class_count: 7
  name: Marinetraffic Context
  property_count: 19
  slug: marinetraffic-context
layout: provider
modified: '2026-05-19'
name: MarineTraffic
nav: Providers
network: true
overview: 'MarineTraffic publishes 3 APIs on the [APIs.io](https://apis.io/) network: Port Operations API, Vessel Tracking API, and Vessels API. Tagged areas include AIS, Maritime, Shipping, and Vessel Tracking.


  The MarineTraffic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MarineTraffic''s developer surface includes authentication, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Marinetraffic Plans Pricing
  plan_count: 1
  slug: marinetraffic-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Marinetraffic Rate Limits
  slug: marinetraffic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: MarineTraffic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: marinetraffic-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 64.9
    developer_ergonomics: 31.0
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/screenshots/marinetraffic-2026-06-20T184951.png
security:
- kind: authentication
  name: Marinetraffic Authentication
  slug: marinetraffic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marinetraffic Domain Security
  slug: marinetraffic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marinetraffic
tags:
- AIS
- Maritime
- Shipping
- Vessel Tracking
website: https://www.kpler.com/product/maritime/data-services
---
