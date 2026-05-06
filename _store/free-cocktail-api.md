---
aid: free-cocktail-api
name: Free Cocktail API
description: The Free Cocktail API is a resource that provides access to a vast database of cocktail recipes, ingredients, and images.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-07'
modified: '2026-04-28'
position: Consumer
tags:
  - Beverages
  - Cocktails
  - Drinks
  - Ingredients
  - Recipes
url: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: free-cocktail-api:free-cocktail-api
    name: Free Cocktail API
    tags:
      - Beverages
      - Cocktails
      - Drinks
      - Ingredients
      - Recipes
    humanURL: https://www.thecocktaildb.com/api.php
    baseURL: https://www.thecocktaildb.com/api/json/v1
    properties:
      - url: https://www.thecocktaildb.com/api.php
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/openapi/free-cocktail-api-openapi.yml
        type: OpenAPI
    description: The Free Cocktail API provides access to a vast database of cocktail recipes, ingredients, and images.
common:
  - type: Website
    url: https://www.thecocktaildb.com/
  - type: Documentation
    url: https://www.thecocktaildb.com/api.php
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
