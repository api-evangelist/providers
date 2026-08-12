---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Waxell Agentic Access
  operation_count: 12
  slug: waxell-agentic-access
  summary_line: 12 operations · 10 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Waxell Developer MCP is a hosted Model Context Protocol server that lets coding agents (Claude Code, Cursor, Windsurf, VS Code, Claude Desktop) query a Waxell instance in real time. It exposes 15 live
  name: Waxell Developer MCP Server
  slug: developer-mcp
- description: Model cost catalog and tenant-level overrides
  name: Waxell Cost Management API
  slug: waxell-cost-management-api
- description: Pre-execution policy checks and audit events
  name: Waxell Governance API
  slug: waxell-governance-api
- description: Managed prompts retrievable by name and version
  name: Waxell Prompts API
  slug: waxell-prompts-api
- description: Lifecycle endpoints for agent execution runs
  name: Waxell Runs API
  slug: waxell-runs-api
- description: LLM calls, spans, steps, and quality scores recorded against a run
  name: Waxell Telemetry API
  slug: waxell-telemetry-api
artifact_total: 63
collections:
- collection_type: postman
  name: Waxell Observe Cost Management API
  slug: postman-waxell-cost-management-api
- collection_type: postman
  name: Waxell Observe Cost Management Governance API
  slug: postman-waxell-governance-api
- collection_type: postman
  name: Waxell Observe Cost Management Prompts API
  slug: postman-waxell-prompts-api
- collection_type: postman
  name: Waxell Observe Cost Management Runs API
  slug: postman-waxell-runs-api
- collection_type: postman
  name: Waxell Observe Cost Management Telemetry API
  slug: postman-waxell-telemetry-api
- collection_type: open
  name: Waxell Observe API
  slug: open-waxell-observe
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/waxell/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/waxell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waxell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/waxell-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://waxell.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://waxell.ai/docs/observe/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://waxell.ai/docs/observe/quickstart
- group: build
  title: ''
  type: SDKs
  url: https://waxell.ai/docs/observe/quickstart
- group: start
  title: ''
  type: Console
  url: https://waxell.dev
- group: start
  title: ''
  type: Signup
  url: https://waxell.ai/get-access
- group: commercial
  title: ''
  type: Pricing
  url: https://waxell.ai/get-access
- group: commercial
  title: ''
  type: Plans
  url: plans/waxell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/waxell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/waxell-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.waxell.dev
- group: company
  title: ''
  type: Blog
  url: https://waxell.ai/blog
- group: other
  title: ''
  type: Glossary
  url: https://waxell.ai/glossary
- group: auth
  title: ''
  type: Security
  url: https://waxell.ai/docs/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/callsine.com/trust/pg7qc55eh5ge6ejjv7zxksy
- group: auth
  title: ''
  type: Compliance
  url: https://waxell.ai/docs/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waxell-ai
- group: build
  title: ''
  type: GitHubRepository
  url: https://gitlab.com/waxell/agentforge
- group: design
  title: ''
  type: SpectralRules
  url: rules/waxell-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/waxell-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/waxell-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/waxell-start-run-example.json
- group: build
  title: ''
  type: Examples
  url: examples/waxell-record-llm-call-example.json
- group: build
  title: ''
  type: Examples
  url: examples/waxell-policy-check-example.json
- group: build
  title: ''
  type: Examples
  url: examples/waxell-get-prompt-example.json
- group: agent
  title: ''
  type: LlmsText
  url: https://waxell.ai/llms.txt
created: '2026-05-06'
description: Waxell is an AI agent governance and observability platform that provides runtime policy enforcement, auto-instrumented LLM telemetry, MCP governance, cost management, and durable workflow execution for agents built in any Python framework or third-party agentic tool (Claude Code, Cursor, LangChain, CrewAI, OpenAI Agents SDK, and 200+ more).
examples:
- key_count: 2
  name: Waxell Get Prompt Example
  slug: waxell-get-prompt-example
- key_count: 2
  name: Waxell Policy Check Example
  slug: waxell-policy-check-example
- key_count: 2
  name: Waxell Record Llm Call Example
  slug: waxell-record-llm-call-example
- key_count: 2
  name: Waxell Start Run Example
  slug: waxell-start-run-example
features:
- description: Two-line setup auto-instruments 200+ libraries (OpenAI, Anthropic, LangChain, LlamaIndex, CrewAI, LiteLLM, etc.) without code changes.
  name: Auto-Instrumentation
- description: 26 policy categories (cost, kill switch, PII, compliance, scope, safety) returning seven decisions (allow, warn, redact, throttle, block, skip, retry).
  name: Runtime Policy Enforcement
- description: Auto-instrumentor, server middleware, and governance proxy for Model Context Protocol traffic with PII scanning and rug-pull detection.
  name: MCP Governance
- description: Built-in model pricing for 20+ models, tenant overrides via REST, budget enforcement that warns/throttles/blocks at thresholds.
  name: Cost Management
- description: Versioned managed prompts retrievable by name and label (e.g. production, staging) directly from the SDK.
  name: Prompt Management
- description: Durable execution boundary with checkpoint and resume; Redis-backed in production, in-memory for development.
  name: Workflow Envelope
- description: Custom handlers route policy blocks to Slack, webhooks, or terminal prompts for human review.
  name: Human-in-the-Loop Approvals
- description: Immutable, timestamped record of all agent actions, decisions, and governance events.
  name: Audit Trail
- description: Hosted SSE MCP server (dev-mcp.waxell.dev/sse) with 15 live tools and 8 docs resources for coding agents.
  name: Developer MCP
- description: PII fields encrypted at the application layer with AES-256-GCM and AWS KMS (FIPS 140-2 Level 3) before database storage.
  name: Field-Level Encryption
finops:
- name: Waxell Finops
  service_category: AI Agent Governance and Observability
  slug: waxell-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waxell.png
integrations:
- description: Auto-instrumented LLM provider; cost and token tracking out of the box.
  name: OpenAI
- description: Auto-instrumented LLM provider; supports Claude family models.
  name: Anthropic
- description: First-class callback handler (WaxellLangChainHandler) for tracing chains and graphs.
  name: LangChain / LangGraph
- description: Auto-instrumented multi-agent framework support.
  name: CrewAI
- description: Tracing for RAG pipelines built with LlamaIndex.
  name: LlamaIndex
- description: Unified telemetry across LiteLLM-routed providers.
  name: LiteLLM
- description: Governance overlay for Anthropic's Claude Code coding agent via the Developer MCP.
  name: Claude Code
- description: Coding-agent governance via the SSE MCP server at dev-mcp.waxell.dev.
  name: Cursor / Windsurf / VS Code
- description: Auto-instrumentation for OpenAI's Agents SDK runs.
  name: OpenAI Agents SDK
- description: Cloud LLM providers covered by Waxell's auto-instrumentation.
  name: AWS Bedrock / Azure OpenAI / Google Vertex AI
- description: Vector database call tracing with retrieval span recording.
  name: Pinecone / Weaviate / Qdrant / Milvus / Chroma
- description: Human-in-the-loop approval handlers for policy blocks.
  name: Slack / Webhooks
- description: Listed subprocessor for billing.
  name: Stripe
json_schemas:
- name: Waxell LLM Call
  property_count: 11
  slug: waxell-llm-call
- name: Waxell Policy Decision
  property_count: 6
  slug: waxell-policy-decision
- name: Waxell Run
  property_count: 10
  slug: waxell-run
- name: Waxell Span
  property_count: 8
  slug: waxell-span
json_structures:
- name: Waxell Policy Decision Structure
  property_count: 0
  slug: waxell-policy-decision-structure
- name: Waxell Run Structure
  property_count: 0
  slug: waxell-run-structure
jsonld:
- class_count: 26
  name: Waxell Context
  property_count: 6
  slug: waxell-context
layout: provider
modified: '2026-05-19'
name: Waxell
nav: Providers
network: true
overview: 'Waxell publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cost Management API, Governance API, Prompts API, and 2 more. Tagged areas include AI Agent Governance, Observability, Policy Enforcement, LLM Telemetry, and Cost Management.


  The Waxell catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Waxell''s developer surface includes authentication, documentation, getting-started guide, developer console, signup flow, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Waxell Plans Pricing
  plan_count: 2
  slug: waxell-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Waxell Rate Limits
  slug: waxell-rate-limits
rules:
- name: Waxell API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: waxell-jsonschema-spectral-rules
- name: Waxell API Rules
  rule_count: 14
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 9
  slug: waxell-rules
score:
  band: strong
  composite: 61.1
  delta: -2.2
  facets:
    commercial_clarity: 68.4
    contract_quality: 73.4
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waxell/refs/heads/main/screenshots/waxell-2026-06-20T201300.png
security:
- kind: authentication
  name: Waxell Authentication
  slug: waxell-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Waxell Domain Security
  slug: waxell-domain-security
  summary_line: TLSv1.3 · HSTS
slug: waxell
solutions:
- description: Govern third-party agents (Claude Code, Cursor) without code changes via the MCP governance proxy.
  name: Connect
- description: Instrument self-built agents with auto-instrumentation, policy enforcement, and cost attribution.
  name: Observe
- description: Governed execution environment for high-risk workflows with the durable WorkflowEnvelope.
  name: Runtime
tags:
- AI Agent Governance
- Observability
- Policy Enforcement
- LLM Telemetry
- Cost Management
- MCP
- Agent Runtime
use_cases:
- description: Enforce policies on Claude Code, Cursor, Windsurf, VS Code, and Claude Desktop without modifying their code.
  name: Govern Third-Party Coding Agents
- description: Add full observability to LangChain, CrewAI, OpenAI Agents SDK, or custom Python agents with the @waxell.observe decorator.
  name: Instrument Self-Built Agents
- description: Set budgets on token spend per agent, user, or tenant; block runs that exceed configured limits.
  name: Cost-Capped Agent Deployment
- description: Scan MCP tool inputs/outputs for PII, credentials, and secrets with warn/block/redact responses.
  name: PII-Safe MCP Tool Use
- description: Use the WorkflowEnvelope to checkpoint multi-step agent workflows so they can resume after interruption.
  name: Durable Long-Running Workflows
- description: Maintain SOC 2 Ready posture with immutable audit trails, encrypted PII, and EU data residency.
  name: Compliance-Ready AI Operations
---
