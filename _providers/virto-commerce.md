---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 283
  human_in_the_loop: 9
  name: Virto Commerce Agentic Access
  operation_count: 426
  slug: virto-commerce-agentic-access
  summary_line: 426 operations · 283 acting · 9 human-in-the-loop
api_count: 10
apis:
- description: Easily manage your products, categories, variations, and properties
  name: Virto Commerce Catalog API
  slug: virto-commerce-catalog-api
- description: Managing customers contacts and organizations
  name: Virto Commerce Companies and Contacts API
  slug: virto-commerce-companies-and-contacts-api
- description: Simplify inventory management functionality
  name: Virto Commerce Inventory API
  slug: virto-commerce-inventory-api
- description: Marketing system with dynamic contents and promotions management
  name: Virto Commerce Marketing API
  slug: virto-commerce-marketing-api
- description: Document based flexible order management system.
  name: Virto Commerce Order Management API
  slug: virto-commerce-order-management-api
- description: Robust pricing management functionality based on price list and dynamic evaluation
  name: Virto Commerce Pricing API
  slug: virto-commerce-pricing-api
- description: 'Quoter enables business users to execute quote requests online. Once initiated, an online conversation takes place with internal users who interact with the business user''s request. The internal user '
  name: Virto Commerce Quotes API
  slug: virto-commerce-quotes-api
- description: Shopping cart / checkout functionality
  name: Virto Commerce Shopping Cart API
  slug: virto-commerce-shopping-cart-api
- description: Multi store management with individual store settings
  name: Virto Commerce Store API
  slug: virto-commerce-store-api
- description: B2B Innovation Platform
  name: Virto Commerce VirtoCommerce Platform API
  slug: virto-commerce-virtocommerce-platform-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virto-commerce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virto-commerce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virto-commerce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virto-commerce-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://virtocommerce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtocommerce.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/VirtoCommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virto-commerce/
- group: company
  title: ''
  type: Blog
  url: https://virtocommerce.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://virtocommerce.com/virto-commerce-cloud
- group: other
  title: ''
  type: X
  url: https://x.com/VirtoCommerce
- group: commercial
  title: ''
  type: Plans
  url: plans/virto-commerce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virto-commerce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/virto-commerce-finops.yml
- group: docs
  title: ''
  type: SwaggerUI
  url: https://virtostart-demo-admin.govirto.com/docs/index.html
- group: operate
  title: ''
  type: Support
  url: https://help.virtocommerce.com/support/home
- group: operate
  title: ''
  type: Community
  url: https://www.virtocommerce.org/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.virtocommerce.org/c/news-digest/14
created: '2026-06-13'
description: Virto Commerce is an open-source, API-first B2B e-commerce platform built on .NET Core. It provides REST and GraphQL APIs for catalog management, pricing, inventory, order management, customer organizations, marketing, payments, shipping, subscriptions, and complex B2B purchasing workflows including quotes, contracts, and approval routing. The modular architecture offers 100+ independently deployable modules covering the full commerce stack for enterprise deployments.
finops:
- name: Virto Commerce Finops
  service_category: ''
  slug: virto-commerce-finops
graphqls:
- description: Virto Commerce exposes a unified GraphQL API (the "Experience API" or xAPI) as the primary interface for headless storefronts. Built on top of the GraphQL.NET library, the xAPI aggregates catalog, car
  name: Virto Commerce GraphQL API
  slug: virto-commerce-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/virto-commerce.png
jsonld:
- class_count: 15
  name: Virto Commerce Context
  property_count: 0
  slug: virto-commerce-context
layout: provider
modified: '2026-06-13'
name: Virto Commerce
nav: Providers
network: true
overview: 'Virto Commerce publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Companies and Contacts API, Inventory API, and 7 more. Tagged areas include B2B E-Commerce, Catalog Management, Order Management, Pricing, and Inventory.


  The Virto Commerce catalog on APIs.io includes 1 JSON-LD context.


  Virto Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, support, changelog, and 12 more developer resources.'
plans:
- name: Virto Commerce Plans Pricing
  plan_count: 3
  slug: virto-commerce-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Virto Commerce Rate Limits
  slug: virto-commerce-rate-limits
scopes:
- name: Virto Commerce Scopes
  scope_count: 72
  slug: virto-commerce-scopes
  summary_line: 72 scopes · password/clientCredentials
score:
  band: thin
  composite: 41.8
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.1
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/screenshots/virto-commerce-2026-06-20T201036.png
security:
- kind: authentication
  name: Virto Commerce Authentication
  slug: virto-commerce-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Virto Commerce Domain Security
  slug: virto-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virto-commerce
tags:
- B2B E-Commerce
- Catalog Management
- Order Management
- Pricing
- Inventory
- Shopping Cart
- Customer Management
- Marketing
- Payments
- Shipping
- Subscriptions
- Headless Commerce
- Open Source
- .NET
website: https://virtocommerce.com/
---
