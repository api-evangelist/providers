---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.9
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: First-party REST API (~180 operations) covering issues, projects, sprints, comments, agents, docs, goals, forms, automations, chat, and webhooks. Bearer API key auth, cursor pagination, signed webhook
  name: Taskfolk API
  slug: taskfolk-api
- description: Machine-payable credit purchase for a Taskfolk workspace, published as a separate OpenAPI 3.1 document at https://taskfolk.ai/openapi.json. Four operations (/api/mpp/v1/credits/{small|medium|large|cus
  name: Taskfolk Agent Commerce API
  slug: taskfolk-agent-commerce-api
artifact_total: 10
asyncapis:
- description: ''
  name: Taskfolk Webhooks
  slug: taskfolk-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taskfolk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taskfolk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://taskfolk.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://taskfolk.ai/developer
- group: docs
  title: ''
  type: Documentation
  url: https://taskfolk.ai/developer
- group: docs
  title: ''
  type: APIReference
  url: https://taskfolk.ai/api/v1/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://taskfolk.ai/api/skill/taskfolk-product.skill.md
- group: operate
  title: ''
  type: Support
  url: https://taskfolk.ai/support
- group: company
  title: ''
  type: Blog
  url: https://taskfolk.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taskfolk
- group: operate
  title: ''
  type: Roadmap
  url: https://taskfolk.ai/feedback
- group: commercial
  title: ''
  type: Pricing
  url: https://taskfolk.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://taskfolk.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taskfolk.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taskfolk.ai/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://taskfolk.ai/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://taskfolk.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/taskfolk-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taskfolk-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taskfolk-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://taskfolk.ai/.well-known/api-catalog
- group: other
  title: ''
  type: AgentCard
  url: a2a/taskfolk-a2a.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/taskfolk-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taskfolk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/taskfolk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taskfolk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taskfolk-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taskfolk-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taskfolk-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/taskfolk-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/taskfolk-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taskfolk-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/taskfolk-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/taskfolk-product-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/taskfolk-agent-commerce-overlay.yaml
created: '2026-08-20'
description: 'Taskfolk is a project-management and issue-tracking platform built for teams and their AI agents working side by side, operated by UTTER L.L.C-FZ of Dubai, UAE. Workspaces contain projects; projects contain issues moved across board, backlog, list, calendar and timeline views, with sprints, milestones, releases, portfolios, OKR goals, docs, chat, time tracking, custom fields, automations, visual workflows and public intake forms. Every human action has a programmatic twin: a public OpenAPI 3.1 REST API of 187 operations, a first-party hosted MCP server generated one-to-one from the same OpenAPI registry, installable agent skills served as live markdown endpoints, signed webhooks, and an OAuth 2.0 authorization server with 47 scopes, PKCE and anonymous dynamic client registration. AI agents join as named workspace members that are assignable like people and are never billed as seats. Taskfolk also publishes an RFC 9727 API catalog enumerating six agent surfaces including four
  machine-payment protocols (MPP, ACP, UCP and x402) for buying AI credits without a human in the loop.'
image: https://taskfolk.ai/images/brand/taskfolk-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Taskfolk MCP Server
  slug: taskfolk-mcp-server
- description: ''
  name: Taskfolk MCP Server
  slug: taskfolk-mcp-server-2
modified: '2026-08-20'
name: Taskfolk
nav: Providers
network: true
overview: 'Taskfolk publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Agent Commerce API, and 1 more. Tagged areas include Project Management, Issue Tracking, Task Management, Productivity, and Collaboration.


  The Taskfolk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Taskfolk''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Taskfolk Plans Pricing
  plan_count: 3
  slug: taskfolk-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Taskfolk Rate Limits
  slug: taskfolk-rate-limits
scopes:
- name: Taskfolk Scopes
  scope_count: 47
  slug: taskfolk-scopes
  summary_line: 47 scopes · authorizationCode
score:
  band: strong
  composite: 62.3
  delta: -0.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 58.1
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 52.6
  previous_composite: 62.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Taskfolk Authentication
  slug: taskfolk-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Taskfolk Domain Security
  slug: taskfolk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: taskfolk
tags:
- Project Management
- Issue Tracking
- Task Management
- Productivity
- Collaboration
- MCP
- AI Agents
- agent-native
- Agentic Commerce
- A2A
- REST API
- OpenAPI
- Webhook
- Authentication
- Agile
- Sprints
- OKR
- Developer Tools
website: https://taskfolk.ai
---
