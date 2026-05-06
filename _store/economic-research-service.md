---
aid: economic-research-service
name: Economic Research Service
description: The Economic Research Service (ERS) is a division of the United States Department of Agriculture (USDA) that conducts economic research and analysis related to agriculture, food, and rural development. ERS provides policymakers, stakeholders, and the public with valuable information and data to help inform decision-making and policy development.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Economics
  - Federal Government
  - Research
url: https://www.ers.usda.gov/
created: '2024-12-25'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: economic-research-service:ers-data-apis
    name: USDA ERS Data APIs
    description: Access ERS data products in machine-readable formats for analysis or integration into your own applications. Delivered via api.data.gov as REST endpoints. Requires an api.data.gov key.
    humanURL: https://www.ers.usda.gov/developer/data-apis
    baseURL: https://api.ers.usda.gov
    tags:
      - Agriculture
      - Data
      - Economics
    properties:
      - url: https://www.ers.usda.gov/developer/data-apis
        type: Documentation
      - url: https://api.data.gov/signup/
        type: SignUp
  - aid: economic-research-service:ers-geospatial-apis
    name: USDA ERS Geospatial APIs
    description: Integrate ERS map layers into the GIS package of your choice, on their own or mashed up with other geospatial data.
    humanURL: https://www.ers.usda.gov/developer/geospatial-apis
    baseURL: https://www.ers.usda.gov
    tags:
      - Agriculture
      - Geospatial
      - GIS
    properties:
      - url: https://www.ers.usda.gov/developer/geospatial-apis
        type: Documentation
common:
  - type: Website
    url: https://www.ers.usda.gov/
  - type: Documentation
    url: https://www.ers.usda.gov/developer/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
