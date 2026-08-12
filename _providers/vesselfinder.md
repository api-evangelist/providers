---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vesselfinder Agentic Access
  operation_count: 13
  slug: vesselfinder-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 10
apis:
- description: Real-time container track-and-trace.
  name: VesselFinder Containers API
  slug: vesselfinder-containers-api
- description: Sea-route distance and geometry between two points.
  name: VesselFinder Distance API
  slug: vesselfinder-distance-api
- description: Vessels with announced ETAs at a selected port.
  name: VesselFinder Expected Arrivals API
  slug: vesselfinder-expected-arrivals-api
- description: Manage the watchlist of vessels backing the VesselsList method.
  name: VesselFinder List Manager API
  slug: vesselfinder-list-manager-api
- description: All vessels within a predefined geographic area, subscription-based.
  name: VesselFinder Live Data API
  slug: vesselfinder-live-data-api
- description: Static vessel particulars by IMO.
  name: VesselFinder Master Data API
  slug: vesselfinder-master-data-api
- description: Arrival and departure events for vessels or ports.
  name: VesselFinder Port Calls API
  slug: vesselfinder-port-calls-api
- description: Account status and remaining credits.
  name: VesselFinder Status API
  slug: vesselfinder-status-api
- description: On-demand vessel position, voyage, and master data lookups.
  name: VesselFinder Vessels API
  slug: vesselfinder-vessels-api
- description: Predefined-fleet data, subscription-based.
  name: VesselFinder Vessels List API
  slug: vesselfinder-vessels-list-api
artifact_total: 54
collections:
- collection_type: postman
  name: VesselFinder AIS Containers API
  slug: postman-vesselfinder-containers-api
- collection_type: postman
  name: VesselFinder AIS Containers Distance API
  slug: postman-vesselfinder-distance-api
- collection_type: postman
  name: VesselFinder AIS Containers Expected Arrivals API
  slug: postman-vesselfinder-expected-arrivals-api
- collection_type: postman
  name: VesselFinder AIS Containers List Manager API
  slug: postman-vesselfinder-list-manager-api
- collection_type: postman
  name: VesselFinder AIS Containers Live Data API
  slug: postman-vesselfinder-live-data-api
- collection_type: postman
  name: VesselFinder AIS Containers Master Data API
  slug: postman-vesselfinder-master-data-api
- collection_type: postman
  name: VesselFinder AIS Containers Port Calls API
  slug: postman-vesselfinder-port-calls-api
- collection_type: postman
  name: VesselFinder AIS Containers Status API
  slug: postman-vesselfinder-status-api
- collection_type: postman
  name: VesselFinder AIS Containers Vessels API
  slug: postman-vesselfinder-vessels-api
- collection_type: postman
  name: VesselFinder AIS Containers Vessels List API
  slug: postman-vesselfinder-vessels-list-api
- collection_type: open
  name: VesselFinder AIS API
  slug: open-vesselfinder-ais-api
- collection_type: open
  name: VesselFinder Container Tracking API
  slug: open-vesselfinder-container-tracking-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vesselfinder/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vesselfinder-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vesselfinder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vesselfinder-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.vesselfinder.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.vesselfinder.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://container.vesselfinder.com/api/1.0/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.vesselfinder.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vesselfinder.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://api.vesselfinder.com/docs/
- group: operate
  title: ''
  type: FAQ
  url: https://api.vesselfinder.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.vesselfinder.com/docs/flags.html
- group: docs
  title: ''
  type: Documentation
  url: https://api.vesselfinder.com/docs/aistypes.html
- group: docs
  title: ''
  type: Documentation
  url: https://api.vesselfinder.com/docs/navstat.html
- group: operate
  title: ''
  type: Support
  url: https://www.vesselfinder.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vesselfinder.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vesselfinder.com/privacy
- group: build
  title: ''
  type: Tools
  url: https://route.vesselfinder.com
- group: company
  title: ''
  type: Blog
  url: https://www.vesselfinder.com/news
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/VesselFinder
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/vesselfinder
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/vesselfinder
- group: other
  title: ''
  type: Application
  url: https://apps.apple.com/us/app/vesselfinder-lite/id918080862
- group: other
  title: ''
  type: Application
  url: https://play.google.com/store/apps/details?id=com.astrapaging.vff
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VesselFinder
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VesselFinder/vesselfinder-api-wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VesselFinder/container-tracking-api-wrapper
- group: commercial
  title: ''
  type: Plans
  url: plans/vesselfinder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vesselfinder-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vesselfinder-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vesselfinder-vocabulary.yml
- group: design
  title: ''
  type: Spectral
  url: rules/vesselfinder-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: VesselFinder is a maritime intelligence company operating a global AIS vessel-tracking network (terrestrial AIS plus satellite AIS) and offering ship positions, voyage history, vessel particulars, port-call events, sea-distance routing, and ocean-container track-and-trace through its developer APIs. The platform pairs a credit-metered AIS REST API (Vessels, PortCalls, ExpectedArrivals, MasterData, Distance, plus subscription feeds VesselsList and LiveData) with a separate Container Tracking API that returns shipment schedules and real-time vessel positions by container number. VesselFinder also runs a public web map, iOS/Android apps, an embeddable map widget, a fleet explorer, and a route planner.
examples:
- key_count: 3
  name: Vesselfinder Container Tracking Example
  slug: vesselfinder-container-tracking-example
- key_count: 3
  name: Vesselfinder Distance Example
  slug: vesselfinder-distance-example
- key_count: 2
  name: Vesselfinder Status Example
  slug: vesselfinder-status-example
features:
- Global AIS vessel tracking network — terrestrial receivers plus satellite AIS coverage
- On-demand REST endpoints for vessel positions (Vessels), port arrivals/departures (PortCalls), and expected arrivals (ExpectedArrivals)
- Static vessel particulars (MasterData) including flag, type, dimensions, tonnage, TEU, deadweight
- Three dataset families — AIS (dynamic), Voyage (last port call), Master (static particulars)
- Sea-route distance and routing API with optional canal/strait gateway preferences and ECA handling
- Subscription feeds — VesselsList for a predefined fleet, LiveData for a predefined rectangular area
- Fleet watchlist management via ListManager (GET, POST, PUT, DELETE)
- Container Tracking API — track ocean-freight containers by container number with optional SCAC carrier
- Asynchronous container lookups with 202 polling and 12-hour caching
- Credit-metered AIS billing (terrestrial 1 credit, satellite 10 credits, master 2–3 credits, distance 1 credit)
- Prepaid AIS credit packs (10k / 20k / 50k) priced in EUR; container subscriptions priced in USD
- JSON (default) and XML response formats
- API key authentication via the userkey query parameter
- Reference taxonomies — Flag Codes, AIS Ship Types, AIS NavStat
- Official PHP and Python wrapper libraries on GitHub for both AIS and Container Tracking APIs
- VesselFinder web platform, iOS/Android apps, embeddable maps, fleet explorer, and route planner
finops:
- name: Vesselfinder Finops
  service_category: Geospatial and Logistics
  slug: vesselfinder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vesselfinder.png
json_schemas:
- name: VesselFinder Container Shipment
  property_count: 3
  slug: vesselfinder-container-shipment
- name: VesselFinder Port Call
  property_count: 7
  slug: vesselfinder-port-call
- name: VesselFinder Vessel
  property_count: 3
  slug: vesselfinder-vessel
json_structures:
- name: Vesselfinder Vessel Structure
  property_count: 0
  slug: vesselfinder-vessel-structure
jsonld:
- class_count: 0
  name: Vesselfinder Context
  property_count: 6
  slug: vesselfinder-context
layout: provider
modified: '2026-05-25'
name: VesselFinder
nav: Providers
network: true
overview: 'VesselFinder publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Containers API, Distance API, Expected Arrivals API, and 7 more. Tagged areas include AIS, Maritime, Vessel Tracking, Container Tracking, and Geospatial.


  The VesselFinder catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  VesselFinder''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, FAQ, support, and 25 more developer resources.'
plans:
- name: Vesselfinder Plans Pricing
  plan_count: 10
  slug: vesselfinder-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Vesselfinder Rate Limits
  slug: vesselfinder-rate-limits
rules:
- name: VesselFinder API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: vesselfinder-jsonschema-spectral-rules
- name: VesselFinder API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 3
  slug: vesselfinder-rules
score:
  band: strong
  composite: 58.8
  delta: -0.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 71.6
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vesselfinder/refs/heads/main/screenshots/vesselfinder-2026-06-20T201006.png
security:
- kind: authentication
  name: Vesselfinder Authentication
  slug: vesselfinder-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Vesselfinder Domain Security
  slug: vesselfinder-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vesselfinder
tags:
- AIS
- Maritime
- Vessel Tracking
- Container Tracking
- Geospatial
- Logistics
- Ports
- Supply Chain
website: https://www.vesselfinder.com
---
