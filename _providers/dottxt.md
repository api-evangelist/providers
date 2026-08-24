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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-24'
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
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dottxt Platform Chat API
  slug: open-dottxt-chat-api
- collection_type: open
  name: dottxt Platform Chat Models API
  slug: open-dottxt-models-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dottxt-platform-overlay.yaml
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
  name: dottxt MCP Server
  slug: dottxt-mcp-server
modified: '2026-07-18'
name: dottxt
nav: Providers
network: true
overview: 'dottxt publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include Company, Artificial Intelligence, LLM, Structured Outputs, and JSON-Schema.


  dottxt''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, and 17 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 30.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 14.9
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 30.1
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
- JSON-Schema
- Machine-Learning
- Developer Tools
- Constrained Decoding
website: https://docs.dottxt.ai
---
