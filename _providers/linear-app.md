---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.4
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: 'Single GraphQL endpoint exposing Linear''s full data model - issues, projects, initiatives, cycles, teams, users, comments, documents, customers, customer requests, and more. Auth via OAuth 2.0 Bearer '
  name: Linear GraphQL API
  slug: linear-graphql-api
- description: Outbound webhooks for data-change events across Issues, Issue attachments, Issue comments, Issue labels, Comment reactions, Projects, Project updates, Documents, Initiatives, Initiative updates, Cycle
  name: Linear Webhooks
  slug: linear-webhooks
- description: OAuth 2.0 authorization-code and PKCE flows for third-party apps. Authorize at https://linear.app/oauth/authorize, exchange tokens at https://api.linear.app/oauth/token. Scopes include read, write, is
  name: Linear OAuth 2.0
  slug: linear-oauth
- description: Capabilities for AI agents to operate as first-class actors inside Linear - Agent Interaction Guidelines (AIG), signals, and best-practice patterns for interacting with users and issues.
  name: Linear Agents API
  slug: linear-agents-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/linear-app-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linear-app-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linear-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linear.app
- group: start
  title: ''
  type: Signup
  url: https://linear.app/signup
- group: start
  title: ''
  type: Login
  url: https://linear.app/login
- group: docs
  title: ''
  type: Documentation
  url: https://linear.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://linear.app/developers
- group: docs
  title: ''
  type: APIReference
  url: https://linear.app/developers/graphql
- group: auth
  title: ''
  type: Authentication
  url: https://linear.app/developers/oauth-2-0-authentication
- group: build
  title: ''
  type: SDKs
  url: https://linear.app/developers/sdk
- group: design
  title: ''
  type: Webhooks
  url: https://linear.app/developers/webhooks
- group: other
  title: ''
  type: Agents
  url: https://linear.app/developers/agents
- group: operate
  title: ''
  type: RateLimits
  url: https://linear.app/developers/rate-limiting
- group: operate
  title: ''
  type: StatusPage
  url: https://linearstatus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://linear.app/pricing
- group: other
  title: ''
  type: Enterprise
  url: https://linear.app/enterprise
- group: other
  title: ''
  type: Startups
  url: https://linear.app/startups
- group: other
  title: ''
  type: Sales
  url: https://linear.app/contact/sales
- group: auth
  title: ''
  type: Security
  url: https://linear.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linear.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linear.app/terms
- group: other
  title: ''
  type: DPA
  url: https://linear.app/dpa
- group: operate
  title: ''
  type: ChangeLog
  url: https://linear.app/changelog
- group: company
  title: ''
  type: Blog
  url: https://linear.app/blog
- group: operate
  title: ''
  type: Slack
  url: https://linear.app/join-slack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linear
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/linear/linear
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/linear
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@linear
- group: auth
  title: ''
  type: APIKeys
  url: https://linear.app/settings/api
- group: agent
  title: ''
  type: LlmsText
  url: https://linear.app/llms.txt
created: '2026-05-23'
description: Linear is an issue tracking and product development platform for software teams covering Intake, Plan, Build, Diffs (code review), and Monitor. The public developer surface is a GraphQL API at https://api.linear.app/graphql with OAuth 2.0 and personal API key auth, signed webhooks, a TypeScript SDK, an Agent SDK / Agent Interaction Guidelines for AI agents, and integrations with GitHub, Slack, Figma, Cursor, Codex, GitHub Copilot, and others. Serves 25,000+ product teams.
features:
- GraphQL API at https://api.linear.app/graphql with full introspection
- OAuth 2.0 with PKCE plus personal API key auth
- Strongly-typed TypeScript SDK (v2.x) with webhook helpers
- HMAC-SHA256 signed webhooks via Linear-Signature header
- 15+ webhook resource types (Issues, Projects, Initiatives, Cycles, Customers, etc.)
- Apollo Studio playground for live schema exploration
- Agents framework with Agent Interaction Guidelines
- Native integrations with GitHub, Slack, Figma, Sentry, Zendesk
- AI agent integrations including Codex, GitHub Copilot, Cursor
- Triage inbox for routing intake into actionable issues
- Diffs for structural code review visualization
- Mobile apps for iOS and Android
- 25,000+ product teams using Linear
finops:
- name: Linear App Finops
  service_category: API
  slug: linear-app-finops
graphqls:
- description: 'Single GraphQL endpoint exposing Linear''s full data model - issues, projects, initiatives, cycles, teams, users, comments, documents, customers, customer requests, and more. Auth via OAuth 2.0 Bearer '
  name: Linear GraphQL API
  slug: linear-app-graphql
image: https://linear.app/static/og/homepage.jpg
layout: provider
modified: '2026-05-23'
name: Linear
nav: Providers
network: true
overview: 'Linear publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, Issue Tracking, Productivity, Software-as-a-Service, and GraphQL.


  Linear''s developer surface includes signup flow, documentation, API reference, authentication, pricing, changelog, engineering blog, and 25 more developer resources.'
plans:
- name: Linear App Plans Pricing
  plan_count: 1
  slug: linear-app-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Linear App Rate Limits
  slug: linear-app-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 76.3
  previous_composite: 41.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linear-app/refs/heads/main/screenshots/linear-app-2026-06-20T184548.png
security:
- kind: domain-security
  name: Linear App Domain Security
  slug: linear-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linear App Vulnerability Disclosure
  slug: linear-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Linear App Trust Center
  slug: linear-app-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: linear-app
tags:
- Project Management
- Issue Tracking
- Productivity
- Software-as-a-Service
- GraphQL
- Developer Tools
- Agents
website: https://linear.app
---
