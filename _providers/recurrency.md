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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Supplier product catalog retrieval, filtering and upload.
  name: Recurrency E-Procurement API
  slug: recurrency-e-procurement-api
- description: Create, list and retrieve sales orders and quotes.
  name: Recurrency Orders API
  slug: recurrency-orders-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Discover a supplier, find an item, confirm price, create an order, and read it back.
  name: Recurrency procure-to-pay
  slug: recurrency-procure-to-pay
artifact_total: 9
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://recurrency.gitbook.io/recurrency/
- group: docs
  title: ''
  type: Documentation
  url: https://recurrency.gitbook.io/recurrency/
- group: auth
  title: ''
  type: Authentication
  url: authentication/recurrency-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/recurrency-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recurrency-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recurrency-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/recurrency-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/recurrency-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/recurrency-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/recurrency-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/recurrency-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recurrency-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/recurrency-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/recurrency-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/recurrency-procure-to-pay.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recurrency-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recurrency-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/recurrency-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Blog
  url: https://www.recurrency.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recurrency
- group: operate
  title: ''
  type: Support
  url: https://recurrency.gitbook.io/recurrency/support/need-help
- group: start
  title: ''
  type: SignUp
  url: https://www.recurrency.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.recurrency.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.recurrency.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.recurrency.com/
created: '2026-07-17'
description: Recurrency is an AI-powered ERP automation platform for wholesale distributors and B2B suppliers, sitting on top of distribution ERPs to automate and optimize purchasing and sales — forecasting, pricing, reorders and product recommendations across sales, purchasing and operations workflows. Recurrency exposes a public e-procurement REST API (documented on GitBook) for authenticating, retrieving and filtering a supplier's product catalog (items, availability, pricing, locations, groups), uploading catalog data, and creating and managing sales orders and quotes. It also operates a hosted, OAuth-secured MCP server for agent access. Backed by Bessemer Venture Partners.
image: https://storage.googleapis.com/s.mkswft.com/RmlsZTpiNjE4NGRjYy01OGVjLTQ2YWQtOWMyMS0zNjJiZWZiNmYxOTM=/recurrency-dashboard.webp
layout: provider
mcp_servers:
- description: ''
  name: recurrency-mcp.yml
  slug: recurrency-mcpyml
modified: '2026-07-21'
name: Recurrency
nav: Providers
network: true
overview: 'Recurrency publishes 2 APIs on the [APIs.io](https://apis.io/) network: E-Procurement API and Orders API. Tagged areas include Company, Ai Ml, ERP, Distribution, and Wholesale.


  Recurrency''s developer surface includes documentation, authentication, sandbox, engineering blog, support, signup flow, and 20 more developer resources.'
random_paper: 19
scopes:
- name: Recurrency Scopes
  scope_count: 4
  slug: recurrency-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.7
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 45.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Recurrency Authentication
  slug: recurrency-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Recurrency Domain Security
  slug: recurrency-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Recurrency Vulnerability Disclosure
  slug: recurrency-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: recurrency
tags:
- Company
- Ai Ml
- ERP
- Distribution
- Wholesale
- E-Procurement
- Supply Chain
- Orders
website: https://www.recurrency.com/
---
