---
aid: walk-score
name: Walk Score
description: Walk Score measures the walkability, transit accessibility, and bikeability of any address in the United States and Canada. The Walk Score API returns Walk Score, Transit Score, and Bike Score for any geographic location, supporting real estate platforms, commute calculators, urban planning tools, and location intelligence applications. The Public Transit API provides detailed transit data including nearby stops, route networks, and supported cities, enabling comprehensive transportation accessibility analysis.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Walkability
  - Transit
  - Bikeability
  - Location
  - Real Estate
  - Urban Planning
  - Transportation
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/walk-score/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: walk-score:walk-score-api
    name: Walk Score API
    description: Returns the Walk Score, Transit Score, and Bike Score for any location specified by latitude/longitude coordinates and address. Walk Score measures walkability on a scale from 0 (car-dependent) to 100 (walker's paradise). Optionally returns Transit Score and Bike Score in the same response. Supported in the United States and Canada. API calls must originate from server-side scripts.
    humanURL: https://www.walkscore.com/professional/api.php
    baseURL: https://api.walkscore.com
    tags:
      - Walkability
      - Walk Score
      - Transit Score
      - Bike Score
      - Location Intelligence
    properties:
      - type: Documentation
        url: https://www.walkscore.com/professional/api.php
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/walk-score/refs/heads/main/openapi/walk-score-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/walk-score/refs/heads/main/json-schema/walk-score-score-schema.json
  - aid: walk-score:walk-score-transit-api
    name: Walk Score Transit API
    description: Provides detailed public transit data for locations in supported cities including Transit Scores, nearby transit stops with route information, complete transit network data, individual stop and route details, and a list of supported cities. Used for comprehensive transit accessibility analysis in real estate, city planning, and commute optimization applications.
    humanURL: https://www.walkscore.com/professional/public-transit-api.php
    baseURL: https://transit.walkscore.com
    tags:
      - Public Transit
      - Transit Data
      - Transit Score
      - Bus
      - Rail
      - Transportation
    properties:
      - type: Documentation
        url: https://www.walkscore.com/professional/public-transit-api.php
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/walk-score/refs/heads/main/openapi/walk-score-transit-openapi.yml
common:
  - type: Website
    url: https://www.walkscore.com
  - type: Portal
    url: https://www.walkscore.com/professional/api.php
  - type: Documentation
    url: https://walkscore-api.readthedocs.io/en/latest/
  - type: SignUp
    url: https://www.walkscore.com/professional/api-sign-up.php
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
