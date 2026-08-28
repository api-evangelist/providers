---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Snipcart Agentic Access
  operation_count: 30
  slug: snipcart-agentic-access
  summary_line: 30 operations · 12 acting
api_count: 9
apis:
- description: View and track abandoned shopping carts
  name: Snipcart AbandonedCarts API
  slug: snipcart-abandonedcarts-api
- description: View and manage customer data
  name: Snipcart Customers API
  slug: snipcart-customers-api
- description: Manage discount codes and promotions
  name: Snipcart Discounts API
  slug: snipcart-discounts-api
- description: Manage allowed domains for your store
  name: Snipcart Domains API
  slug: snipcart-domains-api
- description: Manage order notifications and emails
  name: Snipcart Notifications API
  slug: snipcart-notifications-api
- description: Manage orders and order lifecycle
  name: Snipcart Orders API
  slug: snipcart-orders-api
- description: Manage product catalog and inventory
  name: Snipcart Products API
  slug: snipcart-products-api
- description: Manage order refunds
  name: Snipcart Refunds API
  slug: snipcart-refunds-api
- description: Retrieve user session information
  name: Snipcart UserSessions API
  slug: snipcart-usersessions-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snipcart REST AbandonedCarts API
  slug: open-snipcart-abandonedcarts-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Customers API
  slug: open-snipcart-customers-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Discounts API
  slug: open-snipcart-discounts-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Domains API
  slug: open-snipcart-domains-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Notifications API
  slug: open-snipcart-notifications-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Orders API
  slug: open-snipcart-orders-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Products API
  slug: open-snipcart-products-api
- collection_type: open
  name: Snipcart REST AbandonedCarts Refunds API
  slug: open-snipcart-refunds-api
- collection_type: open
  name: Snipcart REST AbandonedCarts UserSessions API
  slug: open-snipcart-usersessions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snipcart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snipcart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snipcart-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://snipcart.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snipcart.com/v3/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snipcart
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/snipcart
- group: company
  title: ''
  type: Blog
  url: https://snipcart.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://snipcart.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snipcart.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/snipcart
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.snipcart.com/v3/release-notes
- group: design
  title: ''
  type: Webhooks
  url: https://docs.snipcart.com/v3/webhooks/introduction
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/snipcart/refs/heads/main/plans/snipcart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/snipcart/refs/heads/main/rate-limits/snipcart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/snipcart/refs/heads/main/finops/snipcart-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://snipcart.com/blog/rss
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/snipcart/refs/heads/main/vocabulary/snipcart-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/snipcart/refs/heads/main/json-ld/snipcart-context.jsonld
created: '2026-06-12'
description: Snipcart is a developer-first shopping cart platform that enables merchants to add fully functional e-commerce to any website by embedding a JavaScript snippet. It provides a REST API accessible at https://app.snipcart.com/api for managing orders, customers, products, discounts, notifications, abandoned carts, and custom shipping methods. Authentication uses HTTP Basic Auth with a secret API key generated from the merchant dashboard, and the platform supports webhooks for real-time event notifications on orders, subscriptions, shipping, and taxes. Snipcart is stack-agnostic and integrates with static site generators, headless CMSs, and modern JavaScript frameworks.
finops:
- name: Snipcart Finops
  service_category: ''
  slug: snipcart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snipcart.png
jsonld:
- class_count: 47
  name: Snipcart Context
  property_count: 6
  slug: snipcart-context
layout: provider
modified: '2026-06-12'
name: Snipcart
nav: Providers
network: true
overview: 'Snipcart publishes 9 APIs on the [APIs.io](https://apis.io/) network, including AbandonedCarts API, Customers API, Discounts API, and 6 more. Tagged areas include E-Commerce, Shopping Cart, Order, Product, and Payments.


  The Snipcart catalog on APIs.io includes 1 JSON-LD context.


  Snipcart''s developer surface includes authentication, documentation, engineering blog, pricing, release notes, and 14 more developer resources.'
plans:
- name: Snipcart Plans Pricing
  plan_count: 3
  slug: snipcart-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Snipcart Rate Limits
  slug: snipcart-rate-limits
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 63.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 63.2
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snipcart/refs/heads/main/screenshots/snipcart-2026-06-20T194105.png
security:
- kind: authentication
  name: Snipcart Authentication
  slug: snipcart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Snipcart Domain Security
  slug: snipcart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snipcart
tags:
- E-Commerce
- Shopping Cart
- Order
- Product
- Payments
- Webhook
- Headless Commerce
- JAMstack
website: https://snipcart.com
---
