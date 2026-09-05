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
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 65.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Parallel Agentic Access
  operation_count: 32
  slug: parallel-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 2
apis:
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Chat API provides a programmatic chat-style text generation interface. It accepts a sequence of messages and returns model responses. Intended for assistant-like interactions and evaluation. Strea
  name: Parallel Chat API (Beta) API
  slug: parallel-chat-api-beta-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: Extract returns excerpts or full content from one or more URLs. Inputs are a list of URLs and an optional search objective and keyword queries. The returned excerpts or full content is formatted as ma
  name: Parallel Extract API
  slug: parallel-extract-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditi
  name: Parallel FindAll API
  slug: parallel-findall-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Monitor API watches the web for material changes on a fixed frequency. Each monitor runs once on creation and then on its configured schedule, emitting events when meaningful changes are detected.
  name: Parallel Monitor API
  slug: parallel-monitor-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: Search returns ranked URLs with extended excerpts suitable for LLM consumption. Inputs are a natural-language objective and optional keyword queries. Source policies allow including or excluding speci
  name: Parallel Search API
  slug: parallel-search-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Task API executes web research and extraction tasks. Clients submit a natural-language objective with an optional input schema; the service plans retrieval, fetches relevant URLs, and returns outp
  name: Parallel Tasks API
  slug: parallel-tasks-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Memory API lets agents search and reuse the results of past Task, Monitor and FindAll runs so new research builds on work already done. It exposes retrieve, evict and clear operations over the sto
  name: Parallel Memory API
  slug: parallel-memory-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: An OpenAI-Responses-compatible interface for answers grounded in live web research, with URL citations. Point any Responses-API client — the OpenAI Python SDK, OpenAI TypeScript SDK, the Agents SDK, o
  name: Parallel Responses API
  slug: parallel-responses-api-api
artifact_total: 30
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
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: ChangeLog
  url: changelog/parallel-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parallel.ai/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/parallel-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parallel-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/parallel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parallel-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/parallel-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parallel-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parallel-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/parallel-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parallel-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parallel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/parallel-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/parallel-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parallel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parallel-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parallel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parallel-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parallel-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/parallel-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parallel-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parallel-agentic-access.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/parallel-a2a.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/parallel-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/parallel-plans-pricing.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/parallel-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/parallel-sandbox.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/parallel/overview
created: '2026-07-17'
description: 'Parallel Web Systems builds web APIs purpose-built for AI agents: a high-accuracy Search API, an Extract API that turns URLs into clean LLM-ready markdown, a Task/Deep Research API with tiered processors (lite through ultra), FindAll for natural-language entity discovery and enrichment, a Monitor API for scheduled web-change tracking, an OpenAI-compatible Responses and Chat Completions pair, and a Memory API that lets agents reuse past research. The platform is API-key authenticated over https://api.parallel.ai, ships official Python and TypeScript SDKs and a CLI, emits Standard Webhooks and SSE event streams, and is SOC 2 Type I/II certified. Its agent surface is unusually complete: an anonymous hosted MCP server whose tools are publicly introspectable, an OAuth-gated Task MCP server, a conformant A2A agent card backed by a live /a2a endpoint, provider-published Agent Skills with a discovery document, an llms.txt, and markdown twins of every documentation page. Pricing is
  pay-as-you-go per request per product. Originally surfaced as a Kleiner Perkins portfolio company and enriched from Parallel''s public developer surface.'
image: https://cdn.sanity.io/images/5hzduz3y/production/3e8afb3fd62096a800a8135910fdc375971e17ba-3600x1890.jpg?w=1200&h=630&fit=crop
layout: provider
mcp_servers:
- description: ''
  name: Parallel MCP Server
  slug: parallel-mcp-server
modified: '2026-08-14'
name: Parallel
nav: Providers
network: true
overview: 'Parallel publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Chat API (Beta) API, Extract API, FindAll API, and 5 more. Tagged areas include Company, Artificial Intelligence, Web Search, Agents, and Deep Research.


  The Parallel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Parallel''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, support, and 35 more developer resources.'
plans:
- name: Parallel Plans Pricing
  plan_count: 1
  slug: parallel-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 7
  name: Parallel Rate Limits
  slug: parallel-rate-limits
scopes:
- name: Parallel Scopes
  scope_count: 0
  slug: parallel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 65.3
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/screenshots/parallel-2026-08-17T124455.png
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
slug: parallel
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
website: https://www.parallel.ai
---
