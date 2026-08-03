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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
api_count: 19
apis:
- description: The Customers API from Fudo — 2 operation(s) for customers.
  name: Fudo Customers API
  slug: fudo-customers-api
- description: The Discounts API from Fudo — 2 operation(s) for discounts.
  name: Fudo Discounts API
  slug: fudo-discounts-api
- description: The Expense Categories API from Fudo — 2 operation(s) for expense categories.
  name: Fudo Expense Categories API
  slug: fudo-expense-categories-api
- description: The Expenses API from Fudo — 2 operation(s) for expenses.
  name: Fudo Expenses API
  slug: fudo-expenses-api
- description: The Ingredients API from Fudo — 2 operation(s) for ingredients.
  name: Fudo Ingredients API
  slug: fudo-ingredients-api
- description: The Items API from Fudo — 2 operation(s) for items.
  name: Fudo Items API
  slug: fudo-items-api
- description: The Kitchens API from Fudo — 2 operation(s) for kitchens.
  name: Fudo Kitchens API
  slug: fudo-kitchens-api
- description: The Payment Methods API from Fudo — 2 operation(s) for payment methods.
  name: Fudo Payment Methods API
  slug: fudo-payment-methods-api
- description: The Payments API from Fudo — 2 operation(s) for payments.
  name: Fudo Payments API
  slug: fudo-payments-api
- description: The Product Categories API from Fudo — 2 operation(s) for product categories.
  name: Fudo Product Categories API
  slug: fudo-product-categories-api
- description: The Product Modifiers API from Fudo — 2 operation(s) for product modifiers.
  name: Fudo Product Modifiers API
  slug: fudo-product-modifiers-api
- description: The Products API from Fudo — 2 operation(s) for products.
  name: Fudo Products API
  slug: fudo-products-api
- description: The Providers API from Fudo — 2 operation(s) for providers.
  name: Fudo Providers API
  slug: fudo-providers-api
- description: The Roles API from Fudo — 2 operation(s) for roles.
  name: Fudo Roles API
  slug: fudo-roles-api
- description: The Rooms API from Fudo — 2 operation(s) for rooms.
  name: Fudo Rooms API
  slug: fudo-rooms-api
- description: The Sales API from Fudo — 2 operation(s) for sales.
  name: Fudo Sales API
  slug: fudo-sales-api
- description: The Subitems API from Fudo — 1 operation(s) for subitems.
  name: Fudo Subitems API
  slug: fudo-subitems-api
- description: The Tables API from Fudo — 2 operation(s) for tables.
  name: Fudo Tables API
  slug: fudo-tables-api
- description: The Users API from Fudo — 2 operation(s) for users.
  name: Fudo Users API
  slug: fudo-users-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fudo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fudo-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fudo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fudo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fudo-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fudo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fudo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fudo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fudo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fudo-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.fu.do/api/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fu.do/api/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.fu.do/api/
- group: operate
  title: ''
  type: Support
  url: https://soporte.fu.do
- group: company
  title: ''
  type: Blog
  url: https://blog.fu.do/
- group: commercial
  title: ''
  type: Pricing
  url: https://fu.do/es/precios/
- group: start
  title: ''
  type: SignUp
  url: https://fu.do/es/crear-cuenta/
- group: start
  title: ''
  type: Login
  url: https://app-v2.fu.do/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fu.do/condiciones-de-servicio/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fu.do/es/politicas-de-privacidad/
- group: company
  title: ''
  type: Website
  url: https://fu.do
created: '2026-07-17'
description: Fudo is a cloud-based point-of-sale and restaurant management platform used by more than 25,000 restaurants, bars, and cafes across Latin America. The product covers on-premise and online sales, QR menus, kitchen display, inventory and purchasing, expenses, table and room management, staff roles, and delivery-app integrations (Uber Eats, Rappi, PedidosYa). Fudo publishes a general-purpose public REST API (OpenAPI 3.1, JSON:API style) that lets Pro-plan accounts read and write sales, payments, products, customers, expenses, ingredients, and system configuration for reporting, BI, ERP, and custom integrations. This profile was surfaced as an a16z portfolio company and enriched by the API Evangelist pipeline from Fudo's own developer surface.
image: https://dev.fu.do/assets/images/fudo.svg
layout: provider
mcp_servers:
- description: ''
  name: fudo-mcp.yml
  slug: fudo-mcpyml
modified: '2026-07-19'
name: Fudo
nav: Providers
network: true
overview: 'Fudo publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Discounts API, Expense Categories API, and 16 more. Tagged areas include Company, Restaurant, Point of Sale, Hospitality, and Food and Beverage.


  Fudo''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 14 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.2
    developer_ergonomics: 43.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fudo/refs/heads/main/screenshots/fudo-2026-07-25T215250.png
security:
- kind: authentication
  name: Fudo Authentication
  slug: fudo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fudo Domain Security
  slug: fudo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fudo
tags:
- Company
- Restaurant
- Point of Sale
- Hospitality
- Food and Beverage
- Payments
- Inventory
- Latin America
- SaaS
website: https://fu.do
---
