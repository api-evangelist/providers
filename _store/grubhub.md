---
aid: grubhub
url: https://raw.githubusercontent.com/api-evangelist/grubhub/refs/heads/main/apis.yml
modified: '2026-04-28'
apis:
  - aid: grubhub:menu-api
    name: Grubhub Menu API
    tags:
      - Food Delivery
      - Menus
      - Online Ordering
      - Restaurants
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.grubhub.com
    humanURL: https://developer.grubhub.com/api/menu
    properties:
      - url: https://developer.grubhub.com/api/menu
        type: Documentation
      - url: openapi/grubhub-menu-openapi.yml
        type: OpenAPI
    description: The Grubhub Menu API enables partners and merchants to create, update, and manage restaurant menus within the Grubhub Marketplace. It supports building normalized menu structures including categories, items, modifiers, and pricing. POS integrations are required to sync menus through this API, ensuring that restaurant offerings on Grubhub stay current with their local menu changes.
  - aid: grubhub:orders-api
    name: Grubhub Orders API
    tags:
      - Food Delivery
      - Online Ordering
      - Orders
      - Restaurants
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.grubhub.com
    humanURL: https://developer.grubhub.com/api/orders
    properties:
      - url: https://developer.grubhub.com/api/orders
        type: Documentation
      - url: openapi/grubhub-orders-openapi.yml
        type: OpenAPI
      - url: asyncapi/grubhub-order-events-asyncapi.yml
        type: AsyncAPI
    description: The Grubhub Orders API allows partners to receive, manage, and update order statuses for restaurant orders placed through the Grubhub Marketplace. When a customer places an order, Grubhub sends it to the partner's endpoint via webhook subscription. Partners can confirm orders, update preparation status, mark orders as ready for pickup, and track delivery progress through defined order lifecycle states.
  - aid: grubhub:merchant-data-api
    name: Grubhub Merchant Data API
    tags:
      - Data Management
      - Food Delivery
      - Merchants
      - Restaurants
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.grubhub.com
    humanURL: https://developer.grubhub.com/api/merchant-data
    properties:
      - url: https://developer.grubhub.com/api/merchant-data
        type: Documentation
      - url: openapi/grubhub-merchant-data-openapi.yml
        type: OpenAPI
    description: The Grubhub Merchant Data API provides endpoints for managing merchant information, including store details, tax rates, fulfillment settings, and configuration groups. Partners can retrieve all Grubhub locations associated with a merchant's account, update merchant profiles, and manage operational settings. This API is essential for maintaining accurate restaurant data across the Grubhub platform.
  - aid: grubhub:merchant-schedules-api
    name: Grubhub Merchant Schedules API
    tags:
      - Availability
      - Food Delivery
      - Restaurants
      - Scheduling
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.grubhub.com
    humanURL: https://developer.grubhub.com/docs/6uXmPesMoYmoV6jZx6lVfa/checking-merchant-availability
    properties:
      - url: https://developer.grubhub.com/docs/6uXmPesMoYmoV6jZx6lVfa/checking-merchant-availability
        type: Documentation
      - url: openapi/grubhub-merchant-schedules-openapi.yml
        type: OpenAPI
    description: The Grubhub Merchant Schedules API allows partners to manage restaurant operating hours and availability on the Grubhub Marketplace. It supports setting regular business hours, temporary closures, and special holiday schedules. Partners can check merchant availability status and update schedules to ensure customers see accurate ordering windows for each restaurant location.
  - aid: grubhub:deliveries-api
    name: Grubhub Deliveries API
    tags:
      - Delivery Tracking
      - Drivers
      - Food Delivery
      - Logistics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.grubhub.com
    humanURL: https://developer.grubhub.com/docs/2xRv0wZtNljuMTpizzNqD2/interacting-with-drivers
    properties:
      - url: https://developer.grubhub.com/docs/2xRv0wZtNljuMTpizzNqD2/interacting-with-drivers
        type: Documentation
      - url: openapi/grubhub-deliveries-openapi.yml
        type: OpenAPI
      - url: asyncapi/grubhub-delivery-events-asyncapi.yml
        type: AsyncAPI
    description: The Grubhub Deliveries API enables partners to manage delivery logistics and interact with Grubhub's nationwide courier network. It provides delivery status tracking through key states including driver assignment, pickup ready, and out for delivery. Partners can leverage Grubhub Connect, a full-service delivery solution for delivery aggregators, marketplaces, and enterprise merchants to fulfill orders using Grubhub drivers.
  - aid: grubhub:onboarding-api
    name: Grubhub Onboarding API
    tags:
      - Food Delivery
      - Integration
      - Merchants
      - Onboarding
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.grubhub.com
    humanURL: https://developer.grubhub.com/api/onboarding
    properties:
      - url: https://developer.grubhub.com/api/onboarding
        type: Documentation
      - url: openapi/grubhub-onboarding-openapi.yml
        type: OpenAPI
    description: The Grubhub Onboarding API enables partners to offer self-service integration onboarding directly to their merchants using OAuth-based authentication. It provides endpoints for new merchant referrals, merchant activation and deactivation, merchant association, and reporting onboarding issues. The API can reduce merchant onboarding time from 7-10 days down to as little as 5-10 minutes, significantly decreasing integration downtime.
common:
  - type: JSON-LD
    url: json-ld/grubhub-context.jsonld
  - type: JSONSchema
    url: json-schema/grubhub-order-schema.json
  - type: JSONSchema
    url: json-schema/grubhub-menu-schema.json
  - type: JSONSchema
    url: json-schema/grubhub-merchant-schema.json
description: Grubhub works with brands, point of sale companies, and online ordering providers to power an ordering experience in Grubhub Marketplace and within restaurant-branded web experiences. This documentation describes the normalized endpoints required for ingesting menu content and facilitating order transmission.
---
