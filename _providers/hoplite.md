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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Hoplite platform API at api.hoplite.sh. Documented through the developer docs (no public OpenAPI published as of this profiling). Surfaces include model-provider discovery (GET /api/model-provider
  name: Hoplite API
  slug: hoplite-api
artifact_total: 5
asyncapis:
- description: ''
  name: Hoplite Webhooks
  slug: hoplite-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hoplite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hoplite.sh
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hoplite.sh/docs
- group: docs
  title: ''
  type: Documentation
  url: https://hoplite.sh/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://hoplite.sh/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://hoplite.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hoplite.sh/signup
- group: start
  title: ''
  type: Login
  url: https://hoplite.sh/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hoplite.sh
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hoplite-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hoplite-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/hoplite-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/hoplite-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hoplite-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hoplite-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hoplite-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hoplite-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hoplite-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hoplite-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hoplite-data-model.yml
created: '2026-07-17'
description: Hoplite is a cloud coding-agent platform (Y Combinator S26). You connect a GitHub repository, describe a task in a thread, and an autonomous agent does the work inside an isolated, cloned dev environment (a "sandbox") — reading and editing code, running your test suite, starting your dev server, verifying changes in a built-in browser, and opening a pull request when it's done. Runs stream live into the thread with inline approvals for sensitive actions, a diff view, and a PR rail that tracks checks, reviews, and unresolved comments. Hoplite runs a lineup of OpenAI (GPT-5.6 family, GPT-5.3 Codex) and Anthropic (Fable 5, Opus 4.8, Sonnet 4.6, Haiku 4.5) models, bills on prepaid credits via Stripe, and integrates with GitHub, Slack, Linear, and customer-hosted MCP servers. It also exposes its own hosted MCP server and a CLI so you can drive Hoplite from Claude Code, Cursor, or any MCP client. Founded 2026 in San Francisco by Ryan Morrissey and Bence Redmond.
image: https://hoplite.sh/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: hoplite-mcp.yml
  slug: hoplite-mcpyml
modified: '2026-07-19'
name: Hoplite
nav: Providers
network: true
overview: 'Hoplite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coding Agents, Developer Tools, AI Agents, and Cloud Development Environments.


  The Hoplite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hoplite''s developer surface includes documentation, getting-started guide, pricing, signup flow, CLI, authentication, and 14 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 23.7
  previous_composite: 39.5
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hoplite/refs/heads/main/screenshots/hoplite-2026-07-25T221418.png
security:
- kind: authentication
  name: Hoplite Authentication
  slug: hoplite-authentication
  summary_line: apiKey/oauth2/http-bearer · 3 schemes
- kind: domain-security
  name: Hoplite Domain Security
  slug: hoplite-domain-security
  summary_line: TLSv1.3
slug: hoplite
tags:
- Company
- Coding Agents
- Developer Tools
- AI Agents
- Cloud Development Environments
- DevOps
- MCP
- Pull Requests
- Software Automation
- GitHub
website: https://hoplite.sh
---
