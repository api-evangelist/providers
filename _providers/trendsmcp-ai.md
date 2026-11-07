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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
  score: 47.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trendsmcp Ai Agentic Access
  operation_count: 1
  slug: trendsmcp-ai-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.trendsmcp.ai
  baseurl_source: declared
  description: Trend data operations
  name: trendsmcp-ai Trends API
  slug: trendsmcp-ai-trends-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/trendsmcp-ai/agentic-access/trendsmcp-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trendsmcp-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/trendsmcp-ai/plans/trendsmcp-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trendsmcp-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trendsmcp-ai/rules/trendsmcp-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/trendsmcp-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/trendsmcp-ai/json-ld/trendsmcp-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trendsmcp-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/trendsmcp-ai/vocabulary/trendsmcp-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trendsmcp-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trendsmcp-ai/data-model/trendsmcp-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trendsmcp-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/trendsmcp-ai/authentication/trendsmcp-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trendsmcp-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/trendsmcp-ai/conformance/trendsmcp-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trendsmcp-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trendsmcp-ai/llms/trendsmcp-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trendsmcp-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/trendsmcp-ai/mcp/trendsmcp-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/trendsmcp-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/trendsmcp-ai/mcp/trendsmcp-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trendsmcp-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trendsmcp-ai/well-known/trendsmcp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trendsmcp-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/trendsmcp-ai/hosts/trendsmcp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trendsmcp-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/trendsmcp-ai/vendors/trendsmcp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trendsmcp-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/trendsmcp-ai/packages/trendsmcp-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/trendsmcp-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/trendsmcp-ai/packages/trendsmcp-ai-packages.yml
  title: ''
  type: Packages
  url: packages/trendsmcp-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/trendsmcp-ai/security/trendsmcp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trendsmcp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trendsmcp.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.trendsmcp.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.trendsmcp.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trendsmcp.ai/docs/mcp
- group: operate
  title: ''
  type: Support
  url: mailto:support@trendsmcp.ai
- group: company
  title: ''
  type: Blog
  url: https://www.trendsmcp.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trendsmcp.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trendsmcp.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trendsmcp.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://trendsmcp.ai/openapi.json
  - status: null
    url: https://www.trendsmcp.ai/openapi.json
  - status: null
    url: https://api.trendsmcp.ai/mcp
  - status: 401
    url: https://trendsmcp.ai/mcp
  - status: 401
    url: https://www.trendsmcp.ai/mcp
  - status: 200
    url: https://trendsmcp.ai/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Trends MCP provides a unified MCP server and API that delivers live trend data across dozens of platforms—including Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia, and more—to AI assistants and agents. With a single API key, developers can query normalized trend metrics without managing individual platform credentials. The service offers a free tier of 100 requests per month and paid plans for higher volume, and supports up to five years of weekly historical data.
image: https://www.trendsmcp.ai/brand/trendsmcp.ai/logo.svg
json_schemas:
- name: GetContextRequest
  property_count: 5
  slug: trendsmcp-ai-get-context-request
- name: GetGrowthRequest
  property_count: 7
  slug: trendsmcp-ai-get-growth-request
- name: GetTimeSeriesRequest
  property_count: 6
  slug: trendsmcp-ai-get-time-series-request
- name: GetTopPostsRequest
  property_count: 4
  slug: trendsmcp-ai-get-top-posts-request
- name: GetTopTrendsRequest
  property_count: 8
  slug: trendsmcp-ai-get-top-trends-request
- name: TopTrendsResponse
  property_count: 10
  slug: trendsmcp-ai-top-trends-response
jsonld:
- class_count: 10
  name: Trendsmcp Ai Context
  property_count: 40
  slug: trendsmcp-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.trendsmcp.ai.
  name: trendsmcp-ai MCP Server
  slug: trendsmcp-ai-mcp-yml
modified: '2026-10-29'
name: trendsmcp-ai
nav: Providers
network: true
overview: 'trendsmcp-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Trends API. Tagged areas include Artificial Intelligence, Trends, Data, Analytics, and MCP.


  The trendsmcp-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  trendsmcp-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Trendsmcp Ai Plans Pricing
  plan_count: 4
  slug: trendsmcp-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Trendsmcp Ai Rate Limits
  slug: trendsmcp-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: trendsmcp-ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: trendsmcp-ai-rules
scopes:
- name: Trendsmcp Ai Scopes
  scope_count: 0
  slug: trendsmcp-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 39.3
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
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
screenshot: https://apis.io/screenshots/trendsmcp-ai/trendsmcp-ai-2026-11-03T145054.png
security:
- kind: authentication
  name: Trendsmcp Ai Authentication
  slug: trendsmcp-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trendsmcp Ai Domain Security
  slug: trendsmcp-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trendsmcp-ai
tags:
- Artificial Intelligence
- Trends
- Data
- Analytics
- MCP
- Company
website: https://trendsmcp.ai/
---
