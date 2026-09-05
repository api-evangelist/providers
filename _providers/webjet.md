---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Webjet Agentic Access
  operation_count: 47
  slug: webjet-agentic-access
  summary_line: 47 operations · 43 acting
api_count: 17
apis:
- description: DataStream is a separately-credentialled Trip Ninja product with its own documentation section (setup, authentication, integration lifecycle) and its own public Postman collection. It uses the same To
  name: Trip Ninja DataStream API
  slug: tripninja-datastream-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Adminpanel API from Webjet — 1 operation(s) for adminpanel.
  name: Webjet Adminpanel API
  slug: webjet-adminpanel-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Book API from Webjet — 5 operation(s) for book.
  name: Webjet Book API
  slug: webjet-book-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Booking API from Webjet — 1 operation(s) for booking.
  name: Webjet Booking API
  slug: webjet-booking-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Cancel API from Webjet — 1 operation(s) for cancel.
  name: Webjet Cancel API
  slug: webjet-cancel-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Details API from Webjet — 1 operation(s) for details.
  name: Webjet Details API
  slug: webjet-details-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Generate Solutions API from Webjet — 3 operation(s) for generate solutions.
  name: Webjet Generate Solutions API
  slug: webjet-generate-solutions-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Get Searches API from Webjet — 3 operation(s) for get searches.
  name: Webjet Get Searches API
  slug: webjet-get-searches-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Msdp API from Webjet — 8 operation(s) for msdp.
  name: Webjet Msdp API
  slug: webjet-msdp-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Pre Booking API from Webjet — 1 operation(s) for pre booking.
  name: Webjet Pre Booking API
  slug: webjet-pre-booking-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Price API from Webjet — 3 operation(s) for price.
  name: Webjet Price API
  slug: webjet-price-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Queue API from Webjet — 1 operation(s) for queue.
  name: Webjet Queue API
  slug: webjet-queue-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Report API from Webjet — 4 operation(s) for report.
  name: Webjet Report API
  slug: webjet-report-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Results API from Webjet — 1 operation(s) for results.
  name: Webjet Results API
  slug: webjet-results-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Rules API from Webjet — 1 operation(s) for rules.
  name: Webjet Rules API
  slug: webjet-rules-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Search API from Webjet — 3 operation(s) for search.
  name: Webjet Search API
  slug: webjet-search-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Super Trip API from Webjet — 2 operation(s) for super trip.
  name: Webjet Super Trip API
  slug: webjet-super-trip-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Ticket API from Webjet — 1 operation(s) for ticket.
  name: Webjet Ticket API
  slug: webjet-ticket-api
- baseURL: https://sandbox.tripninja.io
  baseurl_source: declared
  description: The Ticketing API from Webjet — 1 operation(s) for ticketing.
  name: Webjet Ticketing API
  slug: webjet-ticketing-api
arazzos:
- description: The Trip Ninja reporting loop. These operations do not book or cancel anything with an airline — they report to Trip Ninja what your platform already did, which is what drives billing and the machine-
  name: Trip Ninja — report price confirmation, booking, ticketing and cancellation
  slug: webjet-tripninja-report-and-cancel
- description: End-to-end flight retailing against the Trip Ninja surface published in Trip Ninja's own GitHub documentation repository (https://github.com/trip-ninja-inc/trip_ninja_api_docs, last updated 2023-12-14
  name: Trip Ninja — search, confirm price, book and ticket
  slug: webjet-tripninja-search-price-book-ticket
artifact_total: 39
collections:
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-adminpanel-refresh-token
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-farestructure-generate-solutions
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-farestructure-get-searches
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-farestructure-report-book
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-farestructure-report-cancel
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-hotels
- collection_type: open
  name: Trip Ninja Endpoint Documentation
  slug: open-webjet-tripninja-pricing-booking
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-smartflights-generate-solutions
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-smartflights-get-searches
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-smartflights-report-book
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-smartflights-report-cancel
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-v2-booking
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-virtual-interlining-generate-solutions
- collection_type: open
  name: Trip Ninja API Documentation
  slug: open-webjet-tripninja-virtual-interlining-get-searches
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/webjet-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/trip-ninja-inc/trip_ninja_api_docs/issues
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-smartflights-get-searches-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-smartflights-generate-solutions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-smartflights-report-book-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-smartflights-report-cancel-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/webjet-tripninja-search-and-construct.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/webjet-tripninja-report-booking-and-cancellation.md
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-adminpanel-refresh-token-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/webjet-tripninja-rotate-access-token.md
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-farestructure-get-searches-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-farestructure-generate-solutions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-farestructure-report-book-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-farestructure-report-cancel-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-virtual-interlining-get-searches-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-virtual-interlining-generate-solutions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-flights-core-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-pricing-booking-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/webjet-tripninja-price-book-and-ticket.md
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-hotels-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-msdp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-v2-core-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/webjet-v2-booking-overlay.yaml
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
  type: X-MCPServerCandidate
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
layout: provider
modified: '2026-07-28'
name: Webjet
nav: Providers
network: true
overview: 'Webjet publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Trip Ninja DataStream API, Adminpanel API, Book API, and 16 more. Tagged areas include Travel, Australia, OTA, Aviation, and Booking.


  Webjet''s developer surface includes authentication, sandbox, API reference, getting-started guide, pricing, engineering blog, documentation, and 55 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 1
  name: Webjet Rate Limits
  slug: webjet-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 32.7
    discoverability: 55.6
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/webjet/refs/heads/main/screenshots/webjet-2026-08-17T082854.png
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
