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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.4
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Sail Agentic Access
  operation_count: 10
  slug: sail-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 5
apis:
- description: Submit and manage batches of requests.
  name: Sail Batches API API
  slug: sail-batches-api-api
- description: OpenAI-compatible Chat Completions API endpoints.
  name: Sail Chat Completions API API
  slug: sail-chat-completions-api-api
- description: Anthropic-compatible Messages API endpoints.
  name: Sail Messages API API
  slug: sail-messages-api-api
- description: Model discovery endpoints.
  name: Sail Models API API
  slug: sail-models-api-api
- description: OpenAI-compatible Responses API endpoints.
  name: Sail Responses API API
  slug: sail-responses-api-api
artifact_total: 10
asyncapis:
- description: ''
  name: Sail Webhooks
  slug: sail-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.sailresearch.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sailresearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sailresearch.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sailresearch.com/api-reference/chat-completions-api/create-a-chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sailresearch.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.sailresearch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sailresearch.com
- group: company
  title: ''
  type: Blog
  url: https://www.sailresearch.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sailresearchco
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sailresearch.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sailresearch.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.sailresearch.com/dpa
- group: auth
  title: ''
  type: Authentication
  url: authentication/sail-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sail-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sail-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sail-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sail-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sail-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/sail-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sail-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sail-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sail-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sail-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sail-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Sail Research provides cloud infrastructure for running long-horizon AI agents efficiently. Its inference platform serves leading open-source models (GLM, Kimi, DeepSeek, gpt-oss, Gemma, and more) through an OpenAI-compatible Responses and Chat Completions API plus an Anthropic-compatible Messages API, so existing SDKs work as drop-in clients. "Completion windows" (asap, priority, standard, flex) trade latency for 30-80% token savings, and a Batch API processes up to 100,000 requests asynchronously. Sailboxes add persistent virtual-machine compute for agents that need to run indefinitely, with checkpoint/resume, networking, and a native CLI. The platform supports LoRA fine-tunes, Tinker RL rollouts, prompt caching, completion webhooks, and usage/observability (Voyages) for background agents.
image: https://sailresearch.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: sail-mcp.yml
  slug: sail-mcpyml
modified: '2026-07-21'
name: Sail
nav: Providers
network: true
overview: 'Sail publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batches API API, Chat Completions API API, Messages API API, and 2 more. Tagged areas include Company, AI, Machine Learning, LLM, and Inference.


  The Sail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sail''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 19 more developer resources.'
random_paper: 77
score:
  band: developing
  composite: 54.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 71.2
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Sail Authentication
  slug: sail-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sail Domain Security
  slug: sail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sail
tags:
- Company
- AI
- Machine Learning
- LLM
- Inference
- Agents
- Open Source Models
- Infrastructure
- Developer Tools
website: https://www.sailresearch.com/
---
