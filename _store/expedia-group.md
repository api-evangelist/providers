---
aid: expedia-group
name: Expedia Group
description: Expedia Group is an American travel technology company that owns and operates travel fare aggregators and travel metasearch engines, including Expedia, Hotels.com, Vrbo, Travelocity, Hotwire.com, Orbitz, Ebookers, CheapTickets, CarRentals.com, and Trivago. Their developer platform provides APIs for travel inventory, lodging, and analytics.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Flights
  - Hotels
  - Lodging
  - Travel
url: https://developers.expediagroup.com/docs/
created: '2024-06-07'
modified: '2026-05-04'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: expedia-group:rapid
    name: Expedia Rapid API
    description: Expedia Rapid provides access to Expedia Group's hotel inventory, rates, and availability for booking integration.
    humanURL: https://developers.expediagroup.com/docs/products/rapid
    tags:
      - Availability
      - Hotels
      - Rates
    properties:
      - type: Documentation
        url: https://developers.expediagroup.com/docs/products/rapid
      - type: OpenAPI
        url: openapi/expedia-rapid-openapi-original.yml
  - aid: expedia-group:fraud-protection
    name: Expedia Fraud Protection API
    description: API for fraud prevention and protection services within the Expedia Group platform.
    humanURL: https://developers.expediagroup.com/docs/products/fraud-prevention
    tags:
      - Fraud
      - Security
    properties:
      - type: Documentation
        url: https://developers.expediagroup.com/docs/products/fraud-prevention
      - type: OpenAPI
        url: openapi/expedia-fraud-protection-openapi-original.yml
  - aid: expedia-group:lodging
    name: Expedia Lodging API
    description: API for lodging supply and property management within the Expedia Group partner network.
    humanURL: https://developers.expediagroup.com/supply/lodging
    tags:
      - Hotels
      - Lodging
      - Property Management
    properties:
      - type: Documentation
        url: https://developers.expediagroup.com/supply/lodging
      - type: OpenAPI
        url: openapi/expedia-lodging-product-openapi-original.yml
  - aid: expedia-group:deposit
    name: Expedia EPS Deposit API
    description: The EPS Deposit API manages the deposit policy for a property, offering operations to create, update, read, and delete deposit policies for Expedia partner properties.
    humanURL: https://expediaconnectivity.com/developer
    tags:
      - Deposit
      - Lodging
      - Property Management
    properties:
      - type: Documentation
        url: https://expediaconnectivity.com/developer
      - type: OpenAPI
        url: openapi/expedia-deposit-openapi-original.yml
  - aid: expedia-group:loyalty
    name: Expedia Loyalty Earn API
    description: The Loyalty Earn API provides access to loyalty earn transactions across configurable date ranges, returning sorted transaction data for membership programs.
    humanURL: https://developers.expediagroup.com/analytics
    tags:
      - Analytics
      - Loyalty
      - Transactions
    properties:
      - type: Documentation
        url: https://developers.expediagroup.com/analytics
      - type: OpenAPI
        url: openapi/expedia-loyalty-openapi-original.yml
common:
  - type: Portal
    url: https://developers.expediagroup.com/docs/
  - type: SDKs
    url: https://developers.expediagroup.com/docs/sdk
  - type: Blog
    url: https://medium.com/expedia-group-tech
  - type: Support
    url: https://developers.expediagroup.com/docs/support
  - type: Status
    url: https://status.developers.expediagroup.com/
  - type: Features
    data:
      - 'Expedia Group: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Expedia Group Rapid API (formerly EAN) and Partner Central require commercial agreements.
    sources:
      - https://developers.expediagroup.com/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
