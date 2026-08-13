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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Clawvisor Agentic Access
  operation_count: 12
  slug: clawvisor-agentic-access
  summary_line: 12 operations · 8 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Local magic-link session exchange.
  name: Clawvisor Auth API
  slug: clawvisor-auth-api
- description: Discover the services and actions available to the agent.
  name: Clawvisor Catalog API
  slug: clawvisor-catalog-api
- description: Execute authorized actions on downstream services through the gateway.
  name: Clawvisor Gateway API
  slug: clawvisor-gateway-api
- description: Declare, approve, expand, and complete task scopes.
  name: Clawvisor Tasks API
  slug: clawvisor-tasks-api
- description: Mint and revoke scoped agent tokens (admin-gated).
  name: Clawvisor Tokens API
  slug: clawvisor-tokens-api
arazzos:
- description: Declare a read-scoped task, wait for the user to approve it, list and read messages through the gateway under scope, then complete the task. Every operationId is verified against openapi/clawvisor-gat
  name: Clawvisor — approve-scope-and-triage
  slug: clawvisor-triage-inbox
artifact_total: 11
asyncapis:
- description: ''
  name: Clawvisor Callbacks Webhooks
  slug: clawvisor-callbacks-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/clawvisor-gateway-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clawvisor.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/clawvisor/clawvisor/tree/main/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/clawvisor/clawvisor#agent-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/clawvisor/clawvisor#get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clawvisor
- group: operate
  title: ''
  type: Support
  url: https://github.com/clawvisor/clawvisor/issues
- group: commercial
  title: ''
  type: Pricing
  url: https://clawvisor.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.clawvisor.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawvisor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawvisor.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clawvisor-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clawvisor-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clawvisor-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clawvisor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clawvisor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clawvisor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clawvisor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clawvisor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clawvisor-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clawvisor-callbacks-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/clawvisor-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clawvisor-cli.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clawvisor-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clawvisor-agentic-access.yml
created: '2026-07-17'
description: 'Clawvisor is the authorization layer for AI agents — a Y Combinator (Spring 2026) security gateway that sits between an AI agent and the tools it acts on (Gmail, Calendar, Drive, Contacts, GitHub, Slack, Notion, Linear, Stripe, Twilio, iMessage). Agents never hold downstream credentials: they declare a task describing their purpose and the service/action pairs they need, the user approves that scope once, and Clawvisor enforces restrictions, task scope, and LLM intent verification on every request before injecting vaulted, short-lived credentials, executing through an adapter, and writing a full audit trail. It ships open-core as a self-hostable Go daemon with a CLI, web dashboard, TUI, and an OAuth 2.1 MCP server, plus an official Claude Code plugin. Agents integrate over a plain HTTP gateway or MCP — no SDK or agent-code changes required.'
image: https://raw.githubusercontent.com/clawvisor/clawvisor/main/web/public/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: clawvisor-mcp.yml
  slug: clawvisor-mcpyml
modified: '2026-07-18'
name: Clawvisor
nav: Providers
network: true
overview: 'Clawvisor publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Catalog API, Gateway API, and 2 more. Tagged areas include AI Agents, Authorization, Security, Identity, and Access Control.


  The Clawvisor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clawvisor''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 26
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.7
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clawvisor/refs/heads/main/screenshots/clawvisor-2026-07-25T205527.png
security:
- kind: authentication
  name: Clawvisor Authentication
  slug: clawvisor-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clawvisor Domain Security
  slug: clawvisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clawvisor
tags:
- AI Agents
- Authorization
- Security
- Identity
- Access Control
- MCP
- Credential Management
- Governance
- Developer Tools
website: https://clawvisor.com
---
