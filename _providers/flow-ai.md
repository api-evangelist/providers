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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://flow-ai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://flow-ai.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://flow-ai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://flow-ai.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://flow-ai.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://flow-ai.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://flow-ai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flowaicom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flow-ai.com/legal
- group: operate
  title: ''
  type: Support
  url: mailto:hello@flow-ai.com
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/flowaicom
- group: company
  title: ''
  type: Twitter
  url: https://x.com/flowaicom
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@flowaicom
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flow-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/flow-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flow-ai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flow-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flow-ai-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/flow-ai-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flow-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flow-ai-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flow-ai-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flow-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://flow-ai.com/legal
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flow-ai-domain-security.yml
created: '2026-07-17'
description: Flow AI builds infrastructure for embedding schema-aware, deterministic AI agents directly inside analytical SaaS products. Its flagship flowai-harness is a Rust-native runtime with a Python SDK for building production-grade data agents on top of your own data product, organized around five primitives - a data catalog agents use to resolve intent, typed plans and actions executed as auditable state machines with human approval gates, an embedded runtime, Studio (a local UI to run, debug, and evaluate agents), and self-improvement. It runs inside your infrastructure with your own model keys (OpenAI, Anthropic, Gemini, Llama, Mistral, Qwen) and warehouse (Postgres, Snowflake, BigQuery, Databricks, DuckDB). The team also publishes the open Flow Judge LLM-as-a-judge evaluation model and the flow-eval evaluation engine.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flow-ai.png
layout: provider
mcp_servers:
- description: ''
  name: flow-ai-mcp.yml
  slug: flow-ai-mcpyml
modified: '2026-07-19'
name: Flow AI
nav: Providers
network: true
overview: 'Flow AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Infrastructure, and LLM Evaluation.


  Flow AI''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, YouTube channel, and 19 more developer resources.'
random_paper: 47
score:
  band: thin
  composite: 32.2
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 82.1
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 32.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flow-ai/refs/heads/main/screenshots/flow-ai-2026-07-25T214827.png
security:
- kind: authentication
  name: Flow Ai Authentication
  slug: flow-ai-authentication
  summary_line: provider-api-key/sso · 2 schemes
- kind: domain-security
  name: Flow Ai Domain Security
  slug: flow-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flow-ai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Infrastructure
- LLM Evaluation
- Data
- Runtime
- SDK
- Model Context Protocol
- Analytics
website: https://flow-ai.com
---
