---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 17
apis:
- description: The shop authorization flow lets a Shopee seller grant a registered partner application access to their shop. The partner receives a per-shop access token (and refresh token) used for all subsequent v
  name: Shopee Shop Authorization API
  slug: auth
- description: 'Manage shop-level configuration: shop info, shop profile, shop notification, shop notice, warehouse details, and authorised category list.'
  name: Shopee Shop API
  slug: shop
- description: Create, update, retrieve, and delete products and SKUs; manage product attributes, variations, media, stock, and price; submit and check Shopee's category attribute tree.
  name: Shopee Product API
  slug: product
- description: Retrieve order list, order detail, order status updates, buyer information, and items. Supports order cancellation, split, and dispute information.
  name: Shopee Order API
  slug: order
- description: 'Manage shipping for Shopee orders: get shipping parameter, ship order, get shipping document, get tracking number, tracking info, update channel, channel list, and address.'
  name: Shopee Logistics API
  slug: logistics
- description: Retrieve return requests, return detail, dispute reasons, and offer to accept / dispute returns initiated by buyers, with proof-of-return upload and refund coordination.
  name: Shopee Returns API
  slug: returns
- description: 'Create and manage shop-level discount campaigns: add / update / delete discounts, manage discount items, and retrieve discount lists and details.'
  name: Shopee Discount API
  slug: discount
- description: Create, update, list, and end vouchers; manage voucher coverage (product / order level), display channels, and target audience for shop and platform-tier promotions.
  name: Shopee Voucher API
  slug: voucher
- description: Create and manage bundle deal promotions ("buy X for Y price") at the shop level, including bundle deal items and shop list operations.
  name: Shopee Bundle Deal API
  slug: bundle-deal
- description: Add-on Deal API supports "buy main item, get add-on at discount" promotions — including add-on deal CRUD and add-on item management.
  name: Shopee Add-on Deal API
  slug: add-on-deal
- description: Retrieve payout, escrow detail, payment method list, billing transaction info, and wallet transaction list for reconciliation of Shopee marketplace settlements.
  name: Shopee Payment API
  slug: payment
- description: Surface shop performance metrics — penalty points, listing violations, late shipment rate, cancellation rate, and other operational health indicators.
  name: Shopee Account Health API
  slug: account-health
- description: Public endpoints that do not require shop authorization — get shops by partner, refresh access token, get shop and merchants info, and warehouse / region utilities.
  name: Shopee Public API
  slug: public
- description: Subscribe to push notifications for order, item, return, logistics, payment, and shop events; manage push configurations and verify Shopee's HMAC signatures on every delivery.
  name: Shopee Push (Webhook) API
  slug: push
- description: Cross-Border Seller Center (CBSC) APIs let global sellers manage a single master product catalog and publish to one or many Shopee country shops, with per-region price and stock control.
  name: Shopee Global Product (CBSC) API
  slug: global-product
- description: Merchant-level operations for Shopee Mall and CB Merchant accounts that own multiple shops — including merchant info, shop list, and merchant warehouse management.
  name: Shopee Merchant API
  slug: merchant
- description: 'First-Mile APIs (for cross-border sellers) manage the consolidated outbound shipment from a seller''s home market into Shopee''s destination-country logistics network, including manifest generation and '
  name: Shopee First-Mile API
  slug: first-mile
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopee-domain-security.yml
- group: other
  title: ''
  type: Marketplace
  url: https://shopee.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.shopee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.shopee.com/documents
- group: docs
  title: ''
  type: DeveloperGuide
  url: https://open.shopee.com/developer-guide
- group: other
  title: ''
  type: ShopeeMall
  url: https://shopee.sg/mall
- group: other
  title: ''
  type: SellerCenter
  url: https://seller.shopee.com/
- group: other
  title: ''
  type: ShopeePay
  url: https://shopeepay.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.sea.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopee/
- group: agent
  title: ''
  type: LlmsText
  url: https://shopee.sg/llms.txt
created: '2026-05-23'
description: Shopee is Southeast Asia's largest e-commerce marketplace, operated by Sea Limited and active across Singapore, Indonesia, Malaysia, Thailand, the Philippines, Vietnam, Taiwan, and select markets in Latin America (Brazil, Mexico, Colombia, Chile) and Europe (Spain, Poland). Shopee Open Platform (open.shopee.com) exposes a partner / seller-facing REST API (v2) covering shop configuration, product / SKU management, order processing, logistics and shipping label generation, returns and refunds, discounts and vouchers, payments, push notifications, and global cross-border product management. Authentication uses a partner ID + partner key with per-shop access tokens issued via OAuth- style shop authorization.
finops:
- name: Shopee Finops
  service_category: API
  slug: shopee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopee.png
layout: provider
modified: '2026-05-23'
name: Shopee
nav: Providers
network: true
overview: 'Shopee publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-commerce, Marketplace, Southeast Asia, Cross-border, and Orders.


  Shopee''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Shopee Plans Pricing
  plan_count: 1
  slug: shopee-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Shopee Rate Limits
  slug: shopee-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopee/refs/heads/main/screenshots/shopee-2026-06-20T193833.png
security:
- kind: domain-security
  name: Shopee Domain Security
  slug: shopee-domain-security
  summary_line: TLSv1.2 · DMARC
slug: shopee
tags:
- E-commerce
- Marketplace
- Southeast Asia
- Cross-border
- Orders
- Products
- Logistics
- Shopee
website: https://open.shopee.com/
---
