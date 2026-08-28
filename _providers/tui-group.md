---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 653
  human_in_the_loop: 18
  name: Tui Group Agentic Access
  operation_count: 1261
  slug: tui-group-agentic-access
  summary_line: 1261 operations · 653 acting · 18 human-in-the-loop
api_count: 21
apis:
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
- description: Accommodation content companion to the TravelMessage G7 booking interface, described on the portal as OTA content V2.0 and delivered as JSON rather than the G7 XML. Returns the content of a particular
  name: TUI OTA Content API
  slug: tui-ota-content-api
- description: Proxy service exposing the WallDy holiday search over Apigee X. A single POST /offers operation takes accommodation IDs and a travel window with optional party composition, board type, departure and a
  name: TUI WallDy Holiday Offers Search API (search-walldy)
  slug: tui-search-walldy-api
- description: REST service in TUI's search family, listed in the portal's Search category. The public page documents the playground and production base URLs and the x-correlation-id and versioned Accept headers; th
  name: TUI HolidayOffersController API (search-holiday-offers)
  slug: tui-holiday-offers-controller-api
- description: Metasearch partner interface onto TUI's accommodation portfolio for the Central region (Germany). Two documented operations — GET /hotel_inventory returns the hotels portfolio and POST /hotel_availabi
  name: TUI Meta Search Generics API
  slug: tui-meta-search-generic-api
- description: Accommodation content for partners in the Nordic region (Sweden, Denmark, Finland, Norway), exposed as REST endpoints secured with OAuth 2.0 client credentials.
  name: TUI Partner Content API
  slug: tui-partner-content-api
- description: GraphQL endpoint for ship reference content — cabin types, boards and deck plans — queried for specific information related to a ship. The only GraphQL surface in TUI's published catalog.
  name: TUI Ship Content API v1.0
  slug: tui-ship-content-api
- description: TUI Group TravelMessage.v31 from TUI Group — 10 path(s) described in OpenAPI.
  name: TUI Group TravelMessage.v31
  slug: tui-group-tui-b2bota-g7-travelmessage-openapi
- description: TUI Group TUI Cruise Booking APIs from TUI Group — 2 path(s) described in OpenAPI.
  name: TUI Group TUI Cruise Booking APIs
  slug: tui-group-tui-cruise-booking-apis-openapi
- description: TUI Group Cruise Cabin Availability from TUI Group — 1 path(s) described in OpenAPI.
  name: TUI Group Cruise Cabin Availability
  slug: tui-group-tui-cruise-cabin-availability-openapi
- description: TUI Group TUI Cruise Price and Availability. from TUI Group — 6 path(s) described in OpenAPI.
  name: TUI Group TUI Cruise Price and Availability.
  slug: tui-group-tui-cruise-price-and-availability-openapi
- description: TUI Group Flight-ndc-gateway-navitaire from TUI Group — 26 path(s) described in OpenAPI.
  name: TUI Group Flight-ndc-gateway-navitaire
  slug: tui-group-tui-flight-ndc-gateway-openapi
- description: TUI Group Meta Partner Package Live Search from TUI Group — 3 path(s) described in OpenAPI.
  name: TUI Group Meta Partner Package Live Search
  slug: tui-group-tui-meta-partner-package-live-search-openapi
- description: TUI Group Meta Partner Packages & Flights from TUI Group — 5 path(s) described in OpenAPI.
  name: TUI Group Meta Partner Packages & Flights
  slug: tui-group-tui-meta-partner-packages-flights-openapi
- description: TUI Group Supply from TUI Group — 1 path(s) described in OpenAPI.
  name: TUI Group Supply
  slug: tui-group-tui-supply-openapi
artifact_total: 48
collections:
- collection_type: open
  name: TravelMessage.v31
  slug: open-tui-group-tui-b2bota-g7-travelmessage
- collection_type: open
  name: CheckInHandler Service API
  slug: open-tui-group-tui-checkinhandler-service-api
- collection_type: open
  name: TUI Cruise Booking APIs
  slug: open-tui-group-tui-cruise-booking-apis
- collection_type: open
  name: Cruise Cabin Availability
  slug: open-tui-group-tui-cruise-cabin-availability
- collection_type: open
  name: TUI Cruise Price and Availability.
  slug: open-tui-group-tui-cruise-price-and-availability
- collection_type: open
  name: NSKCC Availability Search API
  slug: open-tui-group-tui-flight-availability-search-api
- collection_type: open
  name: flight-ndc-gateway-navitaire
  slug: open-tui-group-tui-flight-ndc-gateway
- collection_type: open
  name: HolidayOffersController API
  slug: open-tui-group-tui-holiday-offers-controller-api
- collection_type: open
  name: Meta Partner Package Live Search
  slug: open-tui-group-tui-meta-partner-package-live-search
- collection_type: open
  name: Meta Partner Packages & Flights
  slug: open-tui-group-tui-meta-partner-packages-flights
- collection_type: open
  name: Meta-Search-Generic API
  slug: open-tui-group-tui-meta-search-generic-api
- collection_type: open
  name: NewSkies-Digital-Api
  slug: open-tui-group-tui-newskies-digital-api
- collection_type: open
  name: NewSkies-GoNow-Api
  slug: open-tui-group-tui-newskies-gonow-api
- collection_type: open
  name: NewSkies Payment API
  slug: open-tui-group-tui-newskies-payment-api
- collection_type: open
  name: TUI NewSkies PriceFile Api
  slug: open-tui-group-tui-newskies-pricefile-api
- collection_type: open
  name: OTA Content API
  slug: open-tui-group-tui-ota-content-api
- collection_type: open
  name: Partner Content API
  slug: open-tui-group-tui-partner-content-api
- collection_type: open
  name: WallDy API
  slug: open-tui-group-tui-search-walldy-api
- collection_type: open
  name: Ship Content API
  slug: open-tui-group-tui-ship-content-api
- collection_type: open
  name: Supply
  slug: open-tui-group-tui-supply
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tui-group-mcp.yml
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
layout: provider
mcp_servers:
- description: ''
  name: TUI Group MCP Server
  slug: tui-group-mcp-server
modified: '2026-07-28'
name: TUI Group
nav: Providers
network: true
overview: 'TUI Group publishes 21 APIs on the [APIs.io](https://apis.io/) network, including TUI New Skies Digital API, TUI New Skies GoNow API, TUI New Skies Payment API, and 18 more. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Tour Operator.


  TUI Group''s developer surface includes authentication, changelog, sandbox, documentation, API reference, signup flow, getting-started guide, and 35 more developer resources.'
random_paper: 16
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
  composite: 51.6
  delta: -0.3
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 30.3
    contract_quality: 51.1
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 60.5
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tui-group/refs/heads/main/screenshots/tui-group-2026-08-17T082459.png
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
