---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Rappi Partners REST API is the integration surface used by approved restaurants, grocery and retail merchants, and middleware/POS providers to operate on the Rappi marketplace. Authentication is O
  name: Rappi Partners REST API
  slug: partners-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rappi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rappi.com/
- group: company
  title: ''
  type: About
  url: https://about.rappi.com/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev-portal.rappi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev-portal.rappi.com/en/api-reference/
- group: auth
  title: ''
  type: Authentication
  url: https://dev-portal.rappi.com/en/api-reference/authentication/
- group: design
  title: ''
  type: Webhooks
  url: https://dev-portal.rappi.com/en/api-reference/webhooks/
- group: build
  title: ''
  type: IntegrationStandards
  url: https://dev-portal.rappi.com/integration-standards/
- group: operate
  title: ''
  type: FAQ
  url: https://dev-portal.rappi.com/en/faqs/
- group: operate
  title: ''
  type: Deprecations
  url: https://dev-portal.rappi.com/en/deprecations/
- group: other
  title: ''
  type: Merchants
  url: https://merchants.rappi.com/
- group: start
  title: ''
  type: StoreSignUp
  url: https://mitienda.rappi.com.mx/
- group: other
  title: ''
  type: Couriers
  url: https://soyrappi.com.mx/
- group: other
  title: ''
  type: RappiPay
  url: https://www.rappipay.mx/
- group: company
  title: ''
  type: Blog
  url: https://blog.rappi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rappiinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rappi
- group: other
  title: ''
  type: YCombinator
  url: https://www.ycombinator.com/companies/rappi
created: '2026-05-24'
description: Rappi is a Colombian-founded pan-Latin American super-app headquartered in Bogotá, with regional hubs in São Paulo and Mexico City. Founded in 2015 by Simón Borrero, Sebastián Mejía, and Felipe Villamarín, and accelerated through Y Combinator's W16 batch, Rappi operates across Argentina, Brazil, Chile, Colombia, Costa Rica, Ecuador, Mexico, Peru, and Uruguay. The platform bundles on-demand delivery (restaurants, groceries via "Súper" and Turbo Fresh, pharmacies, retail, alcohol) with consumer fintech (RappiPay, RappiCard, RappiCash) and adjacent services such as RappiTravel and the RappiPrime subscription. Rappi's developer surface is operated through its Partners program at dev-portal.rappi.com, where approved restaurants, retailers, and middleware providers obtain OAuth 2.0 client credentials to integrate with a REST API for menu and catalog management, store availability, order lifecycle events, financial reconciliation, and webhook subscriptions. Access is not self-serve
  — a Rappi business contact must approve onboarding, after which partners receive development-environment credentials and an integration path to production. SoftBank-backed since 2019, Rappi competes regionally with iFood, Uber Eats, and DiDi Food, with fintech ambitions overlapping Nubank, Mercado Pago, and regional neobanks.
features:
- description: Restaurant, grocery (Súper), pharmacy, retail, and alcohol delivery fulfilled by the Rappi courier fleet across nine LatAm countries.
  name: On-Demand Delivery
- description: Sub-15-minute grocery and convenience delivery from Rappi-operated dark stores in major metropolitan areas.
  name: Turbo Fresh
- description: Consumer fintech wallet, debit, and co-branded credit card products embedded in the super-app and operated as regulated entities in select markets.
  name: RappiPay & RappiCard
- description: In-app flights, hotels, and travel booking surface integrated with the Rappi wallet and loyalty stack.
  name: RappiTravel
- description: Recurring membership offering free delivery, exclusive discounts, and partner perks across the super-app verticals.
  name: RappiPrime Subscription
- description: OAuth-secured REST API for menus, availability, orders, stores, financial reconciliation, and webhooks, gated behind manual partner onboarding.
  name: Partners Developer Portal
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rappi.png
integrations:
- description: Middleware providers connect kitchen and POS platforms to the Rappi Rests API for menu and order flow.
  name: Restaurant POS Systems
- description: Catalog, pricing, and inventory systems push availability updates through the Partners API.
  name: Grocery & Retail ERPs
- description: RappiPay and RappiCard integrate with regional card networks and local payment rails per country.
  name: Payment Networks
- description: RappiTravel aggregates flight and hotel inventory from third-party GDS and travel partners.
  name: Travel Suppliers
layout: provider
modified: '2026-05-24'
name: Rappi
nav: Providers
network: true
overview: 'Rappi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Delivery, Food Delivery, Grocery Delivery, On-Demand, and Last Mile.


  Rappi''s developer surface includes API reference, authentication, FAQ, engineering blog, and 14 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rappi/refs/heads/main/screenshots/rappi-2026-06-20T192604.png
security:
- kind: domain-security
  name: Rappi Domain Security
  slug: rappi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rappi
solutions:
- description: Onboarding, menu management, order capture, and reconciliation tools for restaurant brands on the Rappi marketplace.
  name: Restaurants
- description: Catalog, stock, and store-availability tooling for supermarket, convenience, and specialty retail partners.
  name: Grocery & Retail
- description: Last-mile fulfillment and Rappi-native commerce for enterprise brands seeking LatAm coverage.
  name: Brands & Enterprises
- description: The Rappi super-app for delivery, fintech, travel, and Prime subscription benefits across nine countries.
  name: Consumers
tags:
- Delivery
- Food Delivery
- Grocery Delivery
- On-Demand
- Last Mile
- Logistics
- Super App
- Fintech
- Payments
- Marketplace
- Latin America
- Colombia
use_cases:
- description: Restaurant POS vendors and order aggregators sync menus and push/pull orders between merchant systems and Rappi storefronts.
  name: POS & Aggregator Integration
- description: Supermarket and convenience chains keep large SKU catalogs and real-time stock availability synchronized with Rappi store pages.
  name: Grocery & Retail Catalog Sync
- description: Brands receive Rappi orders via webhook, route them to kitchen or fulfillment systems, and progress status back through the API.
  name: Order Lifecycle Automation
- description: Merchants pull payout, commission, and settlement data through the Financial endpoints for accounting and FP&A pipelines.
  name: Financial Reconciliation
- description: Enterprise brands tap the Rappi courier fleet for branded last-mile delivery in LatAm metros.
  name: Last-Mile as a Service
website: https://www.rappi.com/
---
