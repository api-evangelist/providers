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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 12
apis:
- description: 'Seller authorization flow: a Lazada seller grants a registered Lazada Open Platform app permission to call Lazada APIs on their shop''s behalf, issuing access and refresh tokens scoped per region.'
  name: Lazada Seller Authorization (OAuth) API
  slug: authorization
- description: Create, update, retrieve, and remove products and SKUs; manage variations, attributes, images, and stock; submit to Lazada Category Tree and Category Attribute APIs.
  name: Lazada Product API
  slug: product
- description: Retrieve Lazada's hierarchical category tree, category attributes, and category-specific attribute values used to structure product submissions.
  name: Lazada Category API
  slug: category
- description: Retrieve orders, order items, order details, and buyer information; pack orders into shipments; set status to ready-to-ship and packed; cancel and reject orders.
  name: Lazada Order API
  slug: order
- description: Generate shipping labels (AWB), retrieve shipment providers, manifest pickups, and fetch shipment tracking information across Lazada's regional logistics network (LEX) and 3PL partners.
  name: Lazada Logistics API
  slug: logistics
- description: Retrieve transaction details, fee breakdowns, payout history, and invoice records used by sellers and ERPs to reconcile Lazada marketplace settlements.
  name: Lazada Finance API
  slug: finance
- description: Retrieve shop information, seller performance, store categories, store taxonomy, and seller-account metadata.
  name: Lazada Shop / Seller API
  slug: shop
- description: Create, update, list, and remove seller-level promotions — vouchers (collectible, shop-wide, item-level), FlexiCombo bundles, and product-level discounts.
  name: Lazada Promotion API
  slug: promotion
- description: Upload images to Lazada's CDN-backed image library and retrieve the image URLs used when creating or updating products.
  name: Lazada Image API
  slug: image
- description: Retrieve return requests, return order details, and refund status; submit return acceptance or rejection actions and coordinate reverse-logistics pickup.
  name: Lazada Returns / Reverse API
  slug: returns
- description: Bidirectional buyer-seller messaging API for in-app conversations on Lazada — including sending and retrieving chat sessions, message lists, and templated responses.
  name: Lazada Chat (IM) API
  slug: chat-message
- description: Subscribe to push notifications for order, return, item, and IM events; verify message signatures and ack deliveries from Lazada's message channel.
  name: Lazada Push Notification API
  slug: push-message
artifact_total: 17
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lazada-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lazada-domain-security.yml
- group: other
  title: ''
  type: Marketplace
  url: https://www.lazada.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.lazada.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.lazada.com/apps/doc/doc?nodeId=10557
- group: other
  title: ''
  type: APIExplorer
  url: https://open.lazada.com/apps/doc/api
- group: other
  title: ''
  type: SellerCenter
  url: https://sellercenter.lazada.com/
- group: start
  title: ''
  type: BrandPortal
  url: https://brands.lazada.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.alibabagroup.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.lazada.com/en/about/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lazada/
created: '2026-05-23'
description: Lazada Group is a Southeast Asian e-commerce platform owned by Alibaba Group since 2016, operating localized marketplaces in Singapore, Malaysia, Indonesia, Thailand, the Philippines, and Vietnam. Lazada Open Platform (openapi.lazada.com) provides a partner-facing REST API for sellers, brands, ERP / OMS vendors, and TP (TaoBao Partner) developers — covering Product / Category catalog, Order processing, Logistics and shipping label generation, Finance and payout reconciliation, Shop and Seller profile, Promotion management (vouchers, FlexiCombo, Sponsored Solutions), Image / asset upload, Returns and reverse logistics, and Bidirectional message webhooks. Authentication uses an App Key + App Secret plus a per-seller access token issued via OAuth-style seller authorization, with all requests signed using HMAC-SHA256 in Alibaba's TOP signature scheme.
finops:
- name: Lazada Finops
  service_category: API
  slug: lazada-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lazada.png
layout: provider
modified: '2026-05-23'
name: Lazada
nav: Providers
network: true
overview: 'Lazada publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Marketplace, Southeast Asia, Alibaba, and Order.


  Lazada''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Lazada Plans Pricing
  plan_count: 1
  slug: lazada-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Lazada Rate Limits
  slug: lazada-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lazada/refs/heads/main/screenshots/lazada-2026-06-20T184341.png
security:
- kind: domain-security
  name: Lazada Domain Security
  slug: lazada-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lazada Vulnerability Disclosure
  slug: lazada-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lazada
tags:
- E-Commerce
- Marketplace
- Southeast Asia
- Alibaba
- Order
- Product
- Logistics
- Lazada
website: https://open.lazada.com/
---
