---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://app.matik.io/api/1.0/
  baseurl_source: declared
  description: OAuth 2.0 REST API for automating content generation with Matik — manage templates, generate presentations/documents/spreadsheets, run dynamic content queries against connected data sources, manage da
  name: Matik External API
  slug: matik-external-api
artifact_total: 9
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
- group: build
  title: ''
  type: Postman
  url: https://developer.matik.io/guides/oauth
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/matik-io/api-example-app
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/matik-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/matik-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/matik-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matik-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matik-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matik-plans-pricing.yml
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
  name: Matik MCP Server
  slug: matik-mcp-server
modified: '2026-08-14'
name: Matik
nav: Providers
network: true
overview: 'Matik publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Company, Content Automation, Presentations, Documents, and Data-Driven Content.


  The Matik catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matik''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 26 more developer resources.'
plans:
- name: Matik Plans Pricing
  plan_count: 0
  slug: matik-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Matik Rate Limits
  slug: matik-rate-limits
scopes:
- name: Matik Scopes
  scope_count: 2
  slug: matik-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 46.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Artificial Intelligence
- MCP
website: https://matik.io
---
