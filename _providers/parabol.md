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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Public GraphQL API for Parabol. Authenticated with scoped Personal Access Tokens passed as a Bearer token. A single root `viewer` query returns the authenticated user and their teams, meetings, tasks,
  name: Parabol GraphQL API
  slug: parabol-graphql-api
artifact_total: 8
asyncapis:
- description: Real-time event streams exposed by the Parabol GraphQL API via the Subscription root type, delivered over the graphql-ws WebSocket protocol. Requires a scoped Personal Access Token.
  name: Parabol GraphQL Subscriptions
  slug: parabol-graphql-subscriptions-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.parabol.co/
- group: docs
  title: ''
  type: APIReference
  url: https://action.parabol.co/graphql
- group: docs
  title: ''
  type: Documentation
  url: https://www.parabol.co/friday-ship/introducing-the-parabol-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.parabol.co/friday-ship/introducing-the-parabol-api/
- group: company
  title: ''
  type: Blog
  url: https://www.parabol.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ParabolInc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parabol.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://action.parabol.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parabol.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parabol.co/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.parabol.co/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://parabol.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ParabolInc/parabol/releases
- group: auth
  title: ''
  type: Authentication
  url: authentication/parabol-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/parabol-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parabol-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parabol-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parabol-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parabol-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.parabol.co/security-faq/
- group: auth
  title: ''
  type: TrustCenter
  url: security/parabol-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parabol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.parabol.co/security-faq/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parabol-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/parabol-graphql-subscriptions-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parabol-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/parabol-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parabol-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parabol-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/parabol-changelog.yml
created: '2026-07-17'
description: Parabol is an open-source collaborative workspace that helps teams run more effective, inclusive, and engaging meetings — retrospectives, sprint poker estimation, check-ins/standups, and collaborative Pages documents — all in real time. Parabol exposes a public GraphQL API at action.parabol.co/graphql authenticated with scoped Personal Access Tokens (Bearer), letting developers and AI agents start meetings, create reflections and tasks, read team and organization data, and subscribe to live meeting events. The platform is dual-licensed AGPLv3, self-hostable for air-gapped deployments, and integrates with Jira, GitHub, GitLab, Linear, Azure DevOps, Slack, and Mattermost.
image: https://action-files.parabol.co/production/build/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: parabol-mcp.yml
  slug: parabol-mcpyml
modified: '2026-07-20'
name: Parabol
nav: Providers
network: true
overview: 'Parabol publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Company, Developer Tools, Agile, Retrospectives, and Meetings.


  The Parabol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Parabol''s developer surface includes API reference, documentation, getting-started guide, engineering blog, pricing, signup flow, support, and 24 more developer resources.'
random_paper: 141
scopes:
- name: Parabol Scopes
  scope_count: 16
  slug: parabol-scopes
  summary_line: 16 scopes
score:
  band: developing
  composite: 47.1
  delta: -5.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 56.9
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 52.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/parabol/refs/heads/main/screenshots/parabol-2026-08-07T191355.png
security:
- kind: authentication
  name: Parabol Authentication
  slug: parabol-authentication
  summary_line: http-bearer/personal-access-token · 1 scheme
- kind: domain-security
  name: Parabol Domain Security
  slug: parabol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Parabol Vulnerability Disclosure
  slug: parabol-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Parabol Trust Center
  slug: parabol-trust-center
  summary_line: SOC 2 Type 2, GDPR, CalOPPA
slug: parabol
tags:
- Company
- Developer Tools
- Agile
- Retrospectives
- Meetings
- Collaboration
- GraphQL
- Team Productivity
- Open Source
website: https://www.parabol.co/
---
