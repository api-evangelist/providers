---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Compsapi Com Agentic Access
  operation_count: 4
  slug: compsapi-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.compsapi.com
  baseurl_source: declared
  description: The Comps API from compsapi-com — 1 operation(s) for comps.
  name: compsapi-com Comps API
  slug: compsapi-com-comps-api
- baseURL: https://api.compsapi.com
  baseurl_source: declared
  description: The Health API from compsapi-com — 1 operation(s) for health.
  name: compsapi-com Health API
  slug: compsapi-com-health-api
- baseURL: https://api.compsapi.com
  baseurl_source: declared
  description: The Sold API from compsapi-com — 1 operation(s) for sold.
  name: compsapi-com Sold API
  slug: compsapi-com-sold-api
- baseURL: https://api.compsapi.com
  baseurl_source: declared
  description: The Usage API from compsapi-com — 1 operation(s) for usage.
  name: compsapi-com Usage API
  slug: compsapi-com-usage-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/compsapi-com/agentic-access/compsapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/compsapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/compsapi-com/rate-limits/compsapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/compsapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/compsapi-com/plans/compsapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/compsapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/compsapi-com/rules/compsapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/compsapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/compsapi-com/json-ld/compsapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/compsapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/compsapi-com/vocabulary/compsapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/compsapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/compsapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/compsapi-com/data-model/compsapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/compsapi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/compsapi-com/changelog/compsapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/compsapi-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/compsapi-com/conventions/compsapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/compsapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/compsapi-com/authentication/compsapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/compsapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/compsapi-com/errors/compsapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/compsapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/compsapi-com/conformance/compsapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compsapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/compsapi-com/llms/compsapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compsapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/compsapi-com/mcp/compsapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/compsapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/compsapi-com/mcp/compsapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/compsapi-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/compsapi-com/hosts/compsapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compsapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/compsapi-com/vendors/compsapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compsapi-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.compsapi.com</span
- group: auth
  href: https://artifacts.apis.io/compsapi-com/security/compsapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compsapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compsapi.com/
- group: company
  title: ''
  type: Blog
  url: https://compsapi.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://compsapi.com/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://compsapi.com/docs
- group: start
  title: ''
  type: Login
  url: https://app.compsapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://compsapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compsapi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.compsapi.com
- group: operate
  title: ''
  type: StatusPage
  url: https://compsapi.com/status
- group: operate
  title: ''
  type: Support
  url: https://app.compsapi.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://compsapi.com/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://compsapi.com/openapi.json
  - status: null
    url: https://api.compsapi.com/openapi.json
  - status: 401
    url: https://api.compsapi.com/mcp
  - status: 200
    url: https://compsapi.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: CompsAPI provides a public API delivering eBay sold listings data with up to 1,095 days of price history and the real accepted Best Offer price. It returns up to 240 sales per GET request as JSON, replacing eBay findCompletedItems and Marketplace Insights workflows. The service offers a free tier with an API key, as well as paid plans for higher volume. The company focuses on giving developers easy access to historical eBay sales data for pricing analysis and market research.
image: https://compsapi.com/og.png
json_schemas:
- name: SoldResponse
  property_count: 16
  slug: compsapi-com-sold-response
jsonld:
- class_count: 5
  name: Compsapi Com Context
  property_count: 57
  slug: compsapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.compsapi.com.
  name: compsapi-com MCP Server
  slug: compsapi-com-mcp-yml
modified: '2026-10-30'
name: compsapi-com
nav: Providers
network: true
overview: 'compsapi-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comps API, Health API, Sold API, and 1 more. Tagged areas include Company, eBay, Data, Pricing, and Marketplace.


  The compsapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  compsapi-com''s developer surface includes changelog, authentication, engineering blog, documentation, pricing, signup flow, support, and 24 more developer resources.'
plans:
- name: Compsapi Com Plans Pricing
  plan_count: 4
  slug: compsapi-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Compsapi Com Rate Limits
  slug: compsapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: compsapi-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: compsapi-com-rules
scopes:
- name: Compsapi Com Scopes
  scope_count: 0
  slug: compsapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 83.2
    catalog_earned_first_party: 24.0
    catalog_gap: 31.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 31.4
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/compsapi-com/compsapi-com-2026-11-03T125021.png
security:
- kind: authentication
  name: Compsapi Com Authentication
  slug: compsapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Compsapi Com Domain Security
  slug: compsapi-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: search-sold-listings
  slug: compsapi-com-search-sold
slug: compsapi-com
tags:
- Company
- eBay
- Data
- Pricing
- Marketplace
website: https://compsapi.com/
---
