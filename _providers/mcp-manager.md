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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Control-plane surface that lets an agent or script manage MCP Manager configuration — servers, gateways, identities, hosts, teams, roles, logs, and integrations — with the same actions as the app, sco
  name: MCP Manager Admin API
  slug: mcp-manager-admin-api
artifact_total: 6
asyncapis:
- description: ''
  name: Mcp Manager Webhooks
  slug: mcp-manager-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://mcpmanager.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mcpmanager.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mcpmanager.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mcpmanager.ai/admin-api/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mcpmanager.ai/get-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://mcpmanager.ai/categories/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://mcpmanager.ai/pricing-plans/
- group: start
  title: ''
  type: SignUp
  url: https://mcpmanager.ai/free-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcpmanager.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcpmanager.ai/policy/
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.mcpmanager.ai/admin-api/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mcpmanager.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mcp-manager-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mcp-manager-skill.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mcp-manager-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mcp-manager-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mcp-manager-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mcp-manager-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mcp-manager-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mcp-manager-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/mcp-manager-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mcp-manager-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcp-manager-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mcp-manager-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mcp-manager-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mcp-manager-webhooks.yml
created: '2026-07-17'
description: MCP Manager, by Usercentrics, is an enterprise governance and security layer for the Model Context Protocol (MCP). It sits as a governed gateway between AI clients (Claude, ChatGPT, Cursor, and custom agents) and MCP servers — SaaS tools, internal databases, and custom servers — authenticating every request, brokering per-user or shared identities, inspecting traffic against gateway rules (regex, Microsoft Presidio, and custom rule engines) for PII and prompt-injection defense, provisioning tool allowlists, and logging every call with full attribution plus OpenTelemetry export to any SIEM. It ships an Admin API and MCP server (closed beta) that manage servers, gateways, identities, hosts, teams, roles, and logs over both MCP tools and a REST twin.
image: https://mcpmanager.ai/wp-content/uploads/mcp-manager-og-share-image.png
layout: provider
mcp_servers:
- description: ''
  name: mcp-manager-mcp.yml
  slug: mcp-manager-mcpyml
modified: '2026-07-20'
name: MCP Manager
nav: Providers
network: true
overview: 'MCP Manager publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Model Context Protocol, AI Governance, and API Gateway.


  The MCP Manager catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MCP Manager''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 25
score:
  band: thin
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 63.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 43.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Mcp Manager Authentication
  slug: mcp-manager-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Mcp Manager Domain Security
  slug: mcp-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mcp Manager Trust Center
  slug: mcp-manager-trust-center
  summary_line: SOC 2 Type 2, HIPAA, ISO 27001:2022, ISO 27701:2019, TISAX Level 3
slug: mcp-manager
tags:
- Company
- MCP
- Model Context Protocol
- AI Governance
- API Gateway
- Security
- Observability
- DLP
- Identity
- RBAC
- Enterprise
website: https://mcpmanager.ai/
---
