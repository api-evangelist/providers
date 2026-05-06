---
aid: fatsecret
name: FatSecret
description: FatSecret is a global nutrition and wellness platform whose Platform API exposes a verified database of more than 1.9 million foods across 56 countries, plus recipes, exercises, and user-scoped food diary, exercise diary, and weight tracking. The API is used by more than 35,000 developers and serves over 700 million calls per month.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
specificationVersion: '0.19'
tags:
  - Barcode Scanning
  - Calories
  - Diets
  - Exercise
  - Fitness
  - Food Diary
  - Health
  - Macronutrients
  - Nutrition
  - Recipes
  - Weight Tracking
url: https://raw.githubusercontent.com/api-evangelist/fatsecret/refs/heads/main/apis.yml
apis:
  - aid: fatsecret:platform-api
    name: FatSecret Platform API
    description: Utilized by more than 35,000 developers supporting in excess of 700 million API calls every month for over 1.9 million verified food items, FatSecret's Platform API is the largest data set of global food nutrition information for more than 56 countries. It supports food and recipe search, barcode scanning, image recognition, natural language processing, custom foods, food diary, exercise diary, saved meals, and weight tracking.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://platform.fatsecret.com/rest
    humanURL: https://platform.fatsecret.com/platform-api
    tags:
      - Barcode Scanning
      - Calories
      - Diets
      - Exercise
      - Food Diary
      - Health
      - Nutrition
      - Recipes
      - Weight Tracking
    properties:
      - type: Documentation
        url: https://platform.fatsecret.com/platform-api
      - type: Guides
        url: https://platform.fatsecret.com/docs/guides
      - type: OpenAPI
        url: openapi/fatsecret-platform-openapi.yml
      - type: JSONSchema
        url: json-schema/fatsecret-food-schema.json
      - type: JSONSchema
        url: json-schema/fatsecret-recipe-schema.json
      - type: JSONSchema
        url: json-schema/fatsecret-food-entry-schema.json
common:
  - type: Website
    url: https://platform.fatsecret.com/
  - type: Documentation
    url: https://platform.fatsecret.com/platform-api
  - type: Sign Up
    url: https://platform.fatsecret.com/registration
  - type: Guides
    url: https://platform.fatsecret.com/docs/guides
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
