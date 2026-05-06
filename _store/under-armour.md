---
aid: under-armour
name: Under Armour
description: Under Armour is an American company that manufactures footwear, sports, and casual apparel known for its performance products designed for athletes. Under Armour operates a Connected Fitness platform — powered by MapMyFitness — that provides developer APIs for integrating workout tracking, route data, user profiles, heart rate zones, and fitness devices into third-party applications.
url: https://raw.githubusercontent.com/api-evangelist/under-armour/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Fitness
  - Health
  - Wearables
  - Connected Fitness
  - Sports
  - Fortune 1000
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: under-armour:mapmyfitness-api
    name: MapMyFitness API
    tags:
      - Fitness
      - Workouts
      - Routes
      - Health
      - Connected Fitness
      - OAuth2
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.ua.com
    humanURL: https://developer.mapmyfitness.com/
    properties:
      - url: https://developer.mapmyfitness.com/docs/
        type: Documentation
      - url: https://developer.mapmyfitness.com/docs/v71_OAuth_2_Intro/
        type: Authentication
      - url: openapi/mapmyfitness-openapi.yml
        type: OpenAPI
    description: The MapMyFitness API (Under Armour Connected Fitness API) provides RESTful access to fitness data including workouts, routes, user profiles, heart rate zones, fitness devices, and webhooks. The platform powers MapMyFitness, MapMyRun, MapMyRide, and MapMyWalk and supports over 400 partner apps and devices. Authentication uses OAuth 2.0.
common:
  - type: Website
    url: https://www.under-armour.com
  - type: Developer Portal
    url: https://developer.mapmyfitness.com/
  - type: Documentation
    url: https://developer.mapmyfitness.com/docs/
  - type: Authentication
    url: https://developer.mapmyfitness.com/docs/v71_OAuth_2_Intro/
  - type: Terms of Service
    url: https://developer.mapmyfitness.com/Terms_Of_Service/
  - type: GitHub Org
    url: https://github.com/underarmour
  - type: OpenAPI
    url: openapi/mapmyfitness-openapi.yml
  - type: JSON-LD
    url: json-ld/under-armour-context.jsonld
  - type: Vocabulary
    url: vocabulary/under-armour-vocabulary.yml
  - type: Spectral Rules
    url: rules/under-armour-rules.yml
  - type: JSONSchema
    url: json-schema/under-armour-workout-schema.json
  - type: Capabilities
    url: capabilities/connected-fitness.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
