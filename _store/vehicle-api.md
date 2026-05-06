---
aid: vehicle-api
name: Vehicle API
description: The Vehicle API by Edmunds provides comprehensive access to automotive datasets covering vehicle makes, models, trims, specs, media, pricing (TMV), incentives, dealer information, and reviews. Enables developers to build automotive shopping tools, vehicle configurators, and consumer research applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - Cars
  - Edmunds
  - Pricing
  - Vehicles
url: https://raw.githubusercontent.com/api-evangelist/vehicle-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
created: '2025-01-07'
modified: '2026-05-03'
apis:
  - aid: vehicle-api:vehicle-api
    name: Vehicle API (Edmunds)
    description: The Edmunds Vehicle API provides access to a comprehensive automotive data platform including vehicle makes, models, trims, configurations, specifications, media (photos and videos), True Market Value (TMV) pricing, dealer inventories, incentives, reviews, and consumer ratings. Ideal for building automotive shopping tools, vehicle comparison engines, and dealer management systems.
    humanURL: https://developer.edmunds.com/api-documentation/vehicle/
    tags:
      - Automotive
      - Cars
      - Edmunds
      - Pricing
      - Vehicles
    properties:
      - type: Documentation
        url: https://developer.edmunds.com/api-documentation/vehicle/
      - type: Portal
        url: https://developer.edmunds.com/
      - type: Reference
        url: https://developer.edmunds.com/api-documentation/vehicle/
      - type: Authentication
        url: https://developer.edmunds.com/api-documentation/overview/
      - type: OpenAPI
        url: openapi/vehicle-api-openapi.yml
      - type: JSONSchema
        url: json-schema/vehicle-api-make-schema.json
        title: Vehicle Make Schema
      - type: JSONSchema
        url: json-schema/vehicle-api-model-schema.json
        title: Vehicle Model Schema
      - type: JSONSchema
        url: json-schema/vehicle-api-style-schema.json
        title: Vehicle Style Schema
      - type: JSONSchema
        url: json-schema/vehicle-api-price-schema.json
        title: Vehicle Price Schema
      - type: JSONStructure
        url: json-structure/vehicle-api-make-structure.json
        title: Vehicle Make Structure
      - type: JSONStructure
        url: json-structure/vehicle-api-model-structure.json
        title: Vehicle Model Structure
      - type: Example
        url: examples/vehicle-api-make-example.json
        title: Vehicle Make Example
      - type: Example
        url: examples/vehicle-api-style-example.json
        title: Vehicle Style Example
common:
  - type: Website
    url: https://developer.edmunds.com/
  - type: Portal
    url: https://developer.edmunds.com/
  - type: Documentation
    url: https://developer.edmunds.com/api-documentation/vehicle/
  - type: Authentication
    url: https://developer.edmunds.com/api-documentation/overview/
  - type: GettingStarted
    url: https://developer.edmunds.com/api-documentation/overview/
  - type: Support
    url: https://developer.edmunds.com/support/
  - type: SpectralRules
    url: rules/vehicle-api-spectral-rules.yml
    title: Vehicle API Spectral Rules
  - type: Vocabulary
    url: vocabulary/vehicle-api-vocabulary.yml
    title: Vehicle API Vocabulary
  - type: NaftikoCapability
    url: capabilities/vehicle-data.yaml
    title: Vehicle Data
  - type: Features
    data:
      - name: Vehicle Make and Model Data
        description: Comprehensive database of vehicle makes, models, and trim levels with OEM specifications, features, and configuration options.
      - name: True Market Value Pricing
        description: Edmunds TMV pricing data including new vehicle suggested retail, invoice prices, and used vehicle values by condition and mileage.
      - name: Vehicle Media
        description: Photo and video assets for vehicle makes, models, and trims including exterior, interior, color swatch, and 360-degree images.
      - name: Dealer Inventory
        description: Real-time dealer inventory search with make, model, year, zip code, radius, and price range filtering.
      - name: Incentives and Rebates
        description: Manufacturer incentives, rebates, financing offers, and lease programs by vehicle, region, and customer type.
      - name: Vehicle Reviews and Ratings
        description: Edmunds editorial reviews and consumer ratings for vehicle models including performance, comfort, value, and reliability scores.
  - type: UseCases
    data:
      - name: Automotive Shopping Tools
        description: Build vehicle search and comparison tools that let consumers filter by make, model, year, price, and features with TMV pricing guidance.
      - name: Dealer Management Systems
        description: Power dealer websites and CRM systems with accurate vehicle specs, pricing, and inventory data synced from Edmunds.
      - name: Vehicle Configurator
        description: Enable consumers to build and price vehicles with available trims, packages, options, and colors with live pricing calculations.
      - name: Used Car Valuation
        description: Integrate used vehicle pricing into trade-in calculators, appraisal tools, and consumer value estimators using TMV data.
  - type: Integrations
    data:
      - name: AutoTrader
        description: Cross-reference vehicle listings with AutoTrader inventory using Edmunds vehicle identifiers and specs for consistent data.
      - name: Cars.com
        description: Combine Edmunds vehicle data with Cars.com listings for enriched consumer shopping experiences.
      - name: Dealer CRM Systems
        description: Integrate vehicle specs and pricing into Salesforce, CDK, and Reynolds and Reynolds dealer management systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
