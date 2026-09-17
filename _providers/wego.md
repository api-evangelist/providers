---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'The affiliate metasearch API: partners add Wego flight and hotel comparison to their own site or app. Client-credentials OAuth2, create a search, poll for results, then hand travelers off to Wego part'
  name: Wego Marketplace (Affiliate) API
  slug: wego-affiliate
- description: B2B distribution API for partners to search and retrieve available flight prices and itineraries from Wego inventory. OAuth2 client-credentials with a flight.search scope; staging access is IP-whiteli
  name: Wego Flight B2B Distribution API v3
  slug: wego-distribution-flight
- description: B2B distribution API for partners to pull static property content, price hotel rates for search criteria, and complete the full booking flow (price-check, book, cancel, retrieve). OAuth2 client-creden
  name: Wego Hotel B2B Distribution API
  slug: wego-distribution-hotel
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: Country-keyed reference data an agent can call before any search, and combine. `getCountryHolidays` returns a market's public holidays for spotting long weekends; `getVisaFreeDestinations` returns whe
  name: Wego Countries API
  slug: wego-countries-api
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: 'Send feedback about the Wego CLI/API experience. `submitFeedback` records an optional category plus at least one of a rating (1-5) or a free-text message (the CLI''s `wego feedback`); a category alone '
  name: Wego Feedback API
  slug: wego-feedback-api
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: 'The flight funnel: `createFlightSearch` starts an async search, `getFlightSearchResults` reads ranked snapshots while providers answer, `getFlightTrip` opens one trip with every fare. Fares with `kind'
  name: Wego Flights API
  slug: wego-flights-api
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: The Health API from Wego — 1 operation(s) for health.
  name: Wego Health API
  slug: wego-health-api
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: 'The hotel funnel, same shape as flights: `createHotelSearch`, `getHotelSearchResults` for ranked hotels, `getHotel` for static detail, `getHotelRates` for bookable rooms and rates (cheapest first, wit'
  name: Wego Hotels API
  slug: wego-hotels-api
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: Turn free text into typed travel locations. `getPlaces` resolves a city, airport, district or hotel name to results carrying the codes the flight and hotel searches take as input. `getNearbyPlaces` an
  name: Wego Places API
  slug: wego-places-api
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: The authenticated caller. `getCurrentUser` returns the identity behind the bearer token (the CLI's `wego whoami`).
  name: Wego User API
  slug: wego-user-api
artifact_total: 17
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/security/wego-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wego-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/security/wego-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wego-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wego.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wego.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wego.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wego.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.wego.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.wego.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wego
- group: commercial
  title: ''
  type: TermsOfService
  url: https://company.wego.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://company.wego.com/data-privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.wego.com/login
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/llms/wego-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wego-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/well-known/wego-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wego-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/packages/wego-packages.yml
  title: ''
  type: Packages
  url: packages/wego-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/packages/wego-packages.yml
  title: ''
  type: SDKs
  url: packages/wego-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/cli/wego-cli.yml
  title: ''
  type: CLI
  url: cli/wego-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/conventions/wego-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wego-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/lifecycle/wego-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wego-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/conformance/wego-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wego-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/sandbox/wego-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/wego-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/plans/wego-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wego-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/rate-limits/wego-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wego-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/conformance/wego-conformance.yml
  title: ''
  type: Compliance
  url: conformance/wego-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/authentication/wego-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wego-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/scopes/wego-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wego-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/errors/wego-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wego-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/data-model/wego-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wego-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/mcp/wego-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wego-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/overlays/wego-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wego-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wego/refs/heads/main/mcp/wego-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wego-mcp.yml
created: '2026-09-04'
description: 'Wego (Wego Pte Ltd, Singapore, with a regional base in Dubai) is a travel metasearch engine and online travel agency serving travelers across the Middle East, North Africa, Southeast Asia and beyond. It compares flights and hotels across airlines, hotels and online travel agencies, and sells Book-on-Wego inventory directly. Wego exposes that same search core through four public API surfaces: the OAuth2-protected Wego API (an agent-native REST contract over places, flights, hotels, fares and rates, published as OpenAPI 3.1 at api.wego.com/openapi, plus a remote MCP server, a wego CLI and a published Agent Skill), a Marketplace/Affiliate metasearch API for partners who embed Wego comparison into their own sites, and Flight and Hotel B2B Distribution APIs for partners syndicating Book-on-Wego inventory.'
image: https://avatars.githubusercontent.com/u/69198?v=4
layout: provider
mcp_servers:
- description: ''
  name: Wego MCP server
  slug: wego-mcp-server
modified: '2026-09-04'
name: Wego
nav: Providers
network: true
overview: 'Wego publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Countries API, Feedback API, Flights API, and 4 more. Tagged areas include Company, Travel, Flights, Hotels, and Metasearch.


  Wego''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, sandbox, and 26 more developer resources.'
plans:
- name: Wego Plans Pricing
  plan_count: 0
  slug: wego-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Wego Rate Limits
  slug: wego-rate-limits
scopes:
- name: Wego Scopes
  scope_count: 3
  slug: wego-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 54.6
    developer_ergonomics: 76.2
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 50.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Wego Authentication
  slug: wego-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Wego Domain Security
  slug: wego-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wego Trust Center
  slug: wego-trust-center
  summary_line: GDPR
slug: wego
tags:
- Company
- Travel
- Flights
- Hotels
- Metasearch
- Booking
- agent-native
- Tourism
- Search
website: https://www.wego.com/
---
