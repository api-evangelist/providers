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
  - sandbox
  trial: false
  try_now: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Typesearch Ai Agentic Access
  operation_count: 38
  slug: typesearch-ai-agentic-access
  summary_line: 38 operations · 18 acting
api_count: 2
apis:
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Charts API from typesearch-ai — 2 operation(s) for charts.
  name: typesearch-ai Charts API
  slug: typesearch-ai-charts-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Contents API from typesearch-ai — 1 operation(s) for contents.
  name: typesearch-ai Contents API
  slug: typesearch-ai-contents-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Embed API from typesearch-ai — 1 operation(s) for embed.
  name: typesearch-ai Embed API
  slug: typesearch-ai-embed-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Indexes API from typesearch-ai — 3 operation(s) for indexes.
  name: typesearch-ai Indexes API
  slug: typesearch-ai-indexes-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Jobs API from typesearch-ai — 1 operation(s) for jobs.
  name: typesearch-ai Jobs API
  slug: typesearch-ai-jobs-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Search API from typesearch-ai — 2 operation(s) for search.
  name: typesearch-ai Search API
  slug: typesearch-ai-search-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Similar API from typesearch-ai — 1 operation(s) for similar.
  name: typesearch-ai Similar API
  slug: typesearch-ai-similar-api
- baseURL: https://api.typesearch.ai
  baseurl_source: declared
  description: The Usage API from typesearch-ai — 1 operation(s) for usage.
  name: typesearch-ai Usage API
  slug: typesearch-ai-usage-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/typesearch-ai/agentic-access/typesearch-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/typesearch-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/typesearch-ai/rate-limits/typesearch-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/typesearch-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/typesearch-ai/plans/typesearch-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/typesearch-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/typesearch-ai/rules/typesearch-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/typesearch-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/typesearch-ai/json-ld/typesearch-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/typesearch-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/typesearch-ai/vocabulary/typesearch-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/typesearch-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/typesearch-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/typesearch-ai/data-model/typesearch-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/typesearch-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/typesearch-ai/changelog/typesearch-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/typesearch-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/typesearch-ai/authentication/typesearch-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/typesearch-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/typesearch-ai/errors/typesearch-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/typesearch-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/typesearch-ai/conformance/typesearch-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/typesearch-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/typesearch-ai/llms/typesearch-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/typesearch-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/typesearch-ai/mcp/typesearch-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/typesearch-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/typesearch-ai/hosts/typesearch-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/typesearch-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/typesearch-ai/vendors/typesearch-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/typesearch-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/typesearch-ai/packages/typesearch-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/typesearch-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/typesearch-ai/packages/typesearch-ai-packages.yml
  title: ''
  type: Packages
  url: packages/typesearch-ai-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://app.typesearch.ai/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://typesearch.ai/changelog
- group: auth
  href: https://artifacts.apis.io/typesearch-ai/security/typesearch-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/typesearch-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://typesearch.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://typesearch.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://typesearch.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://typesearch.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://typesearch.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://typesearch.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.typesearch.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://typesearch.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://typesearch.ai/privacy
created: '2026-10-31'
description: typesearch.ai provides a fast, cost‑effective Search API for AI agents. It runs its own indexed news corpus, offering calibrated relevance and drop‑in compatibility with Exa, Tako, and Perplexity SDKs. Pricing starts at $1 per 1,000 searches, delivering up to 7× cheaper results than competitors while supporting rich result filters and content extraction. The service targets developers building AI‑powered applications that need real‑time, searchable news and web content.
image: https://typesearch.ai/og/en/home.png
json_schemas:
- name: ChartRequest
  property_count: 25
  slug: typesearch-ai-chart-request
- name: Chart
  property_count: 21
  slug: typesearch-ai-chart
- name: Job
  property_count: 7
  slug: typesearch-ai-job
- name: SearchRequest
  property_count: 23
  slug: typesearch-ai-search-request
- name: SearchResponse
  property_count: 24
  slug: typesearch-ai-search-response
- name: SimilarRequest
  property_count: 21
  slug: typesearch-ai-similar-request
jsonld:
- class_count: 20
  name: Typesearch Ai Context
  property_count: 96
  slug: typesearch-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.typesearch.ai.
  name: typesearch-ai MCP Server
  slug: typesearch-ai-mcp-yml
modified: '2026-10-31'
name: typesearch-ai
nav: Providers
network: true
overview: 'typesearch-ai publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charts API, Contents API, Embed API, and 5 more. Tagged areas include Company, Artificial Intelligence, Search, Software-as-a-Service, and Data.


  The typesearch-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  typesearch-ai''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
plans:
- name: Typesearch Ai Plans Pricing
  plan_count: 5
  slug: typesearch-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Typesearch Ai Rate Limits
  slug: typesearch-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: typesearch-ai API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: typesearch-ai-rules
scopes:
- name: Typesearch Ai Scopes
  scope_count: 0
  slug: typesearch-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.0
    catalog_earned_first_party: 20.0
    catalog_gap: 33.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.5
  facets:
    access_clarity: 53.9
    contract_governance: 19.7
    contract_quality: 57.5
    developer_ergonomics: 48.1
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/typesearch-ai/typesearch-ai-2026-11-03T145333.png
security:
- kind: authentication
  name: Typesearch Ai Authentication
  slug: typesearch-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Typesearch Ai Domain Security
  slug: typesearch-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: typesearch-ai
tags:
- Company
- Artificial Intelligence
- Search
- Software-as-a-Service
- Data
website: https://typesearch.ai/
---
