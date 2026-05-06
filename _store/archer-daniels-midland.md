---
aid: archer-daniels-midland
name: Archer Daniels Midland
description: Archer Daniels Midland (ADM) is a Fortune 100 global leader in agricultural processing and food ingredient manufacturing, providing nutrition solutions for food, beverage, health, and industrial markets worldwide.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Food Processing
  - Commodities
  - Supply Chain
  - Fortune 100
  - Nutrition
url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: archer-daniels-midland:commodity-data-api
    name: Archer Daniels Midland Commodity Data API
    description: The ADM Commodity Data API represents data integration capabilities for agricultural commodity pricing, supply chain logistics, and product information for partner integrations.
    humanURL: https://www.adm.com/en-us/
    baseURL: https://api.adm.com
    tags:
      - Agriculture
      - Commodities
      - Food Processing
      - Supply Chain
      - Grain
      - Nutrition
    properties:
      - type: Documentation
        url: https://www.adm.com/en-us/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/openapi/archer-daniels-midland-commodity-data-api-openapi.yml
common:
  - type: Portal
    url: https://www.adm.com/en-us/
  - type: Features
    data:
      - name: Commodity Data
        description: Agricultural commodity pricing, market trends, and availability data for corn, soybeans, wheat, and other grains.
      - name: Supply Chain Integration
        description: API integrations for supply chain visibility, logistics, and sourcing of agricultural raw materials.
      - name: Product Catalog
        description: ADM processed food ingredients and agricultural product specifications, nutritional data, and documentation.
      - name: Facility Locations
        description: Global network of processing facilities, grain elevators, and distribution centers.
      - name: Partner Integration
        description: B2B API integrations for key customers and supply chain partners.
  - type: UseCases
    data:
      - name: Commodity Procurement
        description: Automate commodity price tracking and procurement workflows for food manufacturers.
      - name: Supply Chain Visibility
        description: Integrate ADM supply chain data with enterprise ERP and logistics systems.
      - name: Food Ingredient Sourcing
        description: Search and source ADM processed food ingredients for product development.
      - name: Risk Management
        description: Access commodity pricing and market trend data for agricultural commodity risk management.
  - type: Integrations
    data:
      - name: SAP
        description: Integration with SAP ERP for procurement, supply chain, and financial management.
      - name: Oracle
        description: Oracle ERP integration for commodity trading and logistics management.
      - name: CME Group
        description: Integration with commodity futures and options data from CME Group.
      - name: Bloomberg
        description: Commodity market data integration with Bloomberg terminal services.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/rules/archer-daniels-midland-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/vocabulary/archer-daniels-midland-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/archer-daniels-midland/refs/heads/main/json-ld/archer-daniels-midland-commodity-data-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
