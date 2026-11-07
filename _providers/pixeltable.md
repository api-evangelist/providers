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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Read-only Model Context Protocol server served over HTTP at the Pixeltable apex host. Protocol version 2025-06-18, JSON-RPC 2.0 (initialize, tools/list, tools/call). Exposes two tools: search_docs, wh'
  name: Pixeltable WebMCP Server
  slug: pixeltable-webmcp
- description: NLWeb natural-language question-answering endpoint. POST a JSON body containing a non-empty `query` to receive grounded answers with schema.org-typed source results; supports SSE streaming. Answered a
  name: Pixeltable Ask API (NLWeb)
  slug: pixeltable-ask
- description: The authenticated HTTP API behind the Pixeltable Cloud dashboard and the `pxt` CLI. The provider publishes the base URL https://internal-api.pixeltable.com in /.well-known/agent.json and marks it auth
  name: Pixeltable Cloud Control Plane API
  slug: pixeltable-cloud-control-plane
artifact_total: 12
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/pixeltable/pixeltable/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.pixeltable.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pixeltable.com/developers/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pixeltable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pixeltable.com/sdk/latest/pixeltable
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pixeltable.com/overview/pixeltable
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/QPyqFYx2UN
- group: company
  title: ''
  type: Blog
  url: https://pixeltable.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://pixeltable.com/blog/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixeltable
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pixeltable/pixeltable
- group: commercial
  title: ''
  type: Pricing
  url: https://pixeltable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://pixeltable.com/signup
- group: start
  title: ''
  type: Login
  url: https://pixeltable.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pixeltable.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pixeltable.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://pixeltable.com/status
- group: auth
  title: ''
  type: Security
  url: https://pixeltable.com/security
- group: other
  title: ''
  type: Sitemap
  url: https://pixeltable.com/sitemap.xml
- group: other
  href: https://artifacts.apis.io/pixeltable/a2a/pixeltable-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pixeltable-a2a.yml
- group: agent
  href: https://artifacts.apis.io/pixeltable/mcp/pixeltable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pixeltable-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pixeltable/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/pixeltable/llms/pixeltable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pixeltable-llms.txt
- group: agent
  href: https://artifacts.apis.io/pixeltable/well-known/pixeltable-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pixeltable-well-known.yml
- group: build
  href: https://artifacts.apis.io/pixeltable/packages/pixeltable-packages.yml
  title: ''
  type: Packages
  url: packages/pixeltable-packages.yml
- group: build
  href: https://artifacts.apis.io/pixeltable/packages/pixeltable-packages.yml
  title: ''
  type: SDKs
  url: packages/pixeltable-packages.yml
- group: build
  href: https://artifacts.apis.io/pixeltable/cli/pixeltable-cli.yml
  title: ''
  type: CLI
  url: cli/pixeltable-cli.yml
- group: commercial
  href: https://artifacts.apis.io/pixeltable/plans/pixeltable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pixeltable-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/pixeltable/rate-limits/pixeltable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pixeltable-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/pixeltable/changelog/pixeltable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pixeltable-changelog.yml
- group: design
  href: https://artifacts.apis.io/pixeltable/lifecycle/pixeltable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pixeltable-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/pixeltable/authentication/pixeltable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pixeltable-authentication.yml
- group: design
  href: https://artifacts.apis.io/pixeltable/conventions/pixeltable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pixeltable-conventions.yml
- group: design
  href: https://artifacts.apis.io/pixeltable/errors/pixeltable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pixeltable-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pixeltable/conformance/pixeltable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pixeltable-conformance.yml
- group: start
  href: https://artifacts.apis.io/pixeltable/sandbox/pixeltable-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pixeltable-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/pixeltable/security/pixeltable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixeltable-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/pixeltable/security/pixeltable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pixeltable-vulnerability-disclosure.yml
created: '2026-08-17'
description: 'Pixeltable is an open-source (Apache 2.0) Python data infrastructure company building a unified multimodal backend for AI data applications. A single `pip install pixeltable` provides declarative storage, transformation, indexing, retrieval, serving and versioning of images, video, audio, documents and structured data through computed columns that run AI inference incrementally on insert, embedding indexes that stay in sync for vector search, Python UDFs and query functions, and built-in table history and revert. The same declarative schema runs locally via `pxt serve` or a FastAPI router and deploys to Pixeltable Cloud via `pxt deploy` for managed databases, R2-backed media buckets, Deploy endpoints and serverless scale-to-zero workers. Pixeltable integrates 25-plus AI providers including OpenAI, Anthropic, Gemini, Hugging Face, Bedrock, Groq, Mistral, Together, Fireworks, Ollama and Whisper, and positions itself as a replacement for the glue between object storage, Postgres,
  a vector database, an orchestrator and a framework such as LangChain. The company is unusually agent-forward: it publishes an A2A agent card, a callable read-only WebMCP server, an NLWeb ask endpoint, an installable Agent Skill, markdown representations of its pages, and scoped llms.txt context files. A public REST API with OpenAPI and scoped OAuth is stated as in active development.'
finops:
- has_sources: true
  method: derived
  name: Pixeltable Finops
  primary_unit: organization
  service_category: ''
  slug: pixeltable-finops
  template: false
image: https://pixeltable.com/images/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at pixeltable.com over HTTP; 2 tools listed.
  name: Pixeltable MCP Server
  slug: pixeltable-web
modified: '2026-08-17'
name: Pixeltable
nav: Providers
network: true
overview: 'Pixeltable is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Multimodal AI, AI Data Infrastructure, and Vector Search.


  Pixeltable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Pixeltable Plans Pricing
  plan_count: 4
  slug: pixeltable-plans-pricing
- name: Pixeltable Price Estimates
  plan_count: 0
  slug: pixeltable-price-estimates
random_paper: 10
rate_limits:
- limit_count: 1
  name: Pixeltable Rate Limits
  slug: pixeltable-rate-limits
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 63.0
    catalog_earned_first_party: 20.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 80.0
    operational_transparency: 65.8
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pixeltable/pixeltable-2026-09-02T151335.png
security:
- kind: authentication
  name: Pixeltable Authentication
  slug: pixeltable-authentication
  summary_line: none/apiKey/session · 5 schemes
- kind: domain-security
  name: Pixeltable Domain Security
  slug: pixeltable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pixeltable Vulnerability Disclosure
  slug: pixeltable-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 1
skills:
- name: Pixeltable
  slug: pixeltable-skill
slug: pixeltable
tags:
- Company
- Ai Data
- Multimodal AI
- AI Data Infrastructure
- Vector Search
- Embeddings
- RAG
- Agent Memory
- MCP
- Open Source
- Python
- Data Orchestration
- Computed Columns
- Video Processing
- Machine Learning
- A2A
website: https://www.pixeltable.com/
---
