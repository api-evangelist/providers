---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Seller Central Agentic Access
  operation_count: 21
  slug: amazon-seller-central-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 1
apis:
- description: REST API that lets approved developers and sellers manage Amazon Selling Partner accounts including catalog items, listings, orders, shipments, inventory, pricing, fees, reports, feeds, finances, noti
  name: Amazon Selling Partner API (SP-API)
  slug: sp-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Authentication API from Amazon Selling Partner API — 1 operation(s) for authentication.
  name: Amazon Selling Partner API Authentication API
  slug: amazon-seller-central-authentication-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Catalog API from Amazon Selling Partner API — 2 operation(s) for catalog.
  name: Amazon Selling Partner API Catalog API
  slug: amazon-seller-central-catalog-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Feeds API from Amazon Selling Partner API — 1 operation(s) for feeds.
  name: Amazon Selling Partner API Feeds API
  slug: amazon-seller-central-feeds-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Finances API from Amazon Selling Partner API — 1 operation(s) for finances.
  name: Amazon Selling Partner API Finances API
  slug: amazon-seller-central-finances-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Inventory API from Amazon Selling Partner API — 1 operation(s) for inventory.
  name: Amazon Selling Partner API Inventory API
  slug: amazon-seller-central-inventory-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Listings API from Amazon Selling Partner API — 1 operation(s) for listings.
  name: Amazon Selling Partner API Listings API
  slug: amazon-seller-central-listings-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Notifications API from Amazon Selling Partner API — 1 operation(s) for notifications.
  name: Amazon Selling Partner API Notifications API
  slug: amazon-seller-central-notifications-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Orders API from Amazon Selling Partner API — 3 operation(s) for orders.
  name: Amazon Selling Partner API Orders API
  slug: amazon-seller-central-orders-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Pricing API from Amazon Selling Partner API — 1 operation(s) for pricing.
  name: Amazon Selling Partner API Pricing API
  slug: amazon-seller-central-pricing-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Reports API from Amazon Selling Partner API — 2 operation(s) for reports.
  name: Amazon Selling Partner API Reports API
  slug: amazon-seller-central-reports-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Shipping API from Amazon Selling Partner API — 1 operation(s) for shipping.
  name: Amazon Selling Partner API Shipping API
  slug: amazon-seller-central-shipping-api
- baseURL: https://sellingpartnerapi-na.amazon.com
  baseurl_source: declared
  description: The Tokens API from Amazon Selling Partner API — 1 operation(s) for tokens.
  name: Amazon Selling Partner API Tokens API
  slug: amazon-seller-central-tokens-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication API
  slug: open-amazon-seller-central-authentication-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Catalog API
  slug: open-amazon-seller-central-catalog-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Feeds API
  slug: open-amazon-seller-central-feeds-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Finances API
  slug: open-amazon-seller-central-finances-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Inventory API
  slug: open-amazon-seller-central-inventory-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Listings API
  slug: open-amazon-seller-central-listings-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Notifications API
  slug: open-amazon-seller-central-notifications-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Orders API
  slug: open-amazon-seller-central-orders-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Pricing API
  slug: open-amazon-seller-central-pricing-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Reports API
  slug: open-amazon-seller-central-reports-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Shipping API
  slug: open-amazon-seller-central-shipping-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API) Authentication Tokens API
  slug: open-amazon-seller-central-tokens-api
- collection_type: open
  name: Amazon Selling Partner API (SP-API)
  slug: open-amazon-seller-central
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-seller-central-capability-edges.yml
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
overview: 'Amazon Selling Partner API publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Feeds API, and 9 more. Tagged areas include E-Commerce, Marketplace, Selling Partner, Amazon, and Seller Central.


  Amazon Selling Partner API''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- E-Commerce
- Marketplace
- Selling Partner
- Amazon
- Seller Central
- Catalog
- Order
- Inventory
- Fulfillment
website: https://developer.amazonservices.com/
---
