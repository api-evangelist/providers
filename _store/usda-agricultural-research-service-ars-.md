---
aid: usda-agricultural-research-service-ars-
url: https://raw.githubusercontent.com/api-evangelist/usda-agricultural-research-service-ars-/refs/heads/main/apis.yml
apis:
  - aid: usda-agricultural-research-service-ars-:fooddata-central-api
    name: USDA FoodData Central API
    tags:
      - Food Data
      - Nutrition
      - Agriculture
      - Federal Government
      - Open Data
    humanURL: https://fdc.nal.usda.gov/api-guide/
    properties:
      - url: https://fdc.nal.usda.gov/api-guide/
        type: Documentation
      - url: https://fdc.nal.usda.gov/portal-data/external/apispec
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/usda-agricultural-research-service-ars-/refs/heads/main/openapi/usda-ars-fooddata-central-openapi.yml
        type: OpenAPI
    description: The USDA FoodData Central (FDC) API provides access to an integrated data system containing extended nutritional and food component data for thousands of foods. Data types include Foundation Foods, SR Legacy, Survey Foods (FNDDS), Branded Foods, and Experimental Foods. Requires a free data.gov API key.
  - aid: usda-agricultural-research-service-ars-:ag-data-commons-ckan-api
    name: USDA Ag Data Commons CKAN API
    tags:
      - Agricultural Research
      - Open Data
      - Datasets
      - CKAN
      - Federal Government
    humanURL: https://agdatacommons.nal.usda.gov
    properties:
      - url: https://agdatacommons.nal.usda.gov
        type: Portal
      - url: https://data.nal.usda.gov/about-ag-data-commons
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/usda-agricultural-research-service-ars-/refs/heads/main/openapi/usda-ars-ag-data-commons-openapi.yml
        type: OpenAPI
    description: The USDA Ag Data Commons is a DKAN/CKAN-based open data repository for USDA agricultural research datasets. The API provides metadata search and retrieval for datasets from ARS national programs including genomics, crop science, soil health, animal production, and more. No authentication required for read access.
name: USDA Agricultural Research Service (ARS)
tags:
  - Federal Government
  - Agriculture
  - Food Safety
  - Nutrition
  - Open Data
  - Research
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-05-03'
position: Consuming
description: The USDA Agricultural Research Service (ARS) is the principal in-house research agency of the US Department of Agriculture. ARS conducts research to develop and implement solutions to agricultural problems that affect Americans every day. Research areas include crop protection, animal health, food safety, natural resource management, sustainable agriculture, and nutrition. ARS provides public data access through FoodData Central (nutrition data) and the Ag Data Commons (agricultural research datasets repository with CKAN/DKAN API).
features:
  - Food Nutrition Data (FoodData Central)
  - Agricultural Research Datasets (Ag Data Commons)
  - Germplasm Resources (GRIN)
  - Plant Variety Protection
  - Soil Health Data
  - Genomics and Bioinformatics Tools
useCases:
  - Nutrition research and dietary analysis
  - Food labeling and composition analysis
  - Agricultural research data discovery
  - Plant genetics and germplasm research
  - Food safety assessment
  - Sustainable agriculture research
  - Climate and soil health monitoring
integrations:
  - data.gov
  - Ag Data Commons
  - FoodData Central
solutions:
  - Food and Nutrition Research
  - Agricultural Data Discovery
  - Crop and Animal Genetics Research
github:
  - https://github.com/USDA-ARS
  - https://github.com/usda-ars-gbru
  - https://github.com/usda-ars-nwrc
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
