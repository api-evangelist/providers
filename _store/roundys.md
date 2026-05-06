---
aid: roundys
name: Roundy's
description: 'Roundy''s, Inc. is a Midwest grocery retailer and wholly-owned subsidiary of The Kroger Co., founded in Milwaukee, Wisconsin in 1872. Roundy''s operates approximately 150 grocery stores under three retail banners: Pick ''n Save (106 locations throughout Wisconsin), Metro Market (premium Wisconsin grocery stores), and Mariano''s (44 Fresh Market locations throughout the Chicago area). As a Kroger subsidiary, Roundy''s leverages the Kroger developer platform and technology infrastructure including the Kroger API for product catalog, digital coupons, store locations, and loyalty program integrations.'
type: Index
url: https://raw.githubusercontent.com/api-evangelist/roundys/refs/heads/main/apis.yml
tags:
  - Grocery
  - Kroger
  - Midwest
  - Retail
  - Supermarket
  - Wisconsin
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: roundys:kroger-product-catalog-api
    name: Kroger Product Catalog API
    description: As a Kroger subsidiary, Roundy's stores (Pick 'n Save, Metro Market, Mariano's) are accessible through the Kroger Developer Platform product catalog API. The API enables searching and browsing products by keyword, brand, UPC, or department, and retrieving pricing, availability, and location-specific inventory data for Roundy's banner stores.
    humanURL: https://developer.kroger.com/reference/
    properties:
      - type: Documentation
        url: https://developer.kroger.com/reference/
      - type: OpenAPI
        url: https://developer.kroger.com/assets/files/Kroger-API-Spec-23c0b0b34f55c3d32d60fcb23de33a86.yaml
    tags:
      - Grocery
      - Inventory
      - Product Catalog
      - Retail
  - aid: roundys:kroger-stores-api
    name: Kroger Store Locator API
    description: The Kroger Store Locator API allows developers to find Pick 'n Save, Metro Market, and Mariano's store locations by geographic coordinates, ZIP code, or radius. Returns store details including address, hours, departments, phone number, and available services (pharmacy, fuel, click-and-collect).
    humanURL: https://developer.kroger.com/reference/
    properties:
      - type: Documentation
        url: https://developer.kroger.com/reference/
    tags:
      - Grocery
      - Location
      - Retail
      - Store Locator
  - aid: roundys:kroger-cart-api
    name: Kroger Cart and Checkout API
    description: The Kroger Cart API allows authenticated customers to add items directly to their Pick 'n Save, Metro Market, or Mariano's shopping cart for in-store pickup or delivery. Supports product quantity management and shopping list integrations through the Kroger customer identity platform.
    humanURL: https://developer.kroger.com/reference/
    properties:
      - type: Documentation
        url: https://developer.kroger.com/reference/
    tags:
      - Cart
      - Checkout
      - Grocery
      - Retail
      - Shopping
  - aid: roundys:kroger-identity-api
    name: Kroger Identity and Loyalty API
    description: The Kroger Identity API provides OAuth 2.0-based authentication for Kroger customers including Roundy's banner shoppers, enabling access to customer profiles, Plus Card loyalty data, digital coupons, purchase history, and personalized offers.
    humanURL: https://developer.kroger.com/reference/
    properties:
      - type: Documentation
        url: https://developer.kroger.com/reference/
    tags:
      - Authentication
      - Grocery
      - Identity
      - Loyalty
      - OAuth
common:
  - type: Website
    url: https://www.roundys.com
  - type: Pick n Save
    url: https://www.picknsave.com
  - type: Metro Market
    url: https://www.metromarket.net
  - type: Marianos
    url: https://www.marianos.com
  - type: Kroger Developer Platform
    url: https://developer.kroger.com/
  - type: Vocabulary
    url: vocabulary/roundys-vocabulary.yml
  - type: JSON-LD
    url: json-ld/roundys-context.jsonld
  - type: JSONSchema
    url: json-schema/roundys-store-schema.json
  - type: JSONStructure
    url: json-structure/roundys-store-structure.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
