---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: HTTP surface exposed by the AgentSea NestJS module (@lov3kaizen/agentsea-nestjs) when enableRestApi/enableWebSocket are set. Documented operations are GET /agents, GET /agents/:name, POST /agents/:nam
  name: AgentSea Agent REST API
  slug: agent-rest-api
- description: OpenAI-compatible HTTP gateway shipped as @lov3kaizen/agentsea-gateway (and as the Elixir agentsea_web Phoenix app). Run createHTTPServer/startServer and POST /v1/chat/completions with any OpenAI SDK;
  name: AgentSea LLM Gateway
  slug: llm-gateway
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentsea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsea.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agentsea.dev/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentsea.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.agentsea.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentsea.dev/docs/quick-start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lovekaizen/agentsea
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lovekaizen/agentsea
- group: operate
  title: ''
  type: Support
  url: https://github.com/lovekaizen/agentsea/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/lovekaizen/agentsea/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/lovekaizen/agentsea/blob/main/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/agentsea-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agentsea-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/agentsea-cli.yml
- group: design
  title: ''
  type: Components
  url: components/agentsea-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentsea-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentsea-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentsea-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentsea-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentsea-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agentsea-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agentsea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agentsea-rate-limits.yml
created: '2026-08-24'
description: AgentSea is an open-source agent development kit (ADK) for building agentic AI applications, authored by Michael Fatoki-Bello and published under the lovekaizen GitHub account. It ships as twenty TypeScript/Node packages on npm under the @lov3kaizen/agentsea-* scope and, separately, as fourteen native Elixir/OTP libraries on Hex (agentsea_*). The framework covers multi-provider LLM access, agent and crew orchestration, sequential/parallel workflows, memory, embeddings, guardrails, evaluation, red-teaming, cost tracking, semantic caching, document ingest, prompt management, browser and computer use, and voice (TTS/STT), plus a Model Context Protocol client and Agentic Commerce Protocol tooling. AgentSea is self-hosted software rather than a vendor-operated API - its HTTP surface (an /agents REST + Server-Sent Events + WebSocket API via the NestJS module, and an OpenAI-compatible /v1/chat/completions LLM gateway) runs inside the consumer's own deployment. MIT licensed.
image: https://agentsea.dev/opengraph-image
layout: provider
modified: '2026-08-24'
name: AgentSea
nav: Providers
network: true
overview: 'AgentSea publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Orchestration, and Large Language Models.


  AgentSea''s developer surface includes documentation, API reference, getting-started guide, support, changelog, CLI, authentication, and 16 more developer resources.'
plans:
- name: Agentsea Plans Pricing
  plan_count: 0
  slug: agentsea-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Agentsea Rate Limits
  slug: agentsea-rate-limits
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/screenshots/agentsea-2026-09-02T144115.png
security:
- kind: authentication
  name: Agentsea Authentication
  slug: agentsea-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentsea Domain Security
  slug: agentsea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentsea
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Orchestration
- Large Language Models
- MCP
- Agentic Commerce
- Open-Source
- Developer Tools
- SDK
- TypeScript
- Elixir
- Voice
website: https://agentsea.dev
---
