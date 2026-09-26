---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-09-25'
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
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/security/agentsea-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/packages/agentsea-packages.yml
  title: ''
  type: Packages
  url: packages/agentsea-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/packages/agentsea-packages.yml
  title: ''
  type: SDKs
  url: packages/agentsea-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/cli/agentsea-cli.yml
  title: ''
  type: CLI
  url: cli/agentsea-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/components/agentsea-components.yml
  title: ''
  type: Components
  url: components/agentsea-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/llms/agentsea-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsea-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/authentication/agentsea-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsea-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/conventions/agentsea-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentsea-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/conformance/agentsea-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsea-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/lifecycle/agentsea-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentsea-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/changelog/agentsea-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentsea-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/plans/agentsea-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentsea-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentsea/refs/heads/main/rate-limits/agentsea-rate-limits.yml
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
overview: 'AgentSea publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Orchestration, and LLM.


  AgentSea''s developer surface includes documentation, API reference, getting-started guide, support, changelog, CLI, authentication, and 16 more developer resources.'
plans:
- name: Agentsea Plans Pricing
  plan_count: 0
  slug: agentsea-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Agentsea Rate Limits
  slug: agentsea-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- LLM
- MCP
- Agentic Commerce
- Open Source
- Developer Tools
- SDK
- TypeScript
- Elixir
- Voice
website: https://agentsea.dev
---
