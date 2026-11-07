---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Trendsfast Agentic Access
  operation_count: 25
  slug: trendsfast-agentic-access
  summary_line: 25 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: /
  baseurl_source: spec
  description: The Next Move API from TrendsFast — 1 operation(s) for next move.
  name: TrendsFast Next Move API
  slug: trendsfast-next-move-api
- baseURL: /
  baseurl_source: spec
  description: The Next Moves API from TrendsFast — 1 operation(s) for next moves.
  name: TrendsFast Next Moves API
  slug: trendsfast-next-moves-api
- baseURL: /
  baseurl_source: spec
  description: The Projects API from TrendsFast — 11 operation(s) for projects.
  name: TrendsFast Projects API
  slug: trendsfast-projects-api
- baseURL: https://trendsfast.com
  baseurl_source: declared
  description: The Public API from TrendsFast — 1 operation(s) for public.
  name: TrendsFast Public API
  slug: trendsfast-public-api
- baseURL: https://trendsfast.com
  baseurl_source: declared
  description: The Trends API from TrendsFast — 10 operation(s) for trends.
  name: TrendsFast Trends API
  slug: trendsfast-trends-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/trendsfast/agentic-access/trendsfast-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trendsfast-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/trendsfast/rate-limits/trendsfast-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trendsfast-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/trendsfast/rules/trendsfast-rules.yml
  title: ''
  type: Spectral
  url: rules/trendsfast-rules.yml
- group: design
  href: https://artifacts.apis.io/trendsfast/json-ld/trendsfast-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trendsfast-context.jsonld
- group: design
  href: https://artifacts.apis.io/trendsfast/vocabulary/trendsfast-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trendsfast-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trendsfast/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trendsfast/data-model/trendsfast-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trendsfast-data-model.yml
- group: auth
  href: https://artifacts.apis.io/trendsfast/authentication/trendsfast-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trendsfast-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trendsfast/scopes/trendsfast-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/trendsfast-scopes.yml
- group: design
  href: https://artifacts.apis.io/trendsfast/errors/trendsfast-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trendsfast-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trendsfast/conformance/trendsfast-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trendsfast-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trendsfast/llms/trendsfast-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trendsfast-llms.txt
- group: agent
  href: https://artifacts.apis.io/trendsfast/mcp/trendsfast-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trendsfast-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trendsfast/well-known/trendsfast-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trendsfast-well-known.yml
- group: other
  href: https://artifacts.apis.io/trendsfast/hosts/trendsfast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trendsfast-hosts.yml
- group: other
  href: https://artifacts.apis.io/trendsfast/vendors/trendsfast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trendsfast-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://trendsfast.com/news
- group: start
  title: ''
  type: Login
  url: https://trendsfast.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meestierolff
- group: auth
  href: https://artifacts.apis.io/trendsfast/security/trendsfast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trendsfast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trendsfast.com
- group: docs
  title: ''
  type: Documentation
  url: https://trendsfast.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://trendsfast.com/api
- group: operate
  title: ''
  type: Support
  url: https://trendsfast.com/support
- group: company
  title: ''
  type: Blog
  url: https://trendsfast.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://trendsfast.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trendsfast.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trendsfast.com/privacy
created: '2026-10-30'
description: Connect your agent to current trends in your niche. Social, search and AI-search intelligence with sources, context and evidence through one API. TrendsFast offers a free tier with 100 credits and paid plans ranging from $10 per 500 credits to $299 for 40,000 credits per month, enabling developers to integrate real‑time social, search and AI‑driven trend data from platforms like X, TikTok, YouTube, Instagram, Facebook, Reddit, Google and Hacker News.
image: https://trendsfast.com/icons/signal-sprite-512.png
json_schemas:
- name: TrendsApiV3Response
  property_count: 10
  slug: trendsfast-trends-api-v3-response
jsonld:
- class_count: 15
  name: Trendsfast Context
  property_count: 126
  slug: trendsfast-context
layout: provider
mcp_servers:
- description: Remote MCP server at trendsfast.com requiring an API key.
  name: TrendsFast MCP Server
  slug: trendsfast-mcp-yml
modified: '2026-10-30'
name: TrendsFast
nav: Providers
network: true
overview: 'TrendsFast publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Next Move API, Next Moves API, Projects API, and 2 more. Tagged areas include Trends, Social Media, Search, and Artificial Intelligence.


  The TrendsFast catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TrendsFast''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Trendsfast Plans Pricing
  plan_count: 0
  slug: trendsfast-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Trendsfast Rate Limits
  slug: trendsfast-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: TrendsFast API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: trendsfast-rules
scopes:
- name: Trendsfast Scopes
  scope_count: 0
  slug: trendsfast-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 61.2
    catalog_earned_first_party: 12.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 58.3
    developer_ergonomics: 30.2
    discoverability: 59.2
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trendsfast/trendsfast-2026-11-03T145052.png
security:
- kind: authentication
  name: Trendsfast Authentication
  slug: trendsfast-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trendsfast Domain Security
  slug: trendsfast-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: public-trend-explorer
  slug: trendsfast-public_trend_explorer
slug: trendsfast
tags:
- Trends
- Social Media
- Search
- Artificial Intelligence
website: https://trendsfast.com
---
