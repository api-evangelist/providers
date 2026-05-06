---
aid: toyota
url: https://raw.githubusercontent.com/api-evangelist/toyota/refs/heads/main/apis.yml
apis:
  - aid: toyota:toyota-vehicle
    name: Toyota Vehicle API
    tags:
      - Automotive
      - Vehicles
      - Connected Car
      - Vehicle Lifecycle
      - Dealer
    humanURL: https://developer.eig.toyota.com/apis/vehicle
    properties:
      - url: https://developer.eig.toyota.com/apis/vehicle
        type: Documentation
      - url: openapi/toyota-vehicle-openapi.yml
        type: OpenAPI
    description: Toyota Vehicle API provides lifecycle information for vehicles from initial order through retail sale. Enables dealers, fleet managers, and authorized business partners to access vehicle inventory, order status, and vehicle configuration data for Toyota North America vehicles.
  - aid: toyota:toyota-telematics
    name: Toyota Telematics API
    tags:
      - Automotive
      - Telematics
      - Connected Car
      - Fleet Management
      - Vehicle Health
    humanURL: https://developer.eig.toyota.com/apis/telematics
    properties:
      - url: https://developer.eig.toyota.com/apis/telematics
        type: Documentation
      - url: openapi/toyota-telematics-openapi.yml
        type: OpenAPI
    description: Toyota Telematics API provides details related to connected services, satellite radio subscriptions, and vehicle health data for enrolled vehicles based on Unit ID or VIN. Supports fleet management, rental car operations, and telematics insurance use cases.
  - aid: toyota:toyota-connected-services
    name: Toyota Connected Services API
    tags:
      - Automotive
      - Connected Car
      - Remote Control
      - Vehicle Status
      - EV
    humanURL: https://developer.eig.toyota.com/
    properties:
      - url: https://developer.eig.toyota.com/
        type: Documentation
      - url: openapi/toyota-connected-services-openapi.yml
        type: OpenAPI
    description: Toyota Connected Services API enables authorized applications to access real-time vehicle status, remote control features, location data, electric vehicle charging status, climate control, and trip history for Toyota and Lexus connected vehicles.
  - aid: toyota:toyota-dealers
    name: Toyota Dealers API
    tags:
      - Automotive
      - Dealers
      - Dealer Locator
      - Service
      - Inventory
    humanURL: https://developer-sb.eig.toyota.com/apis/dealer
    properties:
      - url: https://developer-sb.eig.toyota.com/apis/dealer
        type: Documentation
    description: Toyota Dealers API enables searching and retrieving dealer information including location, hours, services offered, and inventory. Supports dealer locator applications and service scheduling integrations for Toyota and Lexus dealers.
common:
  - type: Website
    url: https://developer.eig.toyota.com/
  - type: Developer
    url: https://developer.eig.toyota.com/
  - type: Documentation
    url: https://developer.eig.toyota.com/apis
  - type: LinkedIn
    url: https://www.linkedin.com/company/toyota-motor-corporation
  - type: Rules
    url: rules/toyota-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/toyota-vocabulary.yml
  - type: JSONLDContext
    url: json-ld/toyota-context.jsonld
name: Toyota
tags:
  - Automobiles
  - Cars
  - Vehicles
  - Connected Car
  - Telematics
  - Fleet Management
  - Electric Vehicles
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-25'
modified: '2026-05-03'
position: Consumer
description: Toyota Motor Corporation is a Japanese multinational automotive manufacturer that designs, manufactures, and sells vehicles, including cars, trucks, and buses. Founded in 1937, Toyota has become one of the largest automakers in the world, known for its reliability, innovation, and commitment to sustainability. Toyota's developer platform (developer.eig.toyota.com) provides APIs for vehicle lifecycle management, telematics and connected services, dealer data, and fleet management for business partners, dealers, fleet operators, and developers building mobility applications. Toyota's product lineup includes hybrids like the Prius, trucks like the Tacoma, and EVs including the bZ4X.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
