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
- acting_count: 10
  human_in_the_loop: 0
  name: Fyndiq Agentic Access
  operation_count: 16
  slug: fyndiq-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 2
apis:
- description: Create, update, retrieve and delete product articles.
  name: Fyndiq Articles API
  slug: fyndiq-articles-api
- description: Retrieve, fulfil and cancel marketplace orders.
  name: Fyndiq Orders API
  slug: fyndiq-orders-api
artifact_total: 7
collections:
- collection_type: postman
  name: NEW FYNDIQ API
  slug: postman-fyndiq-merchant-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.fyndiq.se
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fyndiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fyndiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://merchantapi.fyndiq.com/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/2328684/7185ENK
- group: operate
  title: ''
  type: Support
  url: https://support.fyndiq.se/hc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fyndiq
- group: start
  title: ''
  type: Login
  url: https://merchantcenter.fyndiq.se/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fyndiq.se/fyndiq/policy-och-villkor/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fyndiq.se/fyndiq/policy-och-villkor/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fyndiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fyndiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fyndiq-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fyndiq-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fyndiq-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fyndiq-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fyndiq-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fyndiq-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/fyndiq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fyndiq-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fyndiq-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fyndiq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fyndiq-domain-security.yml
created: '2026-07-17'
description: Fyndiq is Sweden's largest online marketplace for bargains and deals, connecting merchants with millions of deal-seeking consumers across categories from electronics and mobile accessories to home, fashion, beauty and children's goods. Merchants list products while Fyndiq handles the storefront, customer relations and payments. Fyndiq exposes a REST Merchant API that lets sellers upload and manage product articles (create, bulk, price, quantity, delete) and retrieve, fulfil and cancel orders. The API is JSON over HTTPS, secured with HTTP Basic Authentication (Base64 merchantID:token), with a self-contained sandbox environment for integration testing and official Magento, PrestaShop and WooCommerce integration modules. Fyndiq is part of the CDON marketplace group and was originally backed by Northzone.
image: https://fyndiq.se/fyndiq/fyndiq_share.png
layout: provider
mcp_servers:
- description: ''
  name: fyndiq-mcp.yml
  slug: fyndiq-mcpyml
modified: '2026-07-19'
name: Fyndiq
nav: Providers
network: true
overview: 'Fyndiq publishes 2 APIs on the [APIs.io](https://apis.io/) network: Articles API and Orders API. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Retail.


  Fyndiq''s developer surface includes documentation, API reference, support, authentication, sandbox, and 19 more developer resources.'
random_paper: 39
score:
  band: developing
  composite: 45.5
  delta: 3.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.5
    developer_ergonomics: 71.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 42.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fyndiq/refs/heads/main/screenshots/fyndiq-2026-07-25T215343.png
security:
- kind: authentication
  name: Fyndiq Authentication
  slug: fyndiq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fyndiq Domain Security
  slug: fyndiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fyndiq
tags:
- Company
- Consumer
- Marketplace
- E-Commerce
- Retail
- Products
- Orders
- Sweden
website: https://www.fyndiq.se
---
