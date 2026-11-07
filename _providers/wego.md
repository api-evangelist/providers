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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.4
  scored_at: '2026-11-06'
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
artifact_total: 21
common:
- group: auth
  href: https://artifacts.apis.io/wego/security/wego-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wego-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/wego/security/wego-domain-security.yml
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
  href: https://artifacts.apis.io/wego/llms/wego-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wego-llms.txt
- group: agent
  href: https://artifacts.apis.io/wego/well-known/wego-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wego-well-known.yml
- group: build
  href: https://artifacts.apis.io/wego/packages/wego-packages.yml
  title: ''
  type: Packages
  url: packages/wego-packages.yml
- group: build
  href: https://artifacts.apis.io/wego/packages/wego-packages.yml
  title: ''
  type: SDKs
  url: packages/wego-packages.yml
- group: build
  href: https://artifacts.apis.io/wego/cli/wego-cli.yml
  title: ''
  type: CLI
  url: cli/wego-cli.yml
- group: design
  href: https://artifacts.apis.io/wego/conventions/wego-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wego-conventions.yml
- group: design
  href: https://artifacts.apis.io/wego/lifecycle/wego-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wego-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wego/conformance/wego-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wego-conformance.yml
- group: start
  href: https://artifacts.apis.io/wego/sandbox/wego-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/wego-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/wego/plans/wego-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wego-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wego/rate-limits/wego-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wego-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/wego/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/wego/conformance/wego-conformance.yml
  title: ''
  type: Compliance
  url: conformance/wego-conformance.yml
- group: auth
  href: https://artifacts.apis.io/wego/authentication/wego-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wego-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wego/scopes/wego-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wego-scopes.yml
- group: design
  href: https://artifacts.apis.io/wego/errors/wego-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wego-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wego/data-model/wego-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wego-data-model.yml
- group: build
  href: https://artifacts.apis.io/wego/mcp/wego-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wego-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/wego/overlays/wego-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wego-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/wego/mcp/wego-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wego-mcp.yml
created: '2026-09-04'
description: 'Wego (Wego Pte Ltd, Singapore, with a regional base in Dubai) is a travel metasearch engine and online travel agency serving travelers across the Middle East, North Africa, Southeast Asia and beyond. It compares flights and hotels across airlines, hotels and online travel agencies, and sells Book-on-Wego inventory directly. Wego exposes that same search core through four public API surfaces: the OAuth2-protected Wego API (an agent-native REST contract over places, flights, hotels, fares and rates, published as OpenAPI 3.1 at api.wego.com/openapi, plus a remote MCP server, a wego CLI and a published Agent Skill), a Marketplace/Affiliate metasearch API for partners who embed Wego comparison into their own sites, and Flight and Hotel B2B Distribution APIs for partners syndicating Book-on-Wego inventory.'
finops:
- has_sources: true
  method: derived
  name: Wego Finops
  primary_unit: ''
  service_category: ''
  slug: wego-finops
  template: true
image: https://avatars.githubusercontent.com/u/69198?v=4
layout: provider
mcp_servers:
- description: Wego runs a first-party remote MCP server at https://api.wego.com/mcp. It is the "Wego connector" listed in the Claude connectors directory, and it projects the same flight/hotel/place funnel the REST
  name: Wego MCP server
  slug: wego-mcp-server
modified: '2026-09-04'
name: Wego
nav: Providers
network: true
overview: 'Wego publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Countries API, Feedback API, Flights API, and 7 more. Tagged areas include Company, Travel, Flights, Hotels, and Metasearch.


  The Wego catalog on APIs.io includes 1 Spectral governance ruleset.


  Wego''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, sandbox, and 26 more developer resources.'
plans:
- name: Wego Plans Pricing
  plan_count: 0
  slug: wego-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Wego Rate Limits
  slug: wego-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Wego API Rules
  rule_count: 67
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 7
  slug: wego-rules
scopes:
- name: Wego Scopes
  scope_count: 3
  slug: wego-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 49.2
    developer_ergonomics: 85.7
    discoverability: 75.0
    operational_transparency: 34.2
  previous_composite: 54.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wego/wego-2026-10-11T194316.png
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
skill_count: 2
skills:
- name: wego-setup
  slug: wego-agent-onboarding
- name: wego
  slug: wego-travel-skill
slug: wego
tags:
- Company
- Travel
- Flights
- Hotels
- Metasearch
- Booking
- Agent-Native
- Tourism
- Search
website: https://www.wego.com/
---
