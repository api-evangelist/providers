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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Agno Agi Agentic Access
  operation_count: 26
  slug: agno-agi-agentic-access
  summary_line: 26 operations · 11 acting
api_count: 7
apis:
- description: Run and manage individual agents.
  name: Agno Agents API
  slug: agno-agi-agents-api
- description: Evaluation runs for quality and reliability.
  name: Agno Evals API
  slug: agno-agi-evals-api
- description: Knowledge base content used for retrieval.
  name: Agno Knowledge API
  slug: agno-agi-knowledge-api
- description: Persistent per-user memories.
  name: Agno Memory API
  slug: agno-agi-memory-api
- description: Conversation history and state for agents, teams, and workflows.
  name: Agno Sessions API
  slug: agno-agi-sessions-api
- description: Run and manage teams of agents.
  name: Agno Teams API
  slug: agno-agi-teams-api
- description: Run and manage multi-step workflows.
  name: Agno Workflows API
  slug: agno-agi-workflows-api
artifact_total: 16
asyncapis:
- description: AsyncAPI 2.6 description of AgentOS's **run streaming** surface. AgentOS does not publish a documented public WebSocket API. The asynchronous / event-style transport documented at https://docs.agno.co
  name: Agno AgentOS Run Streaming (HTTP + SSE)
  slug: agno-agi-asyncapi
collections:
- collection_type: open
  name: Agno AgentOS API
  slug: open-agno-agi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agno-agi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agno-agi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agno-agi-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://agno.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agno-agi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agno-agi
- group: company
  title: ''
  type: Website
  url: https://www.agno.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agno.com
- group: commercial
  title: ''
  type: Plans
  url: plans/agno-agi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agno-agi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/agno-agi-finops.yml
created: '2026-07-02'
description: Agno (formerly Phidata) is an open-source Python framework for building multi-agent AI systems, paired with AgentOS - a self-hostable runtime that turns agents, teams, and workflows into a REST API server with 50+ endpoints for runs, sessions, memory, knowledge, and evals. The optional os.agno.com Control Plane connects a browser directly to a self-hosted AgentOS instance for chat, tracing, and monitoring; Agno does not operate a separate multi-tenant inference API of its own.
finops:
- name: Agno Agi Finops
  service_category: AI and Machine Learning
  slug: agno-agi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agno-agi.png
layout: provider
modified: '2026-07-02'
name: Agno
nav: Providers
network: true
overview: 'Agno publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Evals API, Knowledge API, and 4 more. Tagged areas include AI, Agents, Multi-Agent, LLM, and Framework.


  The Agno catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Agno''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Agno Agi Plans Pricing
  plan_count: 3
  slug: agno-agi-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Agno Agi Rate Limits
  slug: agno-agi-rate-limits
rules:
- name: Agno API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 8
  slug: agno-agi-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.7
  delta: 2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.1
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 46.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agno-agi/refs/heads/main/screenshots/agno-agi-2026-07-25T195318.png
security:
- kind: authentication
  name: Agno Agi Authentication
  slug: agno-agi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agno Agi Domain Security
  slug: agno-agi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agno-agi
tags:
- AI
- Agents
- Multi-Agent
- LLM
- Framework
- Open Source
- Runtime
website: https://www.agno.com
---
