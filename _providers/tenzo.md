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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-01'
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
- description: The Tenzo MCP server gives AI assistants read-only access to restaurant analytics, reviews, and manager logs through natural language. Users authorize with their Tenzo account via OAuth on first conne
  name: Tenzo MCP Server
  slug: tenzo-mcp-server
modified: '2026-07-21'
name: Tenzo
nav: Providers
network: true
overview: 'Tenzo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Analytics, Business Intelligence, and Reporting.


  Tenzo''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 12 more developer resources.'
random_paper: 14
scopes:
- name: Tenzo Scopes
  scope_count: 4
  slug: tenzo-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 27.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Point-of-Sale
- Data Aggregation
- MCP
- Artificial Intelligence
website: https://gotenzo.com/
---
