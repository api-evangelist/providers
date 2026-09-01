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
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-09-01'
api_count: 2
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
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vinculum Advance Shipping Notice API
  slug: open-vinculum-advance-shipping-notice-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Authentication Process API
  slug: open-vinculum-authentication-process-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Common API
  slug: open-vinculum-common-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Courier Allocation Process API
  slug: open-vinculum-courier-allocation-process-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Inbounds API
  slug: open-vinculum-inbounds-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Listing Managment API
  slug: open-vinculum-listing-managment-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Manifest API
  slug: open-vinculum-manifest-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Order Managment API
  slug: open-vinculum-order-managment-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Order Returns API
  slug: open-vinculum-order-returns-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Orders API
  slug: open-vinculum-orders-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Products API
  slug: open-vinculum-products-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Purchase Orders API
  slug: open-vinculum-purchase-orders-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Putaway API
  slug: open-vinculum-putaway-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Return to Vendor API
  slug: open-vinculum-return-to-vendor-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Stock API
  slug: open-vinculum-stock-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Transfers API
  slug: open-vinculum-transfers-api
- collection_type: open
  name: Vinculum Advance Shipping Notice Vendors API
  slug: open-vinculum-vendors-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vinculum-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vinculum-eretail-overlay.yaml
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
  name: Vinculum MCP Server
  slug: vinculum-mcp-server
modified: '2026-07-21'
name: Vinculum
nav: Providers
network: true
overview: 'Vinculum publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Advance Shipping Notice API, Authentication Process API, Common API, and 14 more. Tagged areas include Company, E-Commerce, Omnichannel, Order Management, and Warehouse Management.


  Vinculum''s developer surface includes documentation, engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 3
  name: Vinculum Rate Limits
  slug: vinculum-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 38.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 28.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- E-Commerce
- Omnichannel
- Order Management
- Warehouse Management
- Inventory
- Retail
- Marketplaces
website: http://www.vinculumgroup.com
---
