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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trendsapi Ai Agentic Access
  operation_count: 1
  slug: trendsapi-ai-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.trendsapi.ai
  baseurl_source: declared
  description: Trend data operations
  name: trendsapi-ai Trends API
  slug: trendsapi-ai-trends-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/trendsapi-ai/agentic-access/trendsapi-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trendsapi-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/trendsapi-ai/plans/trendsapi-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trendsapi-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trendsapi-ai/rules/trendsapi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/trendsapi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/trendsapi-ai/json-ld/trendsapi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trendsapi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/trendsapi-ai/vocabulary/trendsapi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trendsapi-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trendsapi-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trendsapi-ai/data-model/trendsapi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trendsapi-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/trendsapi-ai/authentication/trendsapi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trendsapi-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/trendsapi-ai/errors/trendsapi-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trendsapi-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trendsapi-ai/conformance/trendsapi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trendsapi-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trendsapi-ai/llms/trendsapi-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trendsapi-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/trendsapi-ai/mcp/trendsapi-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/trendsapi-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/trendsapi-ai/mcp/trendsapi-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trendsapi-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trendsapi-ai/well-known/trendsapi-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trendsapi-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/trendsapi-ai/hosts/trendsapi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trendsapi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/trendsapi-ai/vendors/trendsapi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trendsapi-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/trendsapi-ai/packages/trendsapi-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/trendsapi-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/trendsapi-ai/packages/trendsapi-ai-packages.yml
  title: ''
  type: Packages
  url: packages/trendsapi-ai-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://trendsapi.ai/docs/mcp
- group: auth
  href: https://artifacts.apis.io/trendsapi-ai/security/trendsapi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trendsapi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trendsapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://trendsapi.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://trendsapi.ai/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://trendsapi.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://trendsapi.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trendsapi.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trendsapi.ai/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://trendsapi.ai/llms.txt
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://trendsapi.ai/openapi.json
  - status: null
    url: https://api.trendsapi.ai/mcp
  - status: 401
    url: https://trendsapi.ai/mcp
  - status: 200
    url: https://trendsapi.ai/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Trends API provides a single REST endpoint delivering trend data aggregated from 49 platforms including Google, TikTok, Amazon, Reddit, YouTube, Steam, npm and more. The service normalizes scores on a 0‑100 scale, offers 100 free requests per month with no credit‑card required, and supports JSON responses for easy integration into applications, dashboards, and analytics pipelines. It aims to simplify access to up‑to‑date popularity metrics across major online services for developers, marketers, and data scientists.
image: https://trendsapi.ai/og-image.png
json_schemas:
- name: GetContextRequest
  property_count: 5
  slug: trendsapi-ai-get-context-request
- name: GetGrowthRequest
  property_count: 7
  slug: trendsapi-ai-get-growth-request
- name: GetTimeSeriesRequest
  property_count: 6
  slug: trendsapi-ai-get-time-series-request
- name: GetTopPostsRequest
  property_count: 4
  slug: trendsapi-ai-get-top-posts-request
- name: GetTopTrendsRequest
  property_count: 8
  slug: trendsapi-ai-get-top-trends-request
- name: TopTrendsResponse
  property_count: 10
  slug: trendsapi-ai-top-trends-response
jsonld:
- class_count: 10
  name: Trendsapi Ai Context
  property_count: 40
  slug: trendsapi-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.trendsapi.ai.
  name: trendsapi-ai MCP Server
  slug: trendsapi-ai-mcp-yml
modified: '2026-10-29'
name: trendsapi-ai
nav: Providers
network: true
overview: 'trendsapi-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Trends API. Tagged areas include Company, Data, Trends, Analytics, and Marketing.


  The trendsapi-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  trendsapi-ai''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Trendsapi Ai Plans Pricing
  plan_count: 4
  slug: trendsapi-ai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Trendsapi Ai Rate Limits
  slug: trendsapi-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: trendsapi-ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: trendsapi-ai-rules
scopes:
- name: Trendsapi Ai Scopes
  scope_count: 0
  slug: trendsapi-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 41.0
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trendsapi-ai/trendsapi-ai-2026-11-03T145049.png
security:
- kind: authentication
  name: Trendsapi Ai Authentication
  slug: trendsapi-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trendsapi Ai Domain Security
  slug: trendsapi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: get-context
  slug: trendsapi-ai-get-context
- name: get-growth
  slug: trendsapi-ai-get-growth
- name: get-time-series
  slug: trendsapi-ai-get-time-series
- name: get-top-posts
  slug: trendsapi-ai-get-top-posts
- name: get-top-trends
  slug: trendsapi-ai-get-top-trends
slug: trendsapi-ai
tags:
- Company
- Data
- Trends
- Analytics
- Marketing
website: https://trendsapi.ai/
---
