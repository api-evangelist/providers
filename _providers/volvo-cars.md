---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Receive vehicle data and send commands to the vehicle. Vehicle data covers status, diagnostics, statistics, and metadata — including odometer, fuel amount, tyre pressures, brake status, engine status,
  name: Volvo Cars Connected Vehicle API
  slug: volvo-cars-connected-vehicle-api
- description: Access the most recent energy state of a BEV or PHEV — battery charge level, target battery charge level, charging connection status, charging system status, charging type, charging power, charger pow
  name: Volvo Cars Energy API
  slug: volvo-cars-energy-api
- description: Retrieve detailed information on a vehicle's current location. Designed for interactive applications that need to know where a consenting driver's Volvo is right now. Same regional availability and ra
  name: Volvo Cars Location API
  slug: volvo-cars-location-api
- description: 'API for managing wallboxes, charging sessions, and user ID tokens — the device-side counterpart to the vehicle-side Energy API. Enables integrations that pair a home charger or public charging device '
  name: Volvo Cars Energy Device API
  slug: volvo-cars-energy-device-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volvo-cars-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.volvocars.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.volvocars.com/apis/docs/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/apis/docs/authorisation/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/apis/docs/test-access-tokens/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/apis/docs/observability/
- group: company
  title: ''
  type: Blog
  url: https://developer.volvocars.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.volvocars.com/terms-and-conditions/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.volvocars.com/terms-and-conditions/apis-terms-and-conditions/
- group: other
  title: ''
  type: Regions
  url: https://developer.volvocars.com/terms-and-conditions/apis-supported-locations/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.volvocars.com/cookies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.volvocars.com/intl/legal/privacy/customer-privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/open-source/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volvo-cars
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/volvo-cars/developer-portal-api-samples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/volvo-cars/developer-portal-api-samples/tree/main/oauth2-code-flow-sample
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/volvo-cars/automotive-media-sample
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/volvo-cars/web-platform-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/volvo-cars/sample-android-automotive-wearable-monitoring
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/in-car-apps/
- group: build
  title: ''
  type: Tools
  url: https://developer.volvocars.com/in-car-apps/android-emulator-xc40/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.android.com/cars
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/3d/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.volvocars.com/resources/
- group: operate
  title: ''
  type: Support
  url: mailto:developer.portal@volvocars.com
- group: operate
  title: ''
  type: Support
  url: mailto:opensource@volvocars.com
- group: other
  title: ''
  type: CaseStudies
  url: https://magicmirror.builders/
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: other
  title: ''
  type: Regions
  url: ''
created: '2026-05-25T00:00:00.000Z'
description: Volvo Cars is a Swedish premium automotive OEM (headquartered in Gothenburg, owned by Geely) that operates the Volvo Cars Developer Portal as the public face of its connected-vehicle platform. The portal exposes the Connected Vehicle API, Energy API, Energy Device API, and Location API for third-party developers to build applications around real Volvo cars equipped with Volvo On Call or Google Built-In. APIs use OAuth 2.0 against Volvo ID with explicit owner consent, a VCC-API-Key client identifier, and a free tier capped at 10,000 calls per day per app. The portal also covers Android Automotive in-car app development with an official XC40 Recharge emulator, 3D assets and simulator resources, and an active open-source program at github.com/volvo-cars.
features:
- Connected Vehicle API v2 — read vehicle status, diagnostics, statistics, and metadata, and send commands (lock/unlock, climate start/stop, flash lights, sound horn, engine start/stop) backed by a public OpenAPI specification.
- Energy API v2 — latest energy state for BEV and PHEV models, including battery level, charging status, charging power, estimated charging time, and electric range, plus a capabilities endpoint.
- Energy Device API v1 — wallbox, charging session, and user-ID-token management for the device side of charging.
- Location API v1 — current vehicle location for interactive applications.
- OAuth 2.0 authorization-code flow against Volvo ID with explicit per-vehicle owner consent.
- VCC-API-Key client identifier required on every request alongside the OAuth bearer token.
- Public OpenAPI specifications downloadable per API, plus an in-portal sandbox using a demo Volvo ID account.
- Rate limits exposed and documented (100 rpm per user/app, 10 rpm for commands, 10,000 calls/day per app).
- Manual app-publishing review (14-21 days) to grant production credentials, reflecting Volvo Cars' explicit privacy and safety stance.
- Open-source code samples (Node.js OAuth2 code flow, Connected Vehicle data fetch) on the Volvo Cars GitHub organization.
- In-car app development on Android Automotive OS, with an official Volvo XC40 Recharge emulator and Android-for-Cars tooling.
- 3D assets and a Volvo simulator surface for digital and immersive product experiences.
- Open Source Program Office and an active GitHub organization (developer-portal-api-samples, automotive-media-sample, web-platform-examples, and more).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/volvo-cars.png
layout: provider
modified: '2026-05-25'
name: Volvo Cars
nav: Providers
network: true
overview: 'Volvo Cars publishes 3 APIs on the [APIs.io](https://apis.io/) network: Connected Vehicle API, Energy API, and Location API. Tagged areas include Automotive, Connected Vehicle, Electric Vehicles, Telematics, and Android Automotive.


  Volvo Cars'' developer surface includes developer portal, documentation, getting-started guide, engineering blog, code examples, tooling, support, and 21 more developer resources.'
random_paper: 64
score:
  band: thin
  composite: 28.6
  delta: -3.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 32.3
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/volvo-cars/refs/heads/main/screenshots/volvo-cars-2026-06-20T201139.png
security:
- kind: domain-security
  name: Volvo Cars Domain Security
  slug: volvo-cars-domain-security
  summary_line: TLSv1.3 · DMARC
slug: volvo-cars
tags:
- Automotive
- Connected Vehicle
- Electric Vehicles
- Telematics
- Android Automotive
- OEM
- Mobility
website: https://developer.volvocars.com/
---
