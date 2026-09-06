---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Cubby Operator API is a JSON HTTP API — explicitly not RESTful — oriented around actions performed on system entities rather than transfer of state. Roughly 70 POST endpoints cover access codes, l
  name: Cubby Operator API
  slug: cubby-operator-api
- description: The Cubby Storefront API is the public, unauthenticated-tenant-facing slice of the Cubby platform used to power online rental storefronts — facility search and pricing-group search — and is the same A
  name: Cubby Storefront API
  slug: cubby-storefront-api
- description: 'Cubby operates a hosted Model Context Protocol server at api.cubbystorage.com/mcp. The endpoint is live and OAuth-protected: an unauthenticated JSON-RPC tools/list call returns HTTP 401 with a WWW-Aut'
  name: Cubby MCP Server
  slug: cubby-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Cubby Webhooks
  slug: cubby-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cubby-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cubbystorage.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cubbystorage.github.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://cubbystorage.github.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cubbystorage.github.io/docs/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cubbystorage
- group: company
  title: ''
  type: Blog
  url: https://www.cubbystorage.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.cubbystorage.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.cubbystorage.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cubbystorage.com/api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cubbystorage.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cubby-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cubby-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cubby-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cubby-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cubby-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cubby-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cubby-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cubby-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cubby-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cubby-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/cubby-decline-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cubby-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cubby-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cubby-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cubby-packages.yml
- group: design
  title: ''
  type: Components
  url: components/cubby-components.yml
- group: build
  title: ''
  type: Examples
  url: examples/cubby-examples.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cubby-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cubby-rate-limits.yml
created: '2026-08-11'
description: Cubby is a New York City based software company building an AI-native facility management platform for self-storage operators, replacing legacy FMS systems with facility operations, tenant management, revenue management, e-commerce storefronts, embedded payment processing and AI-driven tenant communications. Cubby publishes a public developer documentation site covering a JSON HTTP Operator API of roughly 70 action-oriented endpoints across facilities, units, leases, customers, leads, payments, coverage, auctions and reporting, a BigQuery analytics data warehouse, Make.com outbound webhooks, embeddable Lit storefront web components, and an OAuth-protected Model Context Protocol server. The company was founded in 2022 by Matt Engfer and Adam Fleming and raised a $63M Series A led by Growth Equity at Goldman Sachs Alternatives in January 2026.
image: https://www.cubbystorage.com/og-logo.png
layout: provider
mcp_servers:
- description: Cubby operates a hosted, remote Model Context Protocol server on its production API host. The endpoint is live and OAuth-protected. An anonymous JSON-RPC tools/list call returns HTTP 401 with a WWW-Au
  name: Cubby MCP Server
  slug: cubby-mcp-server
modified: '2026-08-11'
name: Cubby
nav: Providers
network: true
overview: 'Cubby publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Self Storage, Property Management, Facility Management, and Real-Estate.


  The Cubby catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cubby''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, changelog, and 23 more developer resources.'
plans:
- name: Cubby Plans Pricing
  plan_count: 0
  slug: cubby-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Cubby Rate Limits
  slug: cubby-rate-limits
scopes:
- name: Cubby Scopes
  scope_count: 0
  slug: cubby-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 45.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 43.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cubby/refs/heads/main/screenshots/cubby-2026-08-17T080842.png
security:
- kind: authentication
  name: Cubby Authentication
  slug: cubby-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cubby Domain Security
  slug: cubby-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cubby
tags:
- Company
- Self Storage
- Property Management
- Facility Management
- Real-Estate
- Payments
- Software-as-a-Service
- Artificial Intelligence
- Revenue Management
- E-Commerce
website: https://www.cubbystorage.com/
---
