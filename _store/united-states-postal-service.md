---
name: United States Postal Service
description: The United States Postal Service (USPS) provides a modern REST API platform at developers.usps.com that gives ecommerce websites, shipping software, and logistics systems access to postal data and services. APIs cover address validation, package tracking, domestic and international shipping labels, pricing, carrier pickup scheduling, location finding, and Informed Delivery campaign management. The legacy Web Tools platform was retired January 25, 2026, with all functionality migrated to the new OAuth 2.0-secured API platform.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/united-states-postal-service/refs/heads/main/apis.yml
created: 2024/01/01
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Government
  - Postal Service
  - Shipping
  - Logistics
  - Address Validation
  - Package Tracking
apis:
  - name: USPS Addresses API
    description: Validates and corrects address information to USPS specifications, eliminating errors and improving package delivery. Supports full address standardization, city and state lookup by ZIP Code, and ZIP Code lookup by address.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/addressesv3
    baseURL: https://apis.usps.com
    tags:
      - Addresses
      - Address Validation
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/addressesv3
      - type: OpenAPI
        url: openapi/united-states-postal-service-addresses-openapi.yml
      - type: JSONSchema
        url: json-schema/addresses-address-schema.json
        title: Address Schema
      - type: JSONSchema
        url: json-schema/addresses-city-state-schema.json
        title: City State Schema
      - type: JSONStructure
        url: json-structure/addresses-address-structure.json
        title: Address Structure
      - type: JSON-LD
        url: json-ld/united-states-postal-service-addresses-context.jsonld
      - type: Example
        url: examples/addresses-address-example.json
        title: Address Example
    aid: united-states-postal-service:usps-addresses-api
  - name: USPS Tracking API
    description: Returns tracking status and related details for a given USPS package, including scan events with date, time, and location. Supports single and batch package tracking. Version 3.2 includes enhanced scan event extract notifications.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/trackingv3r2
    baseURL: https://apis.usps.com
    tags:
      - Tracking
      - Package Tracking
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/trackingv3r2
      - type: OpenAPI
        url: openapi/united-states-postal-service-tracking-openapi.yml
      - type: JSONSchema
        url: json-schema/tracking-tracking-event-schema.json
        title: Tracking Event Schema
      - type: JSONStructure
        url: json-structure/tracking-tracking-event-structure.json
        title: Tracking Event Structure
      - type: JSON-LD
        url: json-ld/united-states-postal-service-tracking-context.jsonld
      - type: Example
        url: examples/tracking-tracking-event-example.json
        title: Tracking Event Example
    aid: united-states-postal-service:usps-tracking-api
  - name: USPS Domestic Prices API
    description: Provides postage pricing for domestic USPS shipments based on origin and destination ZIP Codes, weight, dimensions, and mail class. Supports base rate lookups, extra service rates (insurance, signature confirmation, etc.), and total rate calculations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/domesticpricesv3
    baseURL: https://apis.usps.com
    tags:
      - Pricing
      - Postage
      - Shipping
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/domesticpricesv3
      - type: OpenAPI
        url: openapi/united-states-postal-service-domestic-prices-openapi.yml
      - type: JSONSchema
        url: json-schema/domestic-prices-base-rate-request-schema.json
        title: Base Rate Request Schema
      - type: JSONStructure
        url: json-structure/domestic-prices-base-rate-request-structure.json
        title: Base Rate Request Structure
      - type: JSON-LD
        url: json-ld/united-states-postal-service-domestic-context.jsonld
      - type: Example
        url: examples/domestic-prices-base-rate-request-example.json
        title: Base Rate Request Example
    aid: united-states-postal-service:usps-domestic-prices-api
  - name: USPS Carrier Pickup API
    description: Enables free carrier pickup scheduling for next-day service, Monday through Saturday, excluding federal holidays. Supports creating, retrieving, updating, and canceling pickup requests at residential and commercial addresses.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/carrierpickupv3
    baseURL: https://apis.usps.com
    tags:
      - Carrier Pickup
      - Shipping
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/carrierpickupv3
      - type: OpenAPI
        url: openapi/united-states-postal-service-carrier-pickup-openapi.yml
      - type: JSONSchema
        url: json-schema/carrier-pickup-pickup-request-schema.json
        title: Pickup Request Schema
      - type: JSONStructure
        url: json-structure/carrier-pickup-pickup-request-structure.json
        title: Pickup Request Structure
      - type: JSON-LD
        url: json-ld/united-states-postal-service-carrier-context.jsonld
      - type: Example
        url: examples/carrier-pickup-pickup-request-example.json
        title: Pickup Request Example
    aid: united-states-postal-service:usps-carrier-pickup-api
  - name: USPS International Prices API
    description: Provides pricing for international USPS products based on shipment characteristics including destination country, weight, dimensions, and service class.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/internationalpricesv3
    baseURL: https://apis.usps.com
    tags:
      - International
      - Pricing
      - Postage
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/internationalpricesv3
    aid: united-states-postal-service:usps-international-prices-api
  - name: USPS Domestic Labels API
    description: Creates domestic shipping labels with barcodes in multiple formats and generates Shipping Services Files. Requires USPS Ship enrollment and Enterprise Payment Account.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/domesticlabelsv3
    baseURL: https://apis.usps.com
    tags:
      - Labels
      - Shipping
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/domesticlabelsv3
    aid: united-states-postal-service:usps-domestic-labels-api
  - name: USPS International Labels API
    description: Creates international shipping labels and generates required Shipping Services Files for customs compliance.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/internationallabelsv3
    baseURL: https://apis.usps.com
    tags:
      - International
      - Labels
      - Shipping
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/internationallabelsv3
    aid: united-states-postal-service:usps-international-labels-api
  - name: USPS Locations API
    description: Identifies drop-off facilities and destination entry points for various USPS services. Supports post office locator and drop-off location finder.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/locationsv3
    baseURL: https://apis.usps.com
    tags:
      - Locations
      - Post Offices
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/locationsv3
    aid: united-states-postal-service:usps-locations-api
  - name: USPS Service Standards API
    description: Provides delivery benchmarks showing expected transit times between origin and destination ZIP Codes for USPS mail classes.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/standardsv3
    baseURL: https://apis.usps.com
    tags:
      - Service Standards
      - Delivery
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/standardsv3
    aid: united-states-postal-service:usps-service-standards-api
  - name: USPS Shipping Options API
    description: Returns a comprehensive list of pricing, service standards, and shipping options for USPS products in a single API call, eliminating the need to query multiple APIs separately.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/shippingoptionsv3
    baseURL: https://apis.usps.com
    tags:
      - Shipping
      - Pricing
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/shippingoptionsv3
    aid: united-states-postal-service:usps-shipping-options-api
  - name: USPS SCAN Forms API
    description: Links multiple domestic and international labels through a single electronic file number, creating Shipment Confirmation Acceptance Notice forms for batch shipping operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/scanv3
    baseURL: https://apis.usps.com
    tags:
      - SCAN Forms
      - Shipping
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/scanv3
    aid: united-states-postal-service:usps-scan-forms-api
  - name: USPS OAuth API
    description: Industry-standard OAuth 2.0 Client Credentials authentication protecting access to all USPS APIs. Returns Bearer Tokens used in the Authorization header for all USPS API calls.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.usps.com/Oauth
    baseURL: https://apis.usps.com
    tags:
      - Authentication
      - OAuth
      - Government
    properties:
      - type: Documentation
        url: https://developers.usps.com/Oauth
      - type: Authentication
        url: https://developers.usps.com/getting-started
    aid: united-states-postal-service:usps-oauth-api
common:
  - type: Portal
    url: https://developers.usps.com/
  - type: GettingStarted
    url: https://developers.usps.com/getting-started
  - type: Documentation
    url: https://developers.usps.com/apis
  - type: TermsOfService
    url: https://developers.usps.com/terms-and-conditions
  - type: FAQ
    url: https://developers.usps.com/faq
  - type: Support
    url: https://emailus.usps.com/s/web-tools-inquiry
  - type: GitHubOrganization
    url: https://github.com/USPS
  - type: GitHubRepository
    url: https://github.com/USPS/api-examples
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Secure API access using industry-standard OAuth 2.0 Client Credentials flow with Bearer Token authentication.
      - name: RESTful Architecture
        description: All APIs follow RESTful conventions with JSON request and response bodies.
      - name: Sandbox Testing Environment
        description: Testing Environment for Mailers (TEM) at apis-tem.usps.com for safe API testing before going to production.
      - name: Address Standardization
        description: USPS Coding Accuracy Support System (CASS) compliant address validation and standardization.
      - name: Delivery Point Validation
        description: DPV confirmation codes ensure packages can be delivered to the validated address.
      - name: Real-Time Tracking
        description: Live package tracking with scan events, timestamps, and location details from USPS systems.
      - name: Webhook Subscriptions
        description: Event-driven subscription APIs for tracking events, adjustments, and disputes delivered via webhooks.
      - name: Batch Processing
        description: Support for bulk operations including multiple tracking lookups and SCAN Form generation.
  - type: UseCases
    data:
      - name: E-Commerce Shipping Integration
        description: Calculate shipping rates, generate labels, and provide package tracking directly within e-commerce checkout flows.
      - name: Address Verification at Checkout
        description: Validate and standardize customer addresses during checkout to reduce failed deliveries and return rates.
      - name: Shipping Label Generation
        description: Programmatically create domestic and international USPS shipping labels with barcodes for fulfillment operations.
      - name: Carrier Pickup Automation
        description: Schedule and manage USPS carrier pickups automatically based on order fulfillment triggers.
      - name: Logistics Rate Shopping
        description: Compare USPS service options and pricing to select the most cost-effective shipping method.
      - name: Delivery Time Estimation
        description: Display accurate expected delivery dates to customers using USPS service standards data.
      - name: Post Office Finder
        description: Help customers locate the nearest USPS facility for drop-offs or in-person services.
      - name: Informed Delivery Campaigns
        description: Enhance customer engagement by adding digital content to mail pieces viewed through Informed Delivery.
  - type: Integrations
    data:
      - name: Shopify
        description: USPS shipping integration available through Shopify Shipping for label generation and rate calculation.
      - name: WooCommerce
        description: WooCommerce shipping plugins integrate USPS APIs for rate calculation and label printing.
      - name: Magento
        description: Adobe Commerce and Magento integrate USPS for shipping rate display and fulfillment.
      - name: ShipStation
        description: ShipStation multi-carrier shipping platform integrates USPS APIs for ecommerce fulfillment.
      - name: EasyPost
        description: EasyPost shipping API aggregator provides access to USPS services alongside other carriers.
      - name: Stamps.com
        description: Stamps.com and Pitney Bowes shipping platforms integrate USPS APIs for postage and label printing.
  - type: SpectralRules
    url: rules/united-states-postal-service-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/ecommerce-shipping.yaml
    title: E-Commerce Shipping
  - type: NaftikoCapability
    url: capabilities/package-tracking.yaml
    title: Package Tracking
  - type: Vocabulary
    url: vocabulary/united-states-postal-service-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
aid: united-states-postal-service
---
