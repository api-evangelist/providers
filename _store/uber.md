---
aid: uber
url: https://raw.githubusercontent.com/api-evangelist/uber/refs/heads/main/apis.yml
apis:
  - aid: uber:uber-riders
    name: Uber Riders API
    tags:
      - Ride-Sharing
      - Rides
      - Products
      - Estimates
      - Transportation
    humanURL: https://developer.uber.com/docs/riders/introduction
    baseURL: https://api.uber.com/v1.2
    properties:
      - url: https://developer.uber.com/docs/riders/references/api
        type: Documentation
      - url: https://developer.uber.com/docs/riders/ride-requests/introduction
        type: Documentation
      - url: openapi/uber-riders-openapi.yml
        type: OpenAPI
      - url: examples/uber-riders-list-products-example.json
        type: Example
      - url: examples/uber-riders-create-ride-request-example.json
        type: Example
      - url: json-schema/uber-ride-request-schema.json
        type: JSONSchema
    description: The Uber Riders API enables applications to interact with the Uber platform on behalf of riders. It allows requesting rides, getting product listings, price and time estimates, viewing trip history, and managing saved places. Authentication uses OAuth 2.0 bearer tokens.
  - aid: uber:uber-drivers
    name: Uber Drivers API
    tags:
      - Drivers
      - Ride-Sharing
      - Payments
      - Trips
      - Transportation
    humanURL: https://developer.uber.com/docs/drivers/introduction
    baseURL: https://api.uber.com/v1
    properties:
      - url: https://developer.uber.com/docs/drivers/references/api
        type: Documentation
      - url: openapi/uber-drivers-openapi.yml
        type: OpenAPI
    description: The Uber Drivers API allows partners to access driver profile information, payment history, and trip records. It provides access to driver earnings, completed trips, and partner program data via OAuth 2.0 bearer tokens.
  - aid: uber:uber-eats
    name: Uber Eats API
    tags:
      - Food Delivery
      - Restaurants
      - Orders
      - Menus
      - Delivery
    humanURL: https://developer.uber.com/docs/eats/introduction
    baseURL: https://api.uber.com/v1
    properties:
      - url: https://developer.uber.com/docs/eats/introduction
        type: Documentation
      - url: https://developer.uber.com/docs/eats/api-change-log
        type: ChangeLog
      - url: openapi/uber-eats-openapi.yml
        type: OpenAPI
      - url: examples/uber-eats-get-order-example.json
        type: Example
    description: The Uber Eats Marketplace API enables partners to programmatically manage stores, menus, and orders on the Uber Eats platform. It supports real-time menu synchronization, order processing, store operations, promotional campaigns, and analytics reporting. Access requires written approval from Uber.
  - aid: uber:uber-direct
    name: Uber Direct API
    tags:
      - Delivery
      - Courier
      - Logistics
      - Fulfillment
    humanURL: https://developer.uber.com/docs/deliveries/overview
    baseURL: https://api.uber.com/v1
    properties:
      - url: https://developer.uber.com/docs/deliveries/overview
        type: Documentation
      - url: openapi/uber-direct-openapi.yml
        type: OpenAPI
      - url: examples/uber-direct-create-delivery-example.json
        type: Example
      - url: json-schema/uber-delivery-schema.json
        type: JSONSchema
    description: The Uber Direct API allows merchants to leverage Uber's courier network to deliver their orders. It supports on-demand delivery creation, courier tracking, refunds, and location management. Webhooks provide real-time delivery status, courier updates, and shopping progress notifications.
  - aid: uber:uber-guest-rides
    name: Uber Guest Rides API
    tags:
      - Ride-Sharing
      - Guest
      - Trips
      - Transportation
    humanURL: https://developer.uber.com/docs/guest-rides/introduction
    baseURL: https://api.uber.com/v1
    properties:
      - url: https://developer.uber.com/docs/guest-rides/introduction
        type: Documentation
      - url: https://developer.uber.com/docs/guest-rides/about/u4b-api-introduction
        type: Documentation
    description: The Uber Guest Rides API enables businesses to allow their users to request rides from Uber without requiring an Uber account. Uses OAuth 2.0 with the guest.rides scope for authentication.
  - aid: uber:uber-vouchers
    name: Uber Vouchers API
    tags:
      - Vouchers
      - Promotions
      - Incentives
      - Codes
    humanURL: https://developer.uber.com/docs/vouchers/introduction
    baseURL: https://api.uber.com/v1
    properties:
      - url: https://developer.uber.com/docs/vouchers/introduction
        type: Documentation
      - url: openapi/uber-vouchers-openapi.yml
        type: OpenAPI
    description: The Uber Vouchers API allows businesses to create and manage voucher programs and codes for rides and meals. It supports program creation, code generation, bulk distribution, guest management, and code redemption workflows.
  - aid: uber:uber-businesses
    name: Uber for Business API
    tags:
      - Business
      - Enterprise
      - Receipts
      - Trips
      - Expenses
    humanURL: https://developer.uber.com/docs/businesses/introduction
    baseURL: https://api.uber.com/v1.2
    properties:
      - url: https://developer.uber.com/docs/businesses/introduction
        type: Documentation
      - url: https://developer.uber.com/docs/businesses/receipts/references/api
        type: Documentation
      - url: openapi/uber-businesses-openapi.yml
        type: OpenAPI
    description: The Uber for Business API enables organizations to automate workflows within their enterprise Uber accounts. Provides access to trip invoices, receipts, and business travel data for expense management and reporting.
name: Uber
tags:
  - Ride-Sharing
  - Rides
  - Taxis
  - Transportation
  - Food Delivery
  - Delivery
  - Logistics
type: Index
properties:
  - url: rules/uber-rules.yml
    type: SpectralRules
  - url: vocabulary/uber-vocabulary.yml
    type: Vocabulary
  - url: json-ld/uber-context.jsonld
    type: JSONLDContext
  - url: capabilities/ride-management.yaml
    type: NaftikoCapabilities
  - url: capabilities/food-and-delivery.yaml
    type: NaftikoCapabilities
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-05-03'
position: Consumer
description: Uber is a global technology platform offering transportation, food delivery, and logistics services. Its developer platform provides APIs for integrating ride requests, food ordering, on-demand delivery, voucher programs, and business travel management into third-party applications. APIs use OAuth 2.0 authentication with scope-based access controls and support both production and sandbox environments.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
