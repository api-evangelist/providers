---
aid: best-buy
url: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/apis.yml
name: Best Buy
tags:
  - Retail
  - Consumer Electronics
  - E-Commerce
  - Products
  - Stores
x-type: company
created: '2026-04-19'
modified: '2026-05-04'
description: Best Buy is a multinational consumer electronics retailer offering technology products, services, and solutions through stores, online, and in-home consultations. Best Buy provides a developer API giving access to product data, store locations, categories, recommendations, open box offers, and commerce capabilities for partners and developers building retail integrations and applications.
apis:
  - aid: best-buy:products-api
    name: Best Buy Products API
    tags:
      - Products
      - Retail
      - Electronics
      - Pricing
      - Inventory
    humanURL: https://bestbuyapis.github.io/api-documentation/#products-api
    properties:
      - type: Documentation
        url: https://bestbuyapis.github.io/api-documentation/#products-api
      - type: OpenAPI
        url: openapi/best-buy-products-api.yaml
    description: Access over one million current and historical Best Buy products with real-time pricing, availability, specifications, images, customer reviews, and categorization data. Supports detailed queries by SKU, keyword search, and filtering across all product attributes.
  - aid: best-buy:stores-api
    name: Best Buy Stores API
    tags:
      - Stores
      - Locations
      - Retail
      - Geolocation
    humanURL: https://bestbuyapis.github.io/api-documentation/#stores-api
    properties:
      - type: Documentation
        url: https://bestbuyapis.github.io/api-documentation/#stores-api
      - type: OpenAPI
        url: openapi/best-buy-stores-api.yaml
    description: Retrieve comprehensive store location and operational data for 1,587+ Best Buy locations across the United States and Puerto Rico. Supports area-based searches by postal code or latitude/longitude, store hours, services, and in-store product availability.
  - aid: best-buy:categories-api
    name: Best Buy Categories API
    tags:
      - Categories
      - Taxonomy
      - Products
    humanURL: https://bestbuyapis.github.io/api-documentation/#categories-api
    properties:
      - type: Documentation
        url: https://bestbuyapis.github.io/api-documentation/#categories-api
    description: Navigate Best Buy's product taxonomy with access to 4,328+ product categories. Browse hierarchical category paths from root to specific categories and integrate with product searches for category-specific filtering.
  - aid: best-buy:recommendations-api
    name: Best Buy Recommendations API
    tags:
      - Recommendations
      - Personalization
      - Products
    humanURL: https://bestbuyapis.github.io/api-documentation/#recommendations-api
    properties:
      - type: Documentation
        url: https://bestbuyapis.github.io/api-documentation/#recommendations-api
      - type: OpenAPI
        url: openapi/best-buy-recommendations-api.yaml
    description: Leverage customer behavior data to surface relevant products through trending products, most viewed, also viewed, also bought, and viewed-ultimately-bought recommendation types. Supports queries by category ID or specific SKU.
  - aid: best-buy:buying-options-api
    name: Best Buy Buying Options (Open Box) API
    tags:
      - Open Box
      - Refurbished
      - Discounts
      - Products
    humanURL: https://bestbuyapis.github.io/api-documentation/#buying-options-api
    properties:
      - type: Documentation
        url: https://bestbuyapis.github.io/api-documentation/#buying-options-api
    description: Access discounted open box and Geek Squad certified refurbished merchandise with ship-from-store fulfillment. Supports single SKU, batch queries up to 100 SKUs, and category-based discovery with condition ratings updated every 5 minutes.
  - aid: best-buy:commerce-api
    name: Best Buy Commerce API
    tags:
      - Commerce
      - Orders
      - Fulfillment
      - Partners
    humanURL: https://bestbuyapis.github.io/api-documentation/#commerce-api
    properties:
      - type: Documentation
        url: https://bestbuyapis.github.io/api-documentation/#commerce-api
    description: Enable integrated shopping experiences for authorized partners with product availability lookups, shipping cost calculations, and order creation supporting store pickup, ship-to-home, and home delivery fulfillment options.
common:
  - type: Website
    url: https://www.bestbuy.com
  - type: DeveloperPortal
    url: https://developer.bestbuy.com
  - type: Documentation
    url: https://bestbuyapis.github.io/api-documentation/
  - type: GettingStarted
    url: https://bestbuyapis.github.io/api-documentation/#user-guide
  - type: Authentication
    url: https://bestbuyapis.github.io/api-documentation/#authorization
  - type: SignUp
    url: https://developer.bestbuy.com
  - type: GitHubOrganization
    url: https://github.com/BestBuyAPIs
  - type: GitHubRepository
    url: https://github.com/BestBuyAPIs/api-documentation
  - type: Features
    data:
      - 'Best Buy: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Best Buy APIs (Products, Stores) are accessible via developer key; commercial use requires partner agreement.
    sources:
      - https://developer.bestbuy.com/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Product Discovery
        description: Full-text search and filtering across product descriptions, specifications, and reviews.
      - name: Inventory Management
        description: Real-time in-store availability checking by postal code or store ID.
      - name: Recommendation Widgets
        description: Display trending, most-viewed, and also-bought products on product detail pages.
      - name: Store Locator
        description: Proximity-based store search with hours verification and service availability.
      - name: Open Box Sourcing
        description: Identify discounted alternatives with transparent condition ratings.
      - name: Price Monitoring
        description: Track product price changes and availability updates.
      - name: Retail Integration
        description: Build shopping experiences integrated with Best Buy's product catalog and fulfillment.
      - name: Affiliate Commerce
        description: Commission-based product recommendations with affiliate partner integration.
  - type: Integrations
    data:
      - name: Postman
        description: Pre-built Postman collection available for testing and exploring Best Buy APIs.
      - name: Impact Affiliate Network
        description: Affiliate commission integration using Impact Partner ID for revenue attribution.
  - type: RateLimits
    url: https://bestbuyapis.github.io/api-documentation/#rate-limiting
  - type: SpectralRules
    url: rules/best-buy-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/retail-discovery.yaml
  - type: Vocabulary
    url: vocabulary/best-buy-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
