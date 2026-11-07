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
  - scopes
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Mrscraper Agentic Access
  operation_count: 15
  slug: mrscraper-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 2
apis:
- description: Synchronous Google SERP endpoint (POST https://sync.scraper.mrscraper.com/api/google/serp/v2/sync) returning structured search results in JSON or HTML from a query or a complete Google search URL; doc
  name: MrScraper Google SERP API
  slug: mrscraper-google-serp-api
- description: 'Official Model Context Protocol server: hosted Streamable HTTP endpoint at https://mcp.mrscraper.com/mcp behind OAuth 2.1 (PKCE, dynamic client registration, scopes scrape:read / scrape:write / accoun'
  name: MrScraper MCP Server
  slug: mrscraper-mcp-server
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The Analytic API from MrScraper — 1 operation(s) for analytic.
  name: MrScraper Analytic API
  slug: mrscraper-analytic-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The auth API from MrScraper — 1 operation(s) for auth.
  name: MrScraper Auth API
  slug: mrscraper-auth-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The gateway API from MrScraper — 1 operation(s) for gateway.
  name: MrScraper Gateway API
  slug: mrscraper-gateway-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The jobs API from MrScraper — 2 operation(s) for jobs.
  name: MrScraper Jobs API
  slug: mrscraper-jobs-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The Proxies API from MrScraper — 1 operation(s) for proxies.
  name: MrScraper Proxies API
  slug: mrscraper-proxies-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The Results API from MrScraper — 1 operation(s) for results.
  name: MrScraper Results API
  slug: mrscraper-results-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The storage API from MrScraper — 1 operation(s) for storage.
  name: MrScraper Storage API
  slug: mrscraper-storage-api
- baseURL: https://api.mrscraper.com
  baseurl_source: declared
  description: The tasks API from MrScraper — 4 operation(s) for tasks.
  name: MrScraper Tasks API
  slug: mrscraper-tasks-api
artifact_total: 35
asyncapis:
- description: ''
  name: Mrscraper Webhooks
  slug: mrscraper-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.app.mrscraper.com</code
- group: agent
  href: https://artifacts.apis.io/mrscraper/agentic-access/mrscraper-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mrscraper-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/mrscraper/rate-limits/mrscraper-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mrscraper-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mrscraper/plans/mrscraper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mrscraper-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/rules/mrscraper-rules.yml
  title: ''
  type: Spectral
  url: rules/mrscraper-rules.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/json-ld/mrscraper-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mrscraper-context.jsonld
- group: design
  href: https://artifacts.apis.io/mrscraper/vocabulary/mrscraper-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mrscraper-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mrscraper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/asyncapi/mrscraper-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mrscraper-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/data-model/mrscraper-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mrscraper-data-model.yml
- group: build
  href: https://artifacts.apis.io/mrscraper/cli/mrscraper-cli.yml
  title: ''
  type: CLI
  url: cli/mrscraper-cli.yml
- group: operate
  href: https://artifacts.apis.io/mrscraper/changelog/mrscraper-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mrscraper-changelog.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/conventions/mrscraper-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mrscraper-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://mrscraper.com/trust
- group: auth
  href: https://artifacts.apis.io/mrscraper/scopes/mrscraper-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mrscraper-scopes.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/lifecycle/mrscraper-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mrscraper-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/errors/mrscraper-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mrscraper-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mrscraper/conformance/mrscraper-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mrscraper-conformance.yml
- group: other
  href: https://artifacts.apis.io/mrscraper/overlays/mrscraper-scraper-service-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mrscraper-scraper-service-gateway-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mrscraper/llms/mrscraper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mrscraper-llms.txt
- group: build
  href: https://artifacts.apis.io/mrscraper/mcp/mrscraper-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mrscraper-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/mrscraper/mcp/mrscraper-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mrscraper-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mrscraper/well-known/mrscraper-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mrscraper-well-known.yml
- group: other
  href: https://artifacts.apis.io/mrscraper/hosts/mrscraper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mrscraper-hosts.yml
- group: other
  href: https://artifacts.apis.io/mrscraper/vendors/mrscraper-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mrscraper-vendors.yml
- group: build
  href: https://artifacts.apis.io/mrscraper/packages/mrscraper-packages.yml
  title: ''
  type: SDKs
  url: packages/mrscraper-packages.yml
- group: build
  href: https://artifacts.apis.io/mrscraper/packages/mrscraper-packages.yml
  title: ''
  type: Packages
  url: packages/mrscraper-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mrscraper.com
- group: auth
  href: https://artifacts.apis.io/mrscraper/authentication/mrscraper-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mrscraper-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mrscraper/security/mrscraper-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mrscraper-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mrscraper/security/mrscraper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mrscraper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mrscraper.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mrscraper.com/docs/api/overview
- group: company
  title: ''
  type: Blog
  url: https://mrscraper.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mrscraper.com/docs/changelog/2026/v3.4.14
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mrscraper.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mrscraper.com/docs/getting-started/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://mrscraper.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mrscraper.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://mrscraper.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mrscraper.com/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mrscraper-com
- group: start
  title: ''
  type: Login
  url: https://app.mrscraper.com
created: '2026-10-07'
description: 'MrScraper is an AI-powered web scraping platform: a Scraper API (Web Renderer fetch, Scrape JSON/Markdown, screenshots, listing pages and sitemaps on api.mrscraper.com), a Platform API for creating, rerunning and managing scrapers and results (api.app.mrscraper.com/api/v1), Google SERP, residential proxies, a hosted OAuth 2.1 MCP server (mcp.mrscraper.com/mcp), a CLI with agent skills, Node, Python, LangChain and n8n SDKs, and webhooks.'
finops:
- has_sources: true
  method: derived
  name: Mrscraper Finops
  primary_unit: subscription
  service_category: ''
  slug: mrscraper-finops
  template: false
image: https://mrscraper.com/og.png
json_schemas:
- name: auth.SubscriptionAccount
  property_count: 16
  slug: mrscraper-auth-subscription-account
- name: gateway.RequestBody
  property_count: 8
  slug: mrscraper-gateway-request-body
- name: GetApiV1ProxiesUserRequestsBandwidthResponse
  property_count: 2
  slug: mrscraper-get-api-v1-proxies-user-requests-bandwidth-response
- name: GetApiV1ResultsResultidResponse
  property_count: 3
  slug: mrscraper-get-api-v1-results-resultid-response
- name: job.Job
  property_count: 6
  slug: mrscraper-job-job
- name: task.Task
  property_count: 19
  slug: mrscraper-task-task
- name: task.TaskSwagger
  property_count: 20
  slug: mrscraper-task-task-swagger
- name: task.UpdateTaskStatusRequest
  property_count: 4
  slug: mrscraper-task-update-task-status-request
jsonld:
- class_count: 18
  name: Mrscraper Context
  property_count: 65
  slug: mrscraper-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mrscraper.com over streamable HTTP requiring OAuth; 7 tools listed.
  name: MrScraper MCP
  slug: mrscraper-mcp
modified: '2026-10-07'
name: MrScraper
nav: Providers
network: true
overview: 'MrScraper publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytic API, Auth API, Gateway API, and 7 more. Tagged areas include Company, Web Scraping, Data Extraction, Proxies, and AI Agents.


  The MrScraper catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  MrScraper''s developer surface includes CLI, changelog, authentication, API reference, engineering blog, documentation, getting-started guide, and 36 more developer resources.'
plans:
- name: Mrscraper Plans Pricing
  plan_count: 4
  slug: mrscraper-plans-pricing
- name: Mrscraper Price Estimates
  plan_count: 0
  slug: mrscraper-price-estimates
random_paper: 15
rate_limits:
- limit_count: 3
  name: Mrscraper Rate Limits
  slug: mrscraper-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: MrScraper API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: mrscraper-rules
scopes:
- name: Mrscraper Scopes
  scope_count: 4
  slug: mrscraper-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.4
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 50.2
    developer_ergonomics: 50.0
    discoverability: 75.0
    operational_transparency: 57.9
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 44.4
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mrscraper/mrscraper-2026-10-11T111318.png
security:
- kind: authentication
  name: Mrscraper Authentication
  slug: mrscraper-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Mrscraper Domain Security
  slug: mrscraper-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Mrscraper Trust Center
  slug: mrscraper-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: mrscraper-fetch
  slug: mrscraper-fetch
- name: mrscraper-scrape
  slug: mrscraper-scrape
- name: mrscraper-serp
  slug: mrscraper-serp
- name: mrscraper
  slug: mrscraper
slug: mrscraper
tags:
- Company
- Web Scraping
- Data Extraction
- Proxies
- AI Agents
- MCP
- Search
- Browser Automation
website: https://mrscraper.com
---
