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
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: The Categories API from Metrilo — 2 operation(s) for categories.
  name: Metrilo Categories API
  slug: metrilo-categories-api
- description: The Customers API from Metrilo — 4 operation(s) for customers.
  name: Metrilo Customers API
  slug: metrilo-customers-api
- description: The Orders API from Metrilo — 2 operation(s) for orders.
  name: Metrilo Orders API
  slug: metrilo-orders-api
- description: The Products API from Metrilo — 2 operation(s) for products.
  name: Metrilo Products API
  slug: metrilo-products-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metrilo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/Metrilo/custom-integration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metrilo.com
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Metrilo/custom-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metrilo.com/en/collections/57629-getting-started-with-metrilo
- group: operate
  title: ''
  type: Support
  url: https://docs.metrilo.com
- group: company
  title: ''
  type: Blog
  url: https://www.metrilo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Metrilo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metrilo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.metrilo.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.metrilo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metrilo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metrilo.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/metrilo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metrilo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metrilo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metrilo-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metrilo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/metrilo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/metrilo-packages.yml
- group: design
  title: ''
  type: Components
  url: components/metrilo-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metrilo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metrilo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.metrilo.com/en/articles/1613060-metrilo-and-gdpr
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metrilo-llms.txt
created: '2026-07-17'
description: Metrilo is a plug-and-play ecommerce growth platform that combines real-time analytics, an ecommerce CRM, and email marketing for online brands. Founded in 2014 and acquired by Brevo (formerly Sendinblue) in 2021, Metrilo tracks visitor and customer behavior, builds rich customer profiles with 30+ segmentation filters, and powers retention-focused email campaigns. Developers integrate via official plugins for WooCommerce, Magento, and OpenCart, a client-side JavaScript tracking library (window.metrilo), and a server-side ingestion API at trk.mtrl.me/v2 that pushes customers, categories, products, and orders using an API Token plus an HMAC-SHA256 X-Digest request signature.
image: https://www.metrilo.com/images/metrilo-1200x628.png
layout: provider
mcp_servers:
- description: ''
  name: metrilo-mcp.yml
  slug: metrilo-mcpyml
modified: '2026-07-20'
name: Metrilo
nav: Providers
network: true
overview: 'Metrilo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Customers API, Orders API, and 1 more. Tagged areas include Company, Ecommerce, Analytics, CRM, and Email Marketing.


  Metrilo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 54.9
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 49.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Metrilo Authentication
  slug: metrilo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Metrilo Domain Security
  slug: metrilo-domain-security
  summary_line: TLSv1.3
slug: metrilo
tags:
- Company
- Ecommerce
- Analytics
- CRM
- Email Marketing
- Customer Retention
- Tracking
- Marketing
---
