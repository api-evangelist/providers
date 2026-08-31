---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Langdb Agentic Access
  operation_count: 10
  slug: langdb-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 1
apis:
- description: Usage analytics and cost summaries.
  name: LangDB Analytics API
  slug: langdb-analytics-api
- description: OpenAI-compatible chat completions and model routing.
  name: LangDB Chat API
  slug: langdb-chat-api
- description: Vector embeddings for input text.
  name: LangDB Embeddings API
  slug: langdb-embeddings-api
- description: Image generation.
  name: LangDB Images API
  slug: langdb-images-api
- description: Catalog of models available through the gateway.
  name: LangDB Models API
  slug: langdb-models-api
- description: Conversation threads, their messages, and per-thread cost.
  name: LangDB Threads API
  slug: langdb-threads-api
artifact_total: 22
asyncapis:
- description: AsyncAPI 2.6 description of LangDB's **chat completion streaming** surface. LangDB does not publish a WebSocket API for chat. The asynchronous / event-style transport documented at https://docs.langdb
  name: LangDB Chat Completions Streaming (HTTP + SSE)
  slug: langdb-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LangDB AI Gateway Analytics API
  slug: open-langdb-analytics-api
- collection_type: open
  name: LangDB AI Gateway Analytics Chat API
  slug: open-langdb-chat-api
- collection_type: open
  name: LangDB AI Gateway Analytics Embeddings API
  slug: open-langdb-embeddings-api
- collection_type: open
  name: LangDB AI Gateway Analytics Images API
  slug: open-langdb-images-api
- collection_type: open
  name: LangDB AI Gateway Analytics Models API
  slug: open-langdb-models-api
- collection_type: open
  name: LangDB AI Gateway Analytics Threads API
  slug: open-langdb-threads-api
- collection_type: open
  name: LangDB AI Gateway API
  slug: open-langdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/langdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langdb-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/langdb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langdb
- group: company
  title: ''
  type: Website
  url: https://langdb.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langdb.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/langdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/langdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/langdb-finops.yml
created: '2026-06-20'
description: LangDB is an AI gateway and governance platform that routes requests across 250+ models from providers such as OpenAI, Anthropic, Google, Meta, Mistral, and DeepSeek through a single project-scoped, OpenAI-compatible REST API. It layers routing, guardrails, tracing, cost control, and an MCP (Model Context Protocol) gateway on top of that unified interface.
finops:
- name: Langdb Finops
  service_category: AI and Machine Learning
  slug: langdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/langdb.png
layout: provider
modified: '2026-06-20'
name: LangDB
nav: Providers
network: true
overview: 'LangDB publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Chat API, Embeddings API, and 3 more. Tagged areas include Artificial Intelligence, LLM, AI Gateway, Routing, and Governance.


  The LangDB catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LangDB''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Langdb Plans Pricing
  plan_count: 4
  slug: langdb-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Langdb Rate Limits
  slug: langdb-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: LangDB API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: langdb-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 64.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langdb/refs/heads/main/screenshots/langdb-2026-06-20T184302.png
security:
- kind: authentication
  name: Langdb Authentication
  slug: langdb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Langdb Domain Security
  slug: langdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: langdb
tags:
- Artificial Intelligence
- LLM
- AI Gateway
- Routing
- Governance
- MCP
website: https://langdb.ai
---
