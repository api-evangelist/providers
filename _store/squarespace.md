---
aid: squarespace
name: Squarespace
description: Squarespace is an all-in-one website building and e-commerce platform that enables individuals and businesses to create, manage, and scale their online presence. Squarespace provides a suite of Commerce APIs for developers to build integrations managing products, orders, inventory, customer profiles, transactions, and webhook notifications. All APIs use HTTPS REST conventions with API key or OAuth authentication.
image: https://static1.squarespace.com/static/ta/5134cbefe4b0c6fb04df8065/10007/assets/logomark.svg
url: https://www.squarespace.com
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: Squarespace Commerce API
    description: The Squarespace Commerce API provides programmatic access to the commerce features of a Squarespace merchant site. It enables developers to manage products, process orders, track inventory, access customer profiles, retrieve financial transactions, and configure webhook subscriptions. All endpoints use HTTPS and follow REST principles.
    humanUrl: https://developers.squarespace.com/commerce-apis/overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - Commerce
      - E-Commerce
      - REST API
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/commerce-apis/overview
      - type: OpenAPI
        url: openapi/squarespace-commerce-api-openapi.yml
      - type: Authentication
        url: https://developers.squarespace.com/commerce-apis/making-requests
      - type: SpectralRules
        url: rules/squarespace-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/commerce-management.yaml
      - type: NaftikoCapabilities
        url: capabilities/customer-and-reporting.yaml
      - type: JSONLD
        url: json-ld/squarespace-context.jsonld
      - type: Vocabulary
        url: vocabulary/squarespace-vocabulary.yml
  - name: Squarespace Orders API
    description: The Squarespace Orders API provides access to order history for a Squarespace merchant site, supporting both one-time purchases and subscription orders. Developers can retrieve, create, and manage orders, as well as import orders from third-party sales channels into Squarespace.
    humanUrl: https://developers.squarespace.com/commerce-apis/orders-overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - Commerce
      - Orders
      - REST API
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/commerce-apis/orders-overview
      - type: OpenAPI
        url: openapi/squarespace-orders-api-openapi.yml
  - name: Squarespace Products API
    description: The Squarespace Products API allows developers to manage the product catalog of a Squarespace merchant site. It supports physical products, service products, gift cards, and digital downloads, along with their images and variants.
    humanUrl: https://developers.squarespace.com/commerce-apis/products-overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - Commerce
      - Products
      - REST API
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/commerce-apis/products-overview
      - type: OpenAPI
        url: openapi/squarespace-products-api-openapi.yml
  - name: Squarespace Inventory API
    description: The Squarespace Inventory API enables developers to retrieve and update inventory quantities for product variants on a Squarespace merchant site. It supports bulk inventory queries and individual variant stock management.
    humanUrl: https://developers.squarespace.com/commerce-apis/inventory-overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - Commerce
      - Inventory
      - REST API
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/commerce-apis/inventory-overview
      - type: OpenAPI
        url: openapi/squarespace-inventory-api-openapi.yml
  - name: Squarespace Profiles API
    description: The Squarespace Profiles API allows reading customer profiles, mailing list subscribers, and donors for a Squarespace site. It supports filtering by profile type and retrieving individual profile details.
    humanUrl: https://developers.squarespace.com/commerce-apis/profiles-overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - CRM
      - Customer Profiles
      - REST API
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/commerce-apis/profiles-overview
      - type: OpenAPI
        url: openapi/squarespace-profiles-api-openapi.yml
  - name: Squarespace Transactions API
    description: The Squarespace Transactions API provides access to financial transaction records for a Squarespace merchant site. Developers can retrieve transaction history, including payment amounts, fees, and associated order or subscription references.
    humanUrl: https://developers.squarespace.com/commerce-apis/transactions-overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - Commerce
      - Finance
      - Transactions
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/commerce-apis/transactions-overview
      - type: OpenAPI
        url: openapi/squarespace-transactions-api-openapi.yml
  - name: Squarespace Webhook Subscriptions API
    description: The Squarespace Webhook Subscriptions API allows developers to manage webhook endpoint subscriptions for a merchant site. It supports creating, listing, updating, and deleting subscriptions that trigger notifications for order events, extension uninstalls, and other commerce activities.
    humanUrl: https://developers.squarespace.com/webhooks/overview
    baseUrl: https://api.squarespace.com/1.0
    tags:
      - Webhooks
      - Event Notifications
      - REST API
    properties:
      - type: Documentation
        url: https://developers.squarespace.com/webhooks/overview
      - type: OpenAPI
        url: openapi/squarespace-webhook-subscriptions-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/squarespace-webhooks-asyncapi.yml
common:
  - type: Website
    url: https://www.squarespace.com
  - type: DeveloperPortal
    url: https://developers.squarespace.com
  - type: Documentation
    url: https://developers.squarespace.com/commerce-apis/overview
  - type: APIKeys
    url: https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys
  - type: TermsOfService
    url: https://www.squarespace.com/terms-of-service
  - type: PrivacyPolicy
    url: https://www.squarespace.com/privacy
  - type: StatusPage
    url: https://status.squarespace.com
  - type: Blog
    url: https://www.squarespace.com/blog
maintainers:
  - name: Squarespace Developer Support
    url: https://developers.squarespace.com
tags:
  - Commerce
  - E-Commerce
  - Marketing
  - Payments
  - Retail
  - Website Builder
  - Webhooks
---
