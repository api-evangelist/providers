---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Finditparts Agentic Access
  operation_count: 38
  slug: finditparts-agentic-access
  summary_line: 38 operations · 23 acting
api_count: 1
apis:
- description: Shipping and billing address book for a user-specific session.
  name: FinditParts Addresses API
  slug: finditparts-addresses-api
- description: 'Draft-order (cart) lifecycle: line items, addresses, shipping method, coupon, PO number and checkout.'
  name: FinditParts Carts API
  slug: finditparts-carts-api
- description: Order listing, search and detail for a user-specific session.
  name: FinditParts Orders API
  slug: finditparts-orders-api
- description: Partner API-key surface for white-label shipping quotes and order placement.
  name: FinditParts Partners API
  slug: finditparts-partners-api
- description: Part search, part-number lookup and product/variant detail across the FinditParts catalog.
  name: FinditParts Products API
  slug: finditparts-products-api
- description: Hosted USER_SETUP and NEW_ORDER sessions returned as a finditparts.com redirect_url for iframe embedding or redirect.
  name: FinditParts Reseller Customer Sessions API
  slug: finditparts-reseller-customer-sessions-api
- description: Sub-users created on a reseller master account and addressed by customer_reference.
  name: FinditParts Reseller Customers API
  slug: finditparts-reseller-customers-api
- description: User-specific JWT session creation, refresh, inspection and destruction.
  name: FinditParts Sessions API
  slug: finditparts-sessions-api
- description: Shipping method quoting and estimated cost for a proposed set of line items and an address.
  name: FinditParts Shipping API
  slug: finditparts-shipping-api
- description: Direct FinditParts user creation for API-key clients.
  name: FinditParts Users API
  slug: finditparts-users-api
- description: Variant-level price, quantity, cutoff and core lookups.
  name: FinditParts Variants API
  slug: finditparts-variants-api
artifact_total: 56
collections:
- collection_type: open
  name: FinditParts Reseller API
  slug: open-finditparts-reseller-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/finditparts-reseller-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.finditparts.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.finditparts.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.finditparts.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.finditparts.com/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/12847304/TVReeWcY
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinditParts
- group: company
  title: ''
  type: Blog
  url: https://www.finditparts.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.finditparts.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.finditparts.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.finditparts.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.finditparts.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.finditparts.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.finditparts.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/finditparts-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finditparts-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/finditparts-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finditparts-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finditparts-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finditparts-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finditparts-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finditparts-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finditparts-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/finditparts-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/finditparts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finditparts-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finditparts-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finditparts-mcp.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
created: '2026-08-12'
description: FinditParts is a Los Angeles-based online marketplace for heavy-duty truck, trailer, fleet and industrial replacement parts, selling OE, aftermarket and remanufactured components to owner-operators, fleet parts managers and mechanics nationwide. Its developer surface is the FinditParts Reseller API — a partner and reseller integration that lets shop-management platforms, e-commerce sites and fleet applications search the parts catalog with account-specific pricing, look parts up by part number and cross-reference, quote real-time shipping, create and link FinditParts customer accounts through hosted embeddable sessions, build carts and place orders on a linked customer's behalf, and read back order status and shipments.
examples:
- key_count: 2
  name: Finditparts Add Cart Line Item 200
  slug: finditparts-add-cart-line-item-200
- key_count: 2
  name: Finditparts Cancel Reseller Customer Session 200
  slug: finditparts-cancel-reseller-customer-session-200
- key_count: 2
  name: Finditparts Change Cart Line Items 200
  slug: finditparts-change-cart-line-items-200
- key_count: 2
  name: Finditparts Complete Cart With Corporate Billing 200
  slug: finditparts-complete-cart-with-corporate-billing-200
- key_count: 2
  name: Finditparts Complete Cart With Credit Card 200
  slug: finditparts-complete-cart-with-credit-card-200
- key_count: 2
  name: Finditparts Create Address 200
  slug: finditparts-create-address-200
- key_count: 2
  name: Finditparts Create Cart 200
  slug: finditparts-create-cart-200
- key_count: 2
  name: Finditparts Create Reseller Customer 200
  slug: finditparts-create-reseller-customer-200
- key_count: 2
  name: Finditparts Create Reseller Customer Session 200
  slug: finditparts-create-reseller-customer-session-200
- key_count: 3
  name: Finditparts Create Session 200
  slug: finditparts-create-session-200
- key_count: 3
  name: Finditparts Create User 200
  slug: finditparts-create-user-200
- key_count: 2
  name: Finditparts Delete Address 200
  slug: finditparts-delete-address-200
- key_count: 2
  name: Finditparts Destroy Sessions 200
  slug: finditparts-destroy-sessions-200
- key_count: 2
  name: Finditparts Get Cart 200
  slug: finditparts-get-cart-200
- key_count: 2
  name: Finditparts Get Cart Shipping Methods 200
  slug: finditparts-get-cart-shipping-methods-200
- key_count: 2
  name: Finditparts Get Current Session 200
  slug: finditparts-get-current-session-200
- key_count: 2
  name: Finditparts Get Order 200
  slug: finditparts-get-order-200
- key_count: 2
  name: Finditparts Get Product 200
  slug: finditparts-get-product-200
- key_count: 2
  name: Finditparts Get Products Multi 200
  slug: finditparts-get-products-multi-200
- key_count: 2
  name: Finditparts Get Reseller Customer Session 200
  slug: finditparts-get-reseller-customer-session-200
- key_count: 2
  name: Finditparts List Addresses 200
  slug: finditparts-list-addresses-200
- key_count: 3
  name: Finditparts List Orders 200
  slug: finditparts-list-orders-200
- key_count: 3
  name: Finditparts List Reseller Customers 200
  slug: finditparts-list-reseller-customers-200
- key_count: 3
  name: Finditparts Lookup Product By Part Number 200
  slug: finditparts-lookup-product-by-part-number-200
- key_count: 2
  name: Finditparts Partners Place Order 200
  slug: finditparts-partners-place-order-200
- key_count: 2
  name: Finditparts Partners Shipping Methods 200
  slug: finditparts-partners-shipping-methods-200
- key_count: 4
  name: Finditparts Product Search 200
  slug: finditparts-product-search-200
- key_count: 3
  name: Finditparts Refresh Session 200
  slug: finditparts-refresh-session-200
- key_count: 3
  name: Finditparts Search Orders 200
  slug: finditparts-search-orders-200
- key_count: 2
  name: Finditparts Select Cart Shipping Method 200
  slug: finditparts-select-cart-shipping-method-200
- key_count: 2
  name: Finditparts Set Cart Billing Address 200
  slug: finditparts-set-cart-billing-address-200
- key_count: 2
  name: Finditparts Set Cart Coupon 200
  slug: finditparts-set-cart-coupon-200
- key_count: 2
  name: Finditparts Set Cart Po Number 200
  slug: finditparts-set-cart-po-number-200
- key_count: 2
  name: Finditparts Set Cart Shipping Address 200
  slug: finditparts-set-cart-shipping-address-200
- key_count: 2
  name: Finditparts Set Default Address 200
  slug: finditparts-set-default-address-200
- key_count: 2
  name: Finditparts Shipping Methods 200
  slug: finditparts-shipping-methods-200
- key_count: 2
  name: Finditparts Update Address 200
  slug: finditparts-update-address-200
- key_count: 2
  name: Finditparts Variant Lookup 200
  slug: finditparts-variant-lookup-200
image: https://d2jocyn8o0ggnq.cloudfront.net/logos/finditparts.png
layout: provider
mcp_servers:
- description: ''
  name: FinditParts MCP Server
  slug: finditparts-mcp-server
modified: '2026-08-12'
name: FinditParts
nav: Providers
network: true
overview: 'FinditParts publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Carts API, Orders API, and 8 more. Tagged areas include Company, E-Commerce, Marketplace, Automotive, and Parts.


  FinditParts'' developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, code examples, and 23 more developer resources.'
plans:
- name: Finditparts Plans Pricing
  plan_count: 0
  slug: finditparts-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Finditparts Rate Limits
  slug: finditparts-rate-limits
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 61.0
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finditparts/refs/heads/main/screenshots/finditparts-2026-08-17T080926.png
security:
- kind: authentication
  name: Finditparts Authentication
  slug: finditparts-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Finditparts Domain Security
  slug: finditparts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finditparts
tags:
- Company
- E-Commerce
- Marketplace
- Automotive
- Parts
- Heavy Duty Trucking
- Fleet
- Logistics
- Commerce
- Catalog
- Order
- Shipping
website: https://www.finditparts.com/
---
