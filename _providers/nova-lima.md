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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Resource-oriented REST API (v1.0) for Runrun.it work and project management: tasks, projects, boards, clients, teams, users, comments, documents, evaluations, and time-worked reporting. JSON, ISO 8601'
  name: Runrun.it API
  slug: runrunit-api
artifact_total: 7
asyncapis:
- description: ''
  name: Nova Lima Webhooks
  slug: nova-lima-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://runrun.it
- group: start
  title: ''
  type: DeveloperPortal
  url: https://runrun.it/api/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://runrun.it/api/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://runrun.it/api/documentation
- group: operate
  title: ''
  type: Support
  url: https://help.runrun.it/english
- group: company
  title: ''
  type: Blog
  url: https://blog.runrun.it/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Runrunit
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runrun.it/en-US/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/nova-lima-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nova-lima-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nova-lima-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nova-lima-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nova-lima-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nova-lima-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/nova-lima-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nova-lima-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nova-lima-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nova-lima-problem-types.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nova-lima-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nova-lima-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nova-lima-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nova-lima-domain-security.yml
created: '2026-07-17'
description: Runrun.it (headquartered in Nova Lima, Brazil, and backed by 500 Global) is process and project management software that automates work requests and organizes a team's tasks, projects, clients, time tracking, and documents in a single place. Its public REST API (v1.0) exposes tasks, projects, boards and board stages, clients, teams, users, comments, documents, evaluations, templates, and time-worked reporting, authenticated with App-Key and User-Token request headers on paid plans. The platform also publishes an OAuth 2.0/2.1 authorization server (authorization code + PKCE), a hosted OAuth-protected MCP server at /mcp, and a webhook event system covering roughly 35 task, project, client, team, and comment events.
image: https://runrun.it/static/images/logo_1200X630.png
layout: provider
mcp_servers:
- description: ''
  name: nova-lima-mcp.yml
  slug: nova-lima-mcpyml
modified: '2026-07-20'
name: Nova Lima
nav: Providers
network: true
overview: 'Nova Lima publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Project Management, Task Management, Work Management, and Productivity.


  The Nova Lima catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nova Lima''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 0
  name: Nova Lima Rate Limits
  slug: nova-lima-rate-limits
scopes:
- name: Nova Lima Scopes
  scope_count: 1
  slug: nova-lima-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.9
  delta: 8.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.6
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 28.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Nova Lima Authentication
  slug: nova-lima-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Nova Lima Domain Security
  slug: nova-lima-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nova-lima
tags:
- Company
- Project Management
- Task Management
- Work Management
- Productivity
- Time Tracking
- Team Collaboration
- SaaS
- Brazil
website: https://runrun.it
---
