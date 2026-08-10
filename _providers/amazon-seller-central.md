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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Seller Central Agentic Access
  operation_count: 21
  slug: amazon-seller-central-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 13
apis:
- description: REST API that lets approved developers and sellers manage Amazon Selling Partner accounts including catalog items, listings, orders, shipments, inventory, pricing, fees, reports, feeds, finances, noti
  name: Amazon Selling Partner API (SP-API)
  slug: sp-api
- description: The Authentication API from Amazon Selling Partner API — 1 operation(s) for authentication.
  name: Amazon Selling Partner API Authentication API
  slug: amazon-seller-central-authentication-api
- description: The Catalog API from Amazon Selling Partner API — 2 operation(s) for catalog.
  name: Amazon Selling Partner API Catalog API
  slug: amazon-seller-central-catalog-api
- description: The Feeds API from Amazon Selling Partner API — 1 operation(s) for feeds.
  name: Amazon Selling Partner API Feeds API
  slug: amazon-seller-central-feeds-api
- description: The Finances API from Amazon Selling Partner API — 1 operation(s) for finances.
  name: Amazon Selling Partner API Finances API
  slug: amazon-seller-central-finances-api
- description: The Inventory API from Amazon Selling Partner API — 1 operation(s) for inventory.
  name: Amazon Selling Partner API Inventory API
  slug: amazon-seller-central-inventory-api
- description: The Listings API from Amazon Selling Partner API — 1 operation(s) for listings.
  name: Amazon Selling Partner API Listings API
  slug: amazon-seller-central-listings-api
- description: The Notifications API from Amazon Selling Partner API — 1 operation(s) for notifications.
  name: Amazon Selling Partner API Notifications API
  slug: amazon-seller-central-notifications-api
- description: The Orders API from Amazon Selling Partner API — 3 operation(s) for orders.
  name: Amazon Selling Partner API Orders API
  slug: amazon-seller-central-orders-api
- description: The Pricing API from Amazon Selling Partner API — 1 operation(s) for pricing.
  name: Amazon Selling Partner API Pricing API
  slug: amazon-seller-central-pricing-api
- description: The Reports API from Amazon Selling Partner API — 2 operation(s) for reports.
  name: Amazon Selling Partner API Reports API
  slug: amazon-seller-central-reports-api
- description: The Shipping API from Amazon Selling Partner API — 1 operation(s) for shipping.
  name: Amazon Selling Partner API Shipping API
  slug: amazon-seller-central-shipping-api
- description: The Tokens API from Amazon Selling Partner API — 1 operation(s) for tokens.
  name: Amazon Selling Partner API Tokens API
  slug: amazon-seller-central-tokens-api
artifact_total: 17
collections:
- collection_type: open
  name: Amazon Selling Partner API (SP-API)
  slug: open-amazon-seller-central
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-seller-central-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-seller-central-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-seller-central-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://developer.amazonservices.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.amazon.com/sp-api
- group: commercial
  title: ''
  type: Pricing
  url: https://sell.amazon.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://sellercentral.amazon.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer-docs.amazon.com/llms.txt
created: '2026-05-11'
description: The Amazon Selling Partner API (SP-API) is the modern REST-based API that enables Amazon sellers, vendors, and third-party developers to programmatically access Seller Central data and operations including catalog management, orders, inventory, pricing, fulfillment, reports, finances, notifications, and advertising. SP-API uses Login with Amazon (LWA) OAuth 2.0 access tokens for authentication and replaces the legacy Amazon Marketplace Web Service (MWS).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-seller-central.png
layout: provider
modified: '2026-05-11'
name: Amazon Selling Partner API
nav: Providers
network: true
overview: 'Amazon Selling Partner API publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Feeds API, and 9 more. Tagged areas include eCommerce, Marketplace, Selling Partner, Amazon, and Seller Central.


  Amazon Selling Partner API''s developer surface includes authentication, documentation, pricing, signup flow, and 4 more developer resources.'
random_paper: 40
score:
  band: emerging
  composite: 27.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-seller-central/refs/heads/main/screenshots/amazon-seller-central-2026-06-20T171817.png
security:
- kind: authentication
  name: Amazon Seller Central Authentication
  slug: amazon-seller-central-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Seller Central Domain Security
  slug: amazon-seller-central-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amazon-seller-central
tags:
- eCommerce
- Marketplace
- Selling Partner
- Amazon
- Seller Central
- Catalog
- Orders
- Inventory
- Fulfillment
website: https://developer.amazonservices.com/
---
