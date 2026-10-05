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
  schema_version: '0.2'
  score: 65.0
  scored_at: '2026-10-04'
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
  phrasing_intents:
  - id: chat_completions_v1beta_chat_completions_post
    intent: Get a chat completion grounded in web research
    question: Can I get chat-style answers from Parallel using an OpenAI-compatible chat completions request?
  phrasing_ops: 1
  slug: parallel-chat-api-beta-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: Extract returns excerpts or full content from one or more URLs. Inputs are a list of URLs and an optional search objective and keyword queries. The returned excerpts or full content is formatted as ma
  name: Parallel Extract API
  phrasing_intents:
  - id: extract_v1_extract_post
    intent: Extract content from specific web pages
    question: How can I pull the readable content out of a handful of web page URLs?
  phrasing_ops: 1
  slug: parallel-extract-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditi
  name: Parallel FindAll API
  phrasing_intents:
  - id: findall_entity_search_v1beta_findall_entity_search_post
    intent: Quickly search for ranked entities
    question: Is there a fast, low-latency way to get a ranked list of companies matching a plain-language description?
  - id: ingest_findall_run_v1beta_findall_ingest_post
    intent: Turn an objective into a FindAll run spec
    question: Can I turn a plain-English goal into a suggested FindAll specification before starting a run?
  - id: findall_runs_v1_v1beta_findall_runs_post
    intent: Start a FindAll run to discover entities
    question: How do I kick off a FindAll run to find every company that meets my criteria?
  - id: findall_runs_v1_get_v1beta_findall_runs__findall_id__get
    intent: Check the status of a FindAll run
    question: Is my FindAll run still queued, running, or finished?
  - id: cancel_findall_run_v1beta_findall_runs__findall_id__cancel_post
    intent: Cancel a FindAll run
    question: How do I stop a FindAll run that I no longer need?
  - id: enrich_findall_run_v1beta_findall_runs__findall_id__enrich_post
    intent: Add enrichment fields to a FindAll run
    question: Can I add extra researched columns, like headcount or funding, to the entities a FindAll run found?
  - id: get_findall_events_v1beta_findall_runs__findall_id__events_get
    intent: Stream live events from a FindAll run
    question: Can I subscribe to real-time updates as a FindAll run discovers matches?
  - id: extend_findall_run_v1beta_findall_runs__findall_id__extend_post
    intent: Raise the match limit of a FindAll run
    question: My FindAll run hit its match limit; can I ask it to find more entities?
  phrasing_ops: 10
  slug: parallel-findall-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Monitor API watches the web for material changes on a fixed frequency. Each monitor runs once on creation and then on its configured schedule, emitting events when meaningful changes are detected.
  name: Parallel Monitor API
  phrasing_intents:
  - id: create_monitor_v1_monitors_post
    intent: Create a monitor to track web changes
    question: How do I set up a monitor that alerts me when something material changes on the web?
  - id: list_monitors_v1_monitors_get
    intent: List my web monitors
    question: Which web monitors do I currently have running?
  - id: retrieve_monitor_v1_monitors__monitor_id__get
    intent: Get a monitor's configuration
    question: What frequency, query and webhook is a particular monitor configured with?
  - id: cancel_monitor_v1_monitors__monitor_id__cancel_post
    intent: Permanently stop a monitor
    question: How do I permanently stop a monitor from running?
  - id: list_monitor_events_v1_monitors__monitor_id__events_get
    intent: List the changes a monitor detected
    question: What material changes has my monitor picked up recently?
  - id: trigger_monitor_run_v1_monitors__monitor_id__trigger_post
    intent: Run a monitor immediately
    question: Can I make a monitor check for changes right now instead of waiting for its schedule?
  - id: update_monitor_v1_monitors__monitor_id__update_post
    intent: Change a monitor's settings
    question: Can I change how often an existing monitor runs?
  phrasing_ops: 7
  slug: parallel-monitor-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: Search returns ranked URLs with extended excerpts suitable for LLM consumption. Inputs are a natural-language objective and optional keyword queries. Source policies allow including or excluding speci
  name: Parallel Search API
  phrasing_intents:
  - id: v1_search_v1_search_post
    intent: Search the web with keyword queries
    question: How do I run a web search and get back excerpts I can feed to an LLM?
  phrasing_ops: 1
  slug: parallel-search-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Task API executes web research and extraction tasks. Clients submit a natural-language objective with an optional input schema; the service plans retrieval, fetches relevant URLs, and returns outp
  name: Parallel Tasks API
  phrasing_intents:
  - id: tasks_taskgroups_post_v1_tasks_groups_post
    intent: Create a task group to batch runs
    question: How do I group many task runs together so I can track them as one batch?
  - id: tasks_taskgroups_get_v1_tasks_groups__taskgroup_id__get
    intent: Get aggregated status of a task group
    question: How many runs in my task group have finished versus are still running?
  - id: tasks_sessions_events_get_v1_tasks_groups__taskgroup_id__events_get
    intent: Stream status events for a task group
    question: Can I get live notifications as runs in a task group complete?
  - id: tasks_taskgroups_runs_post_v1_tasks_groups__taskgroup_id__runs_post
    intent: Add a batch of task runs to a group
    question: How many task runs can I add to a task group in a single request?
  - id: tasks_taskgroups_runs_get_v1_tasks_groups__taskgroup_id__runs_get
    intent: Fetch the runs in a task group
    question: How do I get every run in a task group along with its inputs and outputs?
  - id: tasks_taskgroups_runs_id_get_v1_tasks_groups__taskgroup_id__runs__run_id__get
    intent: Check one run inside a task group
    question: Can I look up the status of a single run within a specific task group?
  - id: tasks_runs_post_v1_tasks_runs_post
    intent: Start a web research task run
    question: How do I start a single research task with Parallel and get structured output?
  - id: tasks_runs_get_v1_tasks_runs__run_id__get
    intent: Check a task run's status
    question: Is my task run still queued or has it finished?
  phrasing_ops: 12
  slug: parallel-tasks-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: The Memory API lets agents search and reuse the results of past Task, Monitor and FindAll runs so new research builds on work already done. It exposes retrieve, evict and clear operations over the sto
  name: Parallel Memory API
  phrasing_intents:
  - id: clear_memory_v1beta_memory_clear_post
    intent: Clear all entries from a memory scope
    question: How do I wipe everything stored in my Parallel memory?
  - id: evict_memory_source_v1beta_memory_evict_post
    intent: Remove one run or monitor from memory
    question: Can I remove a single task run from memory without deleting the run itself?
  - id: retrieve_memory_v1beta_memory_retrieve_post
    intent: Look up relevant or recent memories
    question: How can I find past research runs in memory that relate to a topic?
  phrasing_ops: 3
  slug: parallel-memory-api
- baseURL: https://api.parallel.ai
  baseurl_source: declared
  description: An OpenAI-Responses-compatible interface for answers grounded in live web research, with URL citations. Point any Responses-API client — the OpenAI Python SDK, OpenAI TypeScript SDK, the Agents SDK, o
  name: Parallel Responses API
  phrasing_intents:
  - id: create_response_v1_responses_post
    intent: Generate a cited answer from live web research
    question: Can I get an answer with URL citations grounded in live web research using the OpenAI Responses format?
  phrasing_ops: 1
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
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/changelog/parallel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/parallel-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parallel.ai/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/lifecycle/parallel-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/parallel-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/authentication/parallel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parallel-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/packages/parallel-packages.yml
  title: ''
  type: Packages
  url: packages/parallel-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/packages/parallel-packages.yml
  title: ''
  type: SDKs
  url: packages/parallel-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/cli/parallel-cli.yml
  title: ''
  type: CLI
  url: cli/parallel-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/mcp/parallel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/parallel-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/llms/parallel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parallel-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/overlays/parallel-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/parallel-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/well-known/parallel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parallel-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/conformance/parallel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parallel-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/security/parallel-trust-center.yml
  title: ''
  type: Compliance
  url: security/parallel-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/security/parallel-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/parallel-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/errors/parallel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parallel-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/lifecycle/parallel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/parallel-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/conventions/parallel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/parallel-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/data-model/parallel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parallel-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/rate-limits/parallel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/parallel-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/asyncapi/parallel-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/parallel-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/security/parallel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parallel-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/agentic-access/parallel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/parallel-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/a2a/parallel-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/parallel-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/mcp/parallel-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/parallel-tool-crosswalk.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/plans/parallel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parallel-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/scopes/parallel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/parallel-scopes.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/parallel/refs/heads/main/sandbox/parallel-sandbox.yml
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
created: '2026-07-17'
description: 'Parallel Web Systems builds web APIs purpose-built for AI agents: a high-accuracy Search API, an Extract API that turns URLs into clean LLM-ready markdown, a Task/Deep Research API with tiered processors (lite through ultra), FindAll for natural-language entity discovery and enrichment, a Monitor API for scheduled web-change tracking, an OpenAI-compatible Responses and Chat Completions pair, and a Memory API that lets agents reuse past research. The platform is API-key authenticated over https://api.parallel.ai, ships official Python and TypeScript SDKs and a CLI, emits Standard Webhooks and SSE event streams, and is SOC 2 Type I/II certified. Its agent surface is unusually complete: an anonymous hosted MCP server whose tools are publicly introspectable, an OAuth-gated Task MCP server, a conformant A2A agent card backed by a live /a2a endpoint, provider-published Agent Skills with a discovery document, an llms.txt, and markdown twins of every documentation page. Pricing is
  pay-as-you-go per request per product. Originally surfaced as a Kleiner Perkins portfolio company and enriched from Parallel''s public developer surface.'
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
overview: 'Parallel publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Chat API (Beta) API, Extract API, FindAll API, and 5 more. Tagged areas include Company, Artificial Intelligence, Web Search, Agents, and Deep Research.


  The Parallel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Parallel''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, support, and 36 more developer resources.'
plans:
- name: Parallel Plans Pricing
  plan_count: 1
  slug: parallel-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 7
  name: Parallel Rate Limits
  slug: parallel-rate-limits
scopes:
- name: Parallel Scopes
  scope_count: 1
  slug: parallel-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 66.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 59.6
    developer_ergonomics: 76.8
    discoverability: 75.0
    operational_transparency: 81.6
  previous_composite: 66.6
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- A2A
website: https://www.parallel.ai
---
