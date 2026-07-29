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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Extend''s REST API for product and shipping protection: manage offers, contracts, orders and line items, refunds, claims, service orders, and leads. Header-based date versioning; OAuth2 client-credenti'
  name: Extend API
  slug: extend-api
artifact_total: 5
asyncapis:
- description: ''
  name: Extend Webhooks
  slug: extend-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/extend-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.extend.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.extend.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.extend.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.extend.com/docs/getting-started-with-extends-api
- group: operate
  title: ''
  type: Support
  url: https://www.extend.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.extend.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helloextend
- group: start
  title: ''
  type: Login
  url: https://merchants.extend.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.extend.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.extend.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.extend.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.extend.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/extend-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/extend-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/extend-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/extend-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/extend-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/extend-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/extend-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/extend-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/extend-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/extend-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/extend-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/extend-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/extend-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/extend-packages.yml
created: '2026-07-17'
description: Extend is a product and shipping protection platform for merchants and ecommerce brands. Its API lets merchants surface extended-warranty and shipping-protection offers at checkout and post-purchase, create and manage protection contracts, process orders and line items, file and track claims, and manage service orders, refunds, and leads. Extend provides separate demo (sandbox) and production environments, header-based date versioning, OAuth2 client-credentials authentication with short-lived access tokens, idempotency keys on writes, and webhooks for claim and service-order status changes, alongside client-side SDKs and prebuilt commerce-platform integrations for Shopify, BigCommerce, Magento, WooCommerce, and Salesforce Commerce Cloud.
image: https://avatars.githubusercontent.com/u/46018312?v=4
layout: provider
mcp_servers:
- description: ''
  name: extend-mcp.yml
  slug: extend-mcpyml
modified: '2026-07-19'
name: Extend
nav: Providers
network: true
overview: 'Extend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Product Protection, Extended Warranty, and Shipping Protection.


  The Extend catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Extend''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 47.5
  delta: 3.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 44.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/screenshots/extend-2026-07-25T213943.png
security:
- kind: authentication
  name: Extend Authentication
  slug: extend-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Extend Domain Security
  slug: extend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: extend
tags:
- Company
- Consumer
- Product Protection
- Extended Warranty
- Shipping Protection
- Ecommerce
- Warranty
- Claims
- Contracts
- Retail
- Insurance
website: https://docs.extend.com
---
