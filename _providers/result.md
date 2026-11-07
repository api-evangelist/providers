---
access_model:
  confidence: high
  label: Paid subscription, self-service sign-up
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://result.dev/pricing
  - https://docs.result.dev/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Remote Model Context Protocol server exposing 74 tools across six categories (plan and operate, build and ship, Company Brain, audience growth, sell and support, run the company) — the same tools Resu
  name: Result MCP Server
  slug: result-mcp-server
- description: 'Hosted application backend consumed through the first-party @resultdev/sdk client and administered with @resultdev/cli: PostgREST-style queries against Postgres with row-level security, Google/GitHub '
  name: Result Backend
  slug: result-backend
- description: Embeddable customer-support launcher, loaded either as a plain script tag from https://result.dev/widget.js with a data-support handle or via @resultdev/sdk support.mount(). It opens the business's ow
  name: Result Support Widget
  slug: result-support-widget
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/result/finops/result-finops.yml
  title: ''
  type: FinOps
  url: finops/result-finops.yml
- group: operate
  href: https://artifacts.apis.io/result/lifecycle/result-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/result-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/result/a2a/result-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/result-a2a.yml
- group: other
  href: https://artifacts.apis.io/result/hosts/result-hosts.yml
  title: ''
  type: Hosts
  url: hosts/result-hosts.yml
- group: other
  href: https://artifacts.apis.io/result/vendors/result-vendors.yml
  title: ''
  type: Vendors
  url: vendors/result-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://result.dev/support
- group: company
  title: ''
  type: Website
  url: https://result.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.result.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.result.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.result.dev/cli/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.result.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://result.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://result.dev/privacy
- group: agent
  href: https://artifacts.apis.io/result/llms/result-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/result-llms.txt
- group: agent
  href: https://artifacts.apis.io/result/mcp/result-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/result-mcp.yml
- group: build
  href: https://artifacts.apis.io/result/packages/result-packages.yml
  title: ''
  type: Packages
  url: packages/result-packages.yml
- group: build
  href: https://artifacts.apis.io/result/packages/result-packages.yml
  title: ''
  type: SDKs
  url: packages/result-packages.yml
- group: build
  href: https://artifacts.apis.io/result/cli/result-cli.yml
  title: ''
  type: CLI
  url: cli/result-cli.yml
- group: design
  href: https://artifacts.apis.io/result/components/result-components.yml
  title: ''
  type: Components
  url: components/result-components.yml
- group: auth
  href: https://artifacts.apis.io/result/authentication/result-authentication.yml
  title: ''
  type: Authentication
  url: authentication/result-authentication.yml
- group: auth
  href: https://artifacts.apis.io/result/scopes/result-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/result-scopes.yml
- group: design
  href: https://artifacts.apis.io/result/conventions/result-conventions.yml
  title: ''
  type: Conventions
  url: conventions/result-conventions.yml
- group: design
  href: https://artifacts.apis.io/result/errors/result-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/result-error-codes.yml
- group: design
  href: https://artifacts.apis.io/result/data-model/result-data-model.yml
  title: ''
  type: DataModel
  url: data-model/result-data-model.yml
- group: start
  href: https://artifacts.apis.io/result/sandbox/result-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/result-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/result/plans/result-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/result-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/result/rate-limits/result-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/result-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/result/lifecycle/result-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/result-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/result/conformance/result-conformance.yml
  title: ''
  type: Conformance
  url: conformance/result-conformance.yml
- group: agent
  href: https://artifacts.apis.io/result/well-known/result-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/result-well-known.yml
- group: auth
  href: https://artifacts.apis.io/result/security/result-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/result-domain-security.yml
created: '2026-07-17'
description: 'Result is a Y Combinator (Spring 2026) all-in-one business operating system, operated by Foundative Inc. (a Delaware corporation), that lets internet entrepreneurs start and run companies end-to-end. The platform unifies app development with built-in payments, AI-powered marketing and content creation, automated customer support, financial analytics, branding and design tools, market research, SEO optimization, legal incorporation, and investor fundraising into a single surface, tied together by a "Company Brain" that retains business context from day one. Result ships a real developer surface on top of that product: Result Backend is a hosted app backend (Postgres with row-level security, Google/GitHub and email-password auth, file storage, WebSocket realtime channels with presence, serverless Deno functions, hosted AI chat/embeddings/ image models, transactional email, cookieless web analytics, embedded customer support and Paddle-backed payments) consumed through the first-party
  @resultdev/sdk client and the @resultdev/cli admin CLI. Result also operates a remote, OAuth-protected Model Context Protocol server at https://api.result.dev/mcp exposing 74 tools across six categories, so coding agents and MCP clients can plan, build, publish, sell and support a business through the same validated tool surface the product uses internally. Founded by Aaryan Kushwah (CEO) and Savio Martin (CTO).'
finops:
- has_sources: true
  method: derived
  name: Result Finops
  primary_unit: subscription
  service_category: ''
  slug: result-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/result.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.result.dev over HTTP requiring OAuth.
  name: Result MCP Server
  slug: result
modified: '2026-08-13'
name: Result
nav: Providers
network: true
overview: 'Result is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Operations, Software-as-a-Service, Entrepreneurship, and Payments.


  Result''s developer surface includes support, documentation, API reference, getting-started guide, CLI, authentication, sandbox, and 24 more developer resources.'
plans:
- name: Result Plans Pricing
  plan_count: 3
  slug: result-plans-pricing
- name: Result Price Estimates
  plan_count: 0
  slug: result-price-estimates
random_paper: 23
rate_limits:
- limit_count: 2
  name: Result Rate Limits
  slug: result-rate-limits
scopes:
- name: Result Scopes
  scope_count: 1
  slug: result-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 63.0
    catalog_earned_first_party: 20.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 76.2
    discoverability: 80.0
    operational_transparency: 28.9
  previous_composite: 45.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/result/result-2026-08-17T081542.png
security:
- kind: authentication
  name: Result Authentication
  slug: result-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Result Domain Security
  slug: result-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: result
tags:
- Company
- Business Operations
- Software-as-a-Service
- Entrepreneurship
- Payments
- Marketing
- No-Code
- Startups
- Artificial Intelligence
- Backend-as-a-Service
- MCP
- Agents
- Database
- Authentication
- Storage
- Serverless
- Real-Time
website: https://result.dev/
---
