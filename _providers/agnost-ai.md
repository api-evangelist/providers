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
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-10'
api_count: 14
apis:
- description: Alert configuration and monitoring
  name: Agnost AI Alerts API
  slug: agnost-ai-alerts-api
- description: API key management
  name: Agnost AI API Keys API
  slug: agnost-ai-api-keys-api
- description: OAuth authentication callbacks
  name: Agnost AI Auth API
  slug: agnost-ai-auth-api
- description: Stripe billing management
  name: Agnost AI Billing API
  slug: agnost-ai-billing-api
- description: LLM-based classification operations
  name: Agnost AI Classification API
  slug: agnost-ai-classification-api
- description: External integrations (Slack)
  name: Agnost AI Connections API
  slug: agnost-ai-connections-api
- description: Conversation message and span retrieval
  name: Agnost AI Conversations API
  slug: agnost-ai-conversations-api
- description: Analytics and metrics for the dashboard
  name: Agnost AI Dashboard API
  slug: agnost-ai-dashboard-api
- description: First-run helpers used during organization setup
  name: Agnost AI Onboarding API
  slug: agnost-ai-onboarding-api
- description: Organization management
  name: Agnost AI Organizations API
  slug: agnost-ai-organizations-api
- description: Event ingestion endpoints used by SDKs
  name: Agnost AI SDK API
  slug: agnost-ai-sdk-api
- description: Sentiment and intent analysis
  name: Agnost AI Sentiments API
  slug: agnost-ai-sentiments-api
- description: Standard Operating Procedures
  name: Agnost AI SOPs API
  slug: agnost-ai-sops-api
- description: Health checks, webhooks, internal endpoints
  name: Agnost AI System API
  slug: agnost-ai-system-api
artifact_total: 20
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agnost.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agnost.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agnost.ai/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agnost.ai/quickstart
- group: build
  title: ''
  type: SDKs
  url: https://docs.agnost.ai/sdks
- group: company
  title: ''
  type: Blog
  url: https://agnost.ai/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.agnost.ai/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agnostai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agnost.ai
- group: operate
  title: ''
  type: Support
  url: https://call.agnost.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://agnost.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.agnost.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agnost.ai/terms
- group: auth
  title: ''
  type: Compliance
  url: https://trust.agnost.ai
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.agnost.ai/mcp
- group: build
  title: ''
  type: Packages
  url: packages/agnost-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agnost-ai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agnost-ai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agnost-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agnost-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/agnost-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agnost-ai-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agnost-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agnost-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agnost-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agnost-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agnost-ai-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agnost-ai-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/agnost-ai-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/agnost-ai-published.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Agnost AI is a production monitoring and product-analytics platform for teams building chat and voice AI agents. It continuously reads production agent conversations, MCP tool calls, and OpenTelemetry traces, clusters recurring intents, feature requests, frustration, and failure patterns, and catches agent failures that offline evals miss. It then turns the highest-impact patterns into reviewed fixes, including pull requests against prompts, tools, and agent harnesses. Agnost is OpenTelemetry-native, works with any LLM and framework, and ships SDKs for Python and TypeScript conversation tracking, MCP-server analytics (Python, TypeScript, Go), plus a hosted OAuth-protected MCP server for querying your dashboard from Claude Desktop, Cursor, and any MCP client. Founded in 2025 and part of Y Combinator's Summer 2026 (S26) batch.
image: https://agnost.ai/logo.png
layout: provider
mcp_servers:
- description: Hosted, OAuth 2.1-protected MCP server (streamable-HTTP) for querying your Agnost dashboard from Claude Desktop, Cursor, and any MCP client.
  name: Agnost MCP Server
  slug: agnost-mcp-server
- description: ''
  name: agnost-ai-mcp.yml
  slug: agnost-ai-mcpyml
modified: '2026-07-18'
name: Agnost AI
nav: Providers
network: true
overview: 'Agnost AI publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, API Keys API, Auth API, and 11 more. Tagged areas include Company, AI Agents, Agent Analytics, Observability, and OpenTelemetry.


  Agnost AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
random_paper: 87
scopes:
- name: Agnost Ai Scopes
  scope_count: 1
  slug: agnost-ai-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.7
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 53.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agnost-ai/refs/heads/main/screenshots/agnost-ai-2026-07-25T195316.png
security:
- kind: authentication
  name: Agnost Ai Authentication
  slug: agnost-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Agnost Ai Domain Security
  slug: agnost-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Agnost Ai Trust Center
  slug: agnost-ai-trust-center
  summary_line: trust center published
slug: agnost-ai
tags:
- Company
- AI Agents
- Agent Analytics
- Observability
- OpenTelemetry
- Model Context Protocol
- Conversational AI
- Monitoring
- Developer Tools
- Analytics
website: https://docs.agnost.ai
---
