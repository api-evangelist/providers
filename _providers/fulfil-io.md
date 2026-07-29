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
- acting_count: 17
  human_in_the_loop: 0
  name: Fulfil Io Agentic Access
  operation_count: 31
  slug: fulfil-io-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 10
apis:
- description: Verify API credentials.
  name: Fulfil Authentication API
  slug: fulfil-io-authentication-api
- description: Customers, suppliers, and contacts via the party.party model.
  name: Fulfil Customers API
  slug: fulfil-io-customers-api
- description: Inventory via stock.move and stock.location models.
  name: Fulfil Inventory & Stock API
  slug: fulfil-io-inventory-stock-api
- description: Production orders via the production model.
  name: Fulfil Manufacturing API
  slug: fulfil-io-manufacturing-api
- description: The generic model interface applicable to any Fulfil model.
  name: Fulfil Model Interface API
  slug: fulfil-io-model-interface-api
- description: Catalog via product.template and product.product models.
  name: Fulfil Products & Variants API
  slug: fulfil-io-products-variants-api
- description: Purchase orders via the purchase.purchase model.
  name: Fulfil Purchases API
  slug: fulfil-io-purchases-api
- description: Sales orders via the sale.sale model.
  name: Fulfil Sales Orders API
  slug: fulfil-io-sales-orders-api
- description: Fulfillment via stock.shipment.out and stock.shipment.in models.
  name: Fulfil Shipments API
  slug: fulfil-io-shipments-api
- description: Webhook subscriptions for real-time ERP events.
  name: Fulfil Webhooks API
  slug: fulfil-io-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: Fulfil REST API (v2)
  slug: open-fulfil-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fulfil-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fulfil-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fulfil-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fulfil-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fulfil-io-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fulfil-io-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fulfilio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fulfil-io
- group: company
  title: ''
  type: Website
  url: https://www.fulfil.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fulfil.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/fulfil-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fulfil-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fulfil-io-finops.yml
created: '2026-07-04'
description: Fulfil is a cloud ERP and operations platform for e-commerce, DTC, and wholesale merchants - unifying order management, inventory, warehouse operations (WMS), manufacturing and production (MRP), purchasing, and accounting in one system, purpose-built for Shopify Plus and high-volume DTC brands. The Fulfil REST API (v2) exposes every ERP model through a single uniform model interface at https://{merchant_id}.fulfil.io/api/v2, advertising 6,000+ endpoints with full create/read/update/delete access, action calls, reports, and wizards across all models. Authentication is via OAuth 2.0 for public apps or personal access tokens (X-API-KEY / HTTP Basic) for private integrations, and outbound webhooks (with a Google Pub/Sub option) deliver real-time ERP events such as order and shipment changes.
finops:
- name: Fulfil Io Finops
  service_category: Business Applications (ERP)
  slug: fulfil-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fulfil-io.png
layout: provider
modified: '2026-07-04'
name: Fulfil
nav: Providers
network: true
overview: 'Fulfil publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customers API, Inventory & Stock API, and 7 more. Tagged areas include ERP, E-commerce, Order Management, Inventory, and Warehouse Management.


  Fulfil''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Fulfil Io Plans Pricing
  plan_count: 4
  slug: fulfil-io-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Fulfil Io Rate Limits
  slug: fulfil-io-rate-limits
scopes:
- name: Fulfil Io Scopes
  scope_count: 2
  slug: fulfil-io-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 40.6
  delta: -2.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fulfil-io/refs/heads/main/screenshots/fulfil-io-2026-07-25T215253.png
security:
- kind: authentication
  name: Fulfil Io Authentication
  slug: fulfil-io-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Fulfil Io Domain Security
  slug: fulfil-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fulfil Io Vulnerability Disclosure
  slug: fulfil-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fulfil Io Trust Center
  slug: fulfil-io-trust-center
  summary_line: SOC 2, GDPR
slug: fulfil-io
tags:
- ERP
- E-commerce
- Order Management
- Inventory
- Warehouse Management
- Manufacturing
- Operations
website: https://www.fulfil.io
---
