---
aid: thecocktaildb
name: TheCocktailDB
description: An open, crowd-sourced database of cocktails and drinks from around the world with a free API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cocktails
  - Drinks
  - Recipes
  - Food And Beverage
created: '2025-03-01'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/thecocktaildb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: thecocktaildb:thecocktaildb
    name: TheCocktailDB API
    description: An open, crowd-sourced database of cocktails and drinks from around the world with a free API. Search cocktails by name, ingredient, category, glass type, or alcoholic content. Look up full recipes with ingredients, measurements, instructions, and images. Free tier available with API key 1.
    humanURL: https://www.thecocktaildb.com/api.php
    baseURL: https://www.thecocktaildb.com/api/json/v1/1
    tags:
      - Cocktails
      - Drinks
      - Recipes
      - Food And Beverage
    properties:
      - type: Documentation
        url: https://www.thecocktaildb.com/api.php
      - type: OpenAPI
        url: openapi/thecocktaildb-openapi.yml
      - type: Sign Up
        url: https://www.thecocktaildb.com/signup.php
      - type: JSONSchema
        url: json-schema/thecocktaildb-drink-schema.json
        title: Drink Schema
      - type: JSONStructure
        url: json-structure/thecocktaildb-drink-structure.json
        title: Drink Structure
      - type: JSON-LD
        url: json-ld/thecocktaildb-context.jsonld
        title: TheCocktailDB JSON-LD Context
common:
  - type: Website
    url: https://www.thecocktaildb.com/
  - type: Documentation
    url: https://www.thecocktaildb.com/api.php
  - type: Sign Up
    url: https://www.thecocktaildb.com/signup.php
  - type: Pricing
    url: https://www.thecocktaildb.com/pricing
    data:
      - name: Free Tier
        description: Access with test API key 1 for development and educational use
      - name: Premium
        description: $10 one-time payment for production API key with full database access
  - type: SpectralRules
    url: rules/thecocktaildb-spectral-rules.yml
    title: TheCocktailDB Spectral Rules
  - type: Vocabulary
    url: vocabulary/thecocktaildb-vocabulary.yml
    title: TheCocktailDB Vocabulary
  - type: NaftikoCapability
    url: capabilities/cocktail-discovery.yaml
    title: Cocktail Discovery
  - type: Features
    data:
      - 'TheCocktailDB: free public API'
      - Free public cocktail recipe API. Patreon supporters get premium API key with no rate limits.
      - 'Public URL: https://www.thecocktaildb.com/'
    sources:
      - https://www.thecocktaildb.com/api.php
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Cocktail App Development
        description: Build cocktail recipe apps and websites
      - name: Bartender Tools
        description: Recipe lookup and ingredient substitution for professional bartenders
      - name: AI Recipe Assistant
        description: Power AI agents that help users find cocktail recipes
      - name: Menu Planning
        description: Plan bar menus by category, ingredient, or glass type
  - type: Integrations
    data:
      - name: TheMealDB
        description: Sister site providing food recipes from the same provider
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
