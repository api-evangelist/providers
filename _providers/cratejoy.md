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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: 'REST interface into most of the data and functionality of interest to Cratejoy merchants and developers: customers, orders, subscriptions, shipments, products, inventory, carts, transactions, addresse'
  name: Cratejoy Merchant API
  slug: cratejoy-merchant-api
- description: 'Front-end API that lets storefront JavaScript read (and sometimes write) data on behalf of the logged-in customer: customer, product, subscription, shipment, address, and survey methods, plus add-to-c'
  name: Cratejoy Store API
  slug: cratejoy-store-api
artifact_total: 6
asyncapis:
- description: ''
  name: Cratejoy Webhooks
  slug: cratejoy-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.cratejoy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cratejoy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cratejoy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cratejoy.com/reference/introduction-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cratejoy.com/reference/quick-start-add-a-tracking-number-to-a-shipment
- group: operate
  title: ''
  type: Support
  url: https://www.cratejoy.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://www.cratejoy.com/blogs/box-insider
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cratejoy
- group: commercial
  title: ''
  type: Pricing
  url: https://sell.cratejoy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sell.cratejoy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cratejoy.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cratejoy.com/pages/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cratejoy.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cratejoy-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cratejoy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cratejoy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cratejoy-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cratejoy-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cratejoy-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/cratejoy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cratejoy-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cratejoy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cratejoy-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cratejoy-domain-security.yml
created: '2026-07-17'
description: 'Cratejoy is a subscription-box commerce platform and marketplace (a CRV and Y Combinator company) that lets independent creators launch, sell, and manage recurring subscription boxes and one-time products. It exposes two public REST APIs: a Merchant API (https://api.cratejoy.com/v1/) covering customers, orders, subscriptions, shipments, products, inventory, carts, transactions, and webhooks; and a front-end Store API for reading and writing customer-scoped data from a storefront theme. Resources are JSON, authenticated with HTTP Basic credentials, paginated, filterable with double-underscore operators, and rate-limited with Retry-After.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cratejoy.png
layout: provider
mcp_servers:
- description: ''
  name: cratejoy-mcp.yml
  slug: cratejoy-mcpyml
modified: '2026-07-18'
name: Cratejoy
nav: Providers
network: true
overview: 'Cratejoy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Subscriptions, Subscription Boxes, and Marketplace.


  The Cratejoy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cratejoy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 120
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 43.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cratejoy/refs/heads/main/screenshots/cratejoy-2026-07-25T210648.png
security:
- kind: authentication
  name: Cratejoy Authentication
  slug: cratejoy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cratejoy Domain Security
  slug: cratejoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cratejoy
tags:
- Company
- Ecommerce
- Subscriptions
- Subscription Boxes
- Marketplace
- Payments
- Orders
- Webhooks
- REST
website: https://www.cratejoy.com/
---
