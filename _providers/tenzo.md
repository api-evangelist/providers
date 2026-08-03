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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'Public REST API for accessing restaurant analytics data — locations, areas, sales, and forecast data — secured with OAuth 2.0 Bearer tokens. Partners integrate via the Authorization Code flow to pull '
  name: Tenzo API
  slug: tenzo-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://gotenzo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gotenzo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.gotenzo.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://support.gotenzo.com/developers/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.gotenzo.com/developers/auth-flow/
- group: auth
  title: ''
  type: Authentication
  url: https://support.gotenzo.com/developers/auth-flow/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tenzo-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tenzo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tenzo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tenzo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tenzo-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tenzo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gotenzo.com/gdpr/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenzo-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gotenzo.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tenzo-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.gotenzo.com/resources/insights/technology/
- group: operate
  title: ''
  type: Support
  url: https://support.gotenzo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gotenzo.com/privacy-policy/
created: '2026-07-17'
description: Tenzo is a restaurant analytics and business-intelligence platform that unifies data from point-of-sale, labor scheduling, inventory, reviews, and reservation systems into a single reporting layer. It aggregates across 90+ integrated platforms and layers AI, demand forecasting, and automated reporting on top so multi-site restaurant operators can manage staffing, food and labor cost, and revenue. Tenzo exposes a public REST API (api.gotenzo.com/public/v1), an OAuth 2.0 Authorization Code (PKCE) partner integration for per-customer access, and a hosted Model Context Protocol (MCP) server for connecting AI assistants directly to restaurant data.
image: https://support.gotenzo.com/wp-content/uploads/2026/05/TenzoLogo_RGB_orange.svg
layout: provider
mcp_servers:
- description: ''
  name: tenzo-mcp.yml
  slug: tenzo-mcpyml
modified: '2026-07-21'
name: Tenzo
nav: Providers
network: true
overview: 'Tenzo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Analytics, Business Intelligence, and Reporting.


  Tenzo''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 12 more developer resources.'
random_paper: 85
scopes:
- name: Tenzo Scopes
  scope_count: 4
  slug: tenzo-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 30.2
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 30.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Tenzo Authentication
  slug: tenzo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tenzo Domain Security
  slug: tenzo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tenzo
tags:
- Company
- Restaurant
- Analytics
- Business Intelligence
- Reporting
- Forecasting
- Hospitality
- Point of Sale
- Data Aggregation
- MCP
- Artificial Intelligence
website: https://gotenzo.com/
---
