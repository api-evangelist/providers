---
aid: fedex
name: FedEx
description: FedEx is a logistics company that provides shipping and delivery services worldwide. They offer a range of solutions for individuals and businesses, including express shipping, freight services, and e-commerce fulfillment. FedEx publishes a suite of REST APIs covering tracking, shipping, rating, address validation, pickup, locator, trade documents, and post-shipment visibility through their developer portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-04'
position: Consumer
tags:
  - Address Validation
  - Freight
  - Logistics
  - Pickup
  - Rating
  - Shipping
  - Tracking
  - Webhooks
url: https://raw.githubusercontent.com/api-evangelist/fedex/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fedex:track
    name: FedEx Track API
    description: Track API allows customers and partners to retrieve up-to-the-minute package and shipment status, scan events, delivery details, and proof of delivery using tracking numbers, reference numbers, or TCN.
    humanURL: https://developer.fedex.com/api/en-us/catalog/track/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Tracking
      - Shipping
      - Logistics
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/track/v1/docs.html
      - type: Getting Started
        url: https://developer.fedex.com/api/en-us/get-started.html
  - aid: fedex:ship
    name: FedEx Ship API
    description: Ship API lets developers create domestic and international shipments, generate shipping labels, validate addresses, schedule pickups, and manage end-to-end shipment workflows programmatically.
    humanURL: https://developer.fedex.com/api/en-us/catalog/ship/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Shipping
      - Labels
      - Logistics
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/ship/v1/docs.html
  - aid: fedex:rate
    name: FedEx Rate API
    description: Rate API returns rate quotes and transit times for FedEx Express, Ground, Freight, and SmartPost services so applications can present pricing and delivery options at checkout or during fulfillment.
    humanURL: https://developer.fedex.com/api/en-us/catalog/rate/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Rating
      - Shipping
      - Pricing
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/rate/v1/docs.html
  - aid: fedex:address-validation
    name: FedEx Address Validation API
    description: Address Validation API verifies postal addresses for deliverability, classifies them as residential or commercial, and corrects common formatting and spelling issues prior to shipment creation.
    humanURL: https://developer.fedex.com/api/en-us/catalog/address-validation/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Address Validation
      - Shipping
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/address-validation/v1/docs.html
  - aid: fedex:pickup
    name: FedEx Pickup API
    description: Pickup API provides programmatic access to schedule, modify, and cancel package pickups, and to determine pickup availability for a given origin and service combination.
    humanURL: https://developer.fedex.com/api/en-us/catalog/pickup/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Pickup
      - Shipping
      - Logistics
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/pickup/v1/docs.html
  - aid: fedex:locations
    name: FedEx Locations API
    description: Locations API helps applications find FedEx Office, FedEx Ship Center, drop boxes, and authorized ship centers near a given address or coordinate, including hours of operation and supported services.
    humanURL: https://developer.fedex.com/api/en-us/catalog/locations/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Locations
      - Shipping
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/locations/v1/docs.html
  - aid: fedex:authorization
    name: FedEx Authorization API
    description: Authorization API issues OAuth 2.0 access tokens used to authenticate all other FedEx API calls. Tokens are obtained via client credentials generated from a FedEx Developer Portal project.
    humanURL: https://developer.fedex.com/api/en-us/catalog/authorization/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Authentication
      - OAuth
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/authorization/v1/docs.html
  - aid: fedex:shipment-visibility-webhook
    name: FedEx Shipment Visibility Webhook
    description: Shipment Visibility Webhook pushes near real-time tracking events to a registered HTTPS endpoint, eliminating the need to repeatedly poll the Track API for shipment status changes.
    humanURL: https://developer.fedex.com/api/en-us/catalog/svm/v1/docs.html
    baseURL: https://apis.fedex.com
    tags:
      - Webhooks
      - Tracking
      - Shipping
    properties:
      - type: Documentation
        url: https://developer.fedex.com/api/en-us/catalog/svm/v1/docs.html
common:
  - type: Website
    url: https://www.fedex.com/
  - type: Documentation
    url: https://developer.fedex.com/api/en-us/home.html
  - type: Getting Started
    url: https://developer.fedex.com/api/en-us/get-started.html
  - type: Catalog
    url: https://developer.fedex.com/api/en-us/catalog.html
  - type: Sign Up
    url: https://developer.fedex.com/api/en-us/home.html
  - type: Features
    data:
      - 'FedEx: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - FedEx Developer Portal APIs (Ship, Rate, Track, Address Validation) require an account; rates vary by ship date / weight / zone.
    sources:
      - https://developer.fedex.com/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
