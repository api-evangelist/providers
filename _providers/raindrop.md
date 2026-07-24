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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 43.3
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Server-to-server ingest/tracking API for sending AI interactions, events, feedback signals, and user identity into Raindrop. Bearer write-key auth; authorized requests return 204. Project targeting vi
  name: Raindrop Ingest API
  slug: raindrop-ingest-api
- description: Read-only Query API for retrieving events, traces, signals, users, and conversations from Raindrop, including search, count, timeseries, and facets. Bearer query-key auth; rate limited (200 RPM, searc
  name: Raindrop Query API
  slug: raindrop-query-api
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.raindrop.ai/docs/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://www.raindrop.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://www.raindrop.ai/docs/query-api/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.raindrop.ai/docs/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/raindrop-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/raindrop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/raindrop-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/raindrop-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/raindrop-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/raindrop-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/raindrop-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/raindrop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/raindrop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/raindrop-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/raindrop-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/raindrop-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/raindrop-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raindrop-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.raindrop.ai/docs/platform/alerts
- group: company
  title: ''
  type: Blog
  url: https://www.raindrop.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.raindrop.ai/docs/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/raindrop-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.raindrop.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auth.raindrop.ai/en/signup
- group: start
  title: ''
  type: Login
  url: https://app.raindrop.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.raindrop.ai/docs/security/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raindrop.ai/docs/security/privacy-policy
created: '2026-07-17'
description: Raindrop is the monitoring and observability platform for AI agents — a "Sentry for AI agents" that discovers silent agent failures in production. AI engineering teams use Raindrop to detect when agents fail, loop, hallucinate, or misbehave; run semantic and keyword Deep Search across millions of agent events; define custom behaviors to track in natural language; get Slack, email, and webhook alerts; inspect step-by-step traces to root-cause issues; and A/B test prompts, models, tool calls, and feature flags with Experiments. Raindrop ships first-party SDKs (TypeScript, Python, Go, Rust beta, Java beta, browser), an ingest HTTP API, a read-only Query API, a hosted MCP server, open-source Agent Skills, and the open-source Workshop local agent debugger. Founded in 2023 and headquartered in San Francisco, Raindrop raised a $15M seed led by Lightspeed Venture Partners in December 2025.
image: https://www.raindrop.ai/social.png
layout: provider
mcp_servers:
- description: ''
  name: raindrop-mcp.yml
  slug: raindrop-mcpyml
modified: '2026-07-20'
name: Raindrop
nav: Providers
network: true
overview: 'Raindrop publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Agents, Observability, and Monitoring.


  Raindrop''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, engineering blog, support, and 21 more developer resources.'
random_paper: 47
scopes:
- name: Raindrop Scopes
  scope_count: 0
  slug: raindrop-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 39.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Raindrop Authentication
  slug: raindrop-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Raindrop Domain Security
  slug: raindrop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Raindrop Trust Center
  slug: raindrop-trust-center
  summary_line: SOC 2 Type II
slug: raindrop
tags:
- Company
- AI
- Agents
- Observability
- Monitoring
- LLMOps
- Developer Tools
- Tracing
website: https://www.raindrop.ai/docs/introduction
---
