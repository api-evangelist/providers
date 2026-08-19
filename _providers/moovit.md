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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Moovit Agentic Access
  operation_count: 34
  slug: moovit-agentic-access
  summary_line: 34 operations
api_count: 9
apis:
- description: Metro agencies and supported transit types.
  name: Moovit General API
  slug: moovit-general-api
- description: GTFS-RT feeds for vehicles, trip updates, and service alerts.
  name: Moovit GTFSRealtime API
  slug: moovit-gtfsrealtime-api
- description: Line metadata, stops, geometry, schedules, and alerts.
  name: Moovit Lines API
  slug: moovit-lines-api
- description: Locate stops, bikes, and scooters near a coordinate.
  name: Moovit Nearby API
  slug: moovit-nearby-api
- description: Live arrival predictions for stops and lines.
  name: Moovit RealTime API
  slug: moovit-realtime-api
- description: Search stops and lines by name or number.
  name: Moovit Search API
  slug: moovit-search-api
- description: Metro service alerts and details.
  name: Moovit ServiceAlerts API
  slug: moovit-servicealerts-api
- description: Stop metadata, lines served, reviews, and photos.
  name: Moovit Stops API
  slug: moovit-stops-api
- description: Multimodal trip planning and itinerary details.
  name: Moovit TripPlan API
  slug: moovit-tripplan-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Moovit Public Transit APIs General API
  slug: open-moovit-general-api
- collection_type: open
  name: Moovit Public Transit APIs General GTFSRealtime API
  slug: open-moovit-gtfsrealtime-api
- collection_type: open
  name: Moovit Public Transit APIs General Lines API
  slug: open-moovit-lines-api
- collection_type: open
  name: Moovit Public Transit APIs General Nearby API
  slug: open-moovit-nearby-api
- collection_type: open
  name: Moovit Public Transit APIs
  slug: open-moovit-public-transit-api
- collection_type: open
  name: Moovit Public Transit APIs General RealTime API
  slug: open-moovit-realtime-api
- collection_type: open
  name: Moovit Public Transit APIs General Search API
  slug: open-moovit-search-api
- collection_type: open
  name: Moovit Public Transit APIs General ServiceAlerts API
  slug: open-moovit-servicealerts-api
- collection_type: open
  name: Moovit Public Transit APIs General Stops API
  slug: open-moovit-stops-api
- collection_type: open
  name: Moovit Public Transit APIs General TripPlan API
  slug: open-moovit-tripplan-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moovit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moovit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moovit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://moovit.com
- group: other
  title: ''
  type: ConsumerApp
  url: https://moovitapp.com
- group: start
  title: ''
  type: Portal
  url: https://moovit.com/maas-solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.moovit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.moovit.com/api-docs/5.1/MoovitPublicTransitAPIs.html
- group: other
  title: ''
  type: Developers
  url: https://moovit.com/developers/
- group: other
  title: ''
  type: ProductPage
  url: https://moovit.com/maas-solutions/transit-apis/
- group: other
  title: ''
  type: ProductPage
  url: https://moovit.com/industries/private-sector/
- group: other
  title: ''
  type: Industries
  url: https://moovit.com/industries/
- group: company
  title: ''
  type: About
  url: https://company.moovit.com/
- group: company
  title: ''
  type: Newsroom
  url: https://moovit.com/press-releases/
- group: company
  title: ''
  type: Blog
  url: https://moovit.com/blog/
- group: other
  title: ''
  type: Insights
  url: https://moovit.com/insights/
- group: company
  title: ''
  type: Careers
  url: https://moovit.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://support.moovitapp.com/hc/en-us
- group: operate
  title: ''
  type: ContactSales
  url: https://moovit.com/contact-sales/
- group: operate
  title: ''
  type: ContactSupport
  url: mailto:support@moovitapp.com
- group: operate
  title: ''
  type: ContactSupport
  url: mailto:helpdesk@moovit.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moovit.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moovit.com/legal/terms-and-conditions/
- group: other
  title: ''
  type: CookiePolicy
  url: https://moovit.com/cookies-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://moovit.com/accessibility-statement/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.mobileye.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.intel.com/
- group: operate
  title: ''
  type: PressRelease
  url: https://www.intc.com/news-events/press-releases/detail/6/intel-acquires-moovit-to-accelerate-mobileyes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Moovit
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/moovit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moovit
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/moovitapp
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/moovit/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/MoovitApp
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/app/moovit/id498477945
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=com.tranzmate
- group: other
  title: ''
  type: WikipediaPage
  url: https://en.wikipedia.org/wiki/Moovit
created: '2026-05-25'
description: Moovit is a Tel Aviv-founded urban mobility company acquired by Intel in May 2020 for approximately $900M and now part of Mobileye's Mobility-as-a- Service (MaaS) business. The Moovit consumer app provides public transit trip planning, real-time arrivals, and service alerts to more than 1.5 billion users across 3,500+ cities in 112+ countries, sourcing both official agency data and crowdsourced transit reports from its global community. Moovit's commercial offering is the Public Transit API suite — a thin, volume-metered HTTP API exposing six API families (Trip Plan, Nearby, Stops, Lines, Real-Time, Service Alerts) plus GTFS-Realtime feeds and a search API. The APIs power Microsoft (Azure Maps), Uber, Lyft, Cubic, and city/transit-agency MaaS deployments. Authentication is HMAC-SHA256 with a metro-scoped request header (USER_LOC or MOOVIT_METRO_ID). Pricing and rate limits are negotiated per customer; there is no self-service developer signup — credentials are issued by helpdesk@moovit.com.
features:
- Multimodal trip-planning API with seamless A-to-B routing across walk, transit, bike, and scooter
- Real-time arrivals with single-stop, multi-stop, and multi-stop-with-alerts batch queries
- Service alerts API (per-line, per-metro, and individual alert detail)
- Stops API — basic info, lines served, reviews, photos, and aggregated details
- Lines API — metadata, stops, shape, pattern shape, schedule, alerts, reviews, and full info
- Nearby API — locate stops, bikes, and scooters within 5km
- GTFS-Realtime feeds (vehicle/trip-updates RT, service-alerts RT, polygon-restricted RT)
- Search API for stops and lines
- HMAC-SHA256 authentication with API_KEY and nonce/timestamp signing
- Metro-scoped requests via USER_LOC (lat, lon) or MOOVIT_METRO_ID header
- Thin, low-latency response surface engineered for high-volume consumer apps
- Volume-metered commercial pricing with negotiated tiers (no self-service)
- 3,500+ cities, 112+ countries, 1.5B+ users covered by Moovit's data graph
- Crowdsourced transit data layered onto official agency feeds
- Customers include Microsoft (Azure Maps), Uber, Lyft, Cubic, and city/transit-agency MaaS deployments
- Directions Widget (web embed) and Deeplinking (mobile) integration options for non-API consumers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moovit.png
layout: provider
modified: '2026-05-25'
name: Moovit
nav: Providers
network: true
overview: 'Moovit publishes 9 APIs on the [APIs.io](https://apis.io/) network, including General API, GTFSRealtime API, Lines API, and 6 more. Tagged areas include Transit, Public Transit, Mobility, Mobility As A Service, and MaaS.


  Moovit''s developer surface includes authentication, developer portal, documentation, engineering blog, support, YouTube channel, and 31 more developer resources.'
random_paper: 74
score:
  band: thin
  composite: 28.3
  delta: -4.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moovit/refs/heads/main/screenshots/moovit-2026-06-20T185803.png
security:
- kind: authentication
  name: Moovit Authentication
  slug: moovit-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Moovit Domain Security
  slug: moovit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moovit
tags:
- Transit
- Public Transit
- Mobility
- Mobility As A Service
- MaaS
- Trip Planning
- Multimodal Routing
- Real Time
- GTFS
- GTFS Realtime
- Service Alerts
- Smart Cities
- Transportation
- Mobileye
- Intel
website: https://moovit.com
---
