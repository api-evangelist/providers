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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Jelly's GraphQL API for costing and kitchen management. Single POST endpoint at api.getjelly.co.uk with bearer-token auth and public introspection; exposes kitchens, ingredients, recipes, dishes, menu
  name: Jelly GraphQL API
  slug: jelly-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jelly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getjelly.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getjelly.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getjelly.co.uk/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getjelly.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getjelly.co.uk/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.getjelly.co.uk/support
- group: start
  title: ''
  type: SignUp
  url: https://kitchen.getjelly.co.uk/signup
- group: start
  title: ''
  type: Login
  url: https://kitchen.getjelly.co.uk/signin
- group: auth
  title: ''
  type: Security
  url: https://www.getjelly.co.uk/security
- group: docs
  title: ''
  type: GraphQL
  url: graphql/jelly-api.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/jelly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jelly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jelly-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jelly-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/jelly-packages.yml
- group: design
  title: ''
  type: Components
  url: components/jelly-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jelly-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jelly-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jelly-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jelly-llms.txt
created: '2026-07-17'
description: Jelly (getjelly.co.uk) is an all-in-one costing and kitchen-management platform for the hospitality industry - restaurants and professional kitchens. It handles supplier invoice processing, ingredient and recipe costing, gross-profit (GP) analysis, menu and dish management, suppliers, products, purchase orders and stock. Jelly runs a GraphQL API at api.getjelly.co.uk (bearer-authenticated, public introspection, 232 queries and 168 mutations) behind its kitchen web app, and publishes a first-party UI component library (Jelly UI, @getjelly/jelly-ui). Surfaced originally as a Seedcamp portfolio company and enriched here from its live public surface.
image: https://kitchen.getjelly.co.uk/icons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: jelly-mcp.yml
  slug: jelly-mcpyml
modified: '2026-07-19'
name: Jelly
nav: Providers
network: true
overview: 'Jelly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Restaurants, Kitchen Management, and Food Costing.


  Jelly''s developer surface includes documentation, pricing, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 34
score:
  band: emerging
  composite: 27.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Jelly Authentication
  slug: jelly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jelly Domain Security
  slug: jelly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jelly Vulnerability Disclosure
  slug: jelly-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: jelly
tags:
- Company
- Hospitality
- Restaurants
- Kitchen Management
- Food Costing
- Recipe Costing
- Invoice Processing
- GraphQL
- SaaS
website: https://www.getjelly.co.uk/
---
