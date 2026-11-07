---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Upriver Ai Agentic Access
  operation_count: 43
  slug: upriver-ai-agentic-access
  summary_line: 43 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Account API from upriver-ai — 1 operation(s) for account.
  name: upriver-ai Account API
  slug: upriver-ai-account-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Audience API from upriver-ai — 2 operation(s) for audience.
  name: upriver-ai Audience API
  slug: upriver-ai-audience-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Brands API from upriver-ai — 1 operation(s) for brands.
  name: upriver-ai Brands API
  slug: upriver-ai-brands-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Breakout Feeds API from upriver-ai — 2 operation(s) for breakout feeds.
  name: upriver-ai Breakout Feeds API
  slug: upriver-ai-breakout-feeds-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Breakout Topics API from upriver-ai — 11 operation(s) for breakout topics.
  name: upriver-ai Breakout Topics API
  slug: upriver-ai-breakout-topics-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Creators API from upriver-ai — 5 operation(s) for creators.
  name: upriver-ai Creators API
  slug: upriver-ai-creators-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Images API from upriver-ai — 1 operation(s) for images.
  name: upriver-ai Images API
  slug: upriver-ai-images-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Products API from upriver-ai — 2 operation(s) for products.
  name: upriver-ai Products API
  slug: upriver-ai-products-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Sponsorships API from upriver-ai — 3 operation(s) for sponsorships.
  name: upriver-ai Sponsorships API
  slug: upriver-ai-sponsorships-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Taxonomy API from upriver-ai — 2 operation(s) for taxonomy.
  name: upriver-ai Taxonomy API
  slug: upriver-ai-taxonomy-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Trends API from upriver-ai — 6 operation(s) for trends.
  name: upriver-ai Trends API
  slug: upriver-ai-trends-api
- baseURL: https://api.upriver.ai
  baseurl_source: declared
  description: The Trends Radar (Beta) API from upriver-ai — 7 operation(s) for trends radar (beta).
  name: upriver-ai Trends Radar (Beta) API
  slug: upriver-ai-trends-radar-beta-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/upriver-ai/agentic-access/upriver-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/upriver-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/upriver-ai/rules/upriver-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/upriver-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/upriver-ai/json-ld/upriver-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/upriver-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/upriver-ai/vocabulary/upriver-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/upriver-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/upriver-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/upriver-ai/data-model/upriver-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upriver-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/upriver-ai/changelog/upriver-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/upriver-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/upriver-ai/authentication/upriver-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upriver-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/upriver-ai/errors/upriver-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/upriver-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/upriver-ai/conformance/upriver-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upriver-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/upriver-ai/llms/upriver-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upriver-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/upriver-ai/a2a/upriver-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/upriver-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/upriver-ai/mcp/upriver-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/upriver-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/upriver-ai/mcp/upriver-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/upriver-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/upriver-ai/hosts/upriver-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upriver-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/upriver-ai/vendors/upriver-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upriver-ai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.upriver.ai/changelog
- group: auth
  href: https://artifacts.apis.io/upriver-ai/security/upriver-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upriver-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upriver.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upriver.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.upriver.ai/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.upriver.ai/index
- group: operate
  title: ''
  type: Support
  url: mailto:support@upriver.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upriver.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upriver.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upriver-ai
created: '2026-10-31'
description: Upriver provides AI-powered structured data on creators, audiences, brands, trends, and sponsorships, enabling marketers and developers to enrich search, targeting, and campaign planning. Its API offers endpoints for brand research, product details, creator profiles, audience personas, sponsorship discovery, trend radar, and media samples, delivering real-time context for advertising and content strategy.
image: https://upriver.ai/opengraph-image.png?opengraph-image.4f851217.png
json_schemas:
- name: CreatorGetResponse
  property_count: 11
  slug: upriver-ai-creator-get-response
- name: CreatorSearchInput
  property_count: 18
  slug: upriver-ai-creator-search-input
- name: CreatorSimilarInput
  property_count: 0
  slug: upriver-ai-creator-similar-input
- name: SearchTopicsRequest
  property_count: 12
  slug: upriver-ai-search-topics-request
- name: TrendDetailResponse
  property_count: 44
  slug: upriver-ai-trend-detail-response
- name: TrendsBroadInput
  property_count: 33
  slug: upriver-ai-trends-broad-input
jsonld:
- class_count: 120
  name: Upriver Ai Context
  property_count: 303
  slug: upriver-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.upriver.ai.
  name: upriver-ai MCP Server
  slug: upriver-ai-mcp-yml
modified: '2026-10-31'
name: upriver-ai
nav: Providers
network: true
overview: 'upriver-ai publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Audience API, Brands API, and 9 more. Tagged areas include Artificial Intelligence, Marketing, Data, Creators, and Brands.


  The upriver-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  upriver-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: upriver-ai API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: upriver-ai-rules
scopes:
- name: Upriver Ai Scopes
  scope_count: 0
  slug: upriver-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 64.1
    developer_ergonomics: 37.4
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Upriver Ai Authentication
  slug: upriver-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Upriver Ai Domain Security
  slug: upriver-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: upriver-ai-audience
  slug: upriver-ai-audience
- name: upriver-ai-brand
  slug: upriver-ai-brand
- name: upriver-ai-creator
  slug: upriver-ai-creator
- name: upriver-ai-trends
  slug: upriver-ai-trends
slug: upriver-ai
tags:
- Artificial Intelligence
- Marketing
- Data
- Creators
- Brands
- Trends
- Sponsorship
website: https://upriver.ai/
---
