---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Swell Agentic Access
  operation_count: 10
  slug: swell-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 4
apis:
- description: Server-side REST API for managing the full commerce model in Swell, including products, variants, stock, categories, orders, carts, payments, refunds, shipments, subscriptions, customers, discounts, g
  name: Swell Backend API
  slug: backend-api
- description: Client-side API and Swell.js SDK for building custom storefronts. Exposes products, categories, accounts, sessions, addresses, credit cards, carts, orders, payments, coupons, promotions, gift cards, s
  name: Swell Frontend (Storefront) API
  slug: frontend-api
- description: The Orders API from Swell — 2 operation(s) for orders.
  name: Swell Orders API
  slug: swell-orders-api
- description: The Products API from Swell — 2 operation(s) for products.
  name: Swell Products API
  slug: swell-products-api
artifact_total: 12
collections:
- collection_type: open
  name: Swell Backend API
  slug: open-swell
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swell-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.swell.is
- group: start
  title: ''
  type: Portal
  url: https://developers.swell.is
- group: docs
  title: ''
  type: Documentation
  url: https://developers.swell.is
- group: start
  title: ''
  type: Signup
  url: https://www.swell.is/signup
- group: start
  title: ''
  type: Login
  url: https://admin.swell.store
- group: commercial
  title: ''
  type: Pricing
  url: https://www.swell.is/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.swell.is/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/swellstores
- group: other
  title: ''
  type: Storefronts
  url: https://www.swell.is/storefronts
- group: other
  title: ''
  type: Apps
  url: https://www.swell.is/apps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swell.is/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swell.is/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.swell.is
created: '2026-05-23'
description: Swell is a composable headless commerce platform that gives developers and brands API-first building blocks for storefronts, subscriptions, B2B, and multi-region commerce. It exposes a server-side Backend API for managing products, orders, customers, content, and operations, plus a client-side Frontend (Storefront) API and Swell.js / Node SDKs for building custom shopping experiences on any stack.
finops:
- name: Swell Finops
  service_category: API
  slug: swell-finops
graphqls:
- description: Client-side API and Swell.js SDK for building custom storefronts. Exposes products, categories, accounts, sessions, addresses, credit cards, carts, orders, payments, coupons, promotions, gift cards, s
  name: Swell GraphQL API
  slug: swell-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swell.png
layout: provider
modified: '2026-05-23'
name: Swell
nav: Providers
network: true
overview: 'Swell publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Products API. Tagged areas include Commerce, Headless Commerce, Composable Commerce, Ecommerce, and Storefront.


  Swell''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, and 9 more developer resources.'
plans:
- name: Swell Plans Pricing
  plan_count: 1
  slug: swell-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 2
  name: Swell Rate Limits
  slug: swell-rate-limits
score:
  band: thin
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 51.3
    developer_ergonomics: 34.8
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 44.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swell/refs/heads/main/screenshots/swell-2026-06-20T194802.png
security:
- kind: authentication
  name: Swell Authentication
  slug: swell-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Swell Domain Security
  slug: swell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swell
tags:
- Commerce
- Headless Commerce
- Composable Commerce
- Ecommerce
- Storefront
- Subscriptions
- B2B
- Products
- Orders
- Customers
website: https://www.swell.is
---
