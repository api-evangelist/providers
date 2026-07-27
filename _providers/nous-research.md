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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nous Research Agentic Access
  operation_count: 2
  slug: nous-research-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: OpenAI-compatible chat completions.
  name: Nous Research Chat API
  slug: nous-research-chat-api
- description: Model discovery and catalog.
  name: Nous Research Models API
  slug: nous-research-models-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nous-research-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nous-research-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nous-research-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/nous-research-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nous-research-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nous-research-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nous-research-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nous-research-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nous-research-inference-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nous-research-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nous-research-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nousresearch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.nousresearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://portal.nousresearch.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://portal.nousresearch.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://portal.nousresearch.com
- group: company
  title: ''
  type: Blog
  url: https://nousresearch.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NousResearch
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/jqVphNsB4H
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/NousResearch
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nousresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nousresearch/
created: '2026-07-17'
description: Nous Research is an AI research and infrastructure company ("The AI Accelerator Company") known for the open-weight Hermes family of language models (including Hermes 4) and for Nous Portal, an OpenAI-compatible inference API served at inference-api.nousresearch.com. The Portal aggregates Nous's own Hermes models alongside a broad catalog of open and frontier third-party models (OpenRouter- style routing, 280+ models) behind a single chat-completions endpoint. Distinctively, the inference API supports the x402 HTTP payment protocol, returning HTTP 402 with a Solana USDC micropayment envelope so agents can pay per request without a pre-provisioned account. Beyond inference, Nous ships the Hermes Agent framework, Atropos RL environments, and Psyche/DisTrO for distributed model training over the internet. Backed by Paradigm.
image: https://nousresearch.com/wp-content/uploads/2024/03/android-chrome-512x512-1-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: nous-research-mcp.yml
  slug: nous-research-mcpyml
modified: '2026-07-20'
name: Nous Research
nav: Providers
network: true
overview: 'Nous Research publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include Company, Ai, Machine Learning, Large Language Models, and Inference.


  Nous Research''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, support, and 17 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 58.4
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 38.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Nous Research Authentication
  slug: nous-research-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nous Research Domain Security
  slug: nous-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nous-research
tags:
- Company
- Ai
- Machine Learning
- Large Language Models
- Inference
- Agents
- Open Weights
- x402
website: https://nousresearch.com
---
