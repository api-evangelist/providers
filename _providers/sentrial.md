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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Track events within agent sessions.
  name: Sentrial Events API
  slug: sentrial-events-api
- description: Create and manage agent sessions.
  name: Sentrial Sessions API
  slug: sentrial-sessions-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sentrial SDK Events API
  slug: open-sentrial-events-api
- collection_type: open
  name: Sentrial SDK Events Sessions API
  slug: open-sentrial-sessions-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentrial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentrial-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.sentrial.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.sentrial.com/docs/api/sessions
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sentrial.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.sentrial.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://sentrial.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sentrial.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sentrial.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sentrialdev
- group: build
  title: ''
  type: Packages
  url: packages/sentrial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sentrial-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sentrial-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sentrial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sentrial-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sentrial-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sentrial-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sentrial-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sentrial-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sentrial-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sentrial-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sentrial-track-agent-session.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sentrial-record-tool-call.md
created: '2026-07-17'
description: Sentrial is an observability platform for AI agents, backed by Y Combinator. It tracks every agent session, tool call, and LLM interaction, then automatically detects issues, diagnoses root causes, and helps teams fix them in code. Developers instrument agents with the Sentrial Python or TypeScript SDK (one-line integrations for LangChain, CrewAI, AutoGen, Mastra, the Vercel AI SDK, and the Claude Agent SDK), by sending OpenTelemetry traces, or by calling the REST ingestion API (https://api.sentrial.com) directly to create sessions and record events. A `sentrial` CLI ships with the SDK for local setup, scriptable session/event inspection, diagnosis, and CI regression gates.
image: https://www.sentrial.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Sentrial MCP Server
  slug: sentrial-mcp-server
modified: '2026-07-21'
name: Sentrial
nav: Providers
network: true
overview: 'Sentrial publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Sessions API. Tagged areas include Company, AI Agents, Observability, Monitoring, and LLM.


  Sentrial''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, and 16 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 61.5
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 37.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sentrial/refs/heads/main/screenshots/sentrial-2026-08-17T081809.png
security:
- kind: authentication
  name: Sentrial Authentication
  slug: sentrial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sentrial Domain Security
  slug: sentrial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sentrial
tags:
- Company
- AI Agents
- Observability
- Monitoring
- LLM
- Developer Tools
- Tracing
---
