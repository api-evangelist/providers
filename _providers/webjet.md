---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Webjet Agentic Access
  operation_count: 47
  slug: webjet-agentic-access
  summary_line: 47 operations · 43 acting
api_count: 10
apis:
- description: SmartFlights is Trip Ninja's current (v3) flight-construction API. A travel platform posts a traveller search to /v3/get-searches/, Trip Ninja returns the set of optimised content queries to run again
  name: Trip Ninja SmartFlights API
  slug: tripninja-smartflights-api
- description: The single documented Admin Panel operation, POST /adminpanel/refresh-token/, exchanges a refresh token for a new access token. Access tokens expire 90 days after issue; refresh tokens have an indefin
  name: Trip Ninja Admin Panel API
  slug: tripninja-admin-panel-api
- description: FareStructure is the deprecated v2 predecessor to SmartFlights, still published under devhub.tripninja.io/deprecated/farestructure/. It automates split ticketing across multiple content sources to bui
  name: Trip Ninja FareStructure API (deprecated)
  slug: tripninja-farestructure-api
- description: Virtual Interlining is the deprecated v2 product that combines segments from carriers with no interline agreement into a single sellable itinerary, published under devhub.tripninja.io/deprecated/virtu
  name: Trip Ninja Virtual Interlining API (deprecated)
  slug: tripninja-virtual-interlining-api
- description: DataStream is a separately-credentialled Trip Ninja product with its own documentation section (setup, authentication, integration lifecycle) and its own public Postman collection. It uses the same To
  name: Trip Ninja DataStream API
  slug: tripninja-datastream-api
- description: A flight search and reporting surface published by Trip Ninja in its own public GitHub documentation repository (github.com/trip-ninja-inc/trip_ninja_api_docs) rather than on the developer hub. Five o
  name: Trip Ninja Flights Core API
  slug: tripninja-flights-core-api
- description: The fullest Trip Ninja transaction surface, published in Trip Ninja's public GitHub documentation repository. Seven operations with real operationIds — PriceConfirm (POST /price/{endpoint}/), CreateBo
  name: Trip Ninja Pricing & Booking API
  slug: tripninja-pricing-booking-api
- description: A hotel shopping surface — Search (POST /search/hotels/{endpoint}), Details (POST /details/hotels/{endpoint}/), Rules (POST /rules/hotels/{endpoint}/) and PriceConfirm plus a price-confirmation remova
  name: Trip Ninja Hotels API
  slug: tripninja-hotels-api
- description: 'MSDP is Trip Ninja''s multi-source dynamic packaging product — flights and hotels combined into one sellable package. Nine operations with real operationIds: MSDPSearch, MSDPGetFlightResults, MSDPGetHo'
  name: Trip Ninja MSDP (Dynamic Packaging) API
  slug: tripninja-msdp-api
- description: Two further GitHub-published OpenAPI 3.0.0 documents describing the 2.0.0-era surface — a core document (/get-searches/, /generate-solutions/) and a booking document (Search, PriceConfirm, CreateBooki
  name: Trip Ninja v2 Legacy API
  slug: tripninja-v2-legacy-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: The Trip Ninja reporting loop. These operations do not book or cancel anything with an airline — they report to Trip Ninja what your platform already did, which is what drives billing and the machine-
  name: Trip Ninja — report price confirmation, booking, ticketing and cancellation
  slug: webjet-tripninja-report-and-cancel
- description: End-to-end flight retailing against the Trip Ninja surface published in Trip Ninja's own GitHub documentation repository (https://github.com/trip-ninja-inc/trip_ninja_api_docs, last updated 2023-12-14
  name: Trip Ninja — search, confirm price, book and ticket
  slug: webjet-tripninja-search-price-book-ticket
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/webjet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webjet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/webjet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/webjet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/webjet-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/webjet-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/webjet-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/webjet-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/webjet-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/webjet-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/webjet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/webjet-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/webjet-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/webjet-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/webjet-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/webjet-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devhub.tripninja.io/
- group: docs
  title: ''
  type: APIReference
  url: https://devhub.tripninja.io/smartflights/get-searches/
- group: start
  title: ''
  type: GettingStarted
  url: https://devhub.tripninja.io/sdk/quick-start-guide/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tripninjadevteam/trip-ninja-public/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tripninja.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.tripninja.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trip-ninja-inc
- group: company
  title: ''
  type: Blog
  url: https://www.tripninja.io/blog
- group: company
  title: ''
  type: Website
  url: https://www.webjetgroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devhub.tripninja.io/
- group: start
  title: ''
  type: Portal
  url: https://app.tripninja.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Webjet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/webjet-group
- group: company
  title: ''
  type: Blog
  url: https://www.webjetgroup.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tripninja.io/legal/qt-tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tripninja.io/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.tripninja.io/legal/gdpr
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.tripninja.io/legal/data-processing
- group: operate
  title: ''
  type: Support
  url: https://www.tripninja.io/contact
- group: company
  title: ''
  type: Website
  url: https://www.tripninja.io/
- group: company
  title: ''
  type: Website
  url: https://www.motorhomerepublic.com/
- group: company
  title: ''
  type: Website
  url: https://www.airportrentals.com/
created: '2026-07-28'
description: 'Webjet Group Limited (ASX: WJL) is the Australian consumer travel company created when Webjet Limited demerged in September 2024 — the B2C half, while the B2B WebBeds bed bank went to Web Travel Group (ASX: WEB). It operates Webjet OTA (webjet.com.au / webjet.co.nz), which the company describes as the number one online travel agency position in Australia and New Zealand; the GoSee vehicle-rental brands Airport Rentals and Motorhome Republic; and Trip Ninja, a travel-technology business selling flight-construction software to other travel platforms. Webjet sits downstream of airline distribution — it resells airline content sourced through GDS and NDC connections rather than owning inventory, and holds ATIA/ATAS accreditation A17325 with an IATA accredited agent entity (Webjet Marketing). Its API posture is honestly lopsided: the consumer brands publish no developer documentation and no public API at all (developer/api/docs subdomains do not resolve; www.webjet.com.au returns
  403 to non-browser clients), while the group''s only public API surface is Trip Ninja''s: the SmartFlights developer hub at devhub.tripninja.io, with eleven OpenAPI 3.0.0 documents rendered in-page, plus six further OpenAPI 3.0.0 documents published in Trip Ninja''s own GitHub organisation (trip-ninja-inc/trip_ninja_api_docs) covering flights core, pricing/booking/ ticketing, hotels, MSDP dynamic packaging and the v2 legacy surface. Seventeen specifications in all, and two Apache-2.0 client libraries on PyPI and NuGet. Docs are freely readable but access is zero self-serve: production use requires a commercial agreement, Trip Ninja-issued admin panel credentials, IP allow-listing and a certification pass, every API host returns 403 to a non-allow-listed IP, and no data-export operation is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: webjet-mcp.yml
  slug: webjet-mcpyml
modified: '2026-07-28'
name: Webjet
nav: Providers
network: true
overview: 'Webjet publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Trip Ninja SmartFlights API, Trip Ninja Admin Panel API, Trip Ninja FareStructure API (deprecated), and 7 more. Tagged areas include Travel, Australia, OTA, Aviation, and Booking.


  Webjet''s developer surface includes authentication, sandbox, API reference, getting-started guide, pricing, engineering blog, documentation, and 32 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 0
  name: Webjet Rate Limits
  slug: webjet-rate-limits
score:
  band: developing
  composite: 47.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 47.8
    developer_ergonomics: 73.4
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: authentication
  name: Webjet Authentication
  slug: webjet-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Webjet Domain Security
  slug: webjet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: webjet
tags:
- Travel
- Australia
- OTA
- Aviation
- Booking
- Distribution
- Flight Search
- Car Rental
- New Zealand
- Travel Technology
website: https://www.webjetgroup.com/
---
