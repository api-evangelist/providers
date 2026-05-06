---
aid: agricultural-statistics-service
url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/apis.yml
name: Agricultural Statistics Service
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Federal Government
  - Statistics
  - Open Data
  - Geospatial
description: The National Agricultural Statistics Service (NASS) is an agency of the United States Department of Agriculture (USDA) whose mission is to support the United States, its agricultural sector, and rural communities by providing accurate, objective, and meaningful statistical information and services. NASS operates the QuickStats API for programmatic access to agricultural survey and census data, as well as geospatial APIs for cropland data, vegetation conditions, and crop moisture monitoring covering the continental United States.
created: '2024-12-03'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agricultural-statistics-service:quickstats-api
    name: USDA NASS QuickStats API
    description: The QuickStats API provides direct programmatic access to the statistical information contained in the NASS Quick Stats database, covering official published aggregate estimates related to U.S. agricultural production. The API supports filtering by commodity, location, and time with comparison operators. Responses are available in JSON, XML, or CSV format. An API key is required; maximum 50,000 records per request.
    humanURL: https://quickstats.nass.usda.gov/api
    baseURL: https://quickstats.nass.usda.gov/api
    tags:
      - Agricultural Statistics
      - Crop Data
      - Livestock Data
      - Census Of Agriculture
      - Open Data
    properties:
      - type: Documentation
        url: https://quickstats.nass.usda.gov/api
      - type: APIReference
        url: https://quickstats.nass.usda.gov/api/#param_define
      - type: Authentication
        url: https://quickstats.nass.usda.gov/api
      - type: OpenAPI
        url: openapi/agricultural-statistics-service-quickstats-api.yaml
      - type: JSONSchema
        url: json-schema/quickstats-api-statistics-record-schema.json
        title: Statistics Record Schema
      - type: JSONSchema
        url: json-schema/quickstats-api-statistics-response-schema.json
        title: Statistics Response Schema
      - type: JSONSchema
        url: json-schema/quickstats-api-count-response-schema.json
        title: Count Response Schema
      - type: JSONStructure
        url: json-structure/quickstats-api-statistics-record-structure.json
        title: Statistics Record Structure
      - type: JSON-LD
        url: json-ld/agricultural-statistics-service-quickstats-api-context.jsonld
  - aid: agricultural-statistics-service:cropland-cros-api
    name: USDA NASS CroplandCROS API
    description: The CroplandCROS API provides access to the Cropland Data Layer (CDL), a crop-specific land cover data layer with 30-meter spatial resolution covering the continental United States. Historical CDL data is available back to 1997 for select states.
    humanURL: https://www.nass.usda.gov/developer/index.php
    baseURL: https://nassgeodata.gmu.edu/CropScapeService
    tags:
      - Cropland
      - Geospatial
      - Remote Sensing
      - Land Cover
    properties:
      - type: Documentation
        url: https://www.nass.usda.gov/developer/index.php
      - type: DataAPI
        url: https://nassgeodata.gmu.edu/CropScapeService
  - aid: agricultural-statistics-service:vegscape-api
    name: USDA NASS VegScape API
    description: The VegScape API delivers vegetation condition indices at 250-meter spatial resolution covering the continental United States. Data includes daily and weekly vegetation index composites available since 2000.
    humanURL: https://www.nass.usda.gov/developer/index.php
    baseURL: https://nassgeodata.gmu.edu/VegScape
    tags:
      - Vegetation
      - Geospatial
      - Crop Monitoring
      - Remote Sensing
    properties:
      - type: Documentation
        url: https://www.nass.usda.gov/developer/index.php
      - type: DataAPI
        url: https://nassgeodata.gmu.edu/VegScape
  - aid: agricultural-statistics-service:crop-casma-api
    name: USDA NASS Crop CASMA API
    description: The Crop CASMA API provides programmatic access to crop vegetation and soil moisture conditions using NASA SMAP and MODIS satellite data for agricultural drought monitoring and crop condition analysis.
    humanURL: https://www.nass.usda.gov/developer/index.php
    baseURL: https://nassgeodata.gmu.edu/CropCASMA
    tags:
      - Soil Moisture
      - Crop Condition
      - Geospatial
      - Drought Monitoring
    properties:
      - type: Documentation
        url: https://www.nass.usda.gov/developer/index.php
      - type: DataAPI
        url: https://nassgeodata.gmu.edu/CropCASMA
common:
  - type: Website
    url: https://www.nass.usda.gov/
  - type: Portal
    url: https://www.nass.usda.gov/developer/index.php
  - type: GitHubOrganization
    url: https://github.com/usda
  - type: TermsOfService
    url: https://www.usda.gov/policies-and-links
  - type: PrivacyPolicy
    url: https://www.usda.gov/privacy-policy
  - type: SpectralRules
    url: rules/agricultural-statistics-service-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/agricultural-statistics-service-vocabulary.yaml
  - type: Features
    data:
      - name: API Key Authentication
        description: All API access requires registration and an API key obtained by agreeing to NASS Terms of Service.
      - name: Multiple Output Formats
        description: The QuickStats API supports JSON, XML, and CSV response formats with optional JSONP callback support.
      - name: Rich Query Operators
        description: Support for comparison operators including GE, LE, GT, LT, NE, LIKE, and NOT_LIKE for flexible data filtering.
      - name: Agricultural Census Data
        description: Access to the complete Census of Agriculture and annual survey estimates covering all major commodity types.
      - name: Geospatial Data Coverage
        description: Geospatial APIs provide 30-meter and 250-meter resolution data layers covering the entire continental United States.
      - name: Historical Time Series
        description: Access to historical agricultural statistics and cropland data extending back to 1997 for select states.
  - type: UseCases
    data:
      - name: Crop Production Analysis
        description: Query crop production estimates by commodity, year, and location for market analysis and supply forecasting.
      - name: Livestock Population Monitoring
        description: Access livestock inventory and production statistics at state and county levels for supply chain planning.
      - name: Geospatial Cropland Mapping
        description: Use the CroplandCROS API to integrate 30-meter resolution cropland data into GIS applications and land use analysis.
      - name: Agricultural Drought Monitoring
        description: Monitor crop condition and soil moisture via the Crop CASMA API to assess drought impacts on agricultural production.
      - name: Agricultural Research
        description: Access the full Quick Stats database for academic research on agricultural trends, productivity, and policy analysis.
      - name: Food Security Assessment
        description: Combine crop production, livestock, and vegetation data to assess regional and national food security conditions.
  - type: Integrations
    data:
      - name: R Package rnassqs
        description: Open-source R package for accessing NASS QuickStats API data directly within R statistical computing environments.
      - name: Python Package usdarnass
        description: Python package providing programmatic access to the USDA NASS QuickStats API for data analysis workflows.
      - name: data.gov Catalog
        description: NASS Quick Stats datasets are cataloged on catalog.data.gov for broader federal data discovery.
      - name: NASA SMAP
        description: Crop CASMA integrates NASA SMAP satellite data for soil moisture monitoring.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
