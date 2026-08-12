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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/belk-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/belk
- group: company
  title: ''
  type: Website
  url: https://www.belk.com
- group: start
  title: Vendor Portal
  type: Portal
  url: https://www.belk.com/vendor-portal
created: '2026-03-23'
description: Belk is a privately-held American department store chain headquartered in Charlotte, North Carolina, serving the southeastern United States. The company sells clothing, handbags, jewelry, beauty products, and home goods. Belk operates an omnichannel retail model with physical stores and an online marketplace. Supplier and marketplace integrations are handled via EDI through value-added networks, with order management integration available through Rithum (formerly CommerceHub) and other channel management platforms.
features:
- description: Belk operates physical stores across the southeastern United States alongside an online retail and marketplace presence at belk.com.
  name: Omnichannel Retail
- description: Third-party vendors can list and sell products on Belk.com through the marketplace program, integrated via Rithum (formerly CommerceHub) channel management platform.
  name: Marketplace Seller Program
- description: Belk uses X12 EDI version 4030 for supplier integration, transmitted through value-added networks (VANs). Required documents include EDI 850 purchase orders, EDI 856 advance ship notices, and EDI 846 inventory feeds.
  name: EDI Supplier Integration
- description: Belk's vendor portal provides document specifications, EDI information, and vendor FAQ resources for suppliers to configure EDI integrations.
  name: Vendor Portal
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/belk.png
integrations:
- description: Rithum, formerly CommerceHub, is the primary integration platform for Belk marketplace sellers to manage orders, inventory, and fulfillment.
  name: Rithum (CommerceHub)
- description: Sellercloud supports Belk account integration through Rithum for omnichannel ecommerce order management and inventory synchronization.
  name: Sellercloud
- description: Alloy.ai provides a Belk retailer portal integration for demand forecasting and retail analytics based on Belk point-of-sale data.
  name: Alloy.ai
- description: Tradeshift supports Belk supplier invoice and procurement document exchange through its B2B network integration.
  name: Tradeshift
- description: ConnectPointz provides EDI compliance and channel management integration for Belk marketplace and supplier connections.
  name: ConnectPointz
layout: provider
modified: '2026-04-19'
name: Belk
nav: Providers
network: true
overview: 'Belk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Beauty, Department Store, E-Commerce, and Fashion.


  Belk''s developer surface includes developer portal and 3 more developer resources.'
press:
- date: '2026-05-25'
  title: TCS ignio™ AIOps Helps Belk Secure AI Edge for Operations
  url: https://www.tcs.com/what-we-do/industries/retail/video/tcs-ignio-aiops-secure-ai-edge-operations
- date: '2026-05-25'
  title: Belk is using gen AI to build its next generation of community
  url: https://www.linkedin.com/posts/lee-t-moore_new-way-now-belk-is-using-gen-ai-to-build-activity-7207357537459851264-DVw9
- date: '2026-05-25'
  title: How Belk elevated its customer experience with ...
  url: https://martech.org/how-belk-elevated-its-customer-experience-with-personalization/
- date: '2026-05-25'
  title: Belk harnesses AI to manage inventory
  url: https://www.retaildive.com/news/belk-harnesses-ai-to-manage-inventory/570588/
- date: '2026-05-25'
  title: BEAUTYSPACE Partners with Belk to Expand Retail and ...
  url: https://www.prnewswire.com/news-releases/beautyspace-partners-with-belk-to-expand-retail-and-digital-footprint-302730630.html
random_paper: 66
score:
  band: minimal
  composite: 6.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/belk/refs/heads/main/screenshots/belk-2026-06-20T173133.png
security:
- kind: domain-security
  name: Belk Domain Security
  slug: belk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: belk
tags:
- Apparel
- Beauty
- Department Store
- E-Commerce
- Fashion
- Home Goods
- Jewelry
- Marketplace
- Retail
- Southeastern US
use_cases:
- description: Third-party vendors integrate with the Belk marketplace to list products, receive orders, and manage fulfillment through approved channel platforms.
  name: Marketplace Selling
- description: Manufacturers and distributors connect to Belk's EDI network to exchange purchase orders, advance ship notices, and inventory feeds in X12 format.
  name: EDI Supplier Compliance
- description: Retail suppliers and analytics platforms consume Belk point-of-sale data through retail portal integrations for demand planning and replenishment.
  name: Retail Analytics
website: https://www.belk.com
---
