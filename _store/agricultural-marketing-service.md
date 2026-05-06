---
aid: agricultural-marketing-service
url: https://raw.githubusercontent.com/api-evangelist/agricultural-marketing-service/refs/heads/main/apis.yml
name: Agricultural Marketing Service
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Federal Government
  - Market News
  - Livestock
  - Dairy
  - Fruits And Vegetables
  - Cotton
  - Tobacco
description: 'The Agricultural Marketing Service (AMS), an agency of the United States Department of Agriculture (USDA), oversees programs in five commodity areas: cotton and tobacco, dairy, fruits and vegetables, livestock and seeds, and poultry. AMS provides testing, standardization, grading, and market news services. AMS operates several public APIs for agricultural market data including the Market Analysis Reporting System (MARS) API for real-time commodity market news and the Livestock Mandatory Price Reporting System (LMPRS) API for livestock price data.'
created: '2024-11-21'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: USDA AMS MARS API (MyMarketNews)
    description: The Market Analysis Reporting System (MARS) API provides programmatic access to USDA AMS agricultural market news data. The API allows users to automatically pull raw market news data including commodity prices, volume, and trade reports across livestock, dairy, fruits, vegetables, grains, and other agricultural commodities. No API key is required for basic access; registered users can obtain an API key for higher rate limits. Data is available in JSON format. Date ranges are limited to 180 days per request with up to 100,000 records per call.
    humanURL: https://mymarketnews.ams.usda.gov/mymarketnews-api
    baseURL: https://marsapi.ams.usda.gov/services/v1.2
    tags:
      - Market News
      - Commodity Prices
      - Agriculture
      - Livestock
      - Dairy
      - Fruits And Vegetables
    properties:
      - type: Documentation
        url: https://mymarketnews.ams.usda.gov/mymarketnews-api
      - type: GettingStarted
        url: https://mymarketnews.ams.usda.gov/mars-api/getting-started
      - type: Authentication
        url: https://mymarketnews.ams.usda.gov/mymarketnews-api/authentication
      - type: OpenAPI
        url: openapi/agricultural-marketing-service-mars-api.yaml
      - type: JSONSchema
        url: json-schema/mars-api-report-schema.json
        title: Report Schema
      - type: JSONSchema
        url: json-schema/mars-api-report-data-schema.json
        title: Report Data Schema
      - type: JSONSchema
        url: json-schema/mars-api-office-schema.json
        title: Office Schema
      - type: JSONStructure
        url: json-structure/mars-api-report-structure.json
        title: Report Structure
      - type: JSONStructure
        url: json-structure/mars-api-report-data-structure.json
        title: Report Data Structure
      - type: JSON-LD
        url: json-ld/agricultural-marketing-service-mars-api-context.jsonld
  - name: USDA AMS LMPRS API (Livestock Mandatory Price Reporting)
    description: The Livestock Mandatory Price Reporting System (LMPRS) API provides programmatic access to federally mandated livestock price report data. The API requires no authentication for public access and returns JSON data. The LMPRS API covers cattle, hogs, lambs, and other livestock price reporting as required by the Livestock Mandatory Reporting Act.
    humanURL: https://mpr.datamart.ams.usda.gov/
    baseURL: https://mpr.datamart.ams.usda.gov
    tags:
      - Livestock
      - Price Reporting
      - Cattle
      - Hogs
      - Agriculture
    properties:
      - type: Documentation
        url: https://www.ams.usda.gov/sites/default/files/media/USDA_LMPRS_API_User_Guide.pdf
        title: LMPRS API User Guide
      - type: DataAPI
        url: https://mpr.datamart.ams.usda.gov/
  - name: USDA Local Food Directories API
    description: The USDA Local Food Directories API provides data sharing access to directory information for farmers markets, food hubs, on-farm markets, community supported agriculture (CSA) operations, and food cooperatives across the United States.
    humanURL: https://www.usdalocalfoodportal.com/fe/datasharing/
    baseURL: https://www.usdalocalfoodportal.com
    tags:
      - Local Food
      - Farmers Markets
      - Food Hubs
      - CSA
      - Agriculture
    properties:
      - type: Documentation
        url: https://www.usdalocalfoodportal.com/fe/datasharing/
      - type: DataAPI
        url: https://www.usdalocalfoodportal.com/api/
common:
  - type: Website
    url: https://www.ams.usda.gov/
  - type: Portal
    url: https://www.ams.usda.gov/resources/apis-open-data
  - type: GitHubOrganization
    url: https://github.com/usda
  - type: TermsOfService
    url: https://www.usda.gov/policies-and-links
  - type: PrivacyPolicy
    url: https://www.usda.gov/privacy-policy
  - type: SpectralRules
    url: rules/agricultural-marketing-service-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/agricultural-marketing-service-vocabulary.yaml
  - type: Features
    data:
      - name: No Authentication Required
        description: The MARS and LMPRS APIs are publicly accessible without authentication; registered users can obtain API keys for higher rate limits.
      - name: JSON Data Format
        description: All API responses are returned in JSON format including errors and paginated results.
      - name: Real-Time Market News
        description: MARS API provides up-to-date commodity price and volume data as reports are released by AMS market reporters.
      - name: Historical Data Access
        description: Access up to 180 days of historical market data per request with up to 100,000 records returned per call.
      - name: Commodity Coverage
        description: Market data covers livestock, dairy, fruits, vegetables, grains, cotton, tobacco, poultry, and other agricultural commodities.
      - name: Mandatory Price Reporting
        description: LMPRS API provides federally mandated livestock price data under the Livestock Mandatory Reporting Act.
  - type: UseCases
    data:
      - name: Agricultural Price Monitoring
        description: Track commodity prices across livestock, dairy, fruits, and vegetables to support trading, purchasing, and production decisions.
      - name: Market Analysis and Research
        description: Pull historical and current market news data for academic research, economic analysis, and policy work.
      - name: Supply Chain Integration
        description: Integrate USDA market news data into supply chain management and procurement systems for real-time pricing.
      - name: Local Food System Mapping
        description: Use the Local Food Directories API to locate and integrate data about farmers markets, CSAs, and food hubs.
      - name: Commodity Price Alerts
        description: Build automated price monitoring systems using the MARS API to trigger alerts when prices cross defined thresholds.
  - type: Integrations
    data:
      - name: Microsoft Excel
        description: USDA AMS provides guides for integrating MARS API data directly into Microsoft Excel for market analysis.
      - name: api.data.gov
        description: AMS APIs are accessible through the federal api.data.gov gateway for consistent API key management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
