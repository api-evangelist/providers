---
aid: themealdb
name: TheMealDB
description: TheMealDB is a comprehensive online platform offering a vast collection of recipes from around the world with a free API. The API and site will always remain free at point of access.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Recipes
  - Meals
  - Food
  - Cooking
created: '2024-11-14'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/themealdb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: themealdb:themealdb
    name: TheMealDB API
    description: Free Recipe API providing access to a crowd-sourced database of meals from around the world. Search by name, category, area/region, or ingredient. Look up full recipes with step-by-step instructions, ingredients, measurements, YouTube videos, and images. The API and site will always remain free at point of access.
    humanURL: https://www.themealdb.com/api.php
    baseURL: https://www.themealdb.com/api/json/v1/1
    tags:
      - Recipes
      - Meals
      - Food
      - Cooking
      - Nutrition
    properties:
      - type: Documentation
        url: https://www.themealdb.com/api.php
      - type: OpenAPI
        url: openapi/themealdb-openapi.yml
      - type: JSONSchema
        url: json-schema/themealdb-meal-schema.json
        title: Meal Schema
      - type: JSONStructure
        url: json-structure/themealdb-meal-structure.json
        title: Meal Structure
      - type: JSON-LD
        url: json-ld/themealdb-context.jsonld
        title: TheMealDB JSON-LD Context
common:
  - type: Website
    url: https://www.themealdb.com/
  - type: Documentation
    url: https://www.themealdb.com/api.php
  - type: Sign Up
    url: https://www.themealdb.com/
  - type: Pricing
    url: https://www.themealdb.com/
    data:
      - name: Free Tier
        description: Always free with test API key 1; no account required for basic access
      - name: Supporter Tier
        description: PayPal supporter for production API key, premium features, and database management
  - type: SpectralRules
    url: rules/themealdb-spectral-rules.yml
    title: TheMealDB Spectral Rules
  - type: Vocabulary
    url: vocabulary/themealdb-vocabulary.yml
    title: TheMealDB Vocabulary
  - type: NaftikoCapability
    url: capabilities/meal-recipe-discovery.yaml
    title: Meal Recipe Discovery
  - type: Features
    data:
      - 'TheMealDB: free public API'
      - Free public meal recipe API. Patreon supporters get premium API key with no rate limits.
      - 'Public URL: https://www.themealdb.com/'
    sources:
      - https://www.themealdb.com/api.php
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Recipe App Development
        description: Build meal recipe apps and cooking websites
      - name: Meal Planning
        description: Plan weekly meals by category, region, or available ingredients
      - name: AI Cooking Assistant
        description: Power AI agents that suggest meals and cooking ideas
      - name: Dietary Filtering
        description: Find meals filtered by ingredients, cuisine, or category
  - type: Integrations
    data:
      - name: TheCocktailDB
        description: Sister site providing cocktail recipes from the same provider
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
