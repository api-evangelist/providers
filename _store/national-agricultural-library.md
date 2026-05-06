---
aid: national-agricultural-library
name: National Agricultural Library
description: The USDA National Agricultural Library houses one of the world's largest collections devoted to agriculture and its related sciences, and operates FoodData Central, an integrated data system providing nutrient profiles for foods.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.nal.usda.gov/
created: '2024-11-21'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Agriculture
  - Federal Government
  - Library
  - Food
  - Nutrition
apis:
  - aid: national-agricultural-library:fooddata-central
    name: USDA FoodData Central API
    description: The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://fdc.nal.usda.gov/api-guide
    baseURL: https://api.nal.usda.gov/fdc/v1
    tags:
      - Food
      - Nutrition
      - Agriculture
      - Open Data
    properties:
      - type: Documentation
        url: https://fdc.nal.usda.gov/api-guide
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/national-agricultural-library/main/openapi/national-agricultural-library-openapi.json
      - type: SignUp
        url: https://fdc.nal.usda.gov/api-key-signup
common:
  - type: Website
    url: https://www.nal.usda.gov/
  - type: Portal
    url: https://fdc.nal.usda.gov/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
