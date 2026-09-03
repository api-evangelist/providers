---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Stayingapi Agentic Access
  operation_count: 9
  slug: stayingapi-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: 'Hosted MCP server (Streamable HTTP, OAuth 2.1/PKCE) exposing 7 read-only tools mapping 1:1 to the REST endpoints: search_stays, check_availability, get_listing, get_price, compare_prices, get_reviews,'
  name: StayingAPI MCP Server
  slug: stayingapi-mcp-server
- description: Published portable SKILL.md agent skill in the stayingapi/travel-skills GitHub repo, referenced from the SDK docs, plus n8n workflow recipes.
  name: StayingAPI Agent Skills
  slug: stayingapi-agent-skills
- baseURL: https://api.stayingapi.com/v1
  baseurl_source: declared
  description: Account, plan and credit balance
  name: StayingAPI Account API
  slug: stayingapi-account-api
- baseURL: https://api.stayingapi.com/v1
  baseurl_source: declared
  description: Accommodation data endpoints
  name: StayingAPI Data API
  slug: stayingapi-data-api
- baseURL: https://api.stayingapi.com/v1
  baseurl_source: declared
  description: Async job polling
  name: StayingAPI Jobs API
  slug: stayingapi-jobs-api
arazzos:
- description: Confirm a listing is bookable for a date window, then get a real quote and its reviews.
  name: StayingAPI — check availability, then price the stay
  slug: stayingapi-availability-then-price
- description: Find a property, compare its price across OTAs, and read the cheapest offer.
  name: StayingAPI — cross-OTA price comparison
  slug: stayingapi-cross-ota-price-comparison
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Staying Account API
  slug: open-stayingapi-account-api
- collection_type: open
  name: Staying Data API
  slug: open-stayingapi-data-api
- collection_type: open
  name: Staying Jobs API
  slug: open-stayingapi-jobs-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stayingapi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stayingapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stayingapi-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/stayingapi-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stayingapi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stayingapi-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://stayingapi.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stayingapi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/stayingapi-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/stayingapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stayingapi-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stayingapi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stayingapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stayingapi-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stayingapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stayingapi.com
- group: operate
  title: ''
  type: Deprecation
  url: https://stayingapi.com/docs/stability
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stayingapi-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://stayingapi.com/changelog
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stayingapi-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://stayingapi.com/docs/try-it
- group: design
  title: ''
  type: Conformance
  url: conformance/stayingapi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stayingapi-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stayingapi-openapi-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stayingapi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stayingapi-plans.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stayingapi-cross-ota-price-comparison.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stayingapi-availability-then-price.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stayingapi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://stayingapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://stayingapi.com/docs/endpoints/search
- group: start
  title: ''
  type: GettingStarted
  url: https://stayingapi.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://stayingapi.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stayingapi
- group: commercial
  title: ''
  type: Pricing
  url: https://stayingapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://stayingapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://stayingapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stayingapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stayingapi.com/privacy
created: '2026-08-03'
description: Unified accommodation-data API returning live search, availability, price, cross-OTA price comparison, and normalized reviews across Airbnb, Booking.com, Vrbo, and Google Hotels via a single normalized JSON schema, so one integration covers four platforms. Delivered over a nine-operation REST API, a hosted MCP server with seven read-only tools, and a typed TypeScript SDK, all drawing on one shared credit balance. Live calls are asynchronous — a scrape returns HTTP 202 with a jobId to poll — while a deterministic stay_test_ sandbox answers synchronously at zero credits. Failed, empty and blocked calls are never billed. Launched July 2026 with a published stability policy, a locked 35-code error catalog, an llms.txt, an RFC 9727 api-catalog and fourteen installable agent skills.
image: https://stayingapi.com/icon.svg
layout: provider
mcp_servers:
- description: StayingAPI operates a first-party hosted MCP server over Streamable HTTP, authenticated with OAuth 2.1 + PKCE (S256) and dynamic client registration, drawing on the same account and the same single cr
  name: StayingAPI
  slug: stayingapi
modified: '2026-08-09'
name: StayingAPI
nav: Providers
network: true
overview: 'StayingAPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Data API, and Jobs API. Tagged areas include Travel, Hospitality, accommodation-data, hotel-api, and Vacation Rental.


  StayingAPI''s developer surface includes authentication, changelog, sandbox, developer console, documentation, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Stayingapi Plans
  plan_count: 5
  slug: stayingapi-plans
random_paper: 10
rate_limits:
- limit_count: 5
  name: Stayingapi Rate Limits
  slug: stayingapi-rate-limits
scopes:
- name: Stayingapi Scopes
  scope_count: 1
  slug: stayingapi-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 76.2
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stayingapi/refs/heads/main/screenshots/stayingapi-2026-08-17T080426.png
security:
- kind: authentication
  name: Stayingapi Authentication
  slug: stayingapi-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Stayingapi Domain Security
  slug: stayingapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stayingapi
tags:
- Travel
- Hospitality
- accommodation-data
- hotel-api
- Vacation Rental
- Short-Term Rental
- Airbnb
- Booking.com
- Vrbo
- google-hotels
- cross-ota-price-comparison
- Availability
- Reviews
- REST
- MCP
- agent-native
- OpenAPI
website: https://stayingapi.com/docs
---
