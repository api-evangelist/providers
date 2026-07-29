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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST data API exposing Grips Intelligence e-commerce analytics. Requests are HTTPS POSTs carrying a GraphQL-style query envelope (query + variables), scoped by domain, date range, and country. Endpoin
  name: Grips Data API
  slug: grips-data-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://gripsintelligence.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gripsintelligence.com/knowledge-base/api
- group: docs
  title: ''
  type: Documentation
  url: https://gripsintelligence.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://gripsintelligence.com/knowledge-base/api
- group: company
  title: ''
  type: About
  url: https://gripsintelligence.com/about
- group: company
  title: ''
  type: Blog
  url: https://gripsintelligence.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gripsintelligence.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gripsintelligence.com/login
- group: start
  title: ''
  type: Login
  url: https://app.gripsintelligence.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gripsintelligence.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gripsintelligence.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://gripsintelligence.com/contact-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gripsintelligence
- group: agent
  title: ''
  type: MCPServer
  url: mcp/grips-intelligence-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grips-intelligence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/grips-intelligence-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/grips-intelligence-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/grips-intelligence-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grips-intelligence-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grips-intelligence-llms.txt
created: '2026-07-17'
description: Grips Intelligence (Peekd) is an e-commerce intelligence platform that provides daily online and offline product sales measurement and competitive analysis. It tracks competitor metrics — units sold, pricing, revenue per product, top sellers, and new product launches — across major retailers, alongside domain-level site metrics such as revenue, conversion rate, average order value, and traffic sources. Data is available at SKU and category granularity for brand and category benchmarking and new-product opportunity discovery. Grips exposes a REST Data API (API-key authenticated) and an OAuth-protected remote MCP server ("Peekd Data MCP") that make its intelligence data programmatically and agent-accessible.
image: https://gripsintelligence.com/favicon/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: grips-intelligence-mcp.yml
  slug: grips-intelligence-mcpyml
modified: '2026-07-19'
name: Grips Intelligence
nav: Providers
network: true
overview: 'Grips Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce Intelligence, Competitive Intelligence, Market Research, and Analytics.


  Grips Intelligence''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, authentication, and 13 more developer resources.'
random_paper: 13
scopes:
- name: Grips Intelligence Scopes
  scope_count: 1
  slug: grips-intelligence-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 28.3
  delta: -0.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.9
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grips-intelligence/refs/heads/main/screenshots/grips-intelligence-2026-07-25T220333.png
security:
- kind: authentication
  name: Grips Intelligence Authentication
  slug: grips-intelligence-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Grips Intelligence Domain Security
  slug: grips-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grips-intelligence
tags:
- Company
- E-commerce Intelligence
- Competitive Intelligence
- Market Research
- Analytics
- Product Intelligence
- Retail
- Data
website: https://gripsintelligence.com/
---
