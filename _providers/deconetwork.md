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
- acting_count: 4
  human_in_the_loop: 0
  name: Deconetwork Agentic Access
  operation_count: 8
  slug: deconetwork-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: The Inventory API from DecoNetwork — 2 operation(s) for inventory.
  name: DecoNetwork Inventory API
  slug: deconetwork-inventory-api
- description: The Orders API from DecoNetwork — 2 operation(s) for orders.
  name: DecoNetwork Orders API
  slug: deconetwork-orders-api
- description: The Products API from DecoNetwork — 2 operation(s) for products.
  name: DecoNetwork Products API
  slug: deconetwork-products-api
- description: The Purchase Orders API from DecoNetwork — 2 operation(s) for purchase orders.
  name: DecoNetwork Purchase Orders API
  slug: deconetwork-purchase-orders-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deconetwork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deconetwork-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deconetwork-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deconetwork
- group: company
  title: ''
  type: Website
  url: https://www.deconetwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.deconetwork.com/developer-resources/
- group: start
  title: ''
  type: SignUp
  url: https://www.deconetwork.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/deconetwork-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deconetwork-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deconetwork-finops.yml
created: '2026-07-11'
description: DecoNetwork is web-to-print and business-management software for custom apparel decorators and print shops - screen printing, embroidery, direct-to-garment, and promotional products - combining branded online stores, quoting, order and artwork management, purchasing, inventory, and production workflow in one platform. For Enterprise subscribers DecoNetwork exposes a documented public JSON API over HTTPS to search and update orders, manage products, manage inventory, and manage purchase orders, letting shops integrate DecoNetwork with external carts, ERP/CRM systems, and custom production automation. Each request is authenticated with account username and password fields; the API is request/response REST returning JSON, and API access is included only on the Enterprise plan.
finops:
- name: Deconetwork Finops
  service_category: Business Management Software
  slug: deconetwork-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deconetwork.png
layout: provider
modified: '2026-07-11'
name: DecoNetwork
nav: Providers
network: true
overview: 'DecoNetwork publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Orders API, Products API, and 1 more. Tagged areas include Custom Apparel, Web to Print, Print Shop Management, Orders, and Products.


  DecoNetwork''s developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Deconetwork Plans Pricing
  plan_count: 3
  slug: deconetwork-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 3
  name: Deconetwork Rate Limits
  slug: deconetwork-rate-limits
score:
  band: thin
  composite: 40.2
  delta: -2.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deconetwork/refs/heads/main/screenshots/deconetwork-2026-07-25T211529.png
security:
- kind: authentication
  name: Deconetwork Authentication
  slug: deconetwork-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Deconetwork Domain Security
  slug: deconetwork-domain-security
  summary_line: TLSv1.3
slug: deconetwork
tags:
- Custom Apparel
- Web to Print
- Print Shop Management
- Orders
- Products
- Inventory
- Production Workflow
- E-commerce
website: https://www.deconetwork.com
---
