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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: OAuth 2.0 REST API for automating content generation with Matik — manage templates, generate presentations/documents/spreadsheets, run dynamic content queries against connected data sources, manage da
  name: Matik External API
  slug: matik-external-api
artifact_total: 7
asyncapis:
- description: ''
  name: Matik Webhooks
  slug: matik-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://matik.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.matik.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.matik.io/docs/category/matik-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.matik.io/docs/matik/matik-external-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.matik.io/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.matik.io
- group: company
  title: ''
  type: Blog
  url: https://www.matik.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matik-io
- group: start
  title: ''
  type: SignUp
  url: https://www.matik.io/request-demo
- group: start
  title: ''
  type: Login
  url: https://app.matik.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.matik.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matik.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.matik.io
- group: auth
  title: ''
  type: Security
  url: https://www.matik.io/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.matik.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/matik-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matik-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/matik-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matik-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/matik-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matik-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matik-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matik-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matik-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matik-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matik-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Matik is a data-driven content automation platform that generates personalized presentations, documents, spreadsheets, reports, and emails directly from connected data sources — BI tools, CRMs, data warehouses, spreadsheets, and REST APIs. Teams in Sales, Customer Success, and Revenue Operations use templates with dynamic content, conditional logic, and AI-generated narratives to produce on-brand content at scale across Google Slides, PowerPoint, PDF, and email. Matik exposes a REST External API (OAuth 2.0) covering templates, presentations, dynamic content, data sources, bulk generation, analytics, webhooks, and AI query building, plus a beta MCP server for agent-driven content generation.
image: https://cdn.prod.website-files.com/6169c25fc3b5f387dbc1b0ab/672c8fdcb72e6d3999cd7f45_Matik%20Logo%20On%20White%20Colored.png
layout: provider
mcp_servers:
- description: ''
  name: matik-mcp.yml
  slug: matik-mcpyml
modified: '2026-07-20'
name: Matik
nav: Providers
network: true
overview: 'Matik publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Automation, Presentations, Documents, and Data-Driven Content.


  The Matik catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matik''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 42
scopes:
- name: Matik Scopes
  scope_count: 2
  slug: matik-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.7
  delta: 7.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 43.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/matik/refs/heads/main/screenshots/matik-2026-07-25T230412.png
security:
- kind: authentication
  name: Matik Authentication
  slug: matik-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Matik Domain Security
  slug: matik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Matik Trust Center
  slug: matik-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, GDPR
slug: matik
tags:
- Company
- Content Automation
- Presentations
- Documents
- Data-Driven Content
- Sales Enablement
- Customer Success
- Revenue Operations
- AI
- MCP
website: https://matik.io
---
