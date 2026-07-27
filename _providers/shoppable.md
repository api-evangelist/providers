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
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Shoppable Agentic Access
  operation_count: 8
  slug: shoppable-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 6
apis:
- description: The Catalog API from Shoppable — 1 operation(s) for catalog.
  name: Shoppable Catalog API
  slug: shoppable-catalog-api
- description: The Checkout API from Shoppable — 1 operation(s) for checkout.
  name: Shoppable Checkout API
  slug: shoppable-checkout-api
- description: The Merchants API from Shoppable — 2 operation(s) for merchants.
  name: Shoppable Merchants API
  slug: shoppable-merchants-api
- description: The OrderData API from Shoppable — 1 operation(s) for orderdata.
  name: Shoppable OrderData API
  slug: shoppable-orderdata-api
- description: The Orders API from Shoppable — 2 operation(s) for orders.
  name: Shoppable Orders API
  slug: shoppable-orders-api
- description: The Products API from Shoppable — 1 operation(s) for products.
  name: Shoppable Products API
  slug: shoppable-products-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoppable-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shoppable-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shoppable-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shoppable-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shoppable-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shoppable-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shoppable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shoppable.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shoppable-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shoppable-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://about.shoppable.com/help/setup-developer-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://ask.shoppable.com
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis-docs/shoppable-dca/shoppable-cloud_api/1.0.2
- group: start
  title: ''
  type: GettingStarted
  url: https://about.shoppable.com/help/setup-developer-documentation
- group: operate
  title: ''
  type: Support
  url: https://ask.shoppable.com
- group: company
  title: ''
  type: Blog
  url: https://about.shoppable.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://about.shoppable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.shoppable.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.shoppable.com/terms#terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.shoppable.com/terms#privacy-policy
- group: company
  title: ''
  type: Website
  url: https://shoppable.com
created: '2026-07-17'
description: Shoppable is embeddable commerce infrastructure that lets shoppers buy any product from any retailer in a single universal cart without leaving the content they are in. Founded in 2011 by Heather Udo, the company powers off-site commerce across editorial content, social media, ads, connected TV, email, and emerging AI/agentic channels through a single integration. Its Shoppable Commerce API Suite (OpenAPI 3.0) exposes product lookup, catalog search, merchant data, order data, and a universal v6 checkout backed by Stripe tokenization, plus a hosted Model Context Protocol (MCP) server for agentic commerce. Shoppable holds four U.S. patents for universal checkout and is backed by 500 Global, MI Ventures, and Bodley Group.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shoppable.png
layout: provider
mcp_servers:
- description: ''
  name: shoppable-mcp.yml
  slug: shoppable-mcpyml
modified: '2026-07-21'
name: Shoppable
nav: Providers
network: true
overview: 'Shoppable publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Checkout API, Merchants API, and 3 more. Tagged areas include Company, Commerce, E-Commerce, Checkout, and Catalog.


  Shoppable''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.3
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 51.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Shoppable Authentication
  slug: shoppable-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shoppable Domain Security
  slug: shoppable-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shoppable
tags:
- Company
- Commerce
- E-Commerce
- Checkout
- Catalog
- Payments
- Agentic Commerce
- MCP
- Embeddable Commerce
- Retail
website: https://shoppable.com
---
