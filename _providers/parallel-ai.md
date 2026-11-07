---
access_model:
  confidence: high
  label: Self-serve signup, pay-as-you-go, free tier
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://docs.parallel.ai/getting-started/pricing
  - https://parallel.ai/pricing
  - https://docs.parallel.ai/integrations/mcp/search-mcp
  trial: true
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 66.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Parallel Agentic Access
  operation_count: 36
  slug: parallel-agentic-access
  summary_line: 36 operations · 18 acting
api_count: 10
apis:
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Chat API provides a programmatic chat-style text generation interface. It accepts a sequence of messages and returns model responses. Intended for assistant-like interactions and evaluation. Strea
  name: Parallel Chat API (Beta) API
  slug: parallel-ai-chat-api-beta-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: Extract returns excerpts or full content from one or more URLs. Inputs are a list of URLs and an optional search objective and keyword queries. The returned excerpts or full content is formatted as ma
  name: Parallel Extract API
  slug: parallel-ai-extract-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditi
  name: Parallel Find All API
  slug: parallel-ai-findall-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Memory API retrieves and manages memories created by Tasks, Monitors, and FindAll runs. Memories can be personal or isolated with a `memory_scope_key`.
  name: Parallel Memory API
  slug: parallel-ai-memory-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Monitor API watches the web for material changes on a fixed frequency. Each monitor runs once on creation and then on its configured schedule, emitting events when meaningful changes are detected.
  name: Parallel Monitor API
  slug: parallel-ai-monitor-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: An OpenAI-Responses-compatible interface for answers grounded in live web research, with URL citations. Point any Responses-API client — the OpenAI Python SDK, OpenAI TypeScript SDK, the Agents SDK, o
  name: Parallel Responses API
  slug: parallel-ai-responses-api-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: Search returns ranked URLs with extended excerpts suitable for LLM consumption. Inputs are a natural-language objective and optional keyword queries. Source policies allow including or excluding speci
  name: Parallel Search API
  slug: parallel-ai-search-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Task API executes web research and extraction tasks. Clients submit a natural-language objective with an optional input schema; the service plans retrieval, fetches relevant URLs, and returns outp
  name: Parallel Tasks API
  slug: parallel-ai-tasks-api
artifact_total: 35
asyncapis:
- description: ''
  name: Parallel Webhooks
  slug: parallel-webhooks
collections:
- collection_type: postman
  name: Parallel Chat API (Beta) Chat API (Beta) Chat API (Beta) API
  slug: postman-parallel-chat-api-beta-api
- collection_type: postman
  name: Parallel Chat API (Beta) Chat API (Beta) Extract API
  slug: postman-parallel-extract-api
- collection_type: postman
  name: Parallel Chat API (Beta) Chat API (Beta) FindAll API
  slug: postman-parallel-findall-api
- collection_type: postman
  name: Parallel Chat API (Beta) Chat API (Beta) Monitor API
  slug: postman-parallel-monitor-api
- collection_type: postman
  name: Parallel Chat API (Beta) Chat API (Beta) Search API
  slug: postman-parallel-search-api
- collection_type: postman
  name: Parallel Chat API (Beta) Chat API (Beta) Tasks API
  slug: postman-parallel-tasks-api
- collection_type: open
  name: Parallel Chat API (Beta) Chat API (Beta) Chat API (Beta) API
  slug: open-parallel-chat-api-beta-api
- collection_type: open
  name: Parallel Chat API (Beta) Chat API (Beta) Extract API
  slug: open-parallel-extract-api
- collection_type: open
  name: Parallel Chat API (Beta) Chat API (Beta) FindAll API
  slug: open-parallel-findall-api
- collection_type: open
  name: Parallel Chat API (Beta) Chat API (Beta) Monitor API
  slug: open-parallel-monitor-api
- collection_type: open
  name: Parallel Chat API (Beta) Chat API (Beta) Search API
  slug: open-parallel-search-api
- collection_type: open
  name: Parallel Chat API (Beta) Chat API (Beta) Tasks API
  slug: open-parallel-tasks-api
common:
- group: other
  href: https://artifacts.apis.io/parallel-ai/capabilities/parallel-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/parallel-ai-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/parallel/overview
- group: company
  title: ''
  type: Website
  url: https://www.parallel.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.parallel.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parallel.ai/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parallel.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.parallel.ai/getting-started/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.parallel.ai/getting-started/pricing
- group: company
  title: ''
  type: Blog
  url: https://parallel.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parallel-web
- group: start
  title: ''
  type: SignUp
  url: https://platform.parallel.ai
- group: operate
  title: ''
  type: Support
  url: https://docs.parallel.ai/resources/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parallel.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parallel.ai/privacy-policy
- group: operate
  href: https://artifacts.apis.io/parallel-ai/changelog/parallel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/parallel-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parallel.ai/
- group: operate
  href: https://artifacts.apis.io/parallel-ai/lifecycle/parallel-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/parallel-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/parallel-ai/authentication/parallel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parallel-authentication.yml
- group: build
  href: https://artifacts.apis.io/parallel-ai/packages/parallel-packages.yml
  title: ''
  type: Packages
  url: packages/parallel-packages.yml
- group: build
  href: https://artifacts.apis.io/parallel-ai/packages/parallel-packages.yml
  title: ''
  type: SDKs
  url: packages/parallel-packages.yml
- group: build
  href: https://artifacts.apis.io/parallel-ai/cli/parallel-cli.yml
  title: ''
  type: CLI
  url: cli/parallel-cli.yml
- group: agent
  href: https://artifacts.apis.io/parallel-ai/mcp/parallel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/parallel-mcp.yml
- group: agent
  href: https://artifacts.apis.io/parallel-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/parallel-ai/llms/parallel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parallel-llms.txt
- group: other
  href: https://artifacts.apis.io/parallel-ai/overlays/parallel-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/parallel-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/parallel-ai/well-known/parallel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parallel-well-known.yml
- group: design
  href: https://artifacts.apis.io/parallel-ai/conformance/parallel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parallel-conformance.yml
- group: auth
  href: https://artifacts.apis.io/parallel-ai/security/parallel-trust-center.yml
  title: ''
  type: Compliance
  url: security/parallel-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/parallel-ai/security/parallel-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/parallel-trust-center.yml
- group: design
  href: https://artifacts.apis.io/parallel-ai/errors/parallel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parallel-problem-types.yml
- group: design
  href: https://artifacts.apis.io/parallel-ai/lifecycle/parallel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/parallel-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/parallel-ai/conventions/parallel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/parallel-conventions.yml
- group: design
  href: https://artifacts.apis.io/parallel-ai/data-model/parallel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parallel-data-model.yml
- group: operate
  href: https://artifacts.apis.io/parallel-ai/rate-limits/parallel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/parallel-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/parallel-ai/asyncapi/parallel-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/parallel-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/parallel-ai/security/parallel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parallel-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/parallel-ai/agentic-access/parallel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/parallel-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/parallel-ai/a2a/parallel-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/parallel-a2a.yml
- group: build
  href: https://artifacts.apis.io/parallel-ai/mcp/parallel-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/parallel-tool-crosswalk.yml
- group: commercial
  href: https://artifacts.apis.io/parallel-ai/plans/parallel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parallel-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/parallel-ai/scopes/parallel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/parallel-scopes.yml
- group: start
  href: https://artifacts.apis.io/parallel-ai/sandbox/parallel-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/parallel-sandbox.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/parallel/overview
- group: operate
  title: ''
  type: Contact
  url: mailto:partnerships@parallel.ai
- group: company
  title: ''
  type: Website
  url: https://parallel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parallel.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parallel.ai/api-reference/search/search
created: '2026-07-17'
description: 'Parallel Web Systems builds web APIs purpose-built for AI agents: a high-accuracy Search API, an Extract API that turns URLs into clean LLM-ready markdown, a Task/Deep Research API with tiered processors (lite through ultra), FindAll for natural-language entity discovery and enrichment, a Monitor API for scheduled web-change tracking, an OpenAI-compatible Responses and Chat Completions pair, and a Memory API that lets agents reuse past research. The platform is API-key authenticated over https://api.parallel.ai, ships official Python and TypeScript SDKs and a CLI, emits Standard Webhooks and SSE event streams, and is SOC 2 Type I/II certified. Its agent surface is unusually complete: an anonymous hosted MCP server whose tools are publicly introspectable, an OAuth-gated Task MCP server, a conformant A2A agent card backed by a live /a2a endpoint, provider-published Agent Skills with a discovery document, an llms.txt, and markdown twins of every documentation page. Pricing is
  pay-as-you-go per request per product. Originally surfaced as a Kleiner Perkins portfolio company and enriched from Parallel''s public developer surface.'
finops:
- has_sources: true
  method: derived
  name: Parallel Ai Finops
  primary_unit: 1,000 requests
  service_category: ''
  slug: parallel-ai-finops
  template: false
image: https://cdn.sanity.io/images/5hzduz3y/production/3e8afb3fd62096a800a8135910fdc375971e17ba-3600x1890.jpg?w=1200&h=630&fit=crop
layout: provider
mcp_servers:
- description: Remote MCP server at search.parallel.ai.
  name: Parallel MCP Server
  slug: parallel-mcp-yml
modified: '2026-08-14'
name: Parallel
nav: Providers
network: true
overview: 'Parallel publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chat API (Beta) API, Extract API, Find All API, and 5 more. Tagged areas include Company, Artificial Intelligence, Web Search, Agents, and Deep Research.


  The Parallel catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Parallel''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, support, and 40 more developer resources.'
plans:
- name: Parallel Ai Price Estimates
  plan_count: 0
  slug: parallel-ai-price-estimates
- name: Parallel Plans Pricing
  plan_count: 9
  slug: parallel-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 7
  name: Parallel Rate Limits
  slug: parallel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Parallel API Rules
  rule_count: 66
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 10
  slug: parallel-ai-rules
scopes:
- name: Parallel Scopes
  scope_count: 1
  slug: parallel-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 71.3
    developer_ergonomics: 78.3
    discoverability: 80.0
    operational_transparency: 81.6
  previous_composite: 73.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/parallel-ai/parallel-2026-08-17T124455.png
security:
- kind: authentication
  name: Parallel Authentication
  slug: parallel-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Parallel Domain Security
  slug: parallel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Parallel Trust Center
  slug: parallel-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II
skill_count: 3
skills:
- name: Run a deep-research Task and fetch the result
  slug: parallel-deep-research
- name: Parallel
  slug: parallel-published-skill
- name: Search the web and extract page content
  slug: parallel-search-and-extract
slug: parallel-ai
tags:
- Company
- Artificial Intelligence
- Web Search
- Agents
- Deep Research
- Web Extraction
- Data Enrichment
- Web Monitoring
- LLM Tools
- A2A
- AI Agents
- MCP
- Agent Skills
- Content Extraction
- Entity Resolution
website: https://www.parallel.ai
---
