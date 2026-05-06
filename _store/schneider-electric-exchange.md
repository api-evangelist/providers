---
aid: schneider-electric-exchange
name: Schneider Electric Exchange
description: Schneider Electric Exchange is a developer platform providing APIs for EcoStruxure energy management, building automation, industrial IoT, and commerce partner integrations. The Exchange platform enables partners and developers to build integrations with Schneider Electric products and services. APIs span EcoStruxure data services (IT Expert, Facility Expert, Transformer Expert, Energy Contextualized Data) and Partner Commerce APIs for product catalog, inventory, pricing, orders, quotes, and marketplace integrations. Authentication uses OAuth 2.0 with client credentials for Partner APIs and subscription-based API keys for EcoStruxure data APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Building Automation
  - Commerce APIs
  - EcoStruxure
  - Energy Management
  - Industrial IoT
  - Schneider Electric
url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: schneider-electric-exchange:ecostruxure-it-expert-api
    name: EcoStruxure IT Expert API
    description: The EcoStruxure IT Expert API provides programmatic access to data center infrastructure management data. It enables integrations to query locations, devices, alarms, sensors, and measurements from the EcoStruxure IT cloud platform. Requires an active IT Expert subscription.
    humanURL: https://community.se.com/t5/EcoStruxure-IT-Expert-API/tkb-p/ecostruxure-it-expert-api
    tags:
      - Data Center
      - EcoStruxure IT
      - Infrastructure Monitoring
      - IoT
    properties:
      - type: Documentation
        url: https://community.se.com/t5/EcoStruxure-IT-Expert-API/tkb-p/ecostruxure-it-expert-api
      - type: API Reference
        url: https://api.ecostruxureit.com/rest/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/json-schema/ecostruxure-it-device-schema.json
  - aid: schneider-electric-exchange:ecostruxure-facility-expert-api
    name: EcoStruxure Facility Expert Data API
    description: API providing time series data and alarms access for buildings and equipment monitored by EcoStruxure Facility Expert. Enables facility managers and integrators to retrieve energy measurements, equipment alarms, and historical sensor data.
    humanURL: https://shop.exchange.se.com/en-US/apps/76237/ecostruxure-facility-expert-data-api
    tags:
      - Building Automation
      - EcoStruxure
      - Facility Management
      - Time Series
    properties:
      - type: Documentation
        url: https://exchange.se.com/devportal/api/ecostruxure-facility-expert-data-api
  - aid: schneider-electric-exchange:ecostruxure-energy-contextualized-data-api
    name: EcoStruxure Energy Contextualized Data API
    description: Provides contextualized energy data from EcoStruxure Energy hubs, including consumption metrics, load profiles, and energy optimization data for buildings and industrial sites.
    humanURL: https://exchange.se.com/develop/products/ecostruxure-energy-contextualized-data-api
    tags:
      - EcoStruxure
      - Energy Management
      - Energy Monitoring
      - Sustainability
    properties:
      - type: Documentation
        url: https://exchange.se.com/develop/products/ecostruxure-energy-contextualized-data-api
  - aid: schneider-electric-exchange:ecostruxure-transformer-expert-api
    name: EcoStruxure Transformer Expert Data API
    description: API providing transformer health analytics and monitoring data. Enables integration of transformer assets into enterprise applications, delivering condition monitoring, diagnostics, and predictive maintenance data.
    humanURL: https://exchange.se.com/develop/products/684854/ecostruxure-transformer-expert-data-api
    tags:
      - Asset Management
      - EcoStruxure
      - Industrial IoT
      - Predictive Maintenance
    properties:
      - type: Documentation
        url: https://exchange.se.com/develop/products/684854/ecostruxure-transformer-expert-data-api
  - aid: schneider-electric-exchange:partner-product-catalog-api
    name: Partner Product Catalog API
    description: Provides access to comprehensive technical data for Schneider Electric products from a single source, including product specifications, technical documentation, and ETIM 10.0 classification data.
    humanURL: https://api-explorer.se.com/en/api/product-catalog-v2
    tags:
      - Commerce
      - Partner Integration
      - Product Catalog
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en/api/product-catalog-v2
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/json-schema/partner-product-schema.json
  - aid: schneider-electric-exchange:partner-product-availability-api
    name: Partner Product Availability API
    description: Provides the date when a required quantity of a product can be delivered to a defined address. Queries Schneider Electric's supply chain for delivery lead times by product reference and delivery location.
    humanURL: https://api-explorer.se.com/en/api/product-availability-v2
    tags:
      - Commerce
      - Inventory
      - Partner Integration
      - Supply Chain
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en/api/product-availability-v2
  - aid: schneider-electric-exchange:partner-net-price-api
    name: Partner Net Price API
    description: Provides real-time access to both public list price and personalized net price for Schneider Electric products based on the partner account and standard commercial discounts.
    humanURL: https://api-explorer.se.com/en
    tags:
      - Commerce
      - Partner Integration
      - Pricing
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en
  - aid: schneider-electric-exchange:partner-order-status-api
    name: Partner Order Status API
    description: Provides current order status, shipment schedule, and list of items for orders associated with a registered buying account. Enables distributors to track order fulfillment in real time.
    humanURL: https://api-explorer.se.com/en/api/distributor-order-status-v1.0
    tags:
      - Commerce
      - Order Management
      - Partner Integration
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en/api/distributor-order-status-v1.0
  - aid: schneider-electric-exchange:partner-distributor-quote-api
    name: Partner Distributor Quote API
    description: A read-only service allowing distributors to retrieve quote-lines based on quotes associated with their accounts. Supports the conversion workflow from quote to order in the partner sales process.
    humanURL: https://api-explorer.se.com/en/api/distributor-quote-v1
    tags:
      - Commerce
      - Partner Integration
      - Quotes
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en/api/distributor-quote-v1
  - aid: schneider-electric-exchange:partner-installed-product-api
    name: Partner Installed Product API
    description: Retrieves public information about installed product warranty start and end dates by providing a product serial number. Supports asset lifecycle management and warranty tracking for field-installed equipment.
    humanURL: https://api-explorer.se.com/en/api/Partner-Installed-Product-v1.0
    tags:
      - Asset Management
      - Partner Integration
      - Warranty
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en/api/Partner-Installed-Product-v1.0
  - aid: schneider-electric-exchange:partner-digital-asset-api
    name: Partner Product Digital Asset API
    description: Provides access to product-related digital assets and visualization services including 360-degree image sets and 3D models for Schneider Electric products.
    humanURL: https://api-explorer.se.com/en/api/product-digital-asset-v1
    tags:
      - Commerce
      - Digital Assets
      - Partner Integration
    properties:
      - type: Documentation
        url: https://api-explorer.se.com/en/api/product-digital-asset-v1
common:
  - type: Portal
    url: https://devportal.exchange.se.com/
  - type: Website
    url: https://exchange.se.com/develop
  - type: Partner Portal
    url: https://api-explorer.se.com/en
  - type: Community
    url: https://community.se.com/t5/EcoStruxure-IT-Expert-API/tkb-p/ecostruxure-it-expert-api
  - type: Documentation
    url: https://exchange.se.com/develop
  - type: LinkedIn
    url: https://www.linkedin.com/showcase/schneider-electric-exchange/
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/json-structure/schneider-electric-exchange-api-structure.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/json-ld/schneider-electric-exchange-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/vocabulary/schneider-electric-exchange-vocabulary.yml
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/examples/ecostruxure-it-get-devices-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
