---
aid: bnsf
name: BNSF
description: BNSF Railway, a subsidiary of Berkshire Hathaway Inc., is one of the largest freight railroad networks in North America. The company operates an extensive network of over 32,000 route miles in 28 states and three Canadian provinces, serving major markets in the United States and connecting with Mexico through rail lines in Texas.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bnsf/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Freight
  - Railroad
  - Shipping
  - Trains
  - Intermodal
  - Logistics
apis:
  - aid: bnsf:bnsf-tracing-api
    name: BNSF Tracing API
    description: The BNSF Tracing API provides real-time shipment tracking from origin to destination for automotive VINs, carload railcars, intermodal units, and trains. Supports bulk queries of up to 300 vehicles or units per request with detailed trip plan and event data.
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    tags:
      - Freight
      - Railroad
      - Tracking
      - Tracing
      - Shipping
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
      - type: Portal
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/developers-console/
  - aid: bnsf:bnsf-hub-operations-api
    name: BNSF Hub Operations API
    description: The BNSF Hub Operations API provides access to intermodal facility data including container and trailer delivery details, storage locations, driver pickup and delivery information, dray bookings, gate operations, and unit status for intermodal hubs across the BNSF network.
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    tags:
      - Freight
      - Intermodal
      - Hub
      - Logistics
      - Operations
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
  - aid: bnsf:bnsf-pricing-rates-api
    name: BNSF Pricing & Rates API
    description: The BNSF Pricing & Rates API provides access to freight shipping prices and rates for both carload and intermodal shipments, enabling customers to obtain BNSF shipping costs programmatically.
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    tags:
      - Freight
      - Pricing
      - Rates
      - Shipping
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
  - aid: bnsf:bnsf-schedules-api
    name: BNSF Schedules API
    description: The BNSF Schedules API provides intermodal transit schedules enabling customers to view planned departure and arrival times to help schedule freight shipments across the BNSF rail network.
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    tags:
      - Freight
      - Schedules
      - Transit
      - Intermodal
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
  - aid: bnsf:bnsf-waybill-management-api
    name: BNSF Waybill Management API
    description: The BNSF Waybill Management API enables customers to submit bills of lading with transit details and retrieve submissions for carload shipments. Supports electronic submission and retrieval of waybill documentation for freight management.
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    tags:
      - Freight
      - Waybill
      - Documentation
      - Carload
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
  - aid: bnsf:bnsf-reference-files-api
    name: BNSF Reference Files API
    description: The BNSF Reference Files API provides access to reference data including city names, commodity descriptions (STCC codes), station data, event codes, and hazardous materials information used in freight operations and waybill processing.
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    tags:
      - Freight
      - Reference
      - Data
      - STCC
      - Stations
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
common:
  - type: Website
    url: https://www.bnsf.com
  - type: Portal
    url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
  - type: Documentation
    url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
  - type: DeveloperConsole
    url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/developers-console/
  - type: Support
    url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/support/
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
