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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Flipkart Marketplace Seller API (v3) lets sellers and integration partners manage listings, orders, shipments, returns, and reports on the Flipkart marketplace programmatically. It is a REST API h
  name: Flipkart Marketplace Seller API
  slug: flipkart-marketplace-seller-api
artifact_total: 6
asyncapis:
- description: ''
  name: Flipkart Notifications Webhooks
  slug: flipkart-notifications-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://seller.flipkart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://seller.flipkart.com/api-docs/FMSAPI.html
- group: docs
  title: ''
  type: APIReference
  url: https://seller.flipkart.com/api-docs/FMSAPI.html
- group: operate
  title: ''
  type: Support
  url: https://seller.flipkart.com/index.html#help/gstin
- group: start
  title: ''
  type: SignUp
  url: https://seller.flipkart.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flipkart.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flipkart.com/pages/privacypolicy
- group: auth
  title: ''
  type: Authentication
  url: authentication/flipkart-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flipkart-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flipkart-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flipkart-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flipkart-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flipkart-notifications-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flipkart-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flipkart-llms.txt
created: '2026-07-17'
description: 'Flipkart is one of India''s largest e-commerce marketplaces, headquartered in Bengaluru and majority-owned by Walmart. For third-party developers and sellers it publishes the Flipkart Marketplace Seller API (v3), an OAuth 2.0 protected REST API hosted at api.flipkart.net that covers listing management, order and shipment management, returns, and report generation, plus an Order Management Notification (webhook) service for order events. Flipkart also runs an affiliate program with its own tooling. This profile captures Flipkart''s public developer surface: the seller API, its OAuth authentication and scopes, conventions, lifecycle, and domain security posture.'
image: https://logo.clearbit.com/flipkart.com
layout: provider
mcp_servers:
- description: ''
  name: flipkart-mcp.yml
  slug: flipkart-mcpyml
modified: '2026-07-19'
name: Flipkart
nav: Providers
network: true
overview: 'Flipkart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Marketplace, and Retail.


  The Flipkart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flipkart''s developer surface includes documentation, API reference, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 61
scopes:
- name: Flipkart Scopes
  scope_count: 2
  slug: flipkart-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 36.6
  delta: 4.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 32.3
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flipkart/refs/heads/main/screenshots/flipkart-2026-07-25T214803.png
security:
- kind: authentication
  name: Flipkart Authentication
  slug: flipkart-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Flipkart Domain Security
  slug: flipkart-domain-security
  summary_line: TLSv1.2 · DMARC
slug: flipkart
tags:
- Company
- Consumer
- E-Commerce
- Marketplace
- Retail
- Sellers
- Orders
- Fulfillment
- India
- OAuth
website: https://seller.flipkart.com/
---
