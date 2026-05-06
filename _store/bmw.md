---
aid: bmw
name: BMW
description: BMW is a German multinational company specializing in manufacturing luxury vehicles and motorcycles. BMW provides automotive data APIs through the Aftersales Online System (AOS) portal and the BMW Open Data Platform, enabling dealers, repair shops, and developers to access vehicle identification, maintenance, technical campaign, pricing, and diagnostic data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bmw/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Automobiles
  - Cars
  - Vehicles
  - Automotive
  - Connected Car
apis:
  - aid: bmw:vehicle-identification-api
    name: BMW Vehicle Identification API
    description: The BMW Vehicle Identification API allows users to access detailed information about BMW vehicles by inputting their unique vehicle identification number (VIN). Provides essential data about a vehicle's make, model, year, trim level, engine size, transmission type, and technical configuration.
    humanURL: https://aos-portal.bmwgroup.com/basic/ui/#/detail/vehicle-identification
    tags:
      - Automobiles
      - VIN
      - Vehicle Identification
      - Aftersales
    properties:
      - type: Documentation
        url: https://aos-portal.bmwgroup.com/basic/ui/#/detail/vehicle-identification
  - aid: bmw:repair-and-maintenance-api
    name: BMW Repair and Maintenance API
    description: The BMW Repair and Maintenance API provides access to maintenance schedules, diagnostic information, and technical specifications for BMW vehicles. Enables automotive technicians and repair shops to access repair procedures and service requirements programmatically.
    humanURL: https://aos-portal.bmwgroup.com/basic/ui/#/detail/repair-maintenance
    tags:
      - Automobiles
      - Repair
      - Maintenance
      - Diagnostics
      - Aftersales
    properties:
      - type: Documentation
        url: https://aos-portal.bmwgroup.com/basic/ui/#/detail/repair-maintenance
  - aid: bmw:technical-campaign-and-map-status-api
    name: BMW Technical Campaign and Map Status API
    description: The BMW Technical Campaign and Map Status API provides real-time data on the status of technical campaigns and software map updates related to BMW vehicles, including campaign progress, completion timelines, and related announcements.
    humanURL: https://aos-portal.bmwgroup.com/basic/ui/#/detail/technical-campaign-map-status
    tags:
      - Automobiles
      - Technical Campaign
      - Recall
      - Software Update
      - Aftersales
    properties:
      - type: Documentation
        url: https://aos-portal.bmwgroup.com/basic/ui/#/detail/technical-campaign-map-status
  - aid: bmw:flat-rates-api
    name: BMW Flat Rates API
    description: The BMW Flat Rates API provides access to a database of fixed prices for specific services and repairs on BMW vehicles, enabling transparent and standardized pricing for vehicle maintenance and repair operations.
    humanURL: https://aos-portal.bmwgroup.com/basic/ui/#/detail/flatrate
    tags:
      - Automobiles
      - Pricing
      - Flat Rates
      - Repair
      - Aftersales
    properties:
      - type: Documentation
        url: https://aos-portal.bmwgroup.com/basic/ui/#/detail/flatrate
  - aid: bmw:smart-maintenance-api
    name: BMW Smart Maintenance API
    description: The BMW Smart Maintenance API provides real-time vehicle health and maintenance need information by connecting to the vehicle's onboard diagnostic system, monitoring engine performance, tire pressure, and overall vehicle condition.
    humanURL: https://aos-portal.bmwgroup.com/basic/ui/#/detail/smart-Maintenance
    tags:
      - Automobiles
      - Smart Maintenance
      - Diagnostics
      - Connected Car
      - Telematics
    properties:
      - type: Documentation
        url: https://aos-portal.bmwgroup.com/basic/ui/#/detail/smart-Maintenance
  - aid: bmw:bmw-open-data-platform
    name: BMW Open Data Platform
    description: The BMW Open Data Platform provides developers, researchers, and innovators with access to vehicle data including performance metrics, sensor data, and diagnostic information. The platform supports development of applications enhancing the driving experience and vehicle performance optimization.
    humanURL: https://bmw-cardata.bmwgroup.com/thirdparty/public/repair-and-maintenance/technical-configuration/api-documentation
    tags:
      - Automobiles
      - Open Data
      - Connected Car
      - Telematics
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://bmw-cardata.bmwgroup.com/thirdparty/public/repair-and-maintenance/technical-configuration/api-documentation
common:
  - url: https://www.bmw.com
    type: Website
  - url: https://aos.bmwgroup.com/bmw-api
    type: Portal
  - url: https://aos.bmwgroup.com/getting-started
    type: GettingStarted
  - url: https://aos.bmwgroup.com/help/overview
    type: Support
  - url: https://aos.bmwgroup.com/price-list
    type: Pricing
  - url: https://aos.bmwgroup.com/conditions-of-use
    type: TermsOfService
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
