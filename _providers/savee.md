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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.savee.com/v1
  baseurl_source: declared
  description: The Boards API from Savee — 3 operation(s) for boards.
  name: Savee Boards API
  slug: savee-boards-api
- baseURL: https://api.savee.com/v1
  baseurl_source: declared
  description: 'The Saves API from Savee — 4 operation(s) for saves: the user''s own saves, the home feed, a board''s saves, and single-save lookup by id or short_id.'
  name: Savee Saves API
  slug: savee-saves-api
- baseURL: https://api.savee.com/v1
  baseurl_source: declared
  description: The Search API from Savee — 1 operation(s) for search.
  name: Savee Search API
  slug: savee-search-api
- baseURL: https://api.savee.com/v1
  baseurl_source: declared
  description: The System API from Savee — 2 operation(s) for system.
  name: Savee System API
  slug: savee-system-api
- baseURL: https://api.savee.com/v1
  baseurl_source: declared
  description: The User API from Savee — 1 operation(s) for user.
  name: Savee User API
  slug: savee-user-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/savee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/savee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/savee-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/savee-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/savee-llms.txt
- group: company
  title: ''
  type: Website
  url: https://savee.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.savee.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/savee-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/savee-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/savee-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/savee-security.txt
- group: auth
  title: ''
  type: Security
  url: security/savee-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/savee-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/savee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/savee-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/savee-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/savee-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/savee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/savee-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.savee.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.savee.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.savee.com/api/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://savee.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://savee.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://savee.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://savee.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saveeit
- group: operate
  title: ''
  type: Support
  url: https://savee.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://savee.com/join
created: '2026-08-26'
description: 'Savee is a curated visual-inspiration platform for designers. Its public surface is programmatic two ways: a read-only REST API — an OpenAPI 3.1 contract of 10 GET operations and 12 schemas served live from api.savee.com/v1/openapi.json, authenticated with a personal access token or OAuth 2.1 — and an official hosted MCP server at mcp.savee.com/mcp with twelve tools (eight read, four opt-in write) behind spec-conformant OAuth 2.1 with PKCE. Both require an active Savee subscription.'
image: https://m.savee-cdn.com/img/default-og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Savee MCP Server
  slug: savee-mcp-server
modified: '2026-09-03'
name: Savee
nav: Providers
network: true
overview: 'Savee publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Boards API, Saves API, Search API, and 2 more. Tagged areas include Design, visual inspiration, Image, Creative, and Moodboards.


  Savee''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 23 more developer resources.'
plans:
- name: Savee Plans Pricing
  plan_count: 4
  slug: savee-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 10
  name: Savee Rate Limits
  slug: savee-rate-limits
scopes:
- name: Savee Scopes
  scope_count: 6
  slug: savee-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 52.5
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 57.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/savee/refs/heads/main/screenshots/savee-2026-09-02T154444.png
security:
- kind: authentication
  name: Savee Authentication
  slug: savee-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Savee Domain Security
  slug: savee-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Savee Vulnerability Disclosure
  slug: savee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: savee
tags:
- Design
- visual inspiration
- Image
- Creative
- Moodboards
- Artificial Intelligence (AI)
website: https://savee.com
---
