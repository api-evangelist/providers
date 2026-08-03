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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: Anthropic-compatible messages endpoint.
  name: LM Studio Anthropic Compatibility API
  slug: lm-studio-anthropic-compatibility-api
- description: Native LM Studio chat inference with generation stats.
  name: LM Studio Chat API
  slug: lm-studio-chat-api
- description: List, load, unload, and download local models.
  name: LM Studio Models API
  slug: lm-studio-models-api
- description: OpenAI-compatible endpoints for reuse of existing OpenAI clients.
  name: LM Studio OpenAI Compatibility API
  slug: lm-studio-openai-compatibility-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://lmstudio.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lmstudio.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://lmstudio.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://lmstudio.ai/docs/app/api/endpoints/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://lmstudio.ai/docs/app
- group: company
  title: ''
  type: Blog
  url: https://lmstudio.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lmstudio-ai
- group: operate
  title: ''
  type: Support
  url: https://github.com/lmstudio-ai/lmstudio-bug-tracker
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lmstudio.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lmstudio.ai/privacy
- group: build
  title: ''
  type: Packages
  url: packages/lm-studio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lm-studio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lm-studio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lm-studio-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lm-studio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lm-studio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lm-studio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lm-studio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lm-studio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lm-studio-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lm-studio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lm-studio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://lmstudio.ai/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lm-studio-domain-security.yml
created: '2026-07-17'
description: 'LM Studio is a desktop application for discovering, downloading, and running large language models (Llama, DeepSeek, Phi, Qwen, gpt-oss, and others) locally on macOS, Windows, and Linux. It runs GGUF and MLX models via llama.cpp and Apple''s MLX engine, and ships a local HTTP server that developers can drive from their own apps: a native LM Studio REST API (beta) under /api/v1 with generation stats, model load/unload/download and MCP-via-API, an OpenAI-compatible surface under /v1 (chat/completions, completions, embeddings, models, responses), and an Anthropic-compatible /v1/messages endpoint. It is complemented by Python (lmstudio) and TypeScript (@lmstudio/sdk) SDKs, the MIT-licensed lms command-line tool, headless/daemon operation, LM Link cross-device routing, and MCP host support. Backed by Matrix Partners.'
image: https://files.lmstudio.ai/bionic/lm-studio-bionic-og.jpg
layout: provider
mcp_servers:
- description: ''
  name: lm-studio-mcp.yml
  slug: lm-studio-mcpyml
modified: '2026-07-20'
name: LM Studio
nav: Providers
network: true
overview: 'LM Studio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Anthropic Compatibility API, Chat API, Models API, and 1 more. Tagged areas include Company, Ai, Local LLM, Machine Learning, and Inference.


  LM Studio''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 18 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 13.1
    developer_ergonomics: 69.0
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 31.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lm-studio/refs/heads/main/screenshots/lm-studio-2026-07-25T225416.png
security:
- kind: authentication
  name: Lm Studio Authentication
  slug: lm-studio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lm Studio Domain Security
  slug: lm-studio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lm Studio Vulnerability Disclosure
  slug: lm-studio-vulnerability-disclosure
  summary_line: disclosure policy published
slug: lm-studio
tags:
- Company
- Ai
- Local LLM
- Machine Learning
- Inference
- Developer Tools
- LLM
- MCP
- SDK
- Desktop Application
website: https://lmstudio.ai
---
