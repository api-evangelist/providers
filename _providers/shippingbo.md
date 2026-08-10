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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: 'Shippingbo''s primary REST/JSON API for managing the full e-commerce logistics lifecycle: orders, order items, products, stocks, customers, shipments, sources, and warehouse pickings. Documentation is '
  name: Shippingbo API
  slug: shippingbo-api
- description: Dedicated Transport Management System API for multi-carrier shipment execution. Supports carrier selection rules, label generation, tracking, and post-shipment customer notifications across 40+ pre-in
  name: Shippingbo TMS API
  slug: shippingbo-tms-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippingbo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shippingbo.com
- group: company
  title: ''
  type: WebsiteEN
  url: https://www.shippingbo.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.shippingbo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shippingbo.com/docs/api/i15i5zn8ewpo0-introduction
- group: auth
  title: ''
  type: AuthorizationServer
  url: https://oauth.shippingbo.com/
- group: other
  title: ''
  type: APIOverview
  url: https://www.shippingbo.com/en/e-commerce/api-e-commerce-connect-automate-and-expand-your-logistics/
- group: other
  title: ''
  type: APIPage
  url: https://go.shippingbo.com/fr/api
- group: other
  title: ''
  type: Product
  url: https://www.shippingbo.com/en/produits/
- group: other
  title: ''
  type: OMS
  url: https://www.shippingbo.com/en/produits/oms/
- group: other
  title: ''
  type: WMS
  url: https://www.shippingbo.com/en/produits/wms/
- group: other
  title: ''
  type: TMS
  url: https://www.shippingbo.com/en/produits/tms/
- group: other
  title: ''
  type: Carriers
  url: https://www.shippingbo.com/en/integrations/transporteurs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shippingbo.com/en/tarifs/
- group: other
  title: ''
  type: Customers
  url: https://www.shippingbo.com/en/clients/
- group: company
  title: ''
  type: Blog
  url: https://www.shippingbo.com/en/blog/
- group: other
  title: ''
  type: Company
  url: https://www.shippingbo.com/en/qui-sommes-nous/
- group: operate
  title: ''
  type: Contact
  url: https://www.shippingbo.com/en/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.shippingbo.com/en/rejoignez-nous/
- group: company
  title: ''
  type: LinkedIn
  url: https://fr.linkedin.com/company/shippingbo-fr
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/shippingbo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@shippingbo
created: '2026-05-25'
description: Shippingbo is a Toulouse, France-based e-commerce logistics SaaS founded in 2016 by Marc Hericher and Romain Parent. The platform unifies an Order Management System (OMS), Warehouse Management System (WMS), and Transport Management System (TMS) behind a single REST API so that merchants, DNVBs, 3PLs, wholesalers, manufacturers, and marketplaces can centralize multi-channel orders, pilot warehouse picking and packing, and execute multi-carrier shipments from one back office. Shippingbo claims 5,000+ active users, 80 million orders, and EUR 5 billion in merchandise handled in 2024, with 2,500+ warehouses equipped across France and Europe. The Shippingbo Developer Portal (powered by Stoplight) exposes a public REST/JSON API covering orders, products, stocks, shipments, customers, pickings, and source connectors, secured by OAuth 2.0 through the oauth.shippingbo.com authorization server. Shippingbo additionally offers a dedicated TMS API for multi-carrier label generation and a
  webhook channel for order state changes, stock changes, and shipment events. Reported developer-facing scale includes 500+ developers, 10+ million orders processed through the APIs, 500+ million webhook deliveries, and 40+ pre-integrated carriers. Shippingbo is a French Tech company backed by IRDI Capital Investissement and GSO Innovation.
features:
- Multi-channel order centralization across e-commerce sites, marketplaces, and private sales
- Real-time inventory across multiple warehouses with platform-specific stock rules
- Guided WMS picking and packing sessions with PDA / barcode-scanner support
- Multi-carrier TMS with 40+ pre-integrated French and European carriers
- Automated carrier selection rules based on weight, destination, service, and cost
- Customer notifications and branded post-purchase tracking
- Returns management
- REST/JSON API (Stoplight-hosted developer portal)
- OAuth 2.0 authentication via oauth.shippingbo.com
- Webhooks for order state changes, stock changes, and shipment events
- Dedicated TMS API usable standalone or with the full platform
- Source connectors for CMS, marketplaces, and ERPs
- 3PL mode for logistics providers operating on behalf of multiple merchants
- Reported scale: 80M+ orders and EUR 5B merchandise handled in 2024
- Reported developer scale: 500+ developers, 10M+ orders, 500M+ webhooks
- 2,500+ warehouses equipped across France and Europe
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippingbo.png
layout: provider
modified: '2026-05-25'
name: Shippingbo
nav: Providers
network: true
overview: 'Shippingbo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Logistics, Ecommerce, Order Management, and Warehouse Management.


  Shippingbo''s developer surface includes documentation, pricing, engineering blog, YouTube channel, and 18 more developer resources.'
random_paper: 31
score:
  band: minimal
  composite: 12.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shippingbo/refs/heads/main/screenshots/shippingbo-2026-06-20T193820.png
security:
- kind: domain-security
  name: Shippingbo Domain Security
  slug: shippingbo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippingbo
tags:
- Shipping
- Logistics
- Ecommerce
- Order Management
- Warehouse Management
- Transport Management
- OMS
- WMS
- TMS
- Multi-Carrier
- Fulfillment
- 3PL
- Marketplaces
- Webhooks
- OAuth2
- SaaS
- France
- French Tech
website: https://www.shippingbo.com
---
