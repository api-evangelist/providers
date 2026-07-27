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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Gelato Agentic Access
  operation_count: 18
  slug: gelato-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 6
apis:
- description: The Ecommerce API from Gelato — 4 operation(s) for ecommerce.
  name: Gelato Ecommerce API
  slug: gelato-ecommerce-api
- description: The Orders API from Gelato — 5 operation(s) for orders.
  name: Gelato Orders API
  slug: gelato-orders-api
- description: The Prices API from Gelato — 1 operation(s) for prices.
  name: Gelato Prices API
  slug: gelato-prices-api
- description: The Product Catalog API from Gelato — 5 operation(s) for product catalog.
  name: Gelato Product Catalog API
  slug: gelato-product-catalog-api
- description: The Shipment API from Gelato — 1 operation(s) for shipment.
  name: Gelato Shipment API
  slug: gelato-shipment-api
- description: The Stock API from Gelato — 1 operation(s) for stock.
  name: Gelato Stock API
  slug: gelato-stock-api
artifact_total: 14
collections:
- collection_type: open
  name: Gelato API
  slug: open-gelato
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gelato-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gelato-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gelato-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gelato-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gelato-com
- group: company
  title: ''
  type: Website
  url: https://www.gelato.com
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.gelato.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/gelato-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gelato-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gelato-finops.yml
created: '2026-06-25'
description: Gelato operates a global, distributed print-on-demand production network that lets ecommerce sellers produce and ship products locally in 30+ countries. The Gelato API exposes REST endpoints across dedicated subdomains for orders, the product catalog, pricing and stock, shipment methods, ecommerce store products and templates, plus webhooks - all authenticated with an X-API-KEY header.
finops:
- name: Gelato Finops
  service_category: Print on Demand and Fulfillment
  slug: gelato-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gelato.png
layout: provider
modified: '2026-06-25'
name: Gelato
nav: Providers
network: true
overview: 'Gelato publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Ecommerce API, Orders API, Prices API, and 3 more. Tagged areas include Print on Demand, Ecommerce, Fulfillment, Distributed Production, and Orders.


  Gelato''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Gelato Plans Pricing
  plan_count: 4
  slug: gelato-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 4
  name: Gelato Rate Limits
  slug: gelato-rate-limits
score:
  band: thin
  composite: 39.7
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gelato/refs/heads/main/screenshots/gelato-2026-07-25T215522.png
security:
- kind: authentication
  name: Gelato Authentication
  slug: gelato-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gelato Domain Security
  slug: gelato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gelato Vulnerability Disclosure
  slug: gelato-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gelato
tags:
- Print on Demand
- Ecommerce
- Fulfillment
- Distributed Production
- Orders
website: https://www.gelato.com
---
