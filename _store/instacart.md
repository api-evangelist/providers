---
aid: instacart
url: https://raw.githubusercontent.com/api-evangelist/instacart/refs/heads/main/apis.yml
modified: '2026-03-20'
apis:
  - aid: instacart:developer-platform-api
    name: Instacart Developer Platform API
    tags:
      - Delivery
      - E-Commerce
      - Grocery
      - Products
      - Recipes
      - Shopping
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://connect.instacart.com
    humanURL: https://docs.instacart.com/developer_platform_api/
    properties:
      - url: https://docs.instacart.com/developer_platform_api/
        type: Documentation
      - type: OpenAPI
        url: openapi/instacart-developer-platform-api-openapi.yml
    description: The Instacart Developer Platform API is a REST-based API that allows app developers to add Instacart shopping capabilities to their websites and applications. It provides endpoints for creating product shopping lists and recipe pages on Instacart Marketplace, enabling users to select a store, add ingredients or products to a cart, and check out.
  - aid: instacart:connect-fulfillment-api
    name: Instacart Connect Fulfillment API
    tags:
      - Delivery
      - E-Commerce
      - Fulfillment
      - Grocery
      - Pickup
      - Retail
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://connect.instacart.com
    humanURL: https://docs.instacart.com/connect/fulfillment/
    properties:
      - url: https://docs.instacart.com/connect/fulfillment/
        type: Documentation
      - type: OpenAPI
        url: openapi/instacart-connect-fulfillment-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/instacart-connect-events-asyncapi.yml
    description: The Instacart Connect Fulfillment API enables retailers to integrate Instacart fulfillment capabilities directly into their e-commerce sites. It combines grocery, delivery, and pickup functionality into a single API, allowing retailers to offer full-service shopping where Instacart shoppers pick items and suggest replacements, as well as same-day or scheduled delivery and pickup options.
  - aid: instacart:connect-post-checkout-api
    name: Instacart Connect Post-Checkout API
    tags:
      - Delivery
      - Fulfillment
      - Orders
      - Retail
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://connect.instacart.com
    humanURL: https://docs.instacart.com/connect/post-checkout/
    properties:
      - url: https://docs.instacart.com/connect/post-checkout/
        type: Documentation
      - type: OpenAPI
        url: openapi/instacart-connect-post-checkout-api-openapi.yml
    description: The Instacart Connect Post-Checkout API allows retailers to provide their customers with real-time order tracking and shopper interaction after an order has been placed. Retailers can use this API to build custom order status pages that display order details, live tracking information, and shopper communication.
  - aid: instacart:catalog-api
    name: Instacart Catalog API
    tags:
      - Catalog
      - E-Commerce
      - Inventory
      - Products
      - Retail
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://connect.instacart.com
    humanURL: https://docs.instacart.com/catalog/catalog_api/overview/
    properties:
      - url: https://docs.instacart.com/catalog/catalog_api/overview/
        type: Documentation
      - type: OpenAPI
        url: openapi/instacart-catalog-api-openapi.yml
    description: The Instacart Catalog API enables retailers to programmatically manage their product catalogs on the Instacart platform. Retailers can use the API to create or update products and items, with partial updates supported so that only the attributes included in the request body are modified.
  - aid: instacart:shopping-widgets
    name: Instacart Shopping Widgets
    tags:
      - Embedding
      - Retail
      - Shopping
      - Web Components
      - Widgets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.instacart.com/widgets/
    properties:
      - url: https://docs.instacart.com/widgets/
        type: Documentation
    description: Instacart Shopping Widgets are front-end web components that retailers can embed into their websites to add e-commerce functionalities powered by Instacart without interacting with any API directly. The widgets enable features such as product search results, cart management, product collections, and user authentication.
common:
  - type: JSON-LD
    url: json-ld/instacart-context.jsonld
  - type: JSONSchema
    url: json-schema/instacart-order-schema.json
  - type: JSONSchema
    url: json-schema/instacart-product-schema.json
description: Use the public Instacart APIs to add Instacart shopping capabilities to your applications, such as product shopping lists and recipe ingredients.
---
