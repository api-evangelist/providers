---
agent_readiness:
  band: agent-ready
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-09-04'
api_count: 4
apis:
- baseURL: https://api.wego.com
  baseurl_source: declared
  description: 'The public Wego API: resolve travel locations, create asynchronous flight and hotel searches, read ranked results, open one trip or hotel, list fares and room rates, and build wego.com booking or shar'
  name: Wego API
  slug: wego-api
- description: 'The affiliate metasearch API: partners add Wego flight and hotel comparison to their own site or app. Client-credentials OAuth2, create a search, poll for results, then hand travelers off to Wego part'
  name: Wego Marketplace (Affiliate) API
  slug: wego-affiliate
- description: B2B distribution API for partners to search and retrieve available flight prices and itineraries from Wego inventory. OAuth2 client-credentials with a flight.search scope; staging access is IP-whiteli
  name: Wego Flight B2B Distribution API v3
  slug: wego-distribution-flight
- description: B2B distribution API for partners to pull static property content, price hotel rates for search criteria, and complete the full booking flow (price-check, book, cancel, retrieve). OAuth2 client-creden
  name: Wego Hotel B2B Distribution API
  slug: wego-distribution-hotel
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/wego-trust-center.yml
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/wego-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wego-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/wego-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wego-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/wego-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wego-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wego-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wego-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wego-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wego-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wego-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/wego-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wego-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wego-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wego-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wego-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/wego-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wego-api-overlay.yaml
- group: agent
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
overview: 'Wego publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Flights, Hotels, and Metasearch.


  Wego''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, sandbox, and 26 more developer resources.'
plans:
- name: Wego Plans Pricing
  plan_count: 0
  slug: wego-plans-pricing
random_paper: 14
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
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 51.6
    developer_ergonomics: 85.7
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Agent Native
- Tourism
- Search
website: https://www.wego.com/
---
