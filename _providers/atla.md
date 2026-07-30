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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The SDK API from Atla — 3 operation(s) for sdk.
  name: Atla SDK API
  slug: atla-sdk-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.atla-ai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atla-ai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atla-ai.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atla-ai.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.atla-ai.com/troubleshooting-faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atla-ai
- group: company
  title: ''
  type: Website
  url: https://www.atla-ai.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/atla-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atla-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/atla-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/atla-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atla-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atla-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atla-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atla-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atla-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atla-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atla-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atla-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Atla builds frontier AI evaluation models (Selene) and Atla Insights, an observability platform for monitoring and improving AI agents. Its Insights Data API exposes OpenTelemetry-based traces and spans of instrumented agent runs — list with time-window and metadata filters, fetch multiple by ID, and retrieve a single trace with full spans, summaries, and custom metrics. Atla ships official Python and JavaScript SDKs and an MCP server. The company is UK-based and backed by Creandum. Note: the Atla Insights platform is scheduled to sunset on 16 February 2026, and the separate Selene evaluation API SDK and MCP server were archived in 2025.'
image: https://avatars.githubusercontent.com/atla-ai
layout: provider
mcp_servers:
- description: ''
  name: atla-mcp.yml
  slug: atla-mcpyml
modified: '2026-07-18'
name: Atla
nav: Providers
network: true
overview: 'Atla publishes 1 API on the [APIs.io](https://apis.io/) network: SDK API. Tagged areas include Company, SaaS, Artificial Intelligence, LLM Evaluation, and AI Agents.


  Atla''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 15 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 38.8
  delta: 0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 58.5
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 38.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atla/refs/heads/main/screenshots/atla-2026-07-25T201538.png
security:
- kind: authentication
  name: Atla Authentication
  slug: atla-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Atla Domain Security
  slug: atla-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: atla
tags:
- Company
- SaaS
- Artificial Intelligence
- LLM Evaluation
- AI Agents
- Observability
- Monitoring
- OpenTelemetry
website: https://www.atla-ai.com/
---
