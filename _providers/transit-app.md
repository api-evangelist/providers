---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Transit App Agentic Access
  operation_count: 16
  slug: transit-app-agentic-access
  summary_line: 16 operations
api_count: 3
apis:
- description: The Map Layers API from Transit — 2 operation(s) for map layers.
  name: Transit Map Layers API
  slug: transit-app-map-layers-api
- description: The Public API from Transit — 13 operation(s) for public.
  name: Transit Public API
  slug: transit-app-public-api
- description: The Vehicles API from Transit — 1 operation(s) for vehicles.
  name: Transit Vehicles API
  slug: transit-app-vehicles-api
artifact_total: 7
collections:
- collection_type: open
  name: Transit API (Stable)
  slug: open-transit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transit-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transit-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transit-app-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://transitapp.com
- group: start
  title: ''
  type: Portal
  url: https://transitapp.com
- group: start
  title: ''
  type: APIPortal
  url: https://transitapp.com/apis
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.transitapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.transitapp.com/v4.html
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.transitapp.com/v3.html
- group: start
  title: ''
  type: PartnerPortal
  url: https://resources.transitapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://resources.transitapp.com/article/397-on-demand-transit-api-guidelines
- group: company
  title: ''
  type: Blog
  url: https://blog.transitapp.com/
- group: company
  title: ''
  type: AboutUs
  url: https://transitapp.com/about
- group: other
  title: ''
  type: Vision
  url: https://transitapp.com/vision
- group: company
  title: ''
  type: Press
  url: https://transitapp.com/press
- group: operate
  title: ''
  type: Help
  url: https://help.transitapp.com/
- group: company
  title: ''
  type: Careers
  url: https://transitapp.com/jobs
- group: operate
  title: ''
  type: Contact
  url: mailto:partners+website@transit.app
- group: company
  title: ''
  type: Partners
  url: https://transitapp.com/apis
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transitapp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transitapp.com/terms
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/app/transit-bus-subway-times/id498151501
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=com.thetransitapp.droid
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transitapp
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/transitapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transit-app
- group: build
  title: ''
  type: Tools
  url: https://github.com/transitapp/gtfs-flex-to-GOFS
- group: build
  title: ''
  type: Tools
  url: https://github.com/transitapp/gtfs-blocks-to-transfers
- group: build
  title: ''
  type: Tools
  url: https://github.com/transitapp/py-gtfs-loader
- group: build
  title: ''
  type: Sample
  url: https://github.com/transitapp/Transit-TV
- group: other
  title: ''
  type: Benchmark
  url: https://github.com/transitapp/ETA-Accuracy-Benchmark
created: '2026-05-25'
description: Transit is a Montreal-based mobility app that provides real-time public transit, multimodal trip planning, and shared-mobility navigation across 1,000+ cities worldwide. The consumer app displays nearby buses, subways, trains, bikeshare, scooters, carshare, and on-demand transit the moment it opens, and is augmented by "GO" crowdsourced vehicle locations contributed by millions of riders. Transit operates a partner program for transit agencies, mobility operators, and third-party developers, exposing its routing, real-time, alerts, and shared-mobility surface through the public Transit API (api-doc.transitapp.com, v4 stable). The v4 API is a single OpenAPI 3.1 contract covering nearby routes and stops, stop departures, multimodal trip planning, placemarks for shared-mobility vehicles and docks, available networks, route and trip details, service alerts, and real-time vehicle positions. Authentication is an apiKey header; the free tier allows 5 requests per minute and 1,500 calls
  per month after key approval, with custom commercial plans available through partners@transit.app.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transit-app.png
layout: provider
modified: '2026-05-25'
name: Transit
nav: Providers
network: true
overview: 'Transit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Map Layers API, Public API, and Vehicles API. Tagged areas include Transit, Public Transit, Multimodal, Mobility, and Trip Planning.


  Transit''s developer surface includes authentication, developer portal, documentation, engineering blog, tooling, and 26 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 31.4
  delta: -2.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 52.2
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transit-app/refs/heads/main/screenshots/transit-app-2026-06-20T195546.png
security:
- kind: authentication
  name: Transit App Authentication
  slug: transit-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transit App Domain Security
  slug: transit-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transit-app
tags:
- Transit
- Public Transit
- Multimodal
- Mobility
- Trip Planning
- Routing
- Real-Time
- GTFS
- GOFS
- Bikeshare
- Scooters
- Carshare
- On-Demand Transit
- Service Alerts
- Shared Mobility
- Crowdsourced Data
website: https://transitapp.com
---
