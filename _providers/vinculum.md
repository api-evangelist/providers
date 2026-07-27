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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-27'
api_count: 17
apis:
- description: API to retrieve or manipulate ASN related information.
  name: Vinculum Advance Shipping Notice API
  slug: vinculum-advance-shipping-notice-api
- description: API to retrieve or manipulate Order related information.
  name: Vinculum Authentication Process API
  slug: vinculum-authentication-process-api
- description: API to facilitate Common Operations.
  name: Vinculum Common API
  slug: vinculum-common-api
- description: API to retrieve or manipulate Order related information.
  name: Vinculum Courier Allocation Process API
  slug: vinculum-courier-allocation-process-api
- description: API to retrieve or manipulate Inbound related information.
  name: Vinculum Inbounds API
  slug: vinculum-inbounds-api
- description: API to retrieve or manipulate Order related information.
  name: Vinculum Listing Managment API
  slug: vinculum-listing-managment-api
- description: API to create Manifest
  name: Vinculum Manifest API
  slug: vinculum-manifest-api
- description: API to retrieve or manipulate Order related information.
  name: Vinculum Order Managment API
  slug: vinculum-order-managment-api
- description: API to retrieve or create return for an order.
  name: Vinculum Order Returns API
  slug: vinculum-order-returns-api
- description: API to retrieve or manipulate Order related information.
  name: Vinculum Orders API
  slug: vinculum-orders-api
- description: API to retrieve or manipulate SKU related information.
  name: Vinculum Products API
  slug: vinculum-products-api
- description: API to retrieve or manipulate Purchase Order related information.
  name: Vinculum Purchase Orders API
  slug: vinculum-purchase-orders-api
- description: API to create putaway
  name: Vinculum Putaway API
  slug: vinculum-putaway-api
- description: API to retrieve or manipulate Return to Vendor related information.
  name: Vinculum Return to Vendor API
  slug: vinculum-return-to-vendor-api
- description: API to retrieve or manipulate Stock related information.
  name: Vinculum Stock API
  slug: vinculum-stock-api
- description: API to create Stock Transfer Order in Eretail
  name: Vinculum Transfers API
  slug: vinculum-transfers-api
- description: API to retrieve or manipulate Vendor related information.
  name: Vinculum Vendors API
  slug: vinculum-vendors-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: http://www.vinculumgroup.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vineretail.com
- group: company
  title: ''
  type: Blog
  url: https://www.vinculumgroup.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vinculumgroup.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.vinculumgroup.com/contact-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/vinculum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vinculum-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vinculum-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vinculum-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vinculum-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vinculum-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vinculum-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vinculum-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vinculum-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vinculum-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vinculum-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vinculum is an AI-driven SaaS company for omnichannel retail and ecommerce. Its Vin eRetail platform unifies order management (OMS), warehouse management (WMS), product information management (PIM), and endless-aisle omnichannel retail across 150+ sales channels and marketplaces for 1,000+ brands, processing 20M+ orders monthly. The Vin eRetail REST API exposes orders, returns, products/SKUs, inventory/stock, vendors, purchase orders, inbounds, advance shipping notices, transfers, and fulfillment operations, alongside a SellerPanel V3 marketplace API for listing, order, and courier-allocation flows. Originally surfaced as an Accel portfolio company, this profile has been enriched from Vinculum's published Swagger.
image: https://erp.vineretail.com/swagger/Vinculum-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: vinculum-mcp.yml
  slug: vinculum-mcpyml
modified: '2026-07-21'
name: Vinculum
nav: Providers
network: true
overview: 'Vinculum publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Advance Shipping Notice API, Authentication Process API, Common API, and 14 more. Tagged areas include Company, Ecommerce, Omnichannel, Order Management, and Warehouse Management.


  Vinculum''s developer surface includes documentation, engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 67
rate_limits:
- limit_count: 0
  name: Vinculum Rate Limits
  slug: vinculum-rate-limits
score:
  band: emerging
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 37.7
    developer_ergonomics: 41.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Vinculum Authentication
  slug: vinculum-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Vinculum Domain Security
  slug: vinculum-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: vinculum
tags:
- Company
- Ecommerce
- Omnichannel
- Order Management
- Warehouse Management
- Inventory
- Retail
- Marketplaces
website: http://www.vinculumgroup.com
---
