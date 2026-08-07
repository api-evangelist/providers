---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Booqable Agentic Access
  operation_count: 60
  slug: booqable-agentic-access
  summary_line: 60 operations · 28 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Inventory availability, levels, and plannings.
  name: Booqable Availability API
  slug: booqable-availability-api
- description: Merchandising groups and store collections.
  name: Booqable Bundles & Collections API
  slug: booqable-bundles-collections-api
- description: People and companies that place orders.
  name: Booqable Customers API
  slug: booqable-customers-api
- description: Invoices, quotes, contracts, and payments.
  name: Booqable Documents API
  slug: booqable-documents-api
- description: Booking, starting, stopping, and transitioning orders and their lines.
  name: Booqable Order Fulfillment API
  slug: booqable-order-fulfillment-api
- description: Rental orders and their lifecycle.
  name: Booqable Orders API
  slug: booqable-orders-api
- description: Parent records grouping product variations.
  name: Booqable Product Groups API
  slug: booqable-product-groups-api
- description: Rentable and sellable catalog products.
  name: Booqable Products API
  slug: booqable-products-api
- description: Locations, tax rates, coupons, employees, and notes.
  name: Booqable Settings API
  slug: booqable-settings-api
- description: Individually identifiable units of trackable products.
  name: Booqable Stock Items API
  slug: booqable-stock-items-api
- description: Event subscriptions delivering HTTPS callbacks.
  name: Booqable Webhooks API
  slug: booqable-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: Booqable API (v4 Boomerang)
  slug: open-booqable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/booqable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/booqable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/booqable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/booqable-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/booqable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/booqable
- group: company
  title: ''
  type: Website
  url: https://booqable.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.booqable.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/booqable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/booqable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/booqable-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://booqable.com/blog/
created: '2026-07-03'
description: Booqable is equipment and inventory rental management software for rental businesses - it handles online bookings, product and stock-item inventory, orders, scheduling and availability, documents and invoicing, payments, and a customer-facing online store. Booqable exposes a documented REST API (v4, "Boomerang") that follows the JSON:API specification. Requests are directed to a company-specific host, https://{company}.booqable.com/api/4, and authenticated with an access token (Bearer) or a signed single-use request. A legacy v1 API remains documented. The API lets developers manage orders, products, product groups, customers, stock items, availability and plannings, documents, payments, and webhooks.
finops:
- name: Booqable Finops
  service_category: Business Applications
  slug: booqable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/booqable.png
layout: provider
modified: '2026-07-03'
name: Booqable
nav: Providers
network: true
overview: 'Booqable publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bundles & Collections API, Customers API, and 8 more. Tagged areas include Rental Management, Inventory, Equipment Rental, Bookings, and Orders.


  Booqable''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Booqable Plans Pricing
  plan_count: 4
  slug: booqable-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 3
  name: Booqable Rate Limits
  slug: booqable-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/booqable/refs/heads/main/screenshots/booqable-2026-07-25T203619.png
security:
- kind: authentication
  name: Booqable Authentication
  slug: booqable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Booqable Domain Security
  slug: booqable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Booqable Trust Center
  slug: booqable-trust-center
  summary_line: SOC 2, ISO 27001
slug: booqable
tags:
- Rental Management
- Inventory
- Equipment Rental
- Bookings
- Orders
- E-commerce
- JSON:API
website: https://booqable.com
---
