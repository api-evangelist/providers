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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 93
  human_in_the_loop: 3
  name: Deliverart Agentic Access
  operation_count: 130
  slug: deliverart-agentic-access
  summary_line: 130 operations · 93 acting · 3 human-in-the-loop
api_count: 16
apis:
- description: The Addresses API from Deliverart — 3 operation(s) for addresses.
  name: Deliverart Addresses API
  slug: deliverart-addresses-api
- description: The Companies API from Deliverart — 2 operation(s) for companies.
  name: Deliverart Companies API
  slug: deliverart-companies-api
- description: The Customer addresses API from Deliverart — 5 operation(s) for customer addresses.
  name: Deliverart Customer addresses API
  slug: deliverart-customer-addresses-api
- description: The Customer business profiles API from Deliverart — 5 operation(s) for customer business profiles.
  name: Deliverart Customer business profiles API
  slug: deliverart-customer-business-profiles-api
- description: The Customers API from Deliverart — 5 operation(s) for customers.
  name: Deliverart Customers API
  slug: deliverart-customers-api
- description: The Deliveries API from Deliverart — 6 operation(s) for deliveries.
  name: Deliverart Deliveries API
  slug: deliverart-deliveries-api
- description: The Delivery fee API from Deliverart — 3 operation(s) for delivery fee.
  name: Deliverart Delivery fee API
  slug: deliverart-delivery-fee-api
- description: The Me API from Deliverart — 16 operation(s) for me.
  name: Deliverart Me API
  slug: deliverart-me-api
- description: The Menu API from Deliverart — 35 operation(s) for menu.
  name: Deliverart Menu API
  slug: deliverart-menu-api
- description: The Orders API from Deliverart — 17 operation(s) for orders.
  name: Deliverart Orders API
  slug: deliverart-orders-api
- description: The Password reset API from Deliverart — 3 operation(s) for password reset.
  name: Deliverart Password reset API
  slug: deliverart-password-reset-api
- description: The Points of sale API from Deliverart — 10 operation(s) for points of sale.
  name: Deliverart Points of sale API
  slug: deliverart-points-of-sale-api
- description: The Registration API from Deliverart — 3 operation(s) for registration.
  name: Deliverart Registration API
  slug: deliverart-registration-api
- description: The Reservation API from Deliverart — 10 operation(s) for reservation.
  name: Deliverart Reservation API
  slug: deliverart-reservation-api
- description: The Take away API from Deliverart — 2 operation(s) for take away.
  name: Deliverart Take away API
  slug: deliverart-take-away-api
- description: The Workshifts API from Deliverart — 5 operation(s) for workshifts.
  name: Deliverart Workshifts API
  slug: deliverart-workshifts-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deliverart-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deliverart-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deliverart-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deliverart-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deliverart-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deliverart-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/deliverart-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/deliverart-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deliverart-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deliverart-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/deliverart-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deliverart-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/deliverart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/deliverart-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deliverart-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidoc.deliverart.it/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.deliverart.it/
- group: docs
  title: ''
  type: APIReference
  url: https://apidoc.deliverart.it/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidoc.deliverart.it/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deliverart.it/prezzi/
- group: start
  title: ''
  type: SignUp
  url: https://www.deliverart.it/richiedi-la-demo/
- group: operate
  title: ''
  type: Support
  url: https://www.deliverart.it/chi-siamo/contatti/
- group: company
  title: ''
  type: Blog
  url: https://www.deliverart.it/risorse/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/8283529
- group: company
  title: ''
  type: Website
  url: https://www.deliverart.it/
created: '2026-07-17'
description: Deliverart is food-delivery management software for restaurants and delivery businesses, founded in Italy and backed by Techstars. It centralizes orders from Just Eat, Glovo, Deliveroo, a restaurant's own website and phone into a single interface; synchronizes menus across sales channels; and manages riders, delivery routing, take-away, the Delivery Order Display System (DODS) and live tracking. The public Deliverart API is an RPC-style HTTPS API (GET for reads, POST for writes) covering orders, menu, customers, points of sale, workshifts, deliveries and reservations, with API key and OAuth2 authentication. Deliverart also ships a modular first-party JavaScript SDK suite on npm.
image: https://www.deliverart.it/wp-content/uploads/2023/02/LinkedIn-Cover.jpg
layout: provider
mcp_servers:
- description: ''
  name: deliverart-mcp.yml
  slug: deliverart-mcpyml
modified: '2026-07-18'
name: Deliverart
nav: Providers
network: true
overview: 'Deliverart publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Companies API, Customer addresses API, and 13 more. Tagged areas include Company, Food Delivery, Restaurants, Order Management, and Logistics.


  Deliverart''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, signup flow, and 19 more developer resources.'
random_paper: 3
scopes:
- name: Deliverart Scopes
  scope_count: 44
  slug: deliverart-scopes
  summary_line: 44 scopes · password
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.0
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 48.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Deliverart Authentication
  slug: deliverart-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Deliverart Domain Security
  slug: deliverart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deliverart
tags:
- Company
- Food Delivery
- Restaurants
- Order Management
- Logistics
- Delivery
- Menu Management
- Point of Sale
website: https://www.deliverart.it/
---
