---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dottxt Agentic Access
  operation_count: 2
  slug: dottxt-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: OpenAI-compatible chat completions with structured output.
  name: dottxt Chat API
  slug: dottxt-chat-api
- description: Models available to your API key.
  name: dottxt Models API
  slug: dottxt-models-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dottxt.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dottxt.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dottxt.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dottxt.ai/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://h1xbpbfsf0w.typeform.com/to/fwQNWmS8
- group: company
  title: ''
  type: Blog
  url: https://blog.dottxt.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dottxt-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dottxt.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dottxt.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/dottxt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dottxt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dottxt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dottxt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dottxt-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/dottxt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dottxt-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dottxt-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dottxt-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/dottxt-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dottxt-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dottxt-agentic-access.yml
created: '2026-07-17'
description: 'dottxt (styled .txt) is the company behind Outlines, the open-source structured-generation library for LLMs with 65M+ downloads. Its hosted platform API (api.dottxt.ai) is an OpenAI-compatible Chat Completions endpoint that guarantees 100% schema-compliant model output by construction using constrained decoding: pass a JSON Schema via `response_format` and the model produces exactly that shape — no retries, no validation loops, no defensive parsing. Output can be streamed as token deltas (SSE) or field-by-field as RFC 6902 JSON Patch events. dottxt also ships self-hosted, drop-in replacements for vLLM, SGLang and TensorRT-LLM inference servers, and composable libraries (dotjson for JSON Schema, dotgrammar for context-free grammars, dotlambda for function calling). Backed by EQT Ventures and Seedcamp.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dottxt.png
layout: provider
mcp_servers:
- description: ''
  name: dottxt-mcp.yml
  slug: dottxt-mcpyml
modified: '2026-07-18'
name: dottxt
nav: Providers
network: true
overview: 'dottxt publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include Company, Artificial Intelligence, LLM, Structured Outputs, and JSON Schema.


  dottxt''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, and 16 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 41.5
  delta: -5.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 49.2
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/dottxt/refs/heads/main/screenshots/dottxt-2026-07-25T212322.png
security:
- kind: authentication
  name: Dottxt Authentication
  slug: dottxt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dottxt Domain Security
  slug: dottxt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dottxt
tags:
- Company
- Artificial Intelligence
- LLM
- Structured Outputs
- JSON Schema
- Machine Learning
- Developer Tools
- Constrained Decoding
website: https://docs.dottxt.ai
---
