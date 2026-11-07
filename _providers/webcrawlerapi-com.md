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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Official Model Context Protocol server distributed as the npm package webcrawler-mcp (npx -y webcrawler-mcp) and run locally over stdio - or self-hosted over streamable HTTP with USE_HTTP=true - by th
  name: WebCrawlerAPI MCP Server
  slug: webcrawlerapi-mcp-server
- description: A2A-style agent card served from https://webcrawlerapi.com/.well-known/agent-card.json describing "WebCrawlerAPI Agent" (version 1.0.0) with three skills - scrape, crawl and crawling-agent - Bearer se
  name: WebCrawlerAPI Agent Card
  slug: webcrawlerapi-a2a-agent-card
- baseURL: https://api.webcrawlerapi.com
  baseurl_source: declared
  description: The Agent API from WebCrawlerAPI — 3 operation(s) for agent.
  name: WebCrawlerAPI Agent API
  slug: webcrawlerapi-com-agent-api
- baseURL: https://api.webcrawlerapi.com
  baseurl_source: declared
  description: The Feeds API from WebCrawlerAPI — 9 operation(s) for feeds.
  name: WebCrawlerAPI Feeds API
  slug: webcrawlerapi-com-feeds-api
- baseURL: https://api.webcrawlerapi.com
  baseurl_source: declared
  description: The Jobs API from WebCrawlerAPI — 6 operation(s) for jobs.
  name: WebCrawlerAPI Jobs API
  slug: webcrawlerapi-com-jobs-api
- baseURL: https://api.webcrawlerapi.com
  baseurl_source: declared
  description: The Organization API from WebCrawlerAPI — 1 operation(s) for organization.
  name: WebCrawlerAPI Organization API
  slug: webcrawlerapi-com-organization-api
- baseURL: https://api.webcrawlerapi.com
  baseurl_source: declared
  description: The Status API from WebCrawlerAPI — 2 operation(s) for status.
  name: WebCrawlerAPI Status API
  slug: webcrawlerapi-com-status-api
- baseURL: https://api.webcrawlerapi.com
  baseurl_source: declared
  description: The V2 Scraping API from WebCrawlerAPI — 2 operation(s) for v2 scraping.
  name: WebCrawlerAPI V2 Scraping API
  slug: webcrawlerapi-com-v2-scraping-api
artifact_total: 21
asyncapis:
- description: ''
  name: Webcrawlerapi Com Webhooks
  slug: webcrawlerapi-com-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://webcrawlerapi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://webcrawlerapi.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://webcrawlerapi.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://api.webcrawlerapi.com/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://webcrawlerapi.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@webcrawlerapi.com
- group: company
  title: ''
  type: Blog
  url: https://webcrawlerapi.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://webcrawlerapi.com/rss.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://webcrawlerapi.com/changelog
- group: operate
  href: https://artifacts.apis.io/webcrawlerapi-com/changelog/webcrawlerapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/webcrawlerapi-com-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webcrawlerapi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WebCrawlerAPI
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Webcrawlerapihq
- group: commercial
  title: ''
  type: Pricing
  url: https://webcrawlerapi.com/docs/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.webcrawlerapi.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dash.webcrawlerapi.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webcrawlerapi.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webcrawlerapi.com/privacy
- group: other
  title: ''
  type: RefundPolicy
  url: https://webcrawlerapi.com/refund
- group: other
  title: ''
  type: Leadership
  url: https://webcrawlerapi.com/about
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/webcrawlerapi/webcrawlerapi-public-workspace/collection/xz2fs5u/webcrawlerapi
- group: agent
  href: https://artifacts.apis.io/webcrawlerapi-com/llms/webcrawlerapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webcrawlerapi-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://webcrawlerapi.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://webcrawlerapi.com/docs/llms.txt
- group: agent
  href: https://artifacts.apis.io/webcrawlerapi-com/well-known/webcrawlerapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webcrawlerapi-com-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://webcrawlerapi.com/.well-known/api-catalog
- group: other
  href: https://artifacts.apis.io/webcrawlerapi-com/a2a/webcrawlerapi-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/webcrawlerapi-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/webcrawlerapi-com/mcp/webcrawlerapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/webcrawlerapi-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/webcrawlerapi-com/mcp/webcrawlerapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/webcrawlerapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/webcrawlerapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/webcrawlerapi-com/packages/webcrawlerapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/webcrawlerapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/webcrawlerapi-com/packages/webcrawlerapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/webcrawlerapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/webcrawlerapi-com/cli/webcrawlerapi-com-cli.yml
  title: ''
  type: CLI
  url: cli/webcrawlerapi-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/webcrawlerapi-com/authentication/webcrawlerapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/webcrawlerapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/webcrawlerapi-com/conventions/webcrawlerapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/webcrawlerapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/webcrawlerapi-com/errors/webcrawlerapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/webcrawlerapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/webcrawlerapi-com/data-model/webcrawlerapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/webcrawlerapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/webcrawlerapi-com/asyncapi/webcrawlerapi-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/webcrawlerapi-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/webcrawlerapi-com/rate-limits/webcrawlerapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/webcrawlerapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/webcrawlerapi-com/plans/webcrawlerapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/webcrawlerapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/webcrawlerapi-com/lifecycle/webcrawlerapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/webcrawlerapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/webcrawlerapi-com/conformance/webcrawlerapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/webcrawlerapi-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/webcrawlerapi-com/overlays/webcrawlerapi-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/webcrawlerapi-com-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/webcrawlerapi-com/security/webcrawlerapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webcrawlerapi-com-domain-security.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://webcrawlerapi.com/legal/subprocessor-list
- group: other
  title: ''
  type: NoticeAndAction
  url: https://webcrawlerapi.com/tos
created: '2026-09-19'
description: 'WebCrawlerAPI is a web crawling and scraping API from 103 Labs (Netherlands) that turns websites into clean, LLM-ready markdown, cleaned text, HTML or link lists for AI agents, support bots and RAG pipelines. It offers asynchronous multi-page crawl jobs (POST /v1/crawl with polling or webhooks), single-page scraping (POST /v2/scrape, sync or async, with prompt-based structured outputs validated against a JSON Schema), scheduled change-detection Feeds delivered as Atom 1.0, JSON Feed 1.1 or webhooks, a prompt-driven autonomous crawling agent with a required per-run spend cap, and organization usage/balance endpoints. Requests authenticate with a Bearer API key; usage is metered per successfully crawled page on a $0/month pay-as-you-go tier or $29/$99/$499 monthly plans, with 7-day caching (cache hits free). Published surfaces: a Swagger 2.0 document behind a live Swagger UI, an Agent API OpenAPI 3.0.3, an A2A agent card and RFC 9727 API catalog at /.well-known/, llms.txt, SDKs
  for JavaScript, Python, PHP, .NET and Java, an npm MCP server (local stdio), the webcr CLI, a Claude Code Agent Skill, a public Postman collection and a dated changelog.'
finops:
- has_sources: true
  method: derived
  name: Webcrawlerapi Com Finops
  primary_unit: page
  service_category: ''
  slug: webcrawlerapi-com-finops
  template: false
image: https://webcrawlerapi.com/favicon.png
layout: provider
mcp_servers:
- description: WebCrawlerAPI ships an official MCP server as an npm package (webcrawler-mcp) that a user runs locally over stdio, or self-hosts over HTTP with USE_HTTP=true. There is NO provider-hosted remote endpoi
  name: WebCrawlerAPI MCP Server
  slug: webcrawler-mcp
- description: ''
  name: webcrawler-mcp on npm (local stdio package)
  slug: webcrawler-mcp-on-npm-local-stdio-package
modified: '2026-09-19'
name: WebCrawlerAPI
nav: Providers
network: true
overview: 'WebCrawlerAPI publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Feeds API, Jobs API, and 5 more. Tagged areas include Web Scraping, Web Crawling, Data Extraction, Markdown, and AI Agents.


  The WebCrawlerAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WebCrawlerAPI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 39 more developer resources.'
plans:
- name: Webcrawlerapi Com Plans Pricing
  plan_count: 3
  slug: webcrawlerapi-com-plans-pricing
- name: Webcrawlerapi Com Price Estimates
  plan_count: 0
  slug: webcrawlerapi-com-price-estimates
random_paper: 20
rate_limits:
- limit_count: 0
  name: Webcrawlerapi Com Rate Limits
  slug: webcrawlerapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: WebCrawlerAPI API Rules
  rule_count: 71
  severity_counts:
    error: 63
    hint: 0
    info: 3
    warn: 5
  slug: webcrawlerapi-com-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.0
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 57.2
    developer_ergonomics: 60.7
    discoverability: 87.5
    operational_transparency: 26.3
  previous_composite: 67.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/webcrawlerapi-com/webcrawlerapi-com-2026-10-11T194345.png
security:
- kind: authentication
  name: Webcrawlerapi Com Authentication
  slug: webcrawlerapi-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Webcrawlerapi Com Domain Security
  slug: webcrawlerapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Monitor a website for changes with Feeds
  slug: webcrawlerapi-com-monitor-website-with-feeds
- name: Run the WebCrawlerAPI crawling agent
  slug: webcrawlerapi-com-run-crawling-agent
- name: webcrawlerapi
  slug: webcrawlerapi-com-webcrawlerapi
slug: webcrawlerapi-com
tags:
- Web Scraping
- Web Crawling
- Data Extraction
- Markdown
- AI Agents
- LLM
- RAG
- Web Feeds
- Change Detection
- Structured Data
- MCP
- A2A
- Agent-Native
website: https://webcrawlerapi.com/
---
