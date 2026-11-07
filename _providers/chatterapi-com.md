---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Chatterapi Com Agentic Access
  operation_count: 42
  slug: chatterapi-com-agentic-access
  summary_line: 42 operations · 5 acting
api_count: 1
apis:
- baseURL: https://chatterapi.com
  baseurl_source: declared
  description: Account, usage, health and the generic run alias.
  name: chatterapi-com Account API
  slug: chatterapi-com-account-api
- baseURL: https://chatterapi.com
  baseurl_source: declared
  description: Tools that search Reddit and X together.
  name: chatterapi-com Everywhere API
  slug: chatterapi-com-everywhere-api
- baseURL: https://chatterapi.com
  baseurl_source: declared
  description: Reddit read tools.
  name: chatterapi-com Reddit API
  slug: chatterapi-com-reddit-api
- baseURL: https://chatterapi.com
  baseurl_source: declared
  description: X read tools.
  name: chatterapi-com X API
  slug: chatterapi-com-x-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/chatterapi-com/agentic-access/chatterapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chatterapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/chatterapi-com/rate-limits/chatterapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chatterapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chatterapi-com/plans/chatterapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chatterapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/rules/chatterapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/chatterapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/json-ld/chatterapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chatterapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/chatterapi-com/vocabulary/chatterapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chatterapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/chatterapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/data-model/chatterapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chatterapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/conventions/chatterapi-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/chatterapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/conventions/chatterapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chatterapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/chatterapi-com/authentication/chatterapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chatterapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/lifecycle/chatterapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chatterapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/errors/chatterapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chatterapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chatterapi-com/conformance/chatterapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chatterapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chatterapi-com/llms/chatterapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatterapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/chatterapi-com/mcp/chatterapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/chatterapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/chatterapi-com/mcp/chatterapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chatterapi-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/chatterapi-com/hosts/chatterapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatterapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatterapi-com/vendors/chatterapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatterapi-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://chatterapi.com/status
- group: start
  title: ''
  type: Login
  url: https://chatterapi.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://chatterapi.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://chatterapi.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://chatterapi.com/docs/endpoints
- group: auth
  href: https://artifacts.apis.io/chatterapi-com/security/chatterapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatterapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatterapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://chatterapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://chatterapi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://chatterapi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatterapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatterapi.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://chatterapi.com/openapi.json
  - status: null
    url: https://api.chatterapi.com/openapi.json
  - status: 401
    url: https://chatterapi.com/mcp
  - status: 401
    url: https://api.chatterapi.com/mcp
  - status: 200
    url: https://chatterapi.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: ChatterAPI provides a unified API that aggregates data from Reddit and X (formerly Twitter) into a single endpoint. With one API key and a shared credit balance, developers can access posts, comments, user profiles, and real‑time streams via REST endpoints. The platform also offers a hosted MCP server so AI agents can invoke the same tools. Documentation includes quickstart guides, authentication details, credit usage, error handling, and a full reference for every Reddit and X tool.
image: https://chatterapi.com/opengraph-image?dd6327c3408cfced
json_schemas:
- name: Lead
  property_count: 13
  slug: chatterapi-com-lead
- name: RedditPost
  property_count: 16
  slug: chatterapi-com-reddit-post
- name: RedditThread
  property_count: 4
  slug: chatterapi-com-reddit-thread
- name: RedditUserAnalysis
  property_count: 10
  slug: chatterapi-com-reddit-user-analysis
- name: Subreddit
  property_count: 10
  slug: chatterapi-com-subreddit
- name: XTweet
  property_count: 18
  slug: chatterapi-com-xtweet
jsonld:
- class_count: 15
  name: Chatterapi Com Context
  property_count: 83
  slug: chatterapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.chatterapi.com.
  name: chatterapi-com MCP Server
  slug: chatterapi-com-mcp-yml
modified: '2026-10-30'
name: chatterapi-com
nav: Providers
network: true
overview: 'chatterapi-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Everywhere API, Reddit API, and 1 more. Tagged areas include Social Media, Reddit, X, Data, and MCP.


  The chatterapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  chatterapi-com''s developer surface includes authentication, changelog, getting-started guide, API reference, documentation, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Chatterapi Com Plans Pricing
  plan_count: 3
  slug: chatterapi-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Chatterapi Com Rate Limits
  slug: chatterapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: chatterapi-com API Rules
  rule_count: 21
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 5
  slug: chatterapi-com-rules
scopes:
- name: Chatterapi Com Scopes
  scope_count: 0
  slug: chatterapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 68.6
    developer_ergonomics: 33.8
    discoverability: 65.0
    operational_transparency: 15.8
  previous_composite: 58.4
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
screenshot: https://apis.io/screenshots/chatterapi-com/chatterapi-com-2026-11-03T123923.png
security:
- kind: authentication
  name: Chatterapi Com Authentication
  slug: chatterapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chatterapi Com Domain Security
  slug: chatterapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: everywhere
  slug: chatterapi-com-everywhere-skill
- name: reddit
  slug: chatterapi-com-reddit-skill
- name: x
  slug: chatterapi-com-x-skill
slug: chatterapi-com
tags:
- Social Media
- Reddit
- X
- Data
- MCP
website: https://chatterapi.com/
---
