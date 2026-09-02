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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Commercelayer Agentic Access
  operation_count: 55
  slug: commercelayer-agentic-access
  summary_line: 55 operations · 31 acting
api_count: 1
apis:
- description: Billing and shipping addresses.
  name: Commerce Layer Addresses API
  slug: commercelayer-addresses-api
- description: Customer accounts.
  name: Commerce Layer Customers API
  slug: commercelayer-customers-api
- description: Line items belonging to an order.
  name: Commerce Layer Line Items API
  slug: commercelayer-line-items-api
- description: Markets binding price list, inventory model, and merchant.
  name: Commerce Layer Markets API
  slug: commercelayer-markets-api
- description: Shopping carts and orders and their checkout lifecycle.
  name: Commerce Layer Orders API
  slug: commercelayer-orders-api
- description: Payment methods available for orders.
  name: Commerce Layer Payment Methods API
  slug: commercelayer-payment-methods-api
- description: Prices belonging to price lists, associated with SKUs.
  name: Commerce Layer Prices API
  slug: commercelayer-prices-api
- description: Discounts, free shipping, free gifts, and other promotions.
  name: Commerce Layer Promotions API
  slug: commercelayer-promotions-api
- description: Order shipments and fulfillment.
  name: Commerce Layer Shipments API
  slug: commercelayer-shipments-api
- description: Stock keeping units describing the product variations being sold.
  name: Commerce Layer SKUs API
  slug: commercelayer-skus-api
- description: Stock quantities for a SKU at a given stock location.
  name: Commerce Layer Stock Items API
  slug: commercelayer-stock-items-api
- description: Event subscriptions delivering signed callbacks.
  name: Commerce Layer Webhooks API
  slug: commercelayer-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Commerce Layer Core Addresses API
  slug: open-commercelayer-addresses-api
- collection_type: open
  name: Commerce Layer Core Addresses Customers API
  slug: open-commercelayer-customers-api
- collection_type: open
  name: Commerce Layer Core Addresses Line Items API
  slug: open-commercelayer-line-items-api
- collection_type: open
  name: Commerce Layer Core Addresses Markets API
  slug: open-commercelayer-markets-api
- collection_type: open
  name: Commerce Layer Core Addresses Orders API
  slug: open-commercelayer-orders-api
- collection_type: open
  name: Commerce Layer Core Addresses Payment Methods API
  slug: open-commercelayer-payment-methods-api
- collection_type: open
  name: Commerce Layer Core Addresses Prices API
  slug: open-commercelayer-prices-api
- collection_type: open
  name: Commerce Layer Core Addresses Promotions API
  slug: open-commercelayer-promotions-api
- collection_type: open
  name: Commerce Layer Core Addresses Shipments API
  slug: open-commercelayer-shipments-api
- collection_type: open
  name: Commerce Layer Core Addresses SKUs API
  slug: open-commercelayer-skus-api
- collection_type: open
  name: Commerce Layer Core Addresses Stock Items API
  slug: open-commercelayer-stock-items-api
- collection_type: open
  name: Commerce Layer Core Addresses Webhooks API
  slug: open-commercelayer-webhooks-api
- collection_type: open
  name: Commerce Layer Core API
  slug: open-commercelayer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commercelayer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/commercelayer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commercelayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commercelayer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commercelayer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commerce-layer
- group: company
  title: ''
  type: Website
  url: https://commercelayer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.commercelayer.io
- group: commercial
  title: ''
  type: Plans
  url: plans/commercelayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/commercelayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/commercelayer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://commercelayer.io/blog
created: '2026-06-21'
description: Commerce Layer is a headless, composable commerce platform that exposes a JSON:API-compliant REST API for building omnichannel storefronts and order management. The Core API serves SKUs, prices, stock, orders, line items, customers, addresses, shipments, payment methods, markets, and promotions, with OAuth2 authentication, market-scoped access tokens, and real-time webhooks.
finops:
- name: Commercelayer Finops
  service_category: Commerce Platform
  slug: commercelayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commercelayer.png
layout: provider
modified: '2026-06-21'
name: Commerce Layer
nav: Providers
network: true
overview: 'Commerce Layer publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Customers API, Line Items API, and 9 more. Tagged areas include Commerce, Headless, Composable, E-Commerce, and JSON:API.


  Commerce Layer''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Commercelayer Plans Pricing
  plan_count: 3
  slug: commercelayer-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Commercelayer Rate Limits
  slug: commercelayer-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commercelayer/refs/heads/main/screenshots/commercelayer-2026-07-25T210126.png
security:
- kind: authentication
  name: Commercelayer Authentication
  slug: commercelayer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Commercelayer Domain Security
  slug: commercelayer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Commercelayer Trust Center
  slug: commercelayer-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: commercelayer
tags:
- Commerce
- Headless
- Composable
- E-Commerce
- JSON:API
- Order
website: https://commercelayer.io
---
