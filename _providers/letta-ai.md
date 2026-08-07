---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 93
  human_in_the_loop: 3
  name: Letta Ai Agentic Access
  operation_count: 167
  slug: letta-ai-agentic-access
  summary_line: 167 operations · 93 acting · 3 human-in-the-loop
api_count: 14
apis:
- description: Cloud-only versioned agent configuration templates.
  name: Letta Agent Templates API
  slug: letta-ai-agent-templates-api
- description: Stateful agents and their lifecycle.
  name: Letta Agents API
  slug: letta-ai-agents-api
- description: Out-of-context long-term memory archives and passages.
  name: Letta Archival Memory API
  slug: letta-ai-archival-memory-api
- description: OpenAI-compatible chat completions backed by a Letta agent.
  name: Letta Chat Completions API
  slug: letta-ai-chat-completions-api
- description: End users of a multi-tenant Letta deployment.
  name: Letta Identities API
  slug: letta-ai-identities-api
- description: Remote Model Context Protocol tool servers.
  name: Letta MCP Servers API
  slug: letta-ai-mcp-servers-api
- description: Core-memory blocks shared across agents, groups, and identities.
  name: Letta Memory Blocks API
  slug: letta-ai-memory-blocks-api
- description: Available models and configured BYOK model providers.
  name: Letta Models and Providers API
  slug: letta-ai-models-and-providers-api
- description: Groups of agents coordinating around shared memory.
  name: Letta Multi-Agent Groups API
  slug: letta-ai-multi-agent-groups-api
- description: Asynchronous execution history behind agent messages.
  name: Letta Runs, Jobs and Steps API
  slug: letta-ai-runs-jobs-and-steps-api
- description: Uploaded files and folders used for agent grounding and retrieval.
  name: Letta Sources and Files API
  slug: letta-ai-sources-and-files-api
- description: The Tag API from Letta — 1 operation(s) for tag.
  name: Letta Tag API
  slug: letta-ai-tag-api
- description: Functions agents can call, including MCP-backed tools.
  name: Letta Tools API
  slug: letta-ai-tools-api
- description: The Voice API from Letta — 1 operation(s) for voice.
  name: Letta Voice API
  slug: letta-ai-voice-api
artifact_total: 23
asyncapis:
- description: AsyncAPI 2.6 description of Letta's **agent message streaming** surface. Letta does not publish a WebSocket API. The only asynchronous / event-style transport documented in Letta's OpenAPI spec (https
  name: Letta Agent Message Streaming (HTTP + SSE)
  slug: letta-ai-asyncapi
collections:
- collection_type: open
  name: Letta API
  slug: open-letta-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/letta-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/letta-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/letta-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/letta-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/letta-ai
- group: company
  title: ''
  type: Website
  url: https://www.letta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.letta.com
- group: commercial
  title: ''
  type: Plans
  url: plans/letta-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/letta-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/letta-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.letta.com/blog
created: '2026-07-02'
description: Letta (formerly MemGPT) builds stateful AI agents with persistent memory that runs as a service. The Letta REST API creates, configures, and messages agents whose memory - core context blocks and archival vector memory - survives across sessions, and manages the tools, data sources, identities, and multi-agent groups those agents use. It is offered as a managed Letta Cloud API and as an open-source, self-hostable server with the same OpenAPI-documented interface.
finops:
- name: Letta Ai Finops
  service_category: AI and Machine Learning
  slug: letta-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/letta-ai.png
layout: provider
modified: '2026-07-02'
name: Letta
nav: Providers
network: true
overview: 'Letta publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agent Templates API, Agents API, Archival Memory API, and 11 more. Tagged areas include AI, Agents, LLM, Memory, and Stateful Agents.


  The Letta catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Letta''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Letta Ai Plans Pricing
  plan_count: 5
  slug: letta-ai-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 5
  name: Letta Ai Rate Limits
  slug: letta-ai-rate-limits
rules:
- name: Letta API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: letta-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.4
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/letta-ai/refs/heads/main/screenshots/letta-ai-2026-07-25T224937.png
security:
- kind: authentication
  name: Letta Ai Authentication
  slug: letta-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Letta Ai Domain Security
  slug: letta-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: letta-ai
tags:
- AI
- Agents
- LLM
- Memory
- Stateful Agents
- MemGPT
website: https://www.letta.com
---
