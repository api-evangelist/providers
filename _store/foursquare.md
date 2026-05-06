---
aid: foursquare
name: Foursquare
description: Foursquare is a location intelligence platform that maintains a global graph of more than 100 million points of interest (POI) and provides developer APIs and SDKs for place search, geotagging, autocomplete, audience measurement, and visit detection across web and mobile.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2025-03-01'
modified: '2026-04-28'
tags:
  - Locations
  - Places
  - Geocoding
  - Recommendations
  - Reviews
  - Movement
url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: foursquare:places-api
    name: Foursquare Places API
    description: The Foursquare Places API provides global POI data with endpoints for place search, nearby, autocomplete, place details, photos, tips, geotagging, and Placemaker submissions.
    humanURL: https://docs.foursquare.com/developer/reference/places-api-overview
    baseURL: https://places-api.foursquare.com
    tags:
      - Places
      - Search
      - Geocoding
      - Autocomplete
    properties:
      - type: Documentation
        url: https://docs.foursquare.com/developer/reference/places-api-overview
      - type: Documentation
        name: Places API Reference
        url: https://docs.foursquare.com/developer/reference/foursquare-api-reference
      - type: SignUp
        url: https://foursquare.com/developers/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/openapi/foursquare-places-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/rules/foursquare-places-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/capabilities/foursquare-places-capabilities.yml
      - type: JSONSchema
        name: Place Schema
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/json-schema/foursquare-place.json
      - type: JSONSchema
        name: Tip Schema
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/json-schema/foursquare-tip.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/json-ld/foursquare-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/vocabulary/foursquare-vocabulary.yml
      - type: Example
        name: Place Example
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/examples/foursquare-place-example.json
      - type: Example
        name: Search Response Example
        url: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/examples/foursquare-search-example.json
  - aid: foursquare:movement-sdk
    name: Foursquare Movement SDK
    description: Mobile SDK for iOS, Android, and React Native that translates passive device location signals into visit events using the Foursquare POI graph.
    humanURL: https://docs.foursquare.com/developer/docs/movement-sdk-overview
    tags:
      - Movement
      - Visits
      - Mobile SDK
    properties:
      - type: Documentation
        url: https://docs.foursquare.com/developer/docs/movement-sdk-overview
  - aid: foursquare:movement-geofence-api
    name: Foursquare Movement Geofence API
    description: Server-side API for managing geofences that trigger events when Movement SDK-equipped devices enter or exit defined places.
    humanURL: https://docs.foursquare.com/developer/reference/movement-geofence-api
    tags:
      - Geofence
      - Movement
    properties:
      - type: Documentation
        url: https://docs.foursquare.com/developer/reference/movement-geofence-api
  - aid: foursquare:studio-data-api
    name: Foursquare Studio Data API
    description: API for managing datasets, maps, and visualizations within Foursquare Studio for geospatial analytics.
    humanURL: https://docs.foursquare.com/developer/reference/studio-data-api
    tags:
      - Studio
      - Geospatial
      - Analytics
    properties:
      - type: Documentation
        url: https://docs.foursquare.com/developer/reference/studio-data-api
  - aid: foursquare:measurement-api
    name: Foursquare Measurement API (MAPI)
    description: API for attribution and audience measurement using Foursquare visit panels.
    humanURL: https://docs.foursquare.com/developer/reference/measurement-api-mapi
    tags:
      - Measurement
      - Attribution
      - Analytics
    properties:
      - type: Documentation
        url: https://docs.foursquare.com/developer/reference/measurement-api-mapi
common:
  - type: Website
    url: https://foursquare.com/
  - type: Developer Portal
    url: https://docs.foursquare.com/developer/
  - type: SignUp
    url: https://foursquare.com/developers/
  - type: Documentation
    url: https://docs.foursquare.com/developer/reference/places-api-overview
  - type: Discord
    name: Foursquare Developer Community
    url: https://discord.gg/foursquare
  - type: Blog
    url: https://location.foursquare.com/resources/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
