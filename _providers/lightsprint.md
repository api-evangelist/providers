---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API over the Lightsprint workspace board — tasks, comments, projects, stacks, and cloud coding agents. Authenticated with OAuth 2.0 authorization-code tokens bound to a single workspace; the repo
  name: Lightsprint API
  slug: lightsprint-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightsprint-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lightsprint.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/SprintsAI/lightsprint-claude-code-plugin#readme
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/SprintsAI/lightsprint-claude-code-plugin#quick-start
- group: company
  title: ''
  type: Blog
  url: https://lightsprint.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lightsprint.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lightsprint.ai/login
- group: start
  title: ''
  type: Login
  url: https://lightsprint.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lightsprint.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightsprint.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/AhK9EBPkqt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SprintsAI
- group: auth
  title: ''
  type: TrustCenter
  url: security/lightsprint-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightsprint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightsprint-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightsprint-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightsprint-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightsprint-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightsprint-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightsprint-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightsprint-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/lightsprint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightsprint-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightsprint-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightsprint-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lightsprint-plans-pricing.yml
- group: company
  title: ''
  type: Careers
  url: https://lightsprint.ai/careers
- group: operate
  title: ''
  type: FAQ
  url: https://lightsprint.ai/faq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightsprint/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/lightsprintai
created: '2026-07-17'
description: Lightsprint is an AI-native product-development platform where developers, product managers, and designers plan, build, and ship together against a codebase a team already runs, rather than a greenfield prototype. Its three surfaces are Plan Mode, which turns plain-English requirements into structured, reviewable visual plans; infinite parallel cloud agents that execute those plans on the team's real repository using Anthropic, Cursor, or Codex models in managed cloud infrastructure instead of on a developer's machine; and per-change preview environments that give every pull request a live URL so non-engineers review a running app instead of a diff. Work is tracked on a workspace board of stacks, projects, tasks, and dependencies exposed through an OAuth 2.0 REST API, a `lightsprint` CLI, a set of published Claude Code Agent Skills, and an n8n community node. Lightsprint was founded by Ben Ong, Benedict Chan, and Heng Hong Lee, and went through Y Combinator's Spring 2026 batch.
image: https://lightsprint.ai/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Lightsprint MCP Server
  slug: lightsprint-mcp-server
modified: '2026-07-19'
name: Lightsprint
nav: Providers
network: true
overview: 'Lightsprint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Artificial Intelligence, Agents, and Software Development.


  Lightsprint''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, authentication, and 24 more developer resources.'
plans:
- name: Lightsprint Plans Pricing
  plan_count: 3
  slug: lightsprint-plans-pricing
random_paper: 11
scopes:
- name: Lightsprint Scopes
  scope_count: 7
  slug: lightsprint-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 39.9
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightsprint/refs/heads/main/screenshots/lightsprint-2026-07-25T225137.png
security:
- kind: authentication
  name: Lightsprint Authentication
  slug: lightsprint-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lightsprint Domain Security
  slug: lightsprint-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Lightsprint Trust Center
  slug: lightsprint-trust-center
  summary_line: SOC 2 Type II
slug: lightsprint
tags:
- Company
- Developer Tools
- Artificial Intelligence
- Agents
- Software Development
- Project Management
- Code Generation
- Team Collaboration
website: https://lightsprint.ai/
---
