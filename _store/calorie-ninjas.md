---
aid: calorie-ninjas
url: https://raw.githubusercontent.com/api-evangelist/calorie-ninjas/refs/heads/main/apis.yml
name: CalorieNinjas
tags:
  - Beverages
  - Foods
  - Image Recognition
  - Nutrition
  - Recipes
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-03-30'
modified: '2026-04-23'
position: Consumer
description: CalorieNinjas provides an easy, free Nutrition Facts and Recipe API. Developers can retrieve nutrition information for over 100,000 foods and beverages using natural language queries, extract nutrition information from images of food-related text (menus, recipes, food journals), and search recipes matching search queries. All endpoints use a simple API key authentication model via the X-Api-Key header.
apis:
  - aid: calorie-ninjas:calorieninjas
    name: CalorieNinjas API
    tags:
      - Beverages
      - Foods
      - Image Recognition
      - Nutrition
      - Recipes
    baseURL: https://api.calorieninjas.com/v1
    humanURL: https://calorieninjas.com/api
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - url: https://calorieninjas.com/api
        type: Documentation
      - url: openapi/calorieninjas-openapi.yml
        type: OpenAPI
      - url: openapi/calorieninjas-openapi-review.yml
        type: Review
    description: 'The CalorieNinjas API returns nutrition and recipe data for 100,000+ foods and beverages. It offers three endpoints: GET /nutrition for natural-language nutrition lookups (returns calories, macros, vitamins, and minerals), POST /imagetextnutrition for extracting nutrition from images containing food/beverage text, and GET /recipe for searching recipes with titles, ingredients, servings, and instructions. All requests authenticate with an API key sent in the X-Api-Key header.'
common:
  - type: Portal
    url: https://calorieninjas.com/
  - type: Documentation
    url: https://calorieninjas.com/api
  - type: Login
    url: https://calorieninjas.com/signin
  - type: Sign Up
    url: https://calorieninjas.com/register
  - type: Terms of Service
    url: https://calorieninjas.com/tos
  - type: Privacy Policy
    url: https://calorieninjas.com/privacy
  - type: Pricing
    url: https://calorieninjas.com/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
