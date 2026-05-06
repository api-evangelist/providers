---
aid: lyft
url: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/apis.yml
apis:
  - aid: lyft:ride-sharing-api
    name: Lyft Ride-Sharing API
    tags:
      - Drivers
      - Estimates
      - Rides
      - Rideshare
      - Transportation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.lyft.com
    humanURL: https://developer.lyft.com/docs
    properties:
      - url: https://developer.lyft.com/docs
        type: Documentation
      - url: openapi/lyft-ride-sharing-openapi.yml
        type: OpenAPI
    description: The Lyft Ride-Sharing API provides developers with programmatic access to Lyft's rideshare platform. It includes endpoints for retrieving cost estimates between locations, estimating pickup ETAs, listing available ride types in a given area, and checking nearby driver availability. The API uses OAuth 2.0 for user-authenticated requests and client tokens for public endpoints.
  - aid: lyft:concierge-api
    name: Lyft Concierge API
    tags:
      - Concierge
      - Enterprise
      - Healthcare
      - Rideshare
      - Transportation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.lyft.com
    humanURL: https://www.lyft.com/developers/products/concierge-api
    properties:
      - url: https://www.lyft.com/developers/products/concierge-api
        type: Documentation
      - url: openapi/lyft-concierge-openapi.yml
        type: OpenAPI
    description: The Lyft Concierge API allows organizations to request rides on behalf of their customers, patients, or employees without requiring those individuals to have a Lyft account. It is designed for enterprise use cases such as healthcare patient transportation, corporate employee transit, and customer service scenarios. The API enables organizations to build customized transportation workflows, schedule rides in advance, track ride status in real time, and manage ride programs at scale.
common:
  - type: JSON-LD
    url: json-ld/lyft-context.jsonld
  - type: JSONSchema
    url: json-schema/lyft-ride-schema.json
  - type: JSONSchema
    url: json-schema/lyft-ride-type-schema.json
  - type: JSONSchema
    url: json-schema/lyft-cost-estimate-schema.json
modified: '2026-04-28'
description: Lyft is a transportation network company that develops, markets, and operates a mobile app offering ride-hailing, vehicles for hire, motorized scooters, bicycle-sharing, and food delivery services.
---
