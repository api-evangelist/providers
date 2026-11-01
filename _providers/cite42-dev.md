---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'cite42-dev API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: cite42-dev API
  slug: cite42-dev-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/cite42-dev/rate-limits/cite42-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cite42-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cite42-dev/rules/cite42-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/cite42-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/cite42-dev/json-ld/cite42-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cite42-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/cite42-dev/vocabulary/cite42-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cite42-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cite42-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cite42-dev/data-model/cite42-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cite42-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cite42-dev/authentication/cite42-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cite42-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/cite42-dev/errors/cite42-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cite42-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cite42-dev/conformance/cite42-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cite42-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cite42-dev/llms/cite42-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cite42-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/cite42-dev/mcp/cite42-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cite42-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cite42-dev/well-known/cite42-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cite42-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/cite42-dev/hosts/cite42-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cite42-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/cite42-dev/vendors/cite42-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cite42-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/cite42-dev/packages/cite42-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/cite42-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/cite42-dev/packages/cite42-dev-packages.yml
  title: ''
  type: Packages
  url: packages/cite42-dev-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.cite42.dev/login
- group: auth
  href: https://artifacts.apis.io/cite42-dev/security/cite42-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cite42-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cite42.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cite42.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.cite42.dev/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cite42.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://www.cite42.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cite42.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cite42.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cite42.dev/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://cite42.dev/mcp
  - status: 401
    url: https://www.cite42.dev/mcp
  - status: 200
    url: https://cite42.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Cite42 provides a pay‑per‑call MCP (Machine‑Callable‑Procedure) server and API that delivers AI agents real‑time visibility, citation, SEO keyword and trend data. It supports integration with Claude, ChatGPT, Codex, Cursor and other LLMs, offering searchable geographic (GEO) data and trend analytics for AI‑driven applications.
image: https://www.cite42.dev/logo.svg
json_schemas:
- name: PostApiV1CompareResponse
  property_count: 8
  slug: cite42-dev-post-api-v1-compare-response
- name: PostApiV1RankingsResponse
  property_count: 6
  slug: cite42-dev-post-api-v1-rankings-response
- name: PostApiV1RedditTrendsResponse
  property_count: 19
  slug: cite42-dev-post-api-v1-reddit-trends-response
- name: PostApiV1SentimentResponse
  property_count: 8
  slug: cite42-dev-post-api-v1-sentiment-response
- name: PostApiV1WorkflowsContentBriefResponse
  property_count: 5
  slug: cite42-dev-post-api-v1-workflows-content-brief-response
- name: PostApiV1YoutubeTrendsResponse
  property_count: 14
  slug: cite42-dev-post-api-v1-youtube-trends-response
jsonld:
- class_count: 36
  name: Cite42 Dev Context
  property_count: 78
  slug: cite42-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at cite42.dev.
  name: cite42-dev MCP Server
  slug: cite42-dev-mcp-yml
modified: '2026-10-30'
name: cite42-dev
nav: Providers
network: true
overview: 'cite42-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, SEO, MCP, and Data.


  The cite42-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cite42-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Cite42 Dev Plans Pricing
  plan_count: 0
  slug: cite42-dev-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Cite42 Dev Rate Limits
  slug: cite42-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: cite42-dev API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: cite42-dev-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 79.9
    catalog_earned_first_party: 0.0
    catalog_gap: 35.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 45.6
    developer_ergonomics: 56.4
    discoverability: 56.7
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cite42 Dev Authentication
  slug: cite42-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cite42 Dev Domain Security
  slug: cite42-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cite42-dev
tags:
- Company
- AI
- SEO
- MCP
- Data
- Visibility
website: https://cite42.dev/
---
