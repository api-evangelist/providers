---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 653
  human_in_the_loop: 18
  name: Tui Group Agentic Access
  operation_count: 1261
  slug: tui-group-agentic-access
  summary_line: 1261 operations · 653 acting · 18 human-in-the-loop
api_count: 21
apis:
- description: TUI's single point of access for IATA New Distribution Capability traffic, routing NDC 21.3 Shopping, Selling and Servicing messages through to Navitaire. Published operations are AirShopping, OfferPr
  name: TUI Flight NDC Gateway (Navitaire)
  slug: tui-flight-ndc-gateway
- description: JSON API onto the Navitaire New Skies passenger service system, used to create and maintain flight bookings and perform operational tasks such as retrieving flight manifests. The set of permitted oper
  name: TUI New Skies Digital API
  slug: tui-newskies-digital-api
- description: Access to Navitaire's full Departure Control System through the TUI Apigee gateway. Documented capability groups are check-in (including reverse check-in and EES validation results), baggage and bag-t
  name: TUI New Skies GoNow API
  slug: tui-newskies-gonow-api
- description: 'PCI-DSS scoped payment proxy in front of Navitaire New Skies, exposing three channels: REST Digital API payments under /rest/api/nsk/{version}/booking/payments (create, retrieve, delete, voucher, DCC/'
  name: TUI New Skies Payment API
  slug: tui-newskies-payment-api
- description: Real-time flight availability and pricing search, documented as the first step in the booking process. A single GET /search operation takes IATA station codes or ISO country codes, an outbound and opt
  name: TUI Flight Availability Search API (NSKCC)
  slug: tui-flight-availability-search-api
- description: Bulk fare-file distribution. Four GET operations — /download/{filename}, /download/{filename}/timestamp, /download/delta and /download/delta/timestamp — return base64-encoded ZIP archives of CSV price
  name: TUI New Skies PriceFile API
  slug: tui-newskies-pricefile-api
- description: REST service in the New Skies flight family described on the portal as the complete API specification for CheckInHandler Service endpoints. The published page documents the playground and production b
  name: TUI CheckInHandler Service API
  slug: tui-checkinhandler-service-api
- description: 'Distribution API for TUI fly Benelux content — the routes and destinations sold on tuifly.be, tui.nl, tuifly.ma and tuifly.fr — offered to third parties who want to resell TUI fly flights. Documented '
  name: TUI Flight OTA API
  slug: tui-flight-ota-api
- description: TUI's B2B tour-operator booking interface for travel agents, implementing the Dutch ANVR G7 standard "standard for ANVR XML-message flow" at TravelMessage version 3.1. Documented dialogues are Availab
  name: TUI TravelMessage G7 v3.1 API
  slug: tui-b2bota-g7-travelmessage
- description: Accommodation content companion to the TravelMessage G7 booking interface, described on the portal as OTA content V2.0 and delivered as JSON rather than the G7 XML. Returns the content of a particular
  name: TUI OTA Content API
  slug: tui-ota-content-api
- description: Bulk package supply feed for OTAs, delivered as XML files placed on a TUI server for SFTP download rather than over HTTP. The message is a TUI custom version 1.5.1 built on the TUI XML Supply standard
  name: TUI Supply v1.5.1
  slug: tui-supply
- description: Proxy service exposing the WallDy holiday search over Apigee X. A single POST /offers operation takes accommodation IDs and a travel window with optional party composition, board type, departure and a
  name: TUI WallDy Holiday Offers Search API (search-walldy)
  slug: tui-search-walldy-api
- description: REST service in TUI's search family, listed in the portal's Search category. The public page documents the playground and production base URLs and the x-correlation-id and versioned Accept headers; th
  name: TUI HolidayOffersController API (search-holiday-offers)
  slug: tui-holiday-offers-controller-api
- description: Metasearch partner interface onto TUI's accommodation portfolio for the Central region (Germany). Two documented operations — GET /hotel_inventory returns the hotels portfolio and POST /hotel_availabi
  name: TUI Meta Search Generics API
  slug: tui-meta-search-generic-api
- description: Metasearch partner interface for the Nordic region (Sweden, Denmark, Finland, Norway). Documented operations are GET /{market}/flights/search/{agent}, GET /{market}/flights/{agent}/route-feed, GET /{m
  name: TUI Meta Partner Packages & Flights API
  slug: tui-meta-partner-packages-flights
- description: Real-time package search for meta partners in the Nordic region, returning live pricing and availability over REST with OAuth 2.0 client credentials.
  name: TUI Partner Live Search API
  slug: tui-meta-partner-package-live-search
- description: Accommodation content for partners in the Nordic region (Sweden, Denmark, Finland, Norway), exposed as REST endpoints secured with OAuth 2.0 client credentials.
  name: TUI Partner Content API
  slug: tui-partner-content-api
- description: Cruise shopping family covering Cruise Offers Search across itineraries, date ranges and durations; Unique Cruise Offers Search for a specific itinerary; Cruise Alternate Cabin and Board Search; Cruis
  name: TUI Cruise Price and Availability API (Cruise Offers v1.0)
  slug: tui-cruise-price-and-availability
- description: Cruise booking flow for OTA partners, documented as three sequential operations — Validate Holiday (validates the booking with customer and travel details and returns the latest prices) at /cruise-ota
  name: TUI Cruise OTA Booking APIs v1.0
  slug: tui-cruise-booking-apis
- description: Returns the physical cabins available on a cruise for a given itinerary, duration, cabin type, occupancy and board, with promo code support.
  name: TUI Cruise Cabin Availability API v1.0
  slug: tui-cruise-cabin-availability
- description: GraphQL endpoint for ship reference content — cabin types, boards and deck plans — queried for specific information related to a ship. The only GraphQL surface in TUI's published catalog.
  name: TUI Ship Content API v1.0
  slug: tui-ship-content-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tui-group-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tui-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.tui.com/p/Policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tui-group-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tui-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tui-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tui-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tui-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tui-group-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tui-group-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tui-group-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tui-group-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tui-group-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tui-group-rate-limits.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tui-group-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tui-group-security.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tui-group-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tui-group-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tui-group-packages.yml
- group: design
  title: ''
  type: Components
  url: components/tui-group-components.yml
- group: build
  title: ''
  type: Postman
  url: https://developer.tui/api-catalog/flight-ndc-gateway-navitaire/postman-collection
- group: docs
  title: ''
  type: XMLSchema
  url: schemas/tui-b2bota-g7-travelmessage-v31.xsd
- group: company
  title: ''
  type: Website
  url: https://www.tuigroup.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tui/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tui/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tui/api-catalog
- group: start
  title: ''
  type: SignUp
  url: https://signup.developer.tui
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tui/docs/general/oauth2
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.tui/docs/getting-started_technical-integration
- group: other
  title: ''
  type: Environments
  url: https://developer.tui/docs/getting-started_environments
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tui/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developer.tui/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.tui/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.tui/privacy-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://vdp.tui.com/p/Policy
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.tui.com/.well-known/security.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuigroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tuigroup/
- group: other
  title: ''
  type: Email
  url: mailto:apiplatform@tui.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.tuigroup.com/en/investors
created: '2026-07-28'
description: 'TUI Group is the world''s largest integrated leisure tourism business — a vertically integrated tour operator that owns the hotels, the cruise ships, the airlines and the retail brands it sells through, serving 34.7 million customers a year across tour operators in 18 countries. The United Kingdom is its largest single source market: TUI UK & Ireland and the UK-registered carrier TUI Airways sit at the centre of the group, alongside Marella Cruises, TUI Musement and the TUI Blue, Robinson and TUI Magic Life hotel brands. The group is domiciled in Hannover, Germany and listed on the Frankfurt MDAX, having ended its London primary listing in 2023. TUI sits at the supply end of the travel distribution chain rather than the intermediation end — it is the principal that creates package holidays, not a GDS or a channel manager — and it distributes chiefly through its own retail estate and websites, supplemented by B2B feeds to travel agents, OTAs and metasearch partners. On the API
  front TUI runs a real, publicly readable developer portal at developer.tui fronted by Apigee X, with 21 documented API products covering flight shopping and booking, departure control, packages, accommodation content, cruise and metasearch distribution. The documentation is genuinely open — base URLs, endpoints, auth flows, quota tiers, downloadable Postman collections and a public OpenAPI 3.0 document for every one of the 21 products (1,261 operations in total, served from the portal''s Swagger UI) are all published without a login — but the runtime is not: every API product requires a partner-manager approval, most airline APIs additionally require a Navitaire New Skies agent profile and a production IP whitelist, and the TUI fly OTA API states plainly that step one is to conclude a contract. There is no self-serve key, no published developer terms of use (the portal''s terms page is still unfilled lorem-ipsum placeholder text), no idempotency contract on any booking or payment operation,
  no status page, no event or webhook surface, and no documented bulk-export or data-portability operation for a departing partner.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-28'
name: TUI Group
nav: Providers
network: true
overview: 'TUI Group publishes 21 APIs on the [APIs.io](https://apis.io/) network, including TUI Flight NDC Gateway (Navitaire), TUI New Skies Digital API, TUI New Skies GoNow API, and 18 more. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Tour Operator.


  TUI Group''s developer surface includes authentication, changelog, sandbox, documentation, API reference, signup flow, getting-started guide, and 34 more developer resources.'
random_paper: 60
rate_limits:
- limit_count: 6
  name: Tui Group Rate Limits
  slug: tui-group-rate-limits
scopes:
- name: Tui Group Scopes
  scope_count: 1
  slug: tui-group-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 52.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 63.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: authentication
  name: Tui Group Authentication
  slug: tui-group-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Tui Group Domain Security
  slug: tui-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tui Group Vulnerability Disclosure
  slug: tui-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tui-group
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Tour Operator
- Distribution
- NDC
- Hospitality
- Hotels
- Cruise
- Booking
- Packages
- Metasearch
website: https://www.tuigroup.com/en
---
