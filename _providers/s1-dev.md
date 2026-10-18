---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: S1 Dev Agentic Access
  operation_count: 13
  slug: s1-dev-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 2
apis:
- description: Official hosted Streamable HTTP MCP server exposing search, news, crawl, sitemap and trending tools to any MCP client, with OAuth 2.1 (PKCE, dynamic client registration via clerk.s1.dev) or a Search1A
  name: Search1API MCP Server
  slug: search1api-mcp-server
- description: Secondary MCP server on the Search1API blog host exposing four read-only content tools (search_posts, list_posts, get_post, list_tags); an anonymous tools/list answered with the tool schemas. Serves b
  name: Search1API Blog MCP Server
  slug: search1api-blog-mcp-server
- baseURL: https://api.search1api.com
  baseurl_source: declared
  description: The Account API from Search1API — 1 operation(s) for account.
  name: Search1API Account API
  slug: s1-dev-account-api
- baseURL: https://api.search1api.com
  baseurl_source: declared
  description: The Crawl API from Search1API — 5 operation(s) for crawl.
  name: Search1API Crawl API
  slug: s1-dev-crawl-api
- baseURL: https://api.search1api.com
  baseurl_source: declared
  description: The Feedback API from Search1API — 1 operation(s) for feedback.
  name: Search1API Feedback API
  slug: s1-dev-feedback-api
- baseURL: https://api.search1api.com
  baseurl_source: declared
  description: The Screenshot API from Search1API — 1 operation(s) for screenshot.
  name: Search1API Screenshot API
  slug: s1-dev-screenshot-api
- baseURL: https://api.search1api.com
  baseurl_source: declared
  description: The Search API from Search1API — 4 operation(s) for search.
  name: Search1API Search API
  slug: s1-dev-search-api
- baseURL: https://api.search1api.com
  baseurl_source: declared
  description: The System API from Search1API — 1 operation(s) for system.
  name: Search1API System API
  slug: s1-dev-system-api
artifact_total: 23
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/agentic-access/s1-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/s1-dev-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/rate-limits/s1-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/s1-dev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/plans/s1-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/s1-dev-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/rules/s1-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/s1-dev-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/json-ld/s1-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/s1-dev-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/vocabulary/s1-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/s1-dev-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/data-model/s1-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/s1-dev-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/cli/s1-dev-cli.yml
  title: ''
  type: CLI
  url: cli/s1-dev-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/changelog/s1-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/s1-dev-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/conventions/s1-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/s1-dev-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/authentication/s1-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/s1-dev-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/scopes/s1-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/s1-dev-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://s1.dev/docs/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/lifecycle/s1-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/s1-dev-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/errors/s1-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/s1-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/conformance/s1-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/s1-dev-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/overlays/s1-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/s1-dev-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/llms/s1-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/s1-dev-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/mcp/s1-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/s1-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/mcp/s1-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/s1-dev-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/well-known/s1-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/s1-dev-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/hosts/s1-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/s1-dev-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/vendors/s1-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/s1-dev-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/packages/s1-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/s1-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/packages/s1-dev-packages.yml
  title: ''
  type: Packages
  url: packages/s1-dev-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://app.s1.dev/playground/ask
- group: company
  title: ''
  type: Website
  url: https://s1.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://s1.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://s1.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://s1.dev/docs/basic/search
- group: start
  title: ''
  type: GettingStarted
  url: https://s1.dev/docs/get-started/quickstart
- group: company
  title: ''
  type: About
  url: https://s1.dev/about
- group: operate
  title: ''
  type: Support
  url: https://s1.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.s1.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://s1.dev/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: https://blog.s1.dev/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superagents-lab
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fatwang2
- group: commercial
  title: ''
  type: Pricing
  url: https://s1.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://app.s1.dev/
- group: start
  title: ''
  type: SignUp
  url: https://app.s1.dev/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blog.s1.dev/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s1.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.search1api.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/security/s1-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/s1-dev-domain-security.yml
created: '2026-10-07'
description: Search1API is web access infrastructure for AI agents, operated by SuperAgents, LLC (Delaware). One credit-metered REST API at api.search1api.com provides multi-engine web search (Google, Bing, DuckDuckGo, Yandex, GitHub, arXiv, Reddit, X, Baidu and more), agentic search routed by the TypeSafe Jev model, news search, page crawling, screenshots, sitemap discovery, trending topics, structured extraction and asynchronous deep crawls. The same account reaches it through an OpenAPI 3.1 contract, official TypeScript and Python SDKs, the s1 CLI, a hosted OAuth 2.1 MCP server at mcp.search1api.com, an Agent Skill, and pay-per-request MPP/x402 payment challenges.
image: https://s1.dev/og-home-v2.png
json_schemas:
- name: AskResponse
  property_count: 4
  slug: s1-dev-ask-response
- name: DeepcrawlStatusResponse
  property_count: 7
  slug: s1-dev-deepcrawl-status-response
- name: NewsBatchResponse
  property_count: 2
  slug: s1-dev-news-batch-response
- name: NewsResponse
  property_count: 3
  slug: s1-dev-news-response
- name: SearchBatchResponse
  property_count: 2
  slug: s1-dev-search-batch-response
- name: SearchResponse
  property_count: 3
  slug: s1-dev-search-response
jsonld:
- class_count: 26
  name: S1 Dev Context
  property_count: 55
  slug: s1-dev-context
layout: provider
mcp_servers:
- description: Search1API operates an official hosted MCP server (Streamable HTTP) at https://mcp.search1api.com/mcp exposing five tools (search, news, crawl, sitemap, trending) over OAuth 2.1 (PKCE + dynamic client
  name: Search1API MCP Server
  slug: search1api
modified: '2026-10-07'
name: Search1API
nav: Providers
network: true
overview: 'Search1API publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Crawl API, Feedback API, and 5 more. Tagged areas include Company, Search, Web Search, Crawling, and Web Scraping.


  The Search1API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Search1API''s developer surface includes CLI, changelog, authentication, sandbox, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: S1 Dev Plans Pricing
  plan_count: 4
  slug: s1-dev-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: S1 Dev Rate Limits
  slug: s1-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Search1API API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 2
  slug: s1-dev-rules
scopes:
- name: S1 Dev Scopes
  scope_count: 2
  slug: s1-dev-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 71.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 63.0
    developer_ergonomics: 80.4
    discoverability: 75.0
    operational_transparency: 76.3
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/s1-dev/refs/heads/main/screenshots/s1-dev-2026-10-11T125455.png
security:
- kind: authentication
  name: S1 Dev Authentication
  slug: s1-dev-authentication
  summary_line: http/oauth2/payment-challenge · 3 schemes
- kind: domain-security
  name: S1 Dev Domain Security
  slug: s1-dev-domain-security
  summary_line: TLSv1.3
slug: s1-dev
tags:
- Company
- Search
- Web Search
- Crawling
- Web Scraping
- News
- AI Agents
- MCP
- Agent Tools
- Data Extraction
- Screenshots
website: https://s1.dev
---
