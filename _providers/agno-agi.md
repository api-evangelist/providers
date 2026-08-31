---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Agno Agi Agentic Access
  operation_count: 26
  slug: agno-agi-agentic-access
  summary_line: 26 operations · 11 acting
api_count: 1
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
artifact_total: 24
asyncapis:
- description: AsyncAPI 2.6 description of AgentOS's **run streaming** surface. AgentOS does not publish a documented public WebSocket API. The asynchronous / event-style transport documented at https://docs.agno.co
  name: Agno AgentOS Run Streaming (HTTP + SSE)
  slug: agno-agi-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agno AgentOS Agents API
  slug: open-agno-agi-agents-api
- collection_type: open
  name: Agno AgentOS Agents Evals API
  slug: open-agno-agi-evals-api
- collection_type: open
  name: Agno AgentOS Agents Knowledge API
  slug: open-agno-agi-knowledge-api
- collection_type: open
  name: Agno AgentOS Agents Memory API
  slug: open-agno-agi-memory-api
- collection_type: open
  name: Agno AgentOS Agents Sessions API
  slug: open-agno-agi-sessions-api
- collection_type: open
  name: Agno AgentOS Agents Teams API
  slug: open-agno-agi-teams-api
- collection_type: open
  name: Agno AgentOS Agents Workflows API
  slug: open-agno-agi-workflows-api
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
overview: 'Agno publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Evals API, Knowledge API, and 4 more. Tagged areas include Artificial Intelligence, Agents, Multi-Agent, LLM, and Framework.


  The Agno catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Agno''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Agno Agi Plans Pricing
  plan_count: 3
  slug: agno-agi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Agno Agi Rate Limits
  slug: agno-agi-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Agno API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 8
  slug: agno-agi-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 52.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 19.5
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Artificial Intelligence
- Agents
- Multi-Agent
- LLM
- Framework
- Open-Source
- Runtime
website: https://www.agno.com
---
