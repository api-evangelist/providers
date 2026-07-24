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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 44.2
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for transaction management, payment authorization, agents, spending rules, analytics, and phone verification. Bearer-token authenticated; JSON envelope with cursor pagination.
  name: Sapiom REST API
  slug: sapiom-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.sapiom.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sapiom.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sapiom.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sapiom.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sapiom.ai/agents/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.sapiom.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sapiom
- group: start
  title: ''
  type: SignUp
  url: https://app.sapiom.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.sapiom.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.sapiom.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.sapiom.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.sapiom.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sapiom-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sapiom-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/sapiom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sapiom-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sapiom-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sapiom-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sapiom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sapiom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sapiom-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sapiom-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sapiom-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sapiom-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapiom-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sapiom-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sapiom-data-model.yml
created: '2026-07-17'
description: 'Sapiom is an execution engine for AI agents that gives agents and code instant, pay-per-use access to a catalog of paid capabilities through a single API key and wallet — no per-vendor accounts. Capabilities include web search and scraping, access to 400+ AI models, image/video generation, audio/text-to-speech, browser automation, compute sandboxes, databases (Postgres/Redis/vector/search), messaging and queues, file storage, private git repositories, GitHub export, email enrichment, domains/DNS, and phone verification. It is reachable three ways: a typed SDK client (@sapiom/tools / ctx.sapiom.*), a hosted remote MCP server (~130 tools), and a REST API (https://api.sapiom.ai/v1) for transaction, agent, spending-rule, and analytics management. Metered access is authorized via an x402 (HTTP 402) payment flow with per-agent spend rules. Sapiom is backed by Accel.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sapiom.png
layout: provider
mcp_servers:
- description: ''
  name: sapiom-mcp.yml
  slug: sapiom-mcpyml
modified: '2026-07-21'
name: Sapiom
nav: Providers
network: true
overview: 'Sapiom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, AI Agents, Agent Infrastructure, and Model Context Protocol.


  Sapiom''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, CLI, and 21 more developer resources.'
random_paper: 37
rate_limits:
- limit_count: 0
  name: Sapiom Rate Limits
  slug: sapiom-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 3.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 87.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sapiom Authentication
  slug: sapiom-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sapiom Domain Security
  slug: sapiom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sapiom
tags:
- Company
- Ai
- AI Agents
- Agent Infrastructure
- Model Context Protocol
- API Gateway
- Payments
- Agentic Commerce
- Developer Tools
- SDK
website: https://www.sapiom.ai/
---
