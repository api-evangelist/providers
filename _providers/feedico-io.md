---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Feedico Io Agentic Access
  operation_count: 8
  slug: feedico-io-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 3
apis:
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: The Auth API from feedico-io — 1 operation(s) for auth.
  name: feedico-io Auth API
  slug: feedico-io-auth-api
- baseURL: https://partner.feedico.io
  baseurl_source: declared
  description: The Catalog API from feedico-io — 1 operation(s) for catalog.
  name: feedico-io Catalog API
  slug: feedico-io-catalog-api
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: Your account coupons (`POST /api/v1/me/coupons`).
  name: feedico-io Coupons API
  slug: feedico-io-coupons-api
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: Your connected merchant programmes (`POST /api/v1/me/networks`).
  name: feedico-io Firms API
  slug: feedico-io-firms-api
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: Cross-tenant aggregated firms, coupons, and products (`POST /api/v1/catalog/*`). No `offerUrl`.
  name: feedico-io Global catalogue API
  slug: feedico-io-global-catalogue-api
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: The Health API from feedico-io — 1 operation(s) for health.
  name: feedico-io Health API
  slug: feedico-io-health-api
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: Your account product feed (`POST /api/v1/me/products`). Includes `images[]`.
  name: feedico-io Products API
  slug: feedico-io-products-api
- baseURL: https://api.feedico.io
  baseurl_source: declared
  description: The User API from feedico-io — 1 operation(s) for user.
  name: feedico-io User API
  slug: feedico-io-user-api
artifact_total: 19
common:
- group: design
  href: https://artifacts.apis.io/feedico-io/data-model/feedico-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/feedico-io-data-model.yml
- group: agent
  href: https://artifacts.apis.io/feedico-io/agentic-access/feedico-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/feedico-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/feedico-io/plans/feedico-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/feedico-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/feedico-io/rules/feedico-io-rules.yml
  title: ''
  type: Spectral
  url: rules/feedico-io-rules.yml
- group: design
  href: https://artifacts.apis.io/feedico-io/vocabulary/feedico-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/feedico-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/feedico-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/feedico-io/authentication/feedico-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/feedico-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/feedico-io/errors/feedico-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/feedico-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/feedico-io/conformance/feedico-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/feedico-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/feedico-io/llms/feedico-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/feedico-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/feedico-io/mcp/feedico-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/feedico-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/feedico-io/hosts/feedico-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/feedico-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/feedico-io/packages/feedico-io-packages.yml
  title: ''
  type: SDKs
  url: packages/feedico-io-packages.yml
- group: build
  href: https://artifacts.apis.io/feedico-io/packages/feedico-io-packages.yml
  title: ''
  type: Packages
  url: packages/feedico-io-packages.yml
- group: start
  title: ''
  type: Login
  url: https://feedico.io/sign-in
- group: docs
  title: ''
  type: APIReference
  url: https://feedico.io/api-docs
- group: auth
  href: https://artifacts.apis.io/feedico-io/security/feedico-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/feedico-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://feedico.io/
- group: docs
  title: ''
  type: Documentation
  url: https://feedico.io/docs
- group: company
  title: ''
  type: Blog
  url: https://feedico.io/blog
- group: operate
  title: ''
  type: Support
  url: https://feedico.io/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://feedico.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://feedico.io/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://feedico.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://feedico.io/docs
created: '2026-10-30'
description: Feedico provides an Affiliate & Coupon API that aggregates multiple affiliate networks (CJ, Awin, Impact, Admitad, etc.) into a single RESTful contract, enabling publishers to retrieve deals, coupons, and product feeds efficiently. The platform offers comprehensive documentation, pricing plans, and developer resources for integration.
image: https://feedico.io/opengraph-image?d616aa5756e09822
json_schemas:
- name: LoginRequest
  property_count: 0
  slug: feedico-io-login-request
- name: LoginSuccess
  property_count: 0
  slug: feedico-io-login-success
- name: MeSuccess
  property_count: 0
  slug: feedico-io-me-success
layout: provider
mcp_servers:
- description: Remote MCP server at partner.feedico.io.
  name: feedico-io MCP Server
  slug: feedico-io-mcp-yml
modified: '2026-10-30'
name: feedico-io
nav: Providers
network: true
overview: 'feedico-io publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Catalog API, Coupons API, and 5 more. Tagged areas include Affiliates, Marketing, E-Commerce, and Coupons.


  The feedico-io catalog on APIs.io includes 1 Spectral governance ruleset.


  feedico-io''s developer surface includes authentication, API reference, documentation, engineering blog, support, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Feedico Io Plans Pricing
  plan_count: 5
  slug: feedico-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Feedico Io Rate Limits
  slug: feedico-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: feedico-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: feedico-io-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 49.7
    developer_ergonomics: 43.3
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/feedico-io/feedico-io-2026-11-03T131919.png
security:
- kind: authentication
  name: Feedico Io Authentication
  slug: feedico-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Feedico Io Domain Security
  slug: feedico-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: feedico-io-health
  slug: feedico-io-health
slug: feedico-io
tags:
- Affiliates
- Marketing
- E-Commerce
- Coupons
website: https://feedico.io/
---
