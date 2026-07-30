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
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Tenant-scoped RESTful API for programmatic management of an organization's MCP infrastructure — MCP server/connector management, user operations, audit logs, and analytics. Authenticated with an x-run
  name: Runlayer Management API
  slug: runlayer-management-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://runlayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runlayer.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runlayer.com/platform-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runlayer.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://runlayer.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runlayer
- group: start
  title: ''
  type: SignUp
  url: https://runlayer.com/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runlayer.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runlayer.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runlayer-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/runlayer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/runlayer-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/runlayer-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/runlayer-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runlayer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runlayer-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/runlayer-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.runlayer.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/runlayer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runlayer-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/runlayer-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runlayer-lifecycle.yml
created: '2026-07-17'
description: Runlayer (operated by Anysource Inc.) is an enterprise AI control plane and enablement layer for AI agents. It sits as a governed layer between the AI clients employees already use (Claude, Cursor, ChatGPT, Codex, GitHub Copilot, VS Code, Windsurf — 300+ clients) and company systems, connecting them to 18,000+ MCP servers with identity, policy enforcement, runtime security (Runlayer Guard), and audit logging on every request. The platform pairs an MCP gateway, an agent builder (Runlayer Agents), a governed skills/plugins registry (Runlayer Catalog), agent IAM, shadow-AI discovery (Runlayer Watch), and observability. Developers get a tenant-scoped REST Management API (/api/v1), a first-party CLI, Python packages, an OAuth broker, and a platform self-MCP (Runlayer MCP). Backed by a $30M Series A from Felicis and Khosla Ventures (June 2026).
image: https://www.runlayer.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: runlayer-mcp.yml
  slug: runlayer-mcpyml
modified: '2026-07-21'
name: Runlayer
nav: Providers
network: true
overview: 'Runlayer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, AI Agents, MCP, and Model Context Protocol.


  Runlayer''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, authentication, and 15 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 32.0
  delta: -0.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 32.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Runlayer Authentication
  slug: runlayer-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Runlayer Domain Security
  slug: runlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Runlayer Trust Center
  slug: runlayer-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: runlayer
tags:
- Company
- AI
- AI Agents
- MCP
- Model Context Protocol
- API Gateway
- Security
- Governance
- Identity
- Observability
- Enterprise
website: https://runlayer.com
---
