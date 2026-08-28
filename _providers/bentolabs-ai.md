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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bentolabs-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bentolabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bentolabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bentolabs.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bentolabs.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://bentolabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BentoLabs-ai
- group: start
  title: ''
  type: Login
  url: https://platform.bentolabs.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bentolabs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bentolabs.ai/privacy
- group: build
  title: ''
  type: Packages
  url: packages/bentolabs-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bentolabs-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bentolabs-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bentolabs-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bentolabs-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bentolabs-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bentolabs-ai-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bentolabs AI builds Bento, a self-learning production infrastructure platform for AI agents. Bento ingests OpenTelemetry traces from agent applications and turns them into readable trajectories, plain-English failure-mode detectors (signals), alerts, clusters, evaluations, and versioned improvements — a closed loop that monitors what runs, surfaces silent regressions and behavioral drift, and compounds learnings back into the agent. It ships a Python SDK, a command-line client, direct OTLP export from any OpenTelemetry-speaking framework (LangChain, LlamaIndex, Mastra, Vercel AI SDK, Google ADK), a hosted MCP server, and packaged Agent Skills for AI coding tools. Y Combinator-backed.
image: https://bentolabs.ai/og/default.png
layout: provider
mcp_servers:
- description: Hosted MCP server for the Bento documentation surface, advertised in the Bento quickstart for per-tool MCP setup across AI coding tools (Claude, Cursor, and others). Serves the documentation/knowledge
  name: Bentolabs AI MCP Server
  slug: bentolabs-ai-mcp-server
modified: '2026-07-18'
name: Bentolabs AI
nav: Providers
network: true
overview: 'Bentolabs AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Observability, OpenTelemetry, and Tracing.


  Bentolabs AI''s developer surface includes documentation, getting-started guide, engineering blog, CLI, authentication, and 13 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 24.9
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.9
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bentolabs-ai/refs/heads/main/screenshots/bentolabs-ai-2026-07-25T202737.png
security:
- kind: authentication
  name: Bentolabs Ai Authentication
  slug: bentolabs-ai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bentolabs Ai Domain Security
  slug: bentolabs-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bentolabs-ai
tags:
- Company
- AI Agents
- Observability
- OpenTelemetry
- Tracing
- LLM Monitoring
- Evaluation
- Agent Infrastructure
- Developer Tools
website: https://bentolabs.ai
---
