---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Hosted remote MCP server (streamable HTTP) exposing board read/write, cockpit supervision, agent runtime, and auto-registered plugin tools. Bearer-authenticated. Listed in the official MCP registry as
  name: Stellary MCP Server
  slug: stellary-mcp-server
- description: 'REST API at the application root covering auth/identity, organizations/workspaces/projects, delivery (cards, comments, attachments, labels), documents, AI runtime (agents, missions, drafts), platform '
  name: Stellary REST API
  slug: stellary-rest-api
artifact_total: 11
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://stellary.co/feed.xml
- group: company
  title: ''
  type: Website
  url: https://www.stellary.co/
- group: auth
  href: https://artifacts.apis.io/stellary/security/stellary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stellary-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/stellary/well-known/stellary-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stellary-well-known.yml
- group: agent
  href: https://artifacts.apis.io/stellary/mcp/stellary-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stellary-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stellary/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/stellary/llms/stellary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stellary-llms.txt
- group: auth
  href: https://artifacts.apis.io/stellary/authentication/stellary-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stellary-authentication.yml
- group: auth
  href: https://artifacts.apis.io/stellary/scopes/stellary-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/stellary-scopes.yml
- group: design
  href: https://artifacts.apis.io/stellary/conventions/stellary-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stellary-conventions.yml
- group: design
  href: https://artifacts.apis.io/stellary/errors/stellary-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stellary-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stellary/lifecycle/stellary-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stellary-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/stellary/changelog/stellary-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stellary-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://stellary.co/docs/changelog/
- group: commercial
  href: https://artifacts.apis.io/stellary/plans/stellary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stellary-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stellary/rate-limits/stellary-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stellary-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/stellary/conformance/stellary-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stellary-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stellary/security/stellary-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stellary-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Anymfah/stellary-mcp/blob/main/SECURITY.md
- group: design
  href: https://artifacts.apis.io/stellary/data-model/stellary-data-model.yml
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
finops:
- has_sources: true
  method: derived
  name: Stellary Finops
  primary_unit: subscription
  service_category: ''
  slug: stellary-finops
  template: false
image: https://stellary.co/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Stellary MCP Server
  slug: mcp
modified: '2026-10-06'
name: Stellary
nav: Providers
network: true
overview: 'Stellary is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, Productivity, AI Agents, Agent Orchestration, and MCP.


  Stellary''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Stellary Plans Pricing
  plan_count: 2
  slug: stellary-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Stellary Rate Limits
  slug: stellary-rate-limits
scopes:
- name: Stellary Scopes
  scope_count: 8
  slug: stellary-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 44.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stellary/stellary-2026-09-02T160837.png
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
skill_count: 1
skills:
- name: stellary-mcp
  slug: stellary-mcp
slug: stellary
tags:
- Project Management
- Productivity
- AI Agents
- Agent Orchestration
- MCP
- Remote MCP
- Developer Tools
- Software-as-a-Service
- Collaboration
website: https://www.stellary.co/
---
