---
aid: united-states-department-of-agriculture
url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/apis.yml
apis:
  - aid: united-states-department-of-agriculture:usda-fooddata-central-api
    name: USDA FoodData Central API
    tags:
      - Food
      - Nutrition
      - Agriculture
      - Federal Government
    humanURL: https://fdc.nal.usda.gov/api-guide/
    baseURL: https://api.nal.usda.gov/fdc/v1
    properties:
      - url: https://fdc.nal.usda.gov/api-guide/
        type: Documentation
      - url: https://api.nal.usda.gov/fdc/v1/yaml-spec?api_key=DEMO_KEY
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/openapi/usda-fooddata-central-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/rules/usda-fooddata-central-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/capabilities/food-data-research.yaml
        type: NaftikoCapability
      - url: https://fdc.nal.usda.gov/api-key-signup/
        type: SignUp
    description: The FoodData Central API provides REST access to FoodData Central (FDC), the USDA's integrated data system that provides expanded nutrient profile data and links to related agricultural and experimental research. The API supports food search, nutrient lookup, and retrieval of food details across multiple food data types including Foundation Foods, SR Legacy, FNDDS, Branded Foods, and Experimental Foods.
  - aid: united-states-department-of-agriculture:usda-nass-quickstats-api
    name: USDA NASS Quick Stats API
    tags:
      - Agriculture
      - Statistics
      - Crops
      - Livestock
      - Federal Government
    humanURL: https://quickstats.nass.usda.gov/api
    baseURL: https://quickstats.nass.usda.gov/api
    properties:
      - url: https://quickstats.nass.usda.gov/api
        type: Documentation
      - url: https://www.nass.usda.gov/developer/index.php
        type: Portal
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/openapi/usda-nass-quickstats-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/capabilities/food-data-research.yaml
        type: NaftikoCapability
    description: The USDA NASS Quick Stats API provides direct access to the National Agricultural Statistics Service's official published aggregate estimates related to U.S. agricultural production. Returns data for commodities, categories, and geographic areas, supporting queries on crops, livestock, economics, and demographics with responses in JSON, CSV, or XML formats.
  - aid: united-states-department-of-agriculture:usda-ers-arms-api
    name: USDA ERS ARMS Data API
    tags:
      - Agriculture
      - Economics
      - Farm Management
      - Federal Government
    humanURL: https://www.ers.usda.gov/developer/data-apis/arms-data-api
    baseURL: https://api.ers.usda.gov/data/arms
    properties:
      - url: https://www.ers.usda.gov/developer/data-apis/arms-data-api
        type: Documentation
      - url: https://www.ers.usda.gov/developer/data-apis/
        type: Portal
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/openapi/usda-ers-arms-openapi.yml
        type: OpenAPI
    description: The USDA Economic Research Service (ERS) ARMS Data API provides access to the Agricultural Resource Management Survey (ARMS), covering farm finances, production practices, and resource use for U.S. farms. Supports attribute- based querying of farm income, balance sheet, costs, and production data by year, state, and report type.
  - aid: united-states-department-of-agriculture:usda-nrcs-awdb-api
    name: USDA NRCS AWDB Water and Climate REST API
    tags:
      - Water
      - Climate
      - Snow
      - SNOTEL
      - Federal Government
    humanURL: https://wcc.sc.egov.usda.gov/awdbRestApi/swagger-ui/index.html
    baseURL: https://wcc.sc.egov.usda.gov/awdbRestApi/services/v1
    properties:
      - url: https://wcc.sc.egov.usda.gov/awdbRestApi/swagger-ui/index.html
        type: SwaggerUI
      - url: https://www.nrcs.usda.gov/sites/default/files/2023-03/AWDB%20Web%20Service%20User%20Guide.pdf
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-department-of-agriculture/refs/heads/main/openapi/usda-nrcs-awdb-openapi.yml
        type: OpenAPI
    description: The USDA Natural Resources Conservation Service (NRCS) Air and Water Database (AWDB) REST API provides access to snow, water, and climate data from SNOTEL (SNOw TELemetry) stations and Soil Climate Analysis Network (SCAN) stations. Supports retrieval of daily, monthly, and annual hydrology and climate data for water resource management.
name: United States Department of Agriculture
tags:
  - Federal Government
  - Agriculture
  - Food Safety
  - Nutrition
  - Rural Development
  - Climate
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-05-03'
position: Consuming
description: The United States Department of Agriculture (USDA) is a federal agency responsible for developing and executing policies related to farming, agriculture, forestry, and food. The USDA works to ensure the sustainability and safety of America's food supply, while also supporting rural development and promoting economic growth in rural communities. USDA provides multiple public APIs including FoodData Central for nutrient data, NASS Quick Stats for agricultural statistics, ERS ARMS for farm economics, and NRCS AWDB for water and climate monitoring data.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
