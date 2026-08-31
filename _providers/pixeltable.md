---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-30'
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
artifact_total: 9
common:
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
  title: ''
  type: AgentCard
  url: a2a/pixeltable-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pixeltable-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixeltable-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pixeltable-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/pixeltable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pixeltable-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pixeltable-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pixeltable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pixeltable-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pixeltable-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pixeltable-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixeltable-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pixeltable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pixeltable-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pixeltable-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pixeltable-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixeltable-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pixeltable-vulnerability-disclosure.yml
created: '2026-08-17'
description: 'Pixeltable is an open-source (Apache 2.0) Python data infrastructure company building a unified multimodal backend for AI data applications. A single `pip install pixeltable` provides declarative storage, transformation, indexing, retrieval, serving and versioning of images, video, audio, documents and structured data through computed columns that run AI inference incrementally on insert, embedding indexes that stay in sync for vector search, Python UDFs and query functions, and built-in table history and revert. The same declarative schema runs locally via `pxt serve` or a FastAPI router and deploys to Pixeltable Cloud via `pxt deploy` for managed databases, R2-backed media buckets, Deploy endpoints and serverless scale-to-zero workers. Pixeltable integrates 25-plus AI providers including OpenAI, Anthropic, Gemini, Hugging Face, Bedrock, Groq, Mistral, Together, Fireworks, Ollama and Whisper, and positions itself as a replacement for the glue between object storage, Postgres,
  a vector database, an orchestrator and a framework such as LangChain. The company is unusually agent-forward: it publishes an A2A agent card, a callable read-only WebMCP server, an NLWeb ask endpoint, an installable Agent Skill, markdown representations of its pages, and scoped llms.txt context files. A public REST API with OpenAPI and scoped OAuth is stated as in active development.'
image: https://pixeltable.com/images/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Pixeltable MCP Server
  slug: pixeltable-mcp-server
modified: '2026-08-17'
name: Pixeltable
nav: Providers
network: true
overview: 'Pixeltable publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Multimodal AI, AI Data Infrastructure, and Vector Search.


  Pixeltable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Pixeltable Plans Pricing
  plan_count: 4
  slug: pixeltable-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Pixeltable Rate Limits
  slug: pixeltable-rate-limits
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 51.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Open-Source
- Python
- Data Orchestration
- Computed Columns
- Video Processing
- Machine-Learning
website: https://www.pixeltable.com/
---
