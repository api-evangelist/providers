---
aid: urban-outfitters
url: https://raw.githubusercontent.com/api-evangelist/urban-outfitters/refs/heads/main/apis.yml
name: Urban Outfitters
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Retail
  - Fashion
  - Apparel
  - Ecommerce
  - Affiliate
  - Marketplace
description: Urban Outfitters is a multi-channel lifestyle retailer offering an eclectic mix of women's, men's, and kids apparel, footwear, accessories, beauty, and home goods. Part of URBN, Inc. (which also owns Anthropologie, Free People, Bhldn, and Nuuly), Urban Outfitters operates stores in the US, Europe, and Canada alongside a robust ecommerce platform. The brand provides affiliate marketing integration through the Rakuten Advertising network and a third-party seller marketplace program (UO MRKT) that accepts independent brands selling through EDI and third-party integration platforms. Urban Outfitters uses Stripe for payment processing, Stripe Connect for marketplace seller payouts, and Stripe Terminal for in-store payments.
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: urban-outfitters:affiliate-api
    name: Urban Outfitters Affiliate Program
    description: Urban Outfitters affiliate program managed through Rakuten Advertising (formerly LinkShare) network. Provides affiliate tracking links, banner ads, marketing copy, and product data feeds for affiliates to promote Urban Outfitters products. Commission rates are approximately 2% per confirmed sale, with a 30-day cookie window and monthly payouts.
    humanURL: https://www.urbanoutfitters.com/help/affiliate
    baseURL: https://api.rakutenadvertising.com
    tags:
      - Affiliate
      - Marketing
      - Product Feed
      - Tracking
    properties:
      - type: Documentation
        url: https://www.urbanoutfitters.com/help/affiliate
      - type: OpenAPI
        url: openapi/urban-outfitters-affiliate-api-openapi.yml
      - type: JSONSchema
        url: json-schema/affiliate-api-product-schema.json
      - type: JSONSchema
        url: json-schema/affiliate-api-affiliate-link-schema.json
      - type: JSONSchema
        url: json-schema/affiliate-api-commission-report-schema.json
      - type: JSONSchema
        url: json-schema/affiliate-api-creative-schema.json
  - aid: urban-outfitters:marketplace-api
    name: Urban Outfitters Marketplace (UO MRKT) Integration
    description: Urban Outfitters operates a curated third-party marketplace called UO MRKT for independent lifestyle and fashion brands. Seller integration is managed through EDI and third-party connectors such as ConnectPointz, SellerCloud, and e-tailize. Provides product catalog sync, inventory management, order routing, and shipment tracking for approved sellers.
    humanURL: https://www.urbanoutfitters.com/mrkt-seller-form
    baseURL: https://www.urbanoutfitters.com
    tags:
      - Marketplace
      - Sellers
      - EDI
      - Inventory
      - Orders
    properties:
      - type: Documentation
        url: https://www.urbanoutfitters.com/mrkt-seller-form
      - type: OpenAPI
        url: openapi/urban-outfitters-marketplace-api-openapi.yml
      - type: JSONSchema
        url: json-schema/marketplace-api-seller-product-schema.json
      - type: JSONSchema
        url: json-schema/marketplace-api-order-schema.json
      - type: JSONSchema
        url: json-schema/marketplace-api-shipment-schema.json
      - type: JSONSchema
        url: json-schema/marketplace-api-inventory-update-schema.json
common:
  - type: Website
    url: https://www.urban-outfitters.com
  - type: Website
    url: https://www.urbanoutfitters.com
  - type: Portal
    url: https://www.urbanoutfitters.com/help/affiliate
    title: Affiliate Portal
  - type: GitHubOrganization
    url: https://github.com/urbn
  - type: JSONLD
    url: json-ld/urban-outfitters-context.jsonld
  - type: SpectralRules
    url: rules/urban-outfitters-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/urban-outfitters-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/retail-commerce.yaml
    title: Retail Commerce
  - type: NaftikoCapability
    url: capabilities/shared/affiliate-api.yaml
    title: Affiliate API (Shared)
  - type: NaftikoCapability
    url: capabilities/shared/marketplace-api.yaml
    title: Marketplace API (Shared)
  - type: Features
    data:
      - name: Affiliate Product Data Feeds
        description: Product catalog data feeds for affiliate partners to display and link Urban Outfitters products.
      - name: Affiliate Tracking Links
        description: Unique tracking links and banner ads through Rakuten Advertising for commission tracking.
      - name: Marketplace Seller Integration
        description: EDI and API-based integration for third-party brands selling through the UO MRKT marketplace.
      - name: Inventory Sync
        description: Real-time inventory synchronization between seller systems and Urban Outfitters marketplace.
      - name: Order Routing
        description: Automated order routing and fulfillment management for marketplace sellers.
      - name: Stripe Payments
        description: Stripe-powered payment processing for both online checkout and in-store POS via Stripe Terminal.
      - name: Stripe Connect Payouts
        description: Automated marketplace seller payouts through Stripe Connect.
  - type: UseCases
    data:
      - name: Content Creator Monetization
        description: Bloggers, influencers, and content creators earning commissions by promoting Urban Outfitters products.
      - name: Comparison Shopping
        description: Price comparison and product discovery platforms integrating Urban Outfitters product catalog.
      - name: Independent Brand Sales
        description: Independent fashion and lifestyle brands expanding distribution through Urban Outfitters marketplace.
      - name: Inventory Management
        description: Sellers using EDI or integration platforms to sync inventory and orders with Urban Outfitters.
  - type: Integrations
    data:
      - name: Rakuten Advertising
        description: Affiliate network platform managing Urban Outfitters affiliate program tracking and payouts.
      - name: ConnectPointz EDI
        description: EDI integration platform for Urban Outfitters marketplace seller connectivity.
      - name: SellerCloud
        description: Multi-channel inventory management platform with Urban Outfitters marketplace connector.
      - name: e-tailize
        description: European multi-channel selling platform with Urban Outfitters marketplace integration.
      - name: Stripe
        description: Payment processing and marketplace payout infrastructure powering all URBN brands.
      - name: Skimlinks
        description: Alternative affiliate network offering higher commission rates for Urban Outfitters.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
