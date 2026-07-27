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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Stamped Agentic Access
  operation_count: 26
  slug: stamped-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 5
apis:
- description: The Customer Actions API from Stamped — 6 operation(s) for customer actions.
  name: Stamped Customer Actions API
  slug: stamped-customer-actions-api
- description: The Customers API from Stamped — 3 operation(s) for customers.
  name: Stamped Customers API
  slug: stamped-customers-api
- description: The Orders API from Stamped — 3 operation(s) for orders.
  name: Stamped Orders API
  slug: stamped-orders-api
- description: The Products API from Stamped — 3 operation(s) for products.
  name: Stamped Products API
  slug: stamped-products-api
- description: The Program Reporting API from Stamped — 2 operation(s) for program reporting.
  name: Stamped Program Reporting API
  slug: stamped-program-reporting-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stamped-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stamped.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.stamped.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.stamped.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.stamped.io/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.stamped.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://stampedsupport.zendesk.com/hc/en-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stamped-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/stamped-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stamped-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stamped-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stamped-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stamped-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stamped-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stamped-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stamped-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/stamped-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Stamped is a reviews, ratings, and loyalty platform for e-commerce brands on Shopify, BigCommerce, and custom/headless platforms. Its V3 API is organized into three domains: Merchant Data (customers, products, orders), Loyalty Operations (points adjustments, VIP tiers, reward redemption, activities, and program reporting), and Reviews. Authentication is a shop-scoped Private API Key sent in the stamped-api-key header. Surfaced as a portfolio company of GV and enriched by the API Evangelist pipeline from Stamped''s public developer documentation at developers.stamped.io.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stamped.png
layout: provider
mcp_servers:
- description: ''
  name: stamped-mcp.yml
  slug: stamped-mcpyml
modified: '2026-07-21'
name: Stamped
nav: Providers
network: true
overview: 'Stamped publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customer Actions API, Customers API, Orders API, and 2 more. Tagged areas include Company, Consumer, Reviews, Ratings, and Loyalty.


  Stamped''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 13 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.3
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 36.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Stamped Authentication
  slug: stamped-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stamped Domain Security
  slug: stamped-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stamped
tags:
- Company
- Consumer
- Reviews
- Ratings
- Loyalty
- E-Commerce
- Customer Marketing
- Shopify
website: https://stamped.io
---
