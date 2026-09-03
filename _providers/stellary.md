---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Hosted remote MCP server (streamable HTTP) exposing board read/write, cockpit supervision, agent runtime, and auto-registered plugin tools. Bearer-authenticated. Listed in the official MCP registry as
  name: Stellary MCP Server
  slug: stellary-mcp-server
- description: 'REST API at the application root covering auth/identity, organizations/workspaces/projects, delivery (cards, comments, attachments, labels), documents, AI runtime (agents, missions, drafts), platform '
  name: Stellary REST API
  slug: stellary-rest-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stellary-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stellary-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stellary-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stellary-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/stellary-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stellary-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stellary-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stellary-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stellary-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stellary-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://stellary.co/docs/changelog/
- group: commercial
  title: ''
  type: Plans
  url: plans/stellary-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stellary-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stellary-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stellary-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Anymfah/stellary-mcp/blob/main/SECURITY.md
- group: design
  title: ''
  type: DataModel
  url: data-model/stellary-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stellary.co/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://stellary.co/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://stellary.co/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://stellary.co/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/ZwR26xNqVb
- group: company
  title: ''
  type: Blog
  url: https://stellary.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Anymfah
- group: commercial
  title: ''
  type: Pricing
  url: https://stellary.co/plans/
- group: start
  title: ''
  type: SignUp
  url: https://app.stellary.co/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stellary.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stellary.co/privacy/
created: '2026-08-31'
description: AI-native project-management software for teams and AI agents, offering an AI Kanban board, knowledge base, cockpit dashboards, AI agent orchestration, automations, plugins, a built-in remote MCP server, and a REST API.
image: https://stellary.co/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Stellary MCP Server
  slug: stellary-mcp-server
- description: ''
  name: Stellary Project Management MCP Server
  slug: stellary-project-management-mcp-server
modified: '2026-09-01'
name: Stellary
nav: Providers
network: true
overview: 'Stellary publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include project-management, productivity, AI-agents, agent-orchestration, and MCP.


  Stellary''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Stellary Plans Pricing
  plan_count: 2
  slug: stellary-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Stellary Rate Limits
  slug: stellary-rate-limits
scopes:
- name: Stellary Scopes
  scope_count: 0
  slug: stellary-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stellary/refs/heads/main/screenshots/stellary-2026-09-02T160837.png
security:
- kind: authentication
  name: Stellary Authentication
  slug: stellary-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Stellary Domain Security
  slug: stellary-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Stellary Vulnerability Disclosure
  slug: stellary-vulnerability-disclosure
  summary_line: Hackerone
slug: stellary
tags:
- project-management
- productivity
- AI-agents
- agent-orchestration
- MCP
- remote-mcp
- developer-tools
- SaaS
- collaboration
website: https://stellary.co/docs/
---
