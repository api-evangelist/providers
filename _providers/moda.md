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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: HTTP ingestion API for sending LLM/agent conversation events to Moda. Accepts batched events (conversation_id, role, message, plus token/model/trace metadata) over a single POST endpoint, authenticate
  name: Moda Ingestion API
  slug: moda-ingestion-api
- description: 'Read-only analytics API for programmatic access to Moda conversation data: overview/KPIs, conversations, world state, topic clusters, frustrations, and tool failures. Authenticated with an API key via'
  name: Moda Data API
  slug: moda-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moda.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moda.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moda.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moda.dev/ingestion/direct-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moda.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://moda.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://moda.dev/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://moda.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moda.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moda.dev/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://moda.dev/login
- group: operate
  title: ''
  type: Support
  url: https://moda.dev/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ModaLabs
- group: build
  title: ''
  type: Packages
  url: packages/moda-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moda-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moda-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moda-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moda-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/moda-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moda-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moda-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moda-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moda-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moda-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moda-changelog.yml
created: '2026-07-17'
description: Moda is a continual-learning and observability layer for AI agents and LLM-native software, built by ModaLabs (YC W26, San Francisco). It turns production agent traces into validated improvements to the agent harness (prompts, tools, workflows, retrieval, memory, evals) rather than the model weights. The platform ingests conversations via a lightweight SDK plus OpenTelemetry/OTLP intake, then provides intent discovery, behavioral failure detection, tool-call failure taxonomies, frustration root-cause attribution, and prompt management. Moda exposes an HTTP ingestion API, a read-only Data API for analytics, first-party Python and TypeScript SDKs, a CLI, a production MCP server, and Claude Code skills so teams and agents can query and act on their agent analytics.
image: https://avatars.githubusercontent.com/u/242691421?v=4
layout: provider
mcp_servers:
- description: ''
  name: moda-mcp.yml
  slug: moda-mcpyml
modified: '2026-07-20'
name: Moda
nav: Providers
network: true
overview: 'Moda publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, LLM Observability, Agent Analytics, and Continual Learning.


  Moda''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, support, and 20 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 36.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moda/refs/heads/main/screenshots/moda-2026-08-07T183912.png
security:
- kind: authentication
  name: Moda Authentication
  slug: moda-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Moda Domain Security
  slug: moda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moda
tags:
- Company
- AI Agents
- LLM Observability
- Agent Analytics
- Continual Learning
- Monitoring
- Developer Tools
- MCP
- OpenTelemetry
- Prompt Management
- Y Combinator
website: https://moda.dev
---
