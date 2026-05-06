---
aid: advance-auto-parts
url: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - name: Advance Auto Parts Catalog API
    description: The Advance Auto Parts Catalog API provides programmatic access to the full product catalog including parts, accessories, batteries, and fluids. Supports vehicle fitment lookups by year/make/model/engine, part number searches, availability checks, pricing, and store inventory queries for professional and DIY customers.
    humanURL: https://www.advanceautoparts.com
    baseURL: https://api.advanceautoparts.com/v1
    tags:
      - Automotive
      - Parts Catalog
      - Inventory
      - Vehicle Fitment
    properties:
      - type: Documentation
        url: https://www.advanceautoparts.com/i/policies/terms-and-conditions
      - type: OpenAPI
        url: openapi/advance-auto-parts-catalog-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/advance-auto-parts-catalog-api-context.jsonld
      - type: SpectralRules
        url: rules/advance-auto-parts-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/catalog-api.yaml
      - type: Vocabulary
        url: vocabulary/advance-auto-parts-vocabulary.yaml
  - name: Advance Auto Parts Commerce API
    description: The Advance Auto Parts Commerce API enables ordering, cart management, loyalty program integration, and order fulfillment for commercial accounts. Supports creating orders, managing Speed Perks loyalty points, tracking shipments, and accessing purchase history for fleet and professional installer accounts.
    humanURL: https://www.advanceautoparts.com/i/help/commercial-accounts
    baseURL: https://api.advanceautoparts.com/commerce/v1
    tags:
      - Automotive
      - E-Commerce
      - Loyalty
      - Order Management
    properties:
      - type: Documentation
        url: https://www.advanceautoparts.com/i/help/commercial-accounts
      - type: OpenAPI
        url: openapi/advance-auto-parts-commerce-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/advance-auto-parts-commerce-api-context.jsonld
      - type: SpectralRules
        url: rules/advance-auto-parts-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/auto-parts-shopping.yaml
      - type: Vocabulary
        url: vocabulary/advance-auto-parts-vocabulary.yaml
common:
  - type: Website
    url: https://www.advanceautoparts.com
  - type: Portal
    url: https://www.advanceautoparts.com/i/help
  - type: Support
    url: https://www.advanceautoparts.com/i/help/customer-service
  - type: Blog
    url: https://www.advanceautoparts.com/gearhead
  - type: TermsOfService
    url: https://www.advanceautoparts.com/i/policies/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.advanceautoparts.com/i/policies/privacy
  - type: Login
    url: https://www.advanceautoparts.com/myaccount/login
  - type: SignUp
    url: https://www.advanceautoparts.com/myaccount/register
  - type: Features
    data:
      - name: Vehicle Fitment Search
        description: Look up compatible parts by year, make, model, engine, and trim for accurate fitment verification.
      - name: Real-Time Inventory
        description: Check part availability and quantity at nearby stores and distribution centers in real time.
      - name: Parts Catalog Access
        description: Access a comprehensive catalog of millions of SKUs including OEM and aftermarket parts, accessories, and fluids.
      - name: Commercial Account Management
        description: Manage commercial accounts, purchase orders, net terms, and invoice history for professional installers.
      - name: Speed Perks Loyalty Integration
        description: Query and apply Speed Perks loyalty points for purchases and track reward status.
      - name: Same-Day Delivery and Store Pickup
        description: Order parts for same-day delivery or in-store pickup with real-time availability confirmation.
      - name: Price and Promo Queries
        description: Retrieve current pricing, promotional discounts, and sale prices for catalog items.
      - name: Order Tracking
        description: Track shipment status and estimated delivery for online and commercial orders.
  - type: UseCases
    data:
      - name: Shop Management Software Integration
        description: Integrate parts ordering directly into auto repair shop management software for seamless procurement.
      - name: Fleet Maintenance Automation
        description: Automate parts procurement for fleet vehicles based on maintenance schedules and repair orders.
      - name: Mobile Parts Lookup App
        description: Build mobile applications that allow technicians to look up and order parts from their smartphones.
      - name: Vehicle Repair Platforms
        description: Embed parts catalog and ordering in vehicle repair estimation and diagnostic platforms.
      - name: Loyalty Program Portals
        description: Build custom loyalty dashboards showing Speed Perks points, rewards, and purchase history.
      - name: Inventory Management Systems
        description: Sync Advance Auto Parts catalog data with shop or warehouse inventory management systems.
  - type: Integrations
    data:
      - name: Mitchell 1 ProDemand
        description: Integration with Mitchell 1 shop management and repair information software for parts ordering.
      - name: ALLDATA
        description: Integration with ALLDATA repair information and shop management platform for professional technicians.
      - name: Amazon
        description: Parts available through Amazon marketplace for broader consumer reach.
      - name: AutoZone MOTOR Data
        description: ACES/PIES automotive data standard compatibility for parts catalog interchange.
      - name: DealerSocket
        description: Dealer management system integration for automotive dealership parts departments.
      - name: Shopify
        description: Storefront integration for resellers using Shopify to list Advance Auto Parts products.
description: Advance Auto Parts is a leading automotive aftermarket parts retailer offering a comprehensive catalog of automotive parts, accessories, batteries, and maintenance items. The company serves both professional automotive technicians and do-it-yourself customers across North America through retail stores, online, and commercial delivery programs.
name: Advance Auto Parts
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
created: '2024-01-01'
specificationVersion: '0.19'
tags:
  - Automotive
  - E-Commerce
  - Parts Catalog
  - Retail
  - Supply Chain
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
