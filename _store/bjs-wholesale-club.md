---
aid: bjs-wholesale-club
url: https://raw.githubusercontent.com/api-evangelist/bjs-wholesale-club/refs/heads/main/apis.yml
name: BJ's Wholesale Club
description: BJ's Wholesale Club is a leading operator of membership warehouse clubs concentrated primarily on the eastern half of the United States. BJ's offers its members significant savings on a wide assortment of merchandise, including fresh foods, groceries, household essentials, and general merchandise. The company operates over 230 clubs and is focused on digital transformation, offering APIs to partners for product data, inventory, pricing, and order management integrations.
tags:
  - Ecommerce
  - Membership
  - Retail
  - Wholesale
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2026-03-21'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: bjs-wholesale-club:bjs-wholesale-club
    name: BJ's Wholesale Club API
    description: BJ's Wholesale Club provides partner and affiliate integrations enabling access to product catalog, pricing, inventory availability, membership verification, and order management capabilities. Integrations are available through their partner program and digital commerce platform.
    humanURL: https://www.bjs.com
    tags:
      - Ecommerce
      - Membership
      - Retail
      - Wholesale
    properties:
      - type: Documentation
        url: https://www.bjs.com
      - type: OpenAPI
        url: openapi/bjs-wholesale-club-openapi.yaml
      - type: JSONSchema
        url: json-schema/bjs-product-schema.json
      - type: JSONSchema
        url: json-schema/bjs-membership-schema.json
      - type: JSONSchema
        url: json-schema/bjs-order-schema.json
      - type: JSONStructure
        url: json-structure/bjs-product-structure.json
      - type: JSONStructure
        url: json-structure/bjs-membership-structure.json
      - type: JSONStructure
        url: json-structure/bjs-order-structure.json
      - type: JSONLD
        url: json-ld/bjs-context.jsonld
      - type: Example
        url: examples/bjs-product-example.json
      - type: Example
        url: examples/bjs-membership-example.json
      - type: Example
        url: examples/bjs-order-example.json
      - type: PrivacyPolicy
        url: https://www.bjs.com/content/privacy-policy
      - type: TermsOfService
        url: https://www.bjs.com/content/terms-and-conditions
common:
  - type: Website
    url: https://www.bjs.com
  - type: PrivacyPolicy
    url: https://www.bjs.com/content/privacy-policy
  - type: TermsOfService
    url: https://www.bjs.com/content/terms-and-conditions
  - type: SignUp
    url: https://www.bjs.com/content/membership
  - type: Support
    url: https://www.bjs.com/content/help-center
  - type: SpectralRules
    url: rules/bjs-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/bjs-wholesale-club.yaml
  - type: Vocabulary
    url: vocabulary/bjs-vocabulary.yaml
  - type: Features
    data:
      - name: Membership Management
        description: Supports membership-based access model for in-club and online purchasing, including membership verification and renewal.
      - name: Product Catalog
        description: Broad product assortment including fresh foods, groceries, household essentials, electronics, and general merchandise available via digital commerce integrations.
      - name: Digital Commerce
        description: Online ordering and delivery capabilities integrating with BJ's digital platform for partner fulfillment and affiliate programs.
      - name: Curbside Pickup
        description: Buy Online, Pick Up In Club capabilities available through BJ's digital platform for member convenience.
      - name: Inventory Availability
        description: Real-time inventory status across BJ's club locations, supporting in-club and curbside pickup fulfillment routing.
      - name: Club Locator
        description: Find BJ's club locations by ZIP code with hours, services, and amenities including gas stations, optical, and tire centers.
  - type: UseCases
    data:
      - name: Affiliate Marketing
        description: Partner programs enabling affiliate marketers to promote BJ's membership and products with commission-based compensation.
      - name: Product Data Integration
        description: Access product catalog and pricing data to enable comparison shopping and product listing integrations.
      - name: Membership Verification
        description: Verify BJ's membership status for partner benefits and co-branded programs.
      - name: Order Management
        description: Manage orders through BJ's digital commerce platform for dropship and fulfillment partnerships.
      - name: Inventory Routing
        description: Route orders to the nearest club with available inventory for curbside pickup or local delivery fulfillment.
  - type: Integrations
    data:
      - name: Commission Junction
        description: BJ's affiliate program is managed through CJ Affiliate (Commission Junction) for tracking and payments.
      - name: Google Shopping
        description: Product feeds integrated with Google Shopping for product discovery and advertising.
      - name: Instacart
        description: BJ's grocery delivery is available through the Instacart platform for same-day delivery to members.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
